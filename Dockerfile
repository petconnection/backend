FROM python:3.6-slim
ENV DJANGO_DEBUG False
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn==19.9.0
COPY . /usr/local/petconnection/
WORKDIR /usr/local/petconnection/
CMD python3 manage.py migrate && gunicorn -w 2 -b 0.0.0.0:8000 backend.wsgi
