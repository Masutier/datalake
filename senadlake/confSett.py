import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def localSett():
    ALLOWED_HOSTS = ['localhost']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'senadlake',
        'loads',
        'raiting',
        'users',
    ]

    return ALLOWED_HOSTS, INSTALLED_APPS


def prodSett():
    ALLOWED_HOSTS = ['url hosting']

    RECAPTCHA_PUBLIC_KEY = config['RECAT_PUBLIC_KEY_DEBUG']
    RECAPTCHA_PRIVATE_KEY = config['RECAT_SECRET_KEY_DEBUG']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'senadlake',
        'captcha',
        'loads',
        'raiting',
        'users',
    ]

    return ALLOWED_HOSTS, RECAPTCHA_PUBLIC_KEY, RECAPTCHA_PRIVATE_KEY, INSTALLED_APPS

def securFileHome():
    with open(BASE_DIR + "/venv/senadlake.json") as config_file:
        config = json.load(config_file)
    return config

def securFileSena():
    with open("/etc/senadlake.json") as config_file:
        config = json.load(config_file)
    return config
