pplox_web is an Django web application that lets you run the pplox interpreter over the web.
Use it at https://pl0x.onrender.com.

## Running Django
Run locally with
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Configuring environment variables
- PPLOX_WEB_SECRET_KEY
- PPLOX_WEB_DEBUG
- PPLOX_WEB_SECURE_SSL_REDIRECT
- PPLOX_WEB_SESSION_COOKIE_SECURE
- PPLOX_WEB_CSRF_COOKIE_SECURE
- PPLOX_WEB_HOST