#Desde que version de python quiero que corra
FROM python:3.11.0
#crear la carpeta dentro del contenedor
WORKDIR /app
#Copiar el archivo de las dependencias al contenedor
COPY requirements.txt /app/requirements.txt
#instalar las dependencias y actualización
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#copiar el código y llevalo a la carpeta
COPY . /app
#mantiene encendido el contenedor 
CMD bash -c "while true; do sleep 1; done"
