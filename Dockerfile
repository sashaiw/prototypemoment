FROM python:3.10

WORKDIR /usr/src/app

RUN pip install pip -U

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY prototypemoment prototypemoment/

CMD [ "python3", "-m", "prototypemoment" ]