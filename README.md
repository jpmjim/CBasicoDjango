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

## El método **__str__**
  Explorando la varible donde se encuentra nuestra pregunta:
  ```bash
  #nos dice que es un Question object 
  q
  #accedo a los atributos del objeto, campos definidos
  q.question.text
  #nos da un objeto tipo timezone
  q.pub_date
  #queryset tiene un elemento
  Question.objects.all()
  ```

  El __ str __ es un método para definir el output que van a tener los objetos cuando los llames, de una forma mas detallada. Dentro de nuestras clases definiendo un metodo.
  ```python
  #archivo models.py dentro de la carpeta polls
  #para el metodo Question
  def __str__(self):
    return self.question_text

  #que cada vez que invoquemos un objeto de tipo Question lo que queremos que nos muestre es el question.text, el valor del texto que es la pregunta.
  #para el metodo Choice
  def __str__(self):
    return self.choice_text
  ```

  Metodo personalizado **retornar V o F si la pregunta fue publicada recientemente**:
  ```python
  #que una pregunta fue publicada recientemente si tiene un dia maximo de antiguedad 
  # importamos timezone
  from django.utils import timezone
  # importamos modulo datetime nativo de python
  import datetime
  #metodo personalizado
  #la pregunta tiene una duración de 24 horas para concidir con el metodo
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  ```

  Despues de editar nuestros modelos siempre ejecutar si es necesario:
  ```bash
  # puede no requerir el comando de migrate
  python3 manage.py makemigrations polls
  python manage.py migration
  # regresamos a la consola interactiva
  python3 manage.py shell
  #importar modelos
  from polls.models import Question, Choice
  #ahora si nos da el valor de una pregunta con el nombre de la pregunta.
  Question.objects.all()
  ```

  Hicimos nuestro primer registro en la DB del proyecto.

