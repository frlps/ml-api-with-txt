FROM python:3.8

COPY ./requirements.txt /usr/requirements.txt

WORKDIR /usr

RUN pip install -r requirements.txt

COPY ./main.py /usr/main.py

ENTRYPOINT [ "python" ]
CMD [ "main.py" ]