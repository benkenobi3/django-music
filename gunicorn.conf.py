import os
import multiprocessing

DJANGO_ENV = os.environ.get('DJANGO_ENV', 'DEBUG')
DEBUG = DJANGO_ENV == 'DEBUG'

bind = '0.0.0.0:' + os.environ.get('DJANGO_APP_PORT', '8000')
log_level = 'debug' if DEBUG else 'info'
proc_name = 'gunicorn-music'