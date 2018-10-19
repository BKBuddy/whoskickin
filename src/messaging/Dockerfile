FROM python:3.7
WORKDIR /root
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /root
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
CMD ["python", "./messaging_scheduler.py"]