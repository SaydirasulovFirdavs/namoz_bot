from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env faylidan o'qib olish
BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("IP")
