from apscheduler.triggers.cron import CronTrigger
from loader import bot, scheduler
from utils.db_api.sqlite import Database
from utils.prayer_api.api import PrayerTimes
from datetime import datetime, timedelta
import asyncio

import os
import random

async def send_notification(user_id, message, audio_path=None):
    try:
        await bot.send_message(user_id, message)
        
        if audio_path and os.path.exists(audio_path):
            from aiogram.types import FSInputFile
            voice = FSInputFile(audio_path)
            await bot.send_voice(user_id, voice)
            
    except Exception as e:
        print(f"Error sending message to {user_id}: {e}")

async def send_daily_wisdom():
    db = Database()
    users = db.select_all_users()
    wisdom = db.get_random_wisdom()
    
    if wisdom:
        content, source = wisdom
        message = f"🌟 **Kunlik Hikmat**\n\n{content}\n\n— *{source}*"
        for user in users:
            try:
                await bot.send_message(user[0], message, parse_mode="Markdown")
            except:
                pass

async def schedule_daily_prayers():
    db = Database()
    users = db.select_all_users()
    prayer_api = PrayerTimes()
    
    region_data = {}
    now = datetime.now()

    for user in users:
        user_id = user[0]
        region = user[2]
        
        if not region:
            continue
            
        if region not in region_data:
            data = prayer_api.get_prayer_times(region)
            if data:
                region_data[region] = data
        
        data = region_data.get(region)
        
        if data:
            times = data['timings']
            hijri_month = int(data['date']['hijri']['month']['number'])
            
            # 9-oy Ramazon
            is_ramadan = (hijri_month == 9)

            prayers_map = {
                'Fajr': 'Bomdod',
                'Sunrise': 'Quyosh chiqishi',
                'Dhuhr': 'Peshin',
                'Asr': 'Asr',
                'Maghrib': 'Shom',
                'Isha': 'Xufton'
            }

            for prayer_en, prayer_uz in prayers_map.items():
                time_str = times.get(prayer_en)
                if time_str:
                    hour, minute = map(int, time_str.split(':')[0:2])
                    prayer_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
                    
                    message_text = f"🕰 {prayer_uz} vaqti bo'ldi! ({time_str})"
                    
                    # Ramazon maxsus xabarlari
                    if is_ramadan:
                        if prayer_en == 'Fajr':
                            message_text = f"🌙 Saharlik (Og'iz yopish) vaqti bo'ldi! ({time_str})\nNiyat: Navvaytu an asuma sovma shahri ramazona minal fajri ilal mag'ribi, xolisan lillahi ta'ala. Allohu Akbar."
                        elif prayer_en == 'Maghrib':
                            message_text = f"🍲 Iftorlik (Og'iz ochish) vaqti bo'ldi! ({time_str})\nDuoni o'qishni unutmang: Allohumma laka sumtu va bika amantu va a'layka tavakkaltu va a'la rizqika aftartu."

                    # Audio path (placeholder)
                    audio_file = "data/text_audio/azon.mp3"
                    
                    if prayer_time > now:
                        # 10 daqiqa oldin eslatma
                        reminder_time = prayer_time - timedelta(minutes=10)
                        if reminder_time > now:
                            scheduler.add_job(
                                send_notification, 
                                'date', 
                                run_date=reminder_time, 
                                args=[user_id, f"🔔 Diqqat! 10 daqiqadan so'ng {prayer_uz} vaqti bo'ladi. Tayyorgarlik ko'rib oling."],
                                id=f"{user_id}_{prayer_en}_10min_{now.strftime('%Y%m%d')}",
                                replace_existing=True
                            )

                        # Asl vaqtidagi eslatma (Azon bilan)
                        scheduler.add_job(
                            send_notification, 
                            'date', 
                            run_date=prayer_time, 
                            args=[user_id, message_text, audio_file],
                            id=f"{user_id}_{prayer_en}_{now.strftime('%Y%m%d')}",
                            replace_existing=True
                        )

async def start_scheduler():
    # Har kuni namoz vaqtlarini yangilash (00:01)
    scheduler.add_job(schedule_daily_prayers, CronTrigger(hour=0, minute=1))
    
    # Har kuni ertalab hikmatli so'z yuborish (08:00)
    scheduler.add_job(send_daily_wisdom, CronTrigger(hour=8, minute=0))
    
    await schedule_daily_prayers()
    scheduler.start()
