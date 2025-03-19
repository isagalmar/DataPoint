# Usar la imagen base oficial de Python 3.12.3
FROM python:3.12.3-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor (si tienes dependencias)
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código de la aplicación al contenedor
COPY app app
COPY data data

ENV DATAPOINT_PORT=8007

# Exponer el puerto que va a usar la aplicación (si es necesario)
EXPOSE ${DATAPOINT_PORT}


# Comando para ejecutar la aplicación
ENTRYPOINT fastapi run app/main.py --port $DATAPOINT_PORT
