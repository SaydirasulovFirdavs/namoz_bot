from aiogram import Router
from . import start, region, tasbih, duolar, qibla, zakat, learn_namoz, tracker, calendar, settings

users_router = Router()
users_router.include_router(start.router)
users_router.include_router(region.router)
users_router.include_router(tasbih.router)
users_router.include_router(duolar.router)
users_router.include_router(qibla.router)
users_router.include_router(zakat.router)
users_router.include_router(learn_namoz.router)
users_router.include_router(tracker.router)
users_router.include_router(calendar.router)
users_router.include_router(settings.router)
