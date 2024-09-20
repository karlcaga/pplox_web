pplox_web is an Django web application that lets you run the pplox interpreter over the web.
Use it at https://pl0x.onrender.com.
Documentation can be found at https://karlcaga.github.io/pplox_web/

## Running Django
Run locally with
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Configuring environment variables
- `PPLOX_WEB_SECRET_KEY` The secret key used by Django
- `PPLOX_WEB_DEBUG` Set to True to enable debug mode, otherwise False
- `PPLOX_WEB_SECURE_SSL_REDIRECT` Set to False to disable SSL redirection, otherwise True
- `PPLOX_WEB_SESSION_COOKIE_SECURE` Set to False to disable session cookies, otherwise True
- `PPLOX_WEB_CSRF_COOKIE_SECURE` Set to False to disable CSRF cookies, otherwise True
- `PPLOX_WEB_HOST` Set to RENDER if hosting on Render

## Deployments

### Docker
You can deploy pplox web on a Docker container using `docker run -dt --restart unless-stopped -p 80:8000 --env-file .env --name pplox_web ghcr.io/karlcaga/pplox_web:main`.
The `.env` file must contain value for `PPLOX_WEB_SECRET_KEY`.