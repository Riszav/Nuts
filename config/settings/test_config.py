import sys
import os
from config.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'TEST': {
            'NAME': BASE_DIR / 'test.db.sqlite3',
        }
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/var/tmp/django_cache",
    }
}

if "create-db" not in sys.argv:
    DATABASES["default"]["TEST"]["NAME"] = os.path.join(BASE_DIR, "test.db.sqlite3")
