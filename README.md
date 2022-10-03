# CBasicoDjango
Curso Básico de Django

## ¿Qué es Django?
  Es uno de los frameworks más populares para crear web apps.

  Es el segundo framework de desarrollo web más usado, siendo Flask el más usado solo por un 1% y el tercero siendo FastAPI.

  Django es un framework, conjunto de reglas y código creado por terceros que te sirve para crear app webs.

  - Aplicaciones importantes que usan django: Instagram, Pinterest, NATGEO, Platzi
  - Django es grati y Open Source
  - Framerwork veloz, es seguro y escalable (Pueda crecer de manera sencilla)
  - Es el segundo framework en el top3.

## Instalación de Django
  Para desarrollar con Djando utilizaremos 3 herramientas en particular ***la consola, el editor de código y un navegador***.

  - Nos movemos a la carpeta donde sera albergada el proyecto:
    ```bash
    mkdir cbasicodjango
    cd cbasicodjango
    ```
  - Cuando trabajamos con python es crear un entorno vitual.
    ```python
    # si no lo tienes instalado usar este comando
    sudo apt install python3.10-venv
    # en la terminal ejecutamos
    python3 -m venv venv
    ```
  - Ignoramos la carpeta en nuestro archivo de **.gitignore**, podemos usar esta página para generar [gitignore.io](https://www.toptal.com/developers/gitignore), escribiendo django.
  - Ingresamos a nuestro entorno creado
    ```bash
    # comando que usaremos
    source ./venv/bin/activate
    ``` 
  - Estando dentro de nuestro instalamos django.
    ```bash
    pip install django
    ```
  - Inicializamos el proyecto un repositorio
    ```bash
    git init
    ```
  - Iniciamos Django con el siguiente comando:
    ```bash
    # asignandole un nombre al proyecto
    django-admin startproject cbasicodjangoapp
    # revisamos la creación con
    ls
    ```

## Explorando los archivos que creó Django
  La diferenciación de las dos carpetas: 
    - La primera carpeta **cbasicodjangoapp** es la contenedora de archivos del proyecto, y no tiene vinculación con Django sin causar ningun efecto.
    - La segunda carpeta la que esta por debajo ***cbasicodjangoapp*** si tiene vinculación con Django, es un paquete de python conteniendo todos los archivos que afectan al proyecto internamente.

  Archivos primera carpeta:
  - **manage.py** nos muestra una lista de comandos disponibles para que el proyecto funcione.

  Archivos segunda carpeta:
  - **__init__.py** indica que es un paquete.
  - **asgi.py** y **wsgi.py** es un conjunto de archivos que nos sirve para hacer el deploy el despliegue de nuestra app.
  - **settings.py** es un archivo que contiene toda la información de la configuración del proyecto, (la zona horaria, el lenguaje, las apss internas dentro del proyecto, la base de datos que usamos).
  - **urls.py** es el archivo donde vamos a trabajar las rutas del proyecto, (viene uno ya definido llamado ***admin***).