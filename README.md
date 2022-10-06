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

## Nuestro primer proyecto: Premios Platzi App
  [Escribiendo tu primera aplicación Django](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
  Dentro de Django hay 2 cosas importantes para diferenciar:
  
  - Proyecto : Un proyecto es una colección de configuraciones y aplicaciones para un sitio web en particular. Un proyecto puede contener varias aplicaciones. Una aplicación puede estar en varios proyectos.

  - Un proyecto en Django, es un conjunto de aplicaciones. Ejemplo: Instagram es un proyecto de Django, que tiene varias aplicaciones, como:
    ```bash
    Feed (donde se cargan las fotos)
    Stories
    Messages
    Etc
    ```
  - Apps : Una aplicación es una aplicación web que hace algo, por ejemplo, un sistema de blogs, una base de datos de registros públicos o una pequeña aplicación de encuestas.

  Cada aplicación que escribe en Django consta de un paquete de Python que sigue una determinada convención. Django viene con una utilidad que genera automáticamente la estructura básica de directorios de una aplicación, por lo que puede concentrarse en escribir código en lugar de crear directorios.

  ![](https://static.platzi.com/media/user_upload/Django-file-Structure-46ebc589-0736-4b81-8cba-e97348f2206c.jpg)

## Nuestro primer proyecto: Premios Platzi App 2
  - Dentro de nuestro proyecto creamos una aplicación llamado polls:
  ```bash
  # dentro de la carpeta del proyecto
  #comando
  python3 manage.py startapp nombre_app
  ```

  - Dentro de la nueva app trabajaremos con el archivo **viwes.py** creando un hola mundo.
  ```python
  #dentro del archivo
  from django.http import HttpResponse 
  # esta es una clase que permite ejecutar una respuesta http

  #función que recibe una request como parametro
  def index(request):
    return HttpResponse("Hello World")
  ```

  - Para visualizar nuestro hello world en nuestro navegador:
  ```python
  #nos movemos dentro de la carpeta del proyectoapp el archivo de urls.py
  #creamos un nuevo elemento dentro del path
  path("polls/", include("polls.urls"))
  ```

  - Dentro de la carpeta de la app polls creamos un archivo **urls.py**.
  ```python
  from django.urls import path
  from . import views
  urlpatterns = [
    path("", views.index, name="index")
  ]
  ```
  Dentro de cada aplicación nueva deben tener un archivo **urls.py** donde contendra una lista de urls que puedan añadir, que a partir de la funcion **include** desde archivo principal por llamarlo que se  encuentra en la carpeta del proyecto se añadira todas las urls de dicha aplicación antes creadas.

  Podremos ver nuestro ***"Hello World""** en la siguiente dirección **http://localhost:8000/polls/**.

## Ajustando el archivo settings.py
  DATABASES: Configuración y conexión a la BD como prederterminado nos coloca **sqlite3** pero tambien podemos usar ***mysql, postgressql,oracle. (Django no soporta bases de datos no relacionales):
  ```python
  #dentro del archivo de settings.py
  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': BASE_DIR / 'db.sqlite3', #sqlite no necesita de otras varibles
      # otras variables que nos podemos encontrar son
      'USER':
      'PASSWORD':
      #para poder acceder a una base dadatos como mysql o postgres 
    }
  }

  # podemos definir nuestra zona horaria, estamos trabajando con zona horaria universal la cual podemos cambiar desde donde nos encontremos.
  TIME_ZONE = 'UTC'

  #INSTALLED_APPS: Indica cuáles son las aplicaciones instaladas en el proyecto
  INSTALLED_APPS = [
    'django.contrib.admin', # Administrador de Django
    'django.contrib.auth', # Maneja la autenticacion de usuarios
    'django.contrib.contenttypes', # Maneja formatos de archivos
    'django.contrib.sessions', # Maneja sesiones de usuarios
    'django.contrib.messages', # Maneja comunicaciones entre usuarios
    'django.contrib.staticfiles', # Maneja archivos estaticos (HTML, CSS, JS)
  ]
  ```
  [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

## ¿Qué es ORM? ¿Qué es un modelo?
  Un ORM (Object-Relational Mapping) es una técnica que nos permite crear una Base de Datos Orientada a Objectos (virtual), que opera sobre la Base de Datos Relacional (real).

  Utilizando un ORM podemos operar sobre la base de datos aprovechando las características propias de la orientación a objetos, como herencia y polimorfismo.

  También podemos acceder a los atributos de una Entidad de la misma forma que accedemos a los atributos de una Clase, realizar operaciones para obtener, crear, modificar y eliminar datos, todo desde el código de programación sin tener que escribir SQL.

  Esto además nos permite escribir el código una sola vez y garantizarnos que va a seguir funcionando incluso si en el futuro se cambia el motor de Base de Datos (por ejemplo, de MySQL a Microsoft SQL Server).

  ![](https://static.platzi.com/media/user_upload/Untitled%20%281%29-1d6350c3-b6d5-4752-ae16-2bd4d9210376.jpg)

## Creando un diagrama entidad-relación para nuestro proyecto
  En es este ejemplo usaremos una relación de uno a muchos, por que una pregunta va tener muchas opciones.
  
  Diagrama entidad relación:
  - Nuestra tabla **questions** tendra tres atributos o columnas(termininologia de base de datos).
  ```bash
    id -----------------int (llave primaria)
    question_text-------varchar (texto de la pregunta)
    pub_date------------datetime (fecha de publicacion)
  ```
  - En el modelo entidad relación cuando tenemos atributos(columnas) relacionados entre modelos(tablas). Se le colocas FK junto al nombre del atributo en el modelo(tabla) en que está relacionando. Esto significa Llave foránea. No ayuda a identificar las columnas relacionadas al momento de pasarlo a código.

  - La tabla **choices** sus atributos.
  ```bash
    id -------------- int
    fk_question------ int (llave foranea "el id de una pregunta")
    choice_text ----- varchar (texto de la opcion)
    votes ----------- int (va ser un contador)
  ```
  Herramienta que podemos usar para el desarrollo de nuestro diagrama [dbdiagram.io](https://dbdiagram.io/home)

  Usando este código:
  ```bash
  Table questions {
    id int [pk, increment]
    question_text varchar
    pub_date datetime
  }

  Table choices {
    id int [pk, increment]
    choice_text varchar
    votes int
    question int [ref: > questions.id]
  }
  ```
  ![](https://static.platzi.com/media/user_upload/PremiosPlatzi-588f66d0-82e2-461f-a3e6-53a2232bfd14.jpg)

## Creando los modelos Question y Choice
  Dentro del archivo de **models.py** que se encuentra en la aplicación de ***polls***.
  
  Las tablas se equivalen a modelos o clases en un archivo de python, nuestro archivo de models vendria hacer la base de datos.
  ```python
  # nuestros modelos
  class Question(models.Model):
    # Atributos
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

  class Choices(models.Model):
    # Atributos
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
  ```

  Dentro de Django genera la **llave primaria** con el modificador de autoincrementar, lo cual no necesitamos crear o añadir el id.

  Nos movemos al archivo de **settings.py** donde añadiremos la aplicación de ***polls***.
  ```python
  INSTALLED_APPS = [
    #aplicación creadas
    "polls.apps.PollsConfig",
    #aplicaciones nativas de django 
    'django.contrib.admin',
    ...
  ]
  ```
  Ejecutamos dos comandos dentro de la carpeta del proyecto:
  ```bash
  # crea un archivo dentro de la carpeta migrations que se enecuentra en polls
  # donde automaticamente django describe toda la creacion de las tablas en la base de datos,
  # uso del concepto de ORM, toma esos modelos convirtiendolos en tablas dentro de la db.
  python3 manage.py makemigrations polls 
  # ejecutando la migración del archivo hacia la bd.
  python3 manage.py migrate
  ```

  Sirve sobre todo al momento de trabajar de forma colaborativa, para poder replicar la estructura creada en otras partes.

## La consola interactiva de Django
  Sabemos que dentro de python tenemos una consola interactiva al cual accedemos con el comando **python3** donde podemos ejecutar lineas de codigo sin la necesidad de crear un archivo y ejecutarlo.

  Comando para acceder a la consola interactiva de Django:
  ```bash
  #consola interactiva tenemos acceso al proyecto
  python3 manage.py shell
  #nos muestra de esta forma
  Python 3.10.6 (main, Aug 10 2022, 11:40:04) [GCC 11.3.0] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  (InteractiveConsole)
  ```

  Renombramos nuestro modelo Choices a ***Choice*** lo cual debemos volver a ejecutar los comandos:
  ```bash
  # creandose una nueva migracion el archivo de nombre 0002_rename_choices_choice.py
  python3 manage.py makemigrations polls
  # aplicamos la migración
  python3 manage.py migrate
  ```

  Comandos dentro de la consola interactiva:
  ```bash
  #llamado a los modelos dentro de polls
  from polls.models import Choice, Question
  #acceder a los atributos, con un conjunto de datos
  Question.objects.all()
  #importamos la función timezone para crear objetos de tipo date, antes de crear una pregunta
  from django.utils import timezone
  #creamos nuestra pregunta dentro de una variable
  q = Question(question_text="¿Cual es el mejor curso de Platzi?", pub_date=timezone.now())
  #para guardar nuestra pregunta
  q.save()
  ```

