from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")

DB_NAME = env.str("DB_NAME")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_HOST = env.str("DB_HOST")
DB_DATABASE = env.str("DB_DATABASE")

SUPERGROUP_CHAT_ID = env.str("SUPERGROUP_CHAT_ID")
