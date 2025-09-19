# Koristi zvanični Python imidž
FROM python:3.11-slim

# Set radnog direktorijuma
WORKDIR /app

# Kopiraj requirements
COPY requirements.txt .

# Instaliraj zavisnosti
RUN pip install --no-cache-dir -r requirements.txt

# Kopiraj ceo projekat
COPY ./app ./app

# Pokreni aplikaciju
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
