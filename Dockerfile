FROM ubuntu:latest
RUN sudo apt-get update -y
RUN sudo apt-get install -y python
#psycopg2-binary
# RUN dnf install postgresql-devel -y
# RUN dnf install python3-devel -y
# RUN dnf install gcc -y
#Greenlet(sql-alchemy)
# RUN dnf install gcc-c++ -y
# RUN dnf install python-psycopg2
COPY requirements.txt /home
RUN pip3 install -r /home/requirements.txt
COPY app flmiguel/app
COPY *.py flmiguel/
WORKDIR flmiguel
ENTRYPOINT ["python3", "run.py"]
EXPOSE 5050