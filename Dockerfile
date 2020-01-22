FROM python:3.7

RUN pip3 install requests
RUN pip3 install flask
RUN pip3 install logzero
RUN pip3 install gunicorn
RUN pip3 install flask_script
COPY app.py /app.py
COPY config.cfg /config.cfg
COPY manage.py /manage.py
COPY files /files
COPY run.sh /run.sh
RUN chmod +x /run.sh

EXPOSE 5000

ENTRYPOINT ["/run.sh"]


