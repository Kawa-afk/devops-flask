# Wybierz obraz bazowy z Pythonem
FROM python:3.10-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj pliki aplikacji do obrazu
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Ustaw polecenie startowe
CMD ["python", "app.py"]