FROM python:3.10-slim

ARG IMAGE_TAG
ENV APP_VERSION=$IMAGE_TAG

WORKDIR /app


RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "app.py"]
