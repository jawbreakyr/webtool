import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = [os.path.join(BASE_DIR, "templates")]


DEBUG = True


SECRET_KEY = ')d-fzz_rl4#ee%5tdsgd)m*xdf*z*f^st_dsg44lg3lt&^8is4'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django-testing-shorturls',
    }
}

INSTALLED_APPS = (
	'shorturls',
	'django.contrib.staticfiles',
	)
ROOT_URLCONF = 'shorturls.urls'
STATIC_URL = '/static/'