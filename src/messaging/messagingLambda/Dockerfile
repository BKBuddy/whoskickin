FROM python:3.7
WORKDIR /root
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /root
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
CMD ["chalice local --port 4000"]