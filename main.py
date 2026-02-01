import asyncio
import logging
import sys

from loader import bot, dp
from utils.notify_admins import on_startup_notify
from utils.db_api.sqlite import Database
from utils.set_bot_commands import set_default_commands

# Handlers
from handlers.users import users_router


import os
from aiohttp import web

async def handle(request):
    return web.Response(text="Bot is running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    logging.info(f"Keep-alive server started on port {port}")

async def main():
    # Logging Configuration
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    
    # Start web server for Render health checks
    await start_web_server()
    
    # Database initialization
    db = Database()
    try:
        db.create_table_users()
        db.create_table_wisdom()
        db.create_table_tasbih()
        db.create_table_tracker()
    except Exception as e:
        print(f"Error creating table: {e}")

    # Set commands
    await set_default_commands(bot)

    # Register routers
    dp.include_router(users_router)

    # Notify admins
    await on_startup_notify(bot)
    
    # Scheduler
    from utils.scheduler import start_scheduler
    await start_scheduler()

    # Start polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
