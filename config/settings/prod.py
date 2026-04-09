from decouple import config

ALLOWED_HOSTS = ["*"]

# Настройки базы данных для продакшена
DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql',
        "NAME": config("SQL_DATABASE"),
        "USER": config("SQL_USER"),
        "PASSWORD": config("SQL_PASSWORD"),
        "HOST": 'pgdb',
        "PORT": 5432,
    }
}

CSRF_TRUSTED_ORIGINS = ["http://"+config('IP_ADDRESS'), "http://"+config('IP_ADDRESS')+":80", "https://"+config('IP_ADDRESS')+":443",
                        "http://"+config('DOMAIN_NAME'), "https://"+config('DOMAIN_NAME'), "https://"+config('DOMAIN_NAME')+":80", "https://"+config('DOMAIN_NAME')+":443"]
