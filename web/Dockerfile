FROM python:3.9
WORKDIR /usr/app
COPY requirements.txt .
RUN apt-get update 
RUN pip install --no-cache-dir --upgrade -r /usr/app/requirements.txt
COPY app ./app
CMD ["python","app/main.py"]
