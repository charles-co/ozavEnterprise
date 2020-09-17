from .base import *


DEBUG = False

ADMINS = (
('Charles O.', 'ch4rles.co@gmail.com'),
)

ALLOWED_HOSTS = ['ozav.com', 'www.ozav.com', '127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}