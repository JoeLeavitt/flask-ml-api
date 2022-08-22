FROM python:3.8-slim

COPY ./requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt

COPY ./src /app/src
COPY ./model /app/model
COPY ./test_images /app/test_images

WORKDIR /app/src

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]