## Filtrando los objetos creados desde la consola interactiva
  Como que con dos metodos especiales que nos brinda django poder hacer busquedas sobre los mismos objetos que vamos creando "drentro de las preguntas".

  [Making queries](https://docs.djangoproject.com/en/3.2/topics/db/queries/#field-lookups-intro)

  Nos movemos a la consola interactiva:
  ```bash
  python3 manage.py shell
  #importamos nuestros modelos 
  from polls.models import Question, Choice
  #que objetos de tiṕos questions tenemos creados
  Question.objects.all()

  #importamos timezone
  from django.utils import timezone
  #añadimos algunas preguntas mas
  Question(question_text="¿Quien es el mejor profesor de Platzi", pub_date=timezone.now()).save()
  Question(question_text="¿Cual es la mejor escuela de Platzi?", pub_date=timezone.now()).save()
  ```

  Ahora podemos realizar busquedas dentro de estas preguntas:
  - Primer metodo que usaremos es **get** es un comando que solo trae un objeto que cumpla con la condición que se especifica en los parametros:
  ```bash
  #django me permite traer el dato  que cumpla con la condición establecido en los paremetros 
  #ejemplo que me traiga la pregunta cuyo identificador id sea igual a 1
  Question.objects.get(pk=1)
  ```

## El método filter
  Para poder hacer la consulta el cual nos devolvera mas de un objeto dentro de la DB debemos utlizar el metodo **filter**, donde django no va buscar por un objeto si no por el conjunto de objetos que cumplan esa condición:
  ```bash
  #ejemplo 1 todos los objetos cuya llave primaria sea igual a 1
  Question.objects.filter(pk=1)
  #nos trae el objeto en formato de conjunto, en formato de iterable "QuerySet" 
  <QuerySet [<Question: ¿Cual es mejor curso de Platzi?>]>
  #al realizar un consulta con parametro que no existe nos devulve un conjunto vacio a diferencia a get que nos da un error
  Question.objects.filter(pk=1)

  #ejemplo 2 por la fecha de publicacion, un operador especial el doble guion abajo "__" el cual nos permite acceder a atributos internos para poder hacer una busqueda mucho mas extensa sobre los datos.
  #sobre los datos de tipo fecha el atributo para buscar por año es "year"
  #traeme todas la preguntas que se publicaron este año, devolviendo nuestras 3 preguntas 
  Question.objects.filter(pub_date___year=timezone.now().year)

  #ejemplo3 traerme todos las preguntas cuyo question_text comiencen con "¿Cual"
  Question.objects.filter(question_text__startswith="Cual")
  ```

## Accediendo al conjunto de respuestas
  No tenemos respuestas a nuestras preguntas estan vacias, no existen opciones para darle a elegir al usuario.

  Nos centraremos en las respuestas de cada una de las preguntas.
  ```bash
  #traerme una pregunta y guardarla en una variable
  q = Question.objects.get(pk=1)
  #revisamos la variable nos devuelve nuestra pregunta

  #como vemos que respuesta tiene la pregunta, acceder al conjunto de respuestas que contiene la pregunta
  q.choice_set.all()

  #creamos las respuestas apartir de cada una de las preguntas que correspondan
  #tomando los atributos que pide el choice
  q.choice_set.create(choice_text="Curso Básico de Python", votes=0)
  q.choice_set.create(choice_text="Curso de Fundamentos de Ingeniería de Software", votes=0)
  q.choice_set.create(choice_text="Curso de Elixir", votes=0)
  #volvemos a ejecutar, tenemos un conjunto de respuestas relacionadas a la pregunta con PK=1 
  q.choice_set.all()
  #acceder cuantas respuestas tiene una pregunta, némero exacto
  q.choice_set.count()
  #consulta con el metodo filter, el conjunto de respuestas que cumplan  con la condición "cuya fecha de publicación de la pregunta a la que pertenecen tenga un año que sea igual al año actual" obtenemos 3 respuestas.
  Choice.objects.filter(question__pub_date__year=timezone.now().year)
  ```

  ### Las formas de crear una Choice (Explicación):
  Cuando una clase/tabla Choice tiene una llave foranea hacia una clase/tabla Question, existen 2 formas de crear las “choices” de una “question” especifica.

  - La primera forma es crear la choice desde su clase, referenciando referenciando el objeto exacto de la question a la que pertenece. Es decir:
  ```bash
  #Primero encontramos el objeto de la question a la que le queremos añadir la choice.
  my_question = Question.objects.get(pk=1)

  #Luego le pasamos ese objeto a la choice.
  my_choice = Choice(
    question_id = my_question,
    choice_text = "text of my choice"
  )
  #OJO: Como dice un compañero, el argumento "votes" no es necesario pasarlo pues ya 	definimos en el modelo de Choice que tendrá un valor predeterminado de 0

  my_choice.save() # Si lo hacemos con esta tecnica es necesario guardar para que los 	cambios se hagan en la db.
  ```

  - La segunda forma, en teoria consiste en que django tiene una API que nos ayuda a encontrar todas las clases que tienen una relación por llave foranea hacia nuestra clase/tabla X (Es decir, en este caso nosotros podemos acceder a todas las clases conectadas por llave foranea a nuestra clase Question , que en este caso solo tenemos la clase Choice pero podrían ser más). He creado una clase igual a Choice pero llamada OptionalChoice y puedo crear sus objetos de la misma forma en la que el profesor lo hace en el video con la clase Choice, así:
  ```bash
  my_question = Question.objects.get(pk=1) #Objeto de la question
  my_question.optionalquestion_set.create(choice_text = "text of my optional choice")
  #Recordar que con esta forma de hacer las cosas no es necesario usar el método save().
  ```

## El administrador de Django
  Una de las ventajas de Django es que posee un administrador de datos de fábrica. La manipulación de datos sin tocar código mediante una interfaz gráfica.

  Nos salimos de nuestra consola interactiva **exit()**.

  Comandos:
  ```bash
  # donde definiremos un usuario y contraseña para poder acceder al administrador de Django
  #ejecutamos el comando
  python3 manage.py createsuperuser
  #nos pedira un nombre de usuario, un correo y la contraseña.
  #al terminar nos moveremos al nevegador a la siguiente dirección
  http://127.0.0.1:8000/admin/login/?next=/admin/
  #donde podremos ingresar al administrador, donde tambien podemos acceder con otras cuentas aparte del super usuario  que podamos crear en la consola.
  ```

  Debemos hacer disponibles a nuestros modelos dentro de administrador, nos diregimos a nuestro archivo de **admin.py** que se encuentra dentro de la carpeta de polls:
  ```python
  #importamos el modelo
  from .models import Choice, Question
  #resgistramos el modelo dentro del administrador 
  admin.site.register(Question) #nuestras preguntas
  admin.site.register(Choice) #las respuestas
  ```

  Dentro administrador podemos acceder a todas las aplicaciones de forma gráfica como ejemplo a nuestra app de Polls, donde por dentro tenemos nuestras preguntas y respuestas ya antes vistas mediante la consola.

## ¿Qué son las views o vistas?
  Django al ser un framework de desarrollo web necesita a cierto punto mostrar páginas web, por que una aplicación web es un conjunto de páginas web que podemos ver y poder interactuar dentro de Django vamos a trabajar mediante las **vistas** o **Views**

  ### Diferencia entre MVC y MTV
  Muy similar a MVC (Modelo, vista, controlador) donde:
  - Modelo - Hace referencia a todo lo que tiene que ver con bases de datos.
  - Vista - Con la parte visual.
  - Controlador - Con toda la parte lógica.

  MTV => MVC:

    Views + Urls => Controller
    Templates => View
    Models => Model

  ![](https://static.platzi.com/media/user_upload/Django-73d3c797-4724-493a-b32b-c666ba1cd545.jpg)

  ### En Django siendo MTV
  - Modelo - Hace referencia a todo lo que tiene que ver con bases de datos (En este caso Django hace demasiada alusión a su nombre donde las bases de datos quedan implícitas y manejamos todo con el ORM)

  - Template - En este caso no debemos confundir el View del MTV con el del MVC puesto en que en Django no hace referencia a lo visual, template si hace alusión con la parte visual de las Web Apps con Django.

  - View - Todo lo relacionado con la lógica es aquí donde entra el tema de las vistas genéricas y demás (Que si solo nos especializamos en el back con Django es lo que mas utilizaremos)

## Creando vistas para la aplicación
  Ya sabesmo que son las vistas, que una aplicación en Django necesita mostrar páginas web que una página web siempre se correspondra a una vista que se expresara con una una función o una clase.

  Como realizar algunas vistas dentro de nuestro archivo de **viwes.py** que se encuentra de la carpeta de polls y para poder añadirlas debemos trabajar dentro de **urls.py** creando las rutas de cada uno de las vistas.
  
  Dentro del archivo podemos encontrar una vista que anterioridad creamos llamado index que es una vista basada en función, las siempre reciben un objeto de tipo http request que al responder muestra una respuesta httprequest en este cado con un string **"hola mundo"**.

## Templates de Django
  Ya tenemos nuestras vistas, ahora pasaremos al frontend las templates para cada una de nuestras vistas ligandolas.

  Para crear las templates o el frontend como quieran llamarlo: 
  - Debemos irnos a la carpeta de la aplicación donde se este trabajando y creamos una nueva carpeta llamada **templates** 
  - Dentro de templates creamos una nueva llamada **polls** donde se desarrolla el frontend de la app

  Dentro de Django para poder trabajar con las templates el frontend, es leer toda la estructura del proyecto tomar todas las carpetas templates para al final combinarlas en una sola. Por eso la creación de subdirectorios de cada de una de las aplicaciones.

  Django tiene un lenguaje de programación para trabajar el frontend que se llama **Django Template System** el cual se crea utilizando los simbolos de **{}** llave y de porcentaje **%**.

  - Dentro de nuestro Visual Studio Code instalamos el plugin de [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django). Para poder trabajar con el auto completado.
  - Para la parte de html dentro de Django, presionamos las teclas de **<kbd>control</kbd> + <kbd>shift</kbd> + <kbd>p</kbd>**, buscamos settings.json elegimos la option de **Open Settings(JSON)** un <kbd>enter</kbd> y abrimos el archivo para poder editarlo:
  ```bash
  # dentro settings.json
  # añadimos las siguientes lineas para el autocompletado de html dentro de django-html
  {
    "emmet.includeLanguages": {
      "django-html": "html"
    },
  }
  ```
  - Y estando dentro de una template de Django podremos trabajar cada uno de las vistas usando html para el desarrollo de frontend:
  ```python
  {% if latest_question_list %}
    <ul></ul>
  {% endif %}
  ```

## Creando el template del home
  - Comenzaremos por nuestro **home**, la vista del index el archivo de ***index.html*** que se encuentra en **polls/templates/polls** mostrandonos una lista de las preguntas que tenemos.
    ```bash
    #template
    {% if latest_question_list %}
      <ul>
      {% for question in latest_question_list  %}
        <li><a href="/polls/{{ question.id }}">{{ question.question_text }}</a></li>
      {% endfor %}
      </ul>
    {% else %}
      <p>No polls are available.</p>
    {% endif %}
    ```
  - Y dentro de nuestras vistas:
    ```bash
    #view index
    def index(request):
      latest_question_list = Question.objects.all()
      return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
      })
    ```
  - El render es una función importada de Django. Necesita tres parámetros
    - El request
    - La ubicación de la template correlacionada. En la ruta se omite la carpeta /template/ ya que Django junta todas las carpetas templates de todas las aplicaciones de nuestro proyecto y las hace una sola
    - Un objeto con la o las variables que le estaremos pasando a nuestra template.
  
  - Puede recibir más parametros, es un shortcut functions de Django, en este documento cortico encontrarás toda la información valiosa para entender el funcionamiento más a profundidad, espero sea de ayuda. Allí se tratan 4 puntos importantes:
    - render()
    - redirect()
    - get_object_or_404()
    - get_list_or_404()
  
  - Django, al igual que FastAPI y Flask usan un lenguaje de templates llamado Jinja( la sintaxis {%%}, {{}}, etc, que menciona), [aquí](https://jinja.palletsprojects.com/en/3.0.x/templates/) les dejo la documentación completa.

  - [Django shortcut functions](https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/)

## Elevando el error 404
  - Cuando un usuario no encuentra algo dentro de la página web nosotros devemos elevar un erro http, en este caso el error 404.

  - Una vista en Django es responsable de dos cosas devolver una respuesta http satisfactoria o de devolver un error.
  
  - HTTP Responses:
    - 100: Información
    - 200: Todo salió bien.
    - 300: Redirección.
    - 400: Error del usuario
    - 500: Error del servidor.

  - Personalizar Error 404 puedes hacer lo siguiente:
    ![](https://static.platzi.com/media/user_upload/404-9d000850-799e-47d6-9afa-2b498fb45420.jpg)
  - En settings.py debes modificar lo siguiente:
    ```python
    DEBUG = False
    ALLOWED_HOSTS = ['*']
    ```
  - Y el archivo debe ir dentro de polls/templates/404.html
    ![](https://static.platzi.com/media/user_upload/Captura%20de%20pantalla%20de%202022-02-05%2000-42-19-e60d1449-d121-4b56-89ba-d351ea78a33f.jpg)

## Utilizando la etiqueta url para evitar el hard coding
  - Dentro de nuestra archivo de **index.html** existe una inconsistencia, es que nunca deberiamos ***hard codear*** un valor "de darle un valor exacto a algo que puede cambiar en el tiempo":
  - En nuestro link de **href** donde estamos especificando una dirección estatica, el cual más adelante podemos cambiar alguna otra.
  - Para poder evitar esto debemos a empezar modularizar el código y cambiar el mal hard coding que se escribio.

  - [El lenguaje de plantillas de Django](https://docs.djangoproject.com/en/4.0/ref/templates/language/)
  - [Etiquetas y filtros de plantilla incorporados](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/)

## Formularios: lo básico
  Es uno de los conceptos fundamentales que deberia saber un **backend developer en python**, los formularios es campos los cuales deben ser rellenados por el usuario, tales datos seran procesados para el debido guardadp en la base de dato"s.

  Nos centraremos en nuestro archivo de ***detail.html*** para tenerlo de manera funcional.

## Creando la vista vote
  El contador de votos para cada uno de las preguntas de sus opciones.

## Creando la vista results
  Visualizar la vista de resultados cuantos votos tienes cada uno de las opciones que tiene la pregunta.

## Generic Views o Class Based Views
  El principio de **Don’t Repeat Yourself**, por ejemplo que tenemos dentro de nuestro archivo de ***views.py*** con las funciones de "detail y results" que tienen la misma estructura rompiendo con el principio de no repetir.

  Las vistas basadas en clases utilizan atributos, a diferencia view function que utilizan parametros. Ademas de tener metodos que te ayudan segun tu desarrollo.

  Dentro de django tenemos muchas posibilidades que vienen de base como:
  - **ListView** que esta diseñada para traer varios elementos de la BD renderizar un templa y mostrarlo
  - **LoginView** y **LogoutView** la vista que permite a los usuarios loguearse o salir.
  - **CreateView** **UpdateView** para edición de registros dentro de la BD como perfil. 
  - [Lista de Classy Class-Based Views](https://ccbv.co.uk/)