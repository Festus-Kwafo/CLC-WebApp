#Pull base image
FROM python:3.9

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /clc-app/
RUN pip install -r /clc-app/requirements.txt

#work directory
WORKDIR /clc-app/src
CMD gunicorn --bind 0.0.0.0:$PORT core.wsgi

# Copy project
COPY . /clc-app/

