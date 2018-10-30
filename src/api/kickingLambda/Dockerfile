FROM python:3.65
WORKDIR /root
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /root
#ENTRYPOINT ["/root/bin/chalice"]
#CMD ["local"]

