FROM python:3.8

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requisitos y el script de Python al contenedor
COPY requirements.txt /app/
COPY tu_script.py /app/
COPY .env /app/

# Instalar los requisitos
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar el script de Python al iniciar el contenedor
CMD ["python", "Report.py"]