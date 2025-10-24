FROM python:3.11-slim

WORKDIR /app

COPY ./app /app/
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y wireguard-tools iproute2 iptables

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
