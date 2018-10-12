FROM python:3.7
WORKDIR /api
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD ./src/api /api
CMD ["python", "./kickin_api.py"]