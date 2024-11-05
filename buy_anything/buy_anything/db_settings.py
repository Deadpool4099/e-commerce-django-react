import os

db_settings = {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('BUY_ANYTHING_DB_HOST'),
        'PORT': os.environ.get('BUY_ANYTHING_DB_PORT'),
        'USER': os.environ.get('BUY_ANYTHING_DB_USER'),
        'PASSWORD':os.environ.get('BUY_ANYTHING_DB_PASSWORD'),
        'NAME': os.environ.get('BUY_ANYTHING_DB_NAME')
}