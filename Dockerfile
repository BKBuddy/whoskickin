FROM python:3.7
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /code
CMD ["python", "src/api/kickin_api.py"]