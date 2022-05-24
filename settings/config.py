import os

DEBUG = int(os.getenv("DEBUG", 0))
APP_SECRET_KEY = os.getenv("APP_SECRET_KEY", "xxx")
APP_ALLOWED_HOSTS = os.getenv("APP_ALLOWED_HOSTS", "localhost").split(" ")

DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "pass")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = int(os.getenv("POSTGRES_PORT", 5432))
DB_NAME = os.getenv("POSTGRES_DB", "db")
DB_URI = f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
