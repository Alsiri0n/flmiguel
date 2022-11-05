FROM ubuntu:latest
# RUN echo python -V
# RUN pip --version
RUN apt-get update && apt-get install -y python3.10 python3-pip
# RUN sudo apt-get install -y python
#psycopg2-binary
# RUN dnf install postgresql-devel -y
# RUN dnf install python3-devel -y
# RUN dnf install gcc -y
#Greenlet(sql-alchemy)
# RUN dnf install gcc-c++ -y
# RUN dnf install python-psycopg2
COPY requirements.txt /home
RUN pip install -r /home/requirements.txt
RUN mkdir -p /usr/src/app/flmiguel
# WORKDIR /usr/src/app/flmiguel
COPY app flmiguel/app
COPY *.py flmiguel/
WORKDIR flmiguel
ENV FLASK_APP run.py
ENTRYPOINT ["python3", "run.py"]
EXPOSE 5050