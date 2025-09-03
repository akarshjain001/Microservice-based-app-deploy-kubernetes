FROM python:3.13.3-alpine

WORKDIR /app

ADD . . 

RUN pip install --no-cache-dir -r requirement.txt

CMD [ "python" , "app.py" ]