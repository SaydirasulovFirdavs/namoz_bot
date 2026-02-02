from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytz
from data import config

bot = Bot(
    token=config.BOT_TOKEN, 
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

TASHKENT = pytz.timezone('Asia/Tashkent')
scheduler = AsyncIOScheduler(timezone=TASHKENT)

