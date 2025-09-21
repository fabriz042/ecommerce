from pathlib import Path
from datetime import timedelta
from environs import Env

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = env.bool('DEBUG', default=False)
SECRET_KEY = env.str('ENV_SECRET_KEY')
ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True

# Custom user model
AUTH_USER_MODEL = 'users.User'

#---------------------Database---------------------
DATABASES = {
    'default': {
        "ENGINE": env.str('DATABASE_ENGINE'),  
        'NAME': env.str('DATABASE_NAME'),          
        'USER': env.str('DATABASE_USER'),        
        'PASSWORD': env.str('DATABASE_PASSWORD'),
        'HOST': env.str('DATABASE_HOST'),              
        'PORT': env.str('DATABASE_PORT'),              
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', 
    'corsheaders',
    'drf_spectacular',
    'django_filters',
    'storages',
    'app.products',
    'app.users',
    'app.goods',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = ['http://localhost:3000']

ROOT_URLCONF = 'config.urls'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    "EXCEPTION_HANDLER": "utils.exceptions.custom_exception_handler"
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': env.timedelta('ACCESS_TOKEN_LIFETIME'),
    'REFRESH_TOKEN_LIFETIME': env.timedelta('REFRESH_TOKEN_LIFETIME'),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# -----------------Storage-------------------

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

AWS_ACCESS_KEY_ID = env.str('MINIO_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = env.str('MINIO_SECRET_KEY')

AWS_STORAGE_BUCKET_NAME = env.str('MINIO_BUCKET_NAME')
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_ENDPOINT_URL = env.str('MINIO_ENDPOINT')
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False

STATIC_URL = 'static/'

# -----------Internationalization---------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
