FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8000

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Fichiers statiques collectés au build (servis par WhiteNoise)
RUN SECRET_KEY=build-only python manage.py collectstatic --noinput

RUN chmod +x start.sh && useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 8000
CMD ["./start.sh"]
