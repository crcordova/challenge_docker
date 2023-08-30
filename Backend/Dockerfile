FROM python:3.10-slim

WORKDIR /app

COPY /requirements.txt .
COPY .env /app/

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de los archivos de la aplicación al directorio de trabajo
COPY . .

CMD ["python", "./Report.py"]