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

## El servidor de desarrollo
  Siempre que crees un proyecto web (Siendo uno mismo el creador) siempre va “vivir” en dos lugares:

  - En local: Entorno de trabajo que creamos y editamos para desarrollar.
  - En producción, es el servidor (Jamas tocamos el código directamente). 
  
  Nos movemos a la carpeta del proyecto.
  ```bash
  cd nombreproyecto
  ```
  Django nos permite utilizar un servidor (local) de desarrollo. Para ver el servidor local debemos ejecutar el comando: **<code>python3 manage.py runserver</code>**

  Detalle de mensaje:

    - Watching for file … : A cada cambio que hagas en los archivo, Django lo notará y lo reflejará en el servidor.
    - System check identified no issues … : No hay problemas y se silenciaron 0.
    - You have 18 unapplied migration(s) … : No se ha creado una base de datos efectiva.
    - Date, Version Django
    - Using settings ‘premiosplatziapp.settings’: Tomar el archivo settings-py, ver la variables de configuración y aplicarlas para tenerlas disponibles al crear el código.
    - Starting development … : Servidor desplegado (iniciado) de manera local en esta dirección **http://127.0.0.1:8000/**.
    - En el archivo de settings.py la opcion de **DEBUG=true** es para funcionamiento local, al momento de enviarlo a producción simplemente cambiamos su valor a **false**.
