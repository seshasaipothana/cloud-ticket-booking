from .base import *
import os
import dj_database_url

SECRET_KEY = os.environ["SECRET_KEY"]


DEBUG = os.environ.get("DEBUG", "False") == "True"



ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///db.sqlite3",
        conn_max_age=600,
        ssl_require=False
    )
}

REDIS_URL = os.environ.get("REDIS_URL")
