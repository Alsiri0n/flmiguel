FROM python:3.10.8-bullseye
RUN useradd microblog
# RUN apt-get update && apt-get install -y python3.10 python3-pip
RUN mkdir -p /usr/src/app/flmiguel
WORKDIR /usr/src/app/flmiguel
RUN python -m venv venv
COPY requirements.txt ./
RUN venv/bin/pip install --no-cache-dir -r ./requirements.txt
RUN venv/bin/pip install gunicorn
COPY app /usr/src/app/flmiguel/app
COPY *.py /usr/src/app/flmiguel/
COPY boot.sh /usr/src/app/flmiguel/
RUN chmod +x /usr/src/app/flmiguel/boot.sh
ENV FLASK_APP run.py
RUN chown -R microblog:microblog /usr/src/app/flmiguel/
USER microblog
ENTRYPOINT ["./boot.sh"]
EXPOSE 5050