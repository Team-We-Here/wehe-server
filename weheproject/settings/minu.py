from .base import *
import environ

ALLOWED_HOSTS = []

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": 'db.sqlite3'}}

