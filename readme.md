Ixelexi
Este proyecto es una aplicación web creada con Django. Proporciona una plataforma para agendar citas para un spa de belleza.

Requisitos previos
Asegúrate de tener instalado Python en tu computadora. 

Instalación
Clona este repositorio en tu computadora:
bash
Copy code
git clone https://github.com/iodaniel/ixelexi.com.git
Accede a la carpeta del proyecto:
python
Copy code
cd [nombre-del-repositorio]
Crea un entorno virtual para el proyecto:
bash
Copy code
python -m env env
Activa el entorno virtual:
bash
Copy code
source venv/bin/activate
Instala las dependencias del proyecto:
Copy code
pip install -r requirements.txt
Ejecuta las migraciones:
Copy code
python manage.py migrate
Crea un superusuario:
Copy code
python manage.py createsuperuser
Inicia el servidor:
Copy code
python manage.py runserver
Abre tu navegador web y accede a la siguiente URL:
javascript
Copy code
http://localhost:8000/
Uso
Para utilizar la aplicacion debes de generar una cuenta para poder acceder al calendario de citas. 

Contribuciones
Las contribuciones son bienvenidas. Por favor, sigue las siguientes instrucciones para contribuir al proyecto:

Crea un fork del repositorio en tu cuenta de GitHub.
Realiza tus cambios en tu fork.
Envía un pull request desde tu fork al repositorio original.
Espera a que tus cambios sean revisados y aceptados.
Licencia
Limitadas no para uso comercial