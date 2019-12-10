FROM python:3.7


RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN echo "en_AU.UTF-8 UTF-8" >> /etc/locale.gen
RUN locale-gen en_AU.UTF-8

ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#CMD python wsgi.py runserver -h 0.0.0.0

#RUN locale-gen en_AU.utf8
ENV LANG en_AU.UTF-8
ENV LANGUAGE en_AU:en
ENV LC_ALL en_AU.UTF-8


CMD tail -f /app/requirements.txt
