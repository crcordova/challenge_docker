
FROM python:3.10-slim

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los archivos de requerimientos al directorio de trabajo
COPY /requirements.txt .
COPY ..env /app/

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de los archivos de la aplicación al directorio de trabajo
COPY . .

# Exponemos el puerto en el que la aplicación FastAPI se ejecutará
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]