FROM python:3.7
WORKDIR /root
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /root
CMD ["chalice local --port 5000"]
