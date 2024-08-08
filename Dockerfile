FROM python:3.12-slim

WORKDIR /app
COPY . .

RUN pip install .

EXPOSE 8000
CMD uvicorn --host 0.0.0.0 madr.app:app
