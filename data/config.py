from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS_ = env.list("ADMINS")  # Bot adminlari
ADMINS = [int(admin) for admin in ADMINS_]  # Bot adminlari