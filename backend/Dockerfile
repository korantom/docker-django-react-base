FROM python:3.7

WORKDIR /app/backend
COPY ./requirements.txt ./requirements.txt

RUN apt-get update -y && \ 
    python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# realy needed?
COPY . ./