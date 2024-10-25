pplox_web is an Django web application that lets you run the [pplox interpreter](https://github.com/karlcaga/pplox) over the web.
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
- `PPLOX_WEB_EXTRA_HOSTS` Set this to your domain or IP

## Deployments
We support deploying on a Linux VPS, and Docker.

### Linux
Install `python`, `pip`, `venv`, and `nginx` using 
```bash
sudo apt update && sudo apt install python3 python3-pip python3-venv nginx
```

Install pplox web from git and install its dependencies 
```bash
sudo mkdir /pplox-web
cd /pplox-web/
git clone https://github.com/karlcaga/pplox_web.git .
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a systemd service file `/etc/systemd/system/pplox_web.service` for pplox-web with the contents:
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
          --bind localhost:8000 \
          pplox_web.wsgi

[Install]
WantedBy=multi-user.target
```

Set the environment variables with `sudo systemctl edit pplox_web` and add
```bash
[Service]
Environment="PPLOX_WEB_DEBUG=False"
Environment="PPLOX_WEB_SECRET_KEY=🤫"
Environment="PPLOX_WEB_SECURE_SSL_REDIRECT=False"
Environment="PPLOX_WEB_SESSION_COOKIE_SECURE=False"
Environment="PPLOX_WEB_CSRF_COOKIE_SECURE=True"
Environment="PPLOX_WEB_EXTRA_HOSTS=YOUR_HOSTNAME"
```

Start the `pplox-web` service with systemd
```bash
sudo systemctl start pplox_web
sudo systemctl enable pplox_web
```

In `/etc/nginx/sites-available/pplox-web` add
```bash
server {
    listen 80;
    server_name server_domain_or_IP;

    location / {
        include proxy_params;
        proxy_pass http://localhost:8000;
    }
}
```

Save the file and enable it by linking it to the `sites-enabled` directory
```bash
ln -s /etc/nginx/sites-available/pplox-web /etc/nginx/sites-enabled
```

Restart Nginx with
```bash
systemctl restart nginx
```

### Docker
You can deploy pplox web on a Docker container using `docker run -dt --restart unless-stopped -p 80:8000 --env-file .env --name pplox_web ghcr.io/karlcaga/pplox_web:main`.
The `.env` file must contain value for `PPLOX_WEB_SECRET_KEY`.
