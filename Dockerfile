FROM python:3.12

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["gunicorn", "--access-logfile", "-", "-b", "0.0.0.0:8000", "pplox_web.wsgi"]
