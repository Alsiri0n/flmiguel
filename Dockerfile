FROM python:3.10.8-bullseye
# RUN apt-get update && apt-get install -y python3.10 python3-pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r /home/requirements.txt
RUN mkdir -p /usr/src/app/flmiguel
WORKDIR /usr/src/app/flmiguel
COPY app /usr/src/app/flmiguel/app
COPY *.py /usr/src/app/flmiguel/
ENTRYPOINT ["python", "run.py"]
EXPOSE 5050