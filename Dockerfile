FROM centos:latest
RUN cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
# RUN dnf install net-tools -y
# RUN dnf install httpd -y
RUN dnf install python3 -y
#psycopg2-binary
RUN dnf install postgresql-devel -y
RUN dnf install python3-devel -y
RUN dnf install gcc -y
#Greenlet(sql-alchemy)
RUN dnf install gcc-c++ -y
# RUN dnf install python-psycopg2
COPY requirements.txt /home
RUN pip3 install -r /home/requirements.txt
COPY app flmiguel/app
COPY *.py flmiguel/
WORKDIR flmiguel
ENTRYPOINT ["python3", "run.py"]
EXPOSE 5050