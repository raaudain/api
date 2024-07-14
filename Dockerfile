FROM python:3-alpine

WORKDIR /code

COPY . /code

RUN apk add --no-cache ffmpeg
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3773"]
