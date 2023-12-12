# Usa una imagen base de Python
FROM python:3.8.2

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del directorio actual al contenedor en /app
COPY . .

# Especifica el comando por defecto cuando se inicia el contenedor
CMD ["python", "./src/main.py"]
