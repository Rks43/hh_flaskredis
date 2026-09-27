# Flask + Redis: счётчик посещений

Веб-приложение на Flask, которое считает количество посещений и хранит их в Redis. Всё упаковано в Docker и запускается через docker-compose.

## Стек

- Python 3.11 (Flask)
- Redis (хранение счётчика)
- Docker / Docker Compose

## Как запустить

```bash
docker-compose up -d
