FROM python:3.12-slim

WORKDIR /src

COPY req.txt .

RUN pip install --no-cache-dir -r req.txt

COPY src .

COPY tg_service.db .

CMD ["python", "main.py"]
