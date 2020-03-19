FROM ubuntu:latest

RUN apt-get update --fix-missing && apt-get upgrade -y
RUN apt-get install python3 openssh-server -y
RUN mkdir /var/run/sshd

RUN groupadd -r ctf && useradd -r -g ctf ctf
RUN echo "ctf:hunter2" | chpasswd

ADD generatefiles.py /home/ctf/generatefiles.py
RUN cd /home/ctf && python3 /home/ctf/generatefiles.py
RUN rm /home/ctf/generatefiles.py

RUN apt-get remove python3 perl -y
RUN cd /bin && chmod a-x $(ls | grep -v bash | grep -v chmod | grep -v sh)
RUN chmod a-x /usr/local/sbin/* /usr/sbin/* /usr/bin/* /sbin/*
RUN chmod a+x /usr/sbin/sshd /bin/ls /bin/pwd /bin/cat

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
