"""
Django settings for eseller project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-af-7=k0-#z1-f)q@axvv#_%w5%5fb5&krb@ki2i(-p$ls2cn9$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'sellerapp',
    'rest_framework',
    'oauth2_provider',
    'corsheaders',
]

# Add openid conncetion requirements
AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)

ACCESS_TOKEN_EXPIRE_SECONDS = 36000
REFRESH_TOKEN_EXPIRE_SECONDS = 86400
OAUTH2_BACKEND_CLASS = 'oauth2_provider.backends.OAuthLibCore'

#
OAUTH2_PROVIDER = {
    "OIDC_ENABLED": True,
    "SCOPES": {
        "openid": "OpenID Connect scope",
        "profile": "User profile",
        "email": "solomonwachira212@gmail.com",
    },
    "OIDC_RSA_PRIVATE_KEY": 
    """-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC/TeauM+u8v5VO
ST56BwOIlW8Xaz/VsaRxH+ThY0CpHE/p1FBLa8aQqZfk7T+rkVeUajDzZJyi0+m5
VJrlDzLzOYFJxogirP+XZILp5vGMY+I8MDwxWKHHcKTuFj9L2LxNgLq3gtVCYJaz
NlYTZRZBpsakd0KpuKKcllYsG/uHxKmDC+Gpu02RbbeBhe+y+aOtcykjzdImiJ5K
Mq5Iih1Fg1zieKmRYdjLQSJ09AJaRImMksBbG3jRlDTHrUIeWTYhVsA/Y0ga7xTu
p1jeZVJnTrSfGRt5dUEVP4rK/QxP9a6wCOADZTEhdgKBLEAgg68F8DvJ4wm81ESA
N3P+nctlAgMBAAECggEANV2b3jipqEuhcOdJwGy4dZ+KD/RhKFGX197X0HAJl6NI
P6h0hbWY/L3ym2/7dPbkgYhmA1+rulh3OLX7R67HvcXq5RO24kV0P11Qj8NW2pz6
fWPPRsy8xJAN0kTuf1AEp3IjpBGhQBUFtRSRSnPGk6XcgACs3f+djST7AO8Facfb
++NEegkXxY/gY1rrNplbtAQdHI1OxqbrOQe3fj1zGhVbI558vS6LpYZETJXlC1ZU
LljvQNKxX8h/GZT64Qo+eINjNhXkVJnURQllr6z8bI9SrxLHNNmNEZInPumxMH2w
XKDnfWrgunUN++WmKKmIOigVXXwYOVhC84jPcghI+QKBgQD+iFq4ySV2ciooQqP2
LRkOnZGQtRvdyqYoRRjHj4xtdzOcUjNlf3CFM76JsIuxCW8iKlWb0yPpUb2I7H1w
81NaMt4RH2gUdwru8xFDFpdvEEAjQS/M7WXTgxAVDC1ZqR0UX+UWH+rOnomdMyyJ
8cvzenmqNWlADJzDbILT5ShdywKBgQDAaDuWMXjF6t7EjRzALI8jMx1thLOk73Nr
kxOtOkCEfNYpkjx3k8JSRkt76M/qdiyJSga7tY+g8LQLPhLhd5MgbD84Y2Ag3pbB
p31m5d95ZqGxO1T07yI/vO7W4dVTWIenhvw3BbIkYEiOZ1lilMZW0At0H8FuM5za
RyfFZCdVjwKBgQDo/jpFgmMXnIO4nN/n3fpc5aG1HAPpL7KPlEiNjHqYTZBh3OEN
XO3MEMSu13vXz/H6DVSWMl1iG5/q8cgWF7bKD1w1wlEMwrewabH4fnqagP6lBuvR
o9IdHpEfIyl0NJjY6LsUWJ0hDACedJSlpT/znb43L3Mr3R+2x+KuQsuDpwKBgQCu
p28/fRTmg7dHr9hjUY91IlcaLRVtKLca9V0tJ+2c1j0Ja2dcHFKOoKSwi7sAV9lB
nmLSTZNdQmIMuoIlDIgPLHOO2hZOf/9VNpaMqynaZ6Fq4jLSS6hJN1WO1Vzx1TD+
j3eu8oqsnoH+Ui4/YFFSSHO9K35IbK17LpAZjDpwXQKBgQCsm4wjktUNWXXylqs8
RaQeu0JZwCshpkTnH7QhVUpq7+tIAhdtH7eL6t4054CZHjZqPtmv0Xwy8nZoS2+e
gDbDr0JiwLMx6ek3AkUhh5s+GzmUTQnaa93JScP6VfAZO11mOIC92GBh7GZjDkbT
Sg3dNju6tTyZwdZq492Mt3W0Pg==
-----END PRIVATE KEY-----"""
}

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '87878131054-8lfegvldei5dspivqdqpvvceor43g220.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['openid', 'email', 'profile']


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

ROOT_URLCONF = 'eseller.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'eseller.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sellerdb',
        'USER': 'merchant',
        'PASSWORD': 'sela00',
        'HOST': '172.31.41.25',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
