import requests
from datetime import datetime

class PrayerTimes:
    def __init__(self):
        self.base_url = "http://api.aladhan.com/v1/timingsByCity"

    def get_prayer_times(self, city: str, country: str = "Uzbekistan"):
        params = {
            "city": city,
            "country": country,
            "method": 2, # ISNA method or others
            "school": 1 # 1 for Hanafi
        }
        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()["data"]
                return data
            return None
        except Exception as e:
            print(f"Error fetching prayer times: {e}")
            return None
    def get_calendar_times(self, city: str, month: int, year: int, country: str = "Uzbekistan"):
        url = f"https://api.aladhan.com/v1/calendarByCity/{year}/{month}"
        params = {
            "city": city,
            "country": country,
            "method": 2,
            "school": 1
        }
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()["data"]
            return None
        except Exception as e:
            print(f"Error fetching calendar: {e}")
            return None
