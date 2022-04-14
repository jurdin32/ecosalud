from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

datos_email={
    'servidor_smtp':'smtp.office365.com',
    'puerto':587,
    'use_tls':True,
    'usuario':'urdin-23@live.com',
    'password':'Urdin32**',
}

POSTGRES={
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ecosalud',
        'USER':'ecosalud',
        'PASSWORD':'ecosalud',
        'HOST':'localhost',
        'PORT': 5432,
    }
}

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}