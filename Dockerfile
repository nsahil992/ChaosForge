# BUILD STAGE

FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# RUN STAGE

FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY app/ app/

RUN useradd -m chaosuser

USER chaosuser

EXPOSE 5050

CMD ["python", "app/app.py"]