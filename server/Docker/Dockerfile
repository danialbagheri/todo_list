FROM python:3

RUN mkdir /code
WORKDIR /code
EXPOSE 8082
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
CMD ["python3", "/code/app/app.py"]
