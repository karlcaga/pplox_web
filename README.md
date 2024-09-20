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

### Linux
Install `python`, `pip`, and `venv` using 

```bash
apt install python3 python3-pip python3-venv
```

Install pplox web from git and installing its dependencies 
```bash
mkdir /pplox-web
cd /pplox-web/
git clone https://github.com/karlcaga/pplox_web.git .
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a systemd service file in `/etc/systemd/system/pplox_web.service` for pplox-web with the contents:
```ini
[Unit]
Description=Gunicorn instance to serve pplox-web
After=network.target

[Service]
User=YOUR_USER
Group=www-data
WorkingDirectory=/pplox-web/
ExecStart=/pplox-web/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/pplox_web.sock \
          pplox_web.wsgi

[Install]
WantedBy=multi-user.target
```

Start the `pplox-web` service with systemd
```bash
systemctl start pplox-web
systemctl enable pplox-web
```

In `/etc/nginx/sites-available/pplox-web` add the following contents
```
server {
    listen 80;
    server_name server_domain_or_IP;

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/pplox_web.sock;
}
```

Save the file and enable it by linking it to the `sites-enabled` directory
```bash
ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
```

Restart Nginx with
```bash
systemctl restart nginx
```


### Docker
You can deploy pplox web on a Docker container using `docker run -dt --restart unless-stopped -p 80:8000 --env-file .env --name pplox_web ghcr.io/karlcaga/pplox_web:main`.
The `.env` file must contain value for `PPLOX_WEB_SECRET_KEY`.