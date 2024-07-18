import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

from app import create_app

# Crear la aplicación y obtener la instancia de la base de datos
app, _ = create_app()  # Ignorar la base de datos para este archivo

if __name__ == '__main__':
    app.run(debug=True)
