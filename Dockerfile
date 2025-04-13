# Imagen base con Python ya instalado
FROM python:3.13

# Crear el directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del backend
COPY . .

# Exponer el puerto (el que uses en tu proyecto Django, normalmente 8000)
EXPOSE 8000

# Comando por defecto para arrancar el servidor (puedes cambiar esto por gunicorn)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
