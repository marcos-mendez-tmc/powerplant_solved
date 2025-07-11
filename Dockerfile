FROM python:3.8-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY app/ ./app/

# Exponer el puerto
EXPOSE 8888

# Comando de ejecución
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8888"]
