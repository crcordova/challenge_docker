FROM python:3.10-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY ../.env /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./bd_init.py" ]