FROM python:3.6

MAINTAINER Sébastian Thune

RUN apt-get update -y && apt-get install -y python3-pip python-dev

EXPOSE 80
EXPOSE 5000

COPY . /venv
WORKDIR /venv

#COPY ./requirements.txt venv/requirements.txt
RUN pip3 install -r requirements.txt


ENTRYPOINT [ "python" ]

CMD ["main.py"]