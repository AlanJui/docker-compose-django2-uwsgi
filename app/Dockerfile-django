FROM python:3.6.2
LABEL maintainer Alan Jui "alanjui.1960@gmail.com"
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
# RUN pip install  -i  https://pypi.python.org/simple/  -r requirements.txt
