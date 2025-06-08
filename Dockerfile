FROM python:3.10-slim

ARG IMAGE_TAG
ENV APP_VERSION=$IMAGE_TAG

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "app.py"]