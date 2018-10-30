FROM python:3.6
WORKDIR /root
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /root
CMD ["python", "./main_api.py"]