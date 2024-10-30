# Guía de Inicio con Django

## ÍNDICE
- <a href="#primeros">Primeros pasos</a>
- <a href="#modelo">Modelo</a>
- <a href="#vistas">Vistas</a>
- <a href="#url">URL</a>
- <a href="#plantillas">Plantillas</a>
- <a href="#formulario">Formulario</a>
- <a href="#css">Añadir CSS</a>

Esta guía la hice para no olvidarme de cómo configurar un entorno de desarrollo con Django paso a paso.

## Flujo de trabajo
1. `Modelo:` Definir los datos que se necesitan y crear las tablas en la base de datos.
2. `Vistas:` La lógca de negocio para manejar las vistas.
3. `URL:` Conectar la vista con una URL para que sea accesble en el ordenador.
4. `Plantillas:` Crear la interfaz HTML y enlazarla con la vista para mostrar los datos.

## Antes que nada: Crear un directorio para el proyecto

Primero, crea un directorio donde se alojará tu proyecto y ubícate dentro de este:

```bash
mkdir supertodo && cd supertodo
```
## 1. Crear entorno virtual <p id="primeros"></p>
Es buena práctica trabajar con un entorno virtual para aislar las dependencias del proyecto. 
```pyhton
python -m venv .venv --prompt supertodo
```
Este comando creará un entorno virtual en la carpeta .venv y establecerá questlog como su nombre para que sea más fácil identificarlo en tu terminal.
## 2. Activar el entorno virtual
Es importante activar el entorno virtual siempre que trabajes en el proyecto para que las dependencias se gestionen correctamente.
Importante activarlo siempre.
```pyhton
source .venv/bin/activate
```
Si todo sale bien, verás que el prompt de la terminal cambia a algo como (questlog).
## 3. Instalar el framework Django
Este comando instalará Django y sus dependencias en tu entorno virtual:
```pyhton
pip install django
```
##  4. Crear la estructura del proyecto
Usa el siguiente comando para generar la estructura inicial de tu proyecto Django:

```pyhton
django-admin startproject main .
```

El último . asegura que la estructura del proyecto se cree en el directorio actual. Deberías ver un archivo manage.py y una carpeta llamada questlog creada en tu directorio.

## 5. Aplicar las premras migraciones
Django viene con un sistema de migraciones que administra los cambios en la base de datos. Antes de empezar a usar el proyecto, aplica las migraciones iniciales:
```pyhton
./manage.py migrate
```
Este comando creará las tablas necesarias en la base de datos, como la gestión de usuarios, permisos, entre otras.
## 6. Crear un usuario administrador.
Para acceder a la interfaz administrativa de Django, primero necesitas crear un usuario administrador:
```pyhton
./manage.py createsuperuser
```
Sigue las indicaciones en la terminal para ingresar un nombre de usuario, dirección de correo electrónico y una contraseña.
## 7. Iniciar el servidor de desarrollo.
Para empezar a trabajar con el proyecto y verlo en acción, inicia el servidor de desarrollo:
```pyhton
./manage.py runserver
```
Por defecto, el servidor estará corriendo en http://127.0.0.1:8000/. Para acceder a la interfaz administrativa, abre esa URL en tu navegador y agrega /admin al final: http://127.0.0.1:8000/admin.

##  Crear una apliciación dentro del proyecto
En Django, las funcionalidades suelen estar organizadas en aplicaciones independientes. Para crear una nueva aplicación dentro de tu proyecto, usa el siguiente comando:

```pyhton
./manage.py startapp tasks
```
Esto creará una nueva carpeta tasks con la estructura básica de una aplicación Django. Recuerda agregar la nueva app a INSTALLED_APPS en settings.py.

# MODELO <p id="modelo"></p>
Los modelos son la representación conceptual abstracta de los datos que queremos represnetar en la tabla.
- Cada módulo se define como una clase en python y cada atributo representa un campo de la tabla.

- Cuando se define un modelo y se reistra, django crea automáticamente las tablas de la base de datos mediante migraciones.
- Djangog proporciona herramientas para manejar las operaciones CRUD(crear, leer, actualizar, eliminar), simplificando la interacción con la base de datos.

## 1. Creamos un primer modelo.

Se vería algo como esto.
Para saber las caracterśiticas de los tipos de datos, se puede acudir a la documentación de Django.

También es en este caso es importante para más adelante añadirle un método str, para controlar cómo se representará el objeto cuando se convierta en un string.

```python
from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=150, unique=True)
    complete_before = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    
```

## 2. Hacer migraciones.
Como hemos modificado la estructura de la aplcación, tenemos que aplicar migraciones en la terminal.

```python
./manage.py makemigrations
```
```python
./manage.py migrate
```

## 3. Activar el modelo en la interfaz administrativa.

Para ello, abre el fichero `admin.py`. 
Registra el modelo Task en el panel administrativo para que puedas gestionarlo (crear, actualizar, eliminar) desde el mismo.

### Añadimos el Slug para que se cree automáticamente en la interfaz admnistrativa
- Personaliza la forma en que el campo slug se genera automáticamente a partir del valor del campo task. Esto es especialmente útil para hacer URLs más fáciles de leer o recordar. En este caso lo utlizaremos para la url individual de cada tarea sea su título en formato slug.

Admin.py se verá algo así:

```python

from django.contrib import admin

# Register your models here.
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['task']}
    

admin.site.register(Task, TaskAdmin)

```
## 4. Incluir la aplicación en la lista de aplicaciones instaladas.

Abrimos el fichero `settings.py`
Y en INSTALLED_APPS = [] escribimos nuestra aplicación de la siguiente manera:

**nombreApp**.apps.**nombreApp**Config

La primera letra de del nombreAppConfig en mayúsculas.

Se vería algo así:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks.apps.TasksConfig',
]
```

## 5. Configurar la zona horaria.
En el mismo fichero de settings.py, para configurar la hora de Canarias, vamos a la línea `TIME_ZONE = 'UTC'` y la cambamos por:

`TIME_ZONE = 'Atlantic/Canary'`

## Probar y crear una tarea en la interfaz adminisrativa.
Recordar que para entrar al navegador, escribimos:
`./manage.py runserver`

Y de nuevo, añadimos /admin a la dirección.
Saldrá Tasks, y podremos crear una tarea.

## Interactuar con la base de datos:

Una vez teniendo algún registro

Acceder a la consola interactiva de Django para interactuar con tus modelos y hacer consultas a la base de datos.

`./manage.py shell`

Este comando importa el modelo Task desde el archivo models.py de la aplicación tasks.
 Aquí estás asumiendo que tu aplicación tasks tiene un modelo llamado Task que representa una tarea 

`from tasks.models import Task`

Consulta a la base de datos para obtener taskss los objetos de la tabla que corresponde al modelo Task.

`Task.objects.all()`

Se pueden guardar consultas en variables y acceder a las propiedades del objeto.

`first_task = Task.objects.first()`

`first_task.title`

También podemos crear una nueva tarea desde la terminal.

## 6. Capturar la URL de la aplicacón en url.py
En el fichero urls.py que se encuentra en el directorio main de la aplicación tasks, 
debemos capturar la URL de la aplicación.


```python
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('tasks:task-list')),
    path('', include('tasks.urls', namespace='tasks')),
]
```
### Explicación de las Rutas en Django

### `path('admin/', admin.site.urls):`
Esto define la ruta para la página de administración de Django.

- `'admin/'`: Es la URL que se debe ingresar para acceder al panel de administración (ejemplo: `localhost:8000/admin`).
- `admin.site.urls`: Usa las URLs predefinidas del panel de administración.

### `path('', lambda request: redirect('tasks:task-list')):`
Aquí se establece una redirección automática cuando el usuario accede a la URL base (`'/'`). En este caso:

- `lambda request: redirect('tasks:task-list')`: Usa una función lambda para redirigir la solicitud.
- `'tasks:task-list'`: Esta es la referencia a una vista llamada `task-list` en la aplicación `tasks`. Este nombre puede estar definido en el archivo `urls.py` dentro de la aplicación `tasks` y apunta a una vista específica (por ejemplo, una lista de tareas).

### `path('', include('tasks.urls', namespace='tasks')):`
Esto incluye todas las URLs definidas en el archivo `urls.py` dentro de la aplicación `tasks`.

- `'tasks.urls'`: Se refiere al archivo de URLs dentro de la aplicación `tasks` (e.g., `tasks/urls.py`).
- `namespace='tasks'`: Define un espacio de nombres para las URLs de esta aplicación, permitiendo usar nombres como `'tasks:task-list'` para hacer referencia a las vistas dentro de `tasks`.


# Vistas <p id="vistas"></p>
Las vistas son funciones que se encargan de recibir la petición HTTP, realizar la lógica necesaria y devolver una respuesta HTTP.

# Estructura de una Vista en Django

Una vista en Django es una función o clase que maneja solicitudes HTTP, realiza alguna lógica y devuelve una respuesta HTTP. Aquí está la estructura básica:

## Estructura de una Vista

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ModelName  # Importa modelos para manipular datos
from .forms import FormName    # Importa formularios personalizados

def nombre_vista(request, otros_parametros=None):
# 1. Procesar solicitud (POST, GET)
# Aquí se verifica el tipo de solicitud (GET o POST), y se maneja en función de ello.
if request.method == 'POST':
    # Procesar datos enviados a través de un formulario (POST)
    pass
else:
    # Manejar solicitud GET o mostrar página inicial
    pass

# 2. Obtener o manipular datos usando modelos
# Interactuar con la base de datos para obtener o modificar datos
items = ModelName.objects.all()

# 3. Lógica adicional (filtrar, ordenar, validar, etc.)
# Procesar los datos obtenidos si es necesario (filtrar, ordenar, etc.)
filtered_items = items.filter(attribute='value')

# 4. Crear contexto (datos) para pasar al template
# Creamos un diccionario con los datos que queremos enviar al template
contexto = {
    'items': items,
    'filtered_items': filtered_items,
    'num_items': items.count(),
}

# 5. Renderizar y devolver la respuesta
# Usamos render() para cargar una plantilla y pasarle el contexto
return render(request, 'plantilla.html', contexto)

```
## En nuestro supertodo:

### Importaciones
```python
from django.shortcuts import redirect, render
from django.utils.text import slugify

from tasks.models import Task

from .form import AddTaskForm, EditTaskForm
```
`redirect:` Redirige a otra URL.

`render:` Carga una plantilla y pasa contexto (datos) para mostrar al usuario.

`slugify:` Convierte un texto en un "slug", que es una versión amigable de una 
cadena para URLs (por ejemplo, "Mi Tarea Importante" → "mi-tarea-importante").

`Task:` Modelo que representa una tarea en la base de datos.

`AddTaskForm y EditTaskForm:` Formularios personalizados para añadir y editar tareas.

### 1. Vista para la lista de todas las tareas.
```python
def task_list(request):
    num_tasks = Task.objects.count()  # Cuenta total de tareas
    tasks = Task.objects.all()        # Todas las tareas
    completed_tasks = Task.objects.filter(done=True)  # Tareas completadas
    pending_tasks = Task.objects.filter(done=False)   # Tareas pendientes

    return render(
        request,
        'tasks/task-list.html',
        {
            'num_tasks': num_tasks,
            'tasks': tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
        },
    )

```

#### Datos que envía al template:

- num_tasks: Número total de tareas.
- tasks: Todas las tareas.
- completed_tasks: Tareas completadas.
- pending_tasks: Tareas pendientes.
- Plantilla: tasks/task-list.html


###  2. Vista para detalles de una tarea específica.

```python
def task_detail(request, task_slug):
    task = Task.objects.get(slug=task_slug) #utilza el slug para obtener la tarea
    return render(request, 'tasks/task-detail.html', {'task': task})
```

#### Datos que envía al template:

- task: La tarea seleccionada.

- Plantilla: tasks/task-detail.html

### 3. Vista para tareas completadas

```python
def completed_tasks(request):
    tasks = Task.objects.filter(done=True)  # Filtra tareas completadas
    return render(request, 'tasks/task-list.html', {'tasks': tasks})
```

#### Datos que envía al template:

- tasks: Tareas que tienen done=True.

- Plantilla: tasks/task-list.html (reutiliza la plantilla de lista de tareas).

### 4. Vista para tareas pendientes

```python
def pending_tasks(request):
    tasks = Task.objects.filter(done=False)  # Filtra tareas pendientes
    return render(request, 'tasks/task-list.html', {'tasks': tasks})
```
#### Datos que envía al template:

- tasks: Tareas que tienen done=False.

- Plantilla: tasks/task-list.html (reutiliza la misma plantilla).


### 5. Vista para alternar el estado de una tarea (de done=True a done=False o viceversa).
```python
def toggle_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)  # Busca la tarea por su slug
    task.done = not task.done                # Cambia el estado de `done` a lo contrario
    task.save()                              # Guarda los cambios
    return redirect('tasks:task-list')

```
- Redirección: Vuelve a la lista de tareas después de actualizar el estado.

### Las vistas de los formualrios están más adelante donde explco los formularios. <a href="#form">Aquí</a>

### 8. Vista para elminar tarea

```python
def delete_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)

    if request.method == 'POST':
        task.delete()  # Elimina la tarea si se confirma
        return redirect('tasks:task-list')

    return render(request, 'tasks/confirm-delete.html', {'task': task})
```


- Descripción: Permite eliminar una tarea después de confirmarlo.

    - Si es una solicitud POST: Elimina la tarea y redirige a la lista.
    - Si es una solicitud GET: Muestra una página de confirmación.

- Plantilla: tasks/confirm-delete.html

# Las URL <p id="url"></p>

Tenemos que crear un archivo llamado `urls.py` dentro de la aplicación. 


```python
from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/add/', views.add_task, name='add-task'),
    path('tasks/task/<task_slug>/', views.task_detail, name='task-detail'),
    path('tasks/task/<task_slug>/edit/', views.edit_task, name='edit-task'),
    path('tasks/task/<task_slug>/delete/', views.delete_task, name='delete-task'),
    path('tasks/task/<task_slug>/toggle/', views.toggle_task, name='toggle-task'),
    path('tasks/pending/', views.pending_tasks, name='pending-tasks'),
    path('tasks/done/', views.completed_tasks, name='completed-tasks'),
]

```

- `from django.urls import path`: Importa la función path, que se utiliza para definir rutas de URL.
- `from . import views`: Importa el módulo views de la misma aplicación. Esto te permite acceder a las vistas 
que has definido en views.py
- `app_name = 'tasks'`: Define un espacio de nombres para las URLs de esta aplicación. Esto es útil para evitar conflictos de nombres si hay aplicaciones con nombres de URL similares en el proyecto. Se utilizará como prefijo para todas las URLs de esta aplicación, permitiendo referenciarlas de manera más sencilla (por ejemplo, tasks:task-list).

## Rutas Definidas y Vistas Asignadas

Se definen las diferentes rutas y se asignan a vistas específicas:

### `path('tasks/', views.task_list, name='task-list')`
- **URL**: `/tasks/`
- **Vista**: `views.task_list`
- **Nombre**: `'task-list'`
- Esta ruta muestra la lista de tareas.

### `path('tasks/add', views.add_task, name='add-task')`
- **URL**: `/tasks/add`
- **Vista**: `views.add_task`
- **Nombre**: `'add-task'`
- Esta ruta permite agregar una nueva tarea.

### `path('tasks/task/<task_slug>/', views.task_detail, name='task-detail')`
- **URL**: `/tasks/task/<task_slug>/`
- **Vista**: `views.task_detail`
- **Nombre**: `'task-detail'`
- Utiliza un parámetro de URL (`<task_slug>`) para mostrar detalles de una tarea específica. `task_slug` es un identificador único para la tarea.

### `path('tasks/edit/<task_slug>/', views.edit_task, name='edit-task')`
- **URL**: `/tasks/edit/<task_slug>/`
- **Vista**: `views.edit_task`
- **Nombre**: `'edit-task'`
- Esta ruta permite editar una tarea específica usando su `task_slug`.

### `path('tasks/delete/<task_slug>/', views.delete_task, name='delete-task')`
- **URL**: `/tasks/delete/<task_slug>/`
- **Vista**: `views.delete_task`
- **Nombre**: `'delete-task'`
- Esta ruta permite eliminar una tarea específica.

### `path('tasks/toggle/<task_slug>/', views.toggle_task, name='toggle-task')`
- **URL**: `/tasks/toggle/<task_slug>/`
- **Vista**: `views.toggle_task`
- **Nombre**: `'toggle-task'`
- Esta ruta cambia el estado (completada/no completada) de una tarea específica.

### `path('tasks/pending', views.pending_tasks, name='pending-tasks')`
- **URL**: `/tasks/pending`
- **Vista**: `views.pending_tasks`
- **Nombre**: `'pending-tasks'`
- Esta ruta muestra solo las tareas pendientes.

### `path('tasks/done', views.completed_tasks, name='completed-tasks')`
- **URL**: `/tasks/done`
- **Vista**: `views.completed_tasks`
- **Nombre**: `'completed-tasks'`
- Esta ruta muestra solo las tareas completadas.

# Plantillas <p id="plantillas"></p>

Dentro de tasks, creamos la carpeta templates, y dentro de esta, un archivo `base.html`.
Este  archivo será el template base para todas las páginas de la aplicación. 

- Contene la estructura básica de html, añade Bootstrap y un linkeao al <a href="#css">css</a>.

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://kit.fontawesome.com/41e2543a08.js" crossorigin="anonymous"></script>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="{% static 'blog/custom.css' %}">
  <title>{% block title %}Supertodo{% endblock title %}</title>
</head>
<body>
  {% block body %}
  {% endblock body %}
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
```

- `{% load static %}`:  Esta línea carga la biblioteca de plantillas de Django que 
permite utilizar la etiqueta {% static %} para referenciar archivos estáticos 
(como CSS, JavaScript, imágenes, etc.). Esto es necesario para que Django 
pueda resolver la URL correcta para los archivos estáticos que has definido en tu proyecto.


- `{% block body %}` y `{% endblock body %}`:
Este bloque se utiliza para definir el contenido principal de la página. Las plantillas que extiendan esta base pueden añadir su propio contenido en este bloque body.

## Resto de plantillas
Ahora, dentro de templates, creamos la carpeta tasks 
de nuevo para que sea más sencillo de redreccionar, y ahí es donde  
se encuentran las plantillas para las vistas de la aplicación.

Este proyecto tiene:

- `tak-list.html`: lista de todas las tareas
- `task-detail.html`: página de una tarea concreta
- `add-task.html`:   formulario para añadir una tarea
- `edit-task.html`: formularo para edtar tarea
- `confirm-delete.html`: págiina para confirmar si borra una tarea


#### Explcacón de las redreccones dentro de la página.
Por ejemplo:

`{% url 'tasks:task-list' %}"`

- `tasks`: Es el namespace definido para las rutas de la aplicación específica en urls.py.
- `task-list`: Es el nombre de la ruta específica dentro de la aplicación tasks, también definido en urls.py

`{% url 'tasks:toggle-task' task.slug %}`

- A veces se debe poner esto al pasar un parámetro llamado slug a la URL, 
porque esa ruta en particular requiere un identificador único (como task.slug) 
para acceder a una tarea específica. 
-  Al usar task.slug en el template, estamos accediendo al campo slug 
del modelo Task para la instancia actual de task en el bucle. 
Esto permite generar una URL única para cada tarea específica en función de su slug.

### task-list.html

```python
{% extends "base.html" %}
{% block  title %}Supertodo: Tasks{% endblock title %}
{% block body %}
  
  <header class="d-flex justify-content-center py-3 bg-success text-white">
    <ul class="nav nav-pills">
      <li class="nav-item"><a href="{% url 'tasks:task-list' %}" class="nav-link active" aria-current="page">All</a></li>
      <li class="nav-item"><a href="{% url 'tasks:pending-tasks' %}" class="nav-link link-light">Pending</a></li>
      <li class="nav-item"><a href="{% url 'tasks:completed-tasks' %}" class="nav-link link-light">Completed</a></li>
      <li class="nav-item"><a href="{% url 'tasks:add-task' %}" class="nav-link link-light">Add Task</a></li>
  </header>
  <section class="py-5 text-center container">
  <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
  {% for task in  tasks %}

  <div class="col">
    <div class="card shadow-sm">
    
      <div class="card-body">
        <h5 class="card-title"><i class="fa fa-thumb-tack" aria-hidden="true"></i>
          {{  task.name }}
          {% if task.done %}
            <i class="fa-solid fa-circle-check"></i> 
          {% else %}
            <i class="fa-solid fa-clock"></i>
          {% endif %}
        </h5>
        <p class="card-text">{{ task.description }}</p>
        <div class="d-flex justify-content-between align-items-center">
          <div class="btn-group">
            <a class="btn btn-sm btn-outline-secondary" href="{% url 'tasks:task-detail' task.slug %}"><i class="fa-solid fa-eye"></i></a>
            <a href="{% url 'tasks:edit-task' task.slug%}" class="btn btn-sm btn-outline-secondary"><i class="fa-solid fa-pen-to-square"></i></a>
            <a href="{% url 'tasks:delete-task' task.slug%}" class="btn btn-sm btn-outline-secondary"><i class="fa-solid fa-eraser"></i></a>
            <form action="{% url 'tasks:toggle-task' task.slug %}" method="POST" style="display: inline;">
              {% csrf_token %}
              <button type="submit" class="btn btn-sm btn-outline-secondary">
                  {% if task.done %}
                  <i class="fa-solid fa-toggle-on"></i>
                  {% else %}
                  <i class="fa-solid fa-toggle-off"></i>
                  {% endif %}
              </button>
          </form>
          </div>
          <small class="text-body-secondary">{{ task.created_at }}</small>
        </div>
      </div>
    </div>
  </div>

  {% endfor %}
</div>
</section>
{% endblock body %}
```
### Elementos interesantes:

- Utiliza lo sigguiente para insertar la plantlla base:

```python
{% extends "base.html" %}
{% block  title %}Supertodo: Tasks{% endblock title %}
{% block body %}
#resto del código
{% endblock body %}
```
- Esto significa que hereda la estructura y el diseño de base.html y solo reemplaza o agrega contenido en los bloques especificados.
- Dentro de {% block title %}, se especifica el título de la página como "Supertodo: Tasks".
Este bloque reemplaza el contenido del bloque title definido en base.html.
<hr>

- Utliza un bucle para caragar todas las tareas:

```python
{% for task in  tasks %}
#resto del código html para mostrarlas como cards
{% endfor %}
```
- Según si está hecha o no, muestra un icono u otros_parametros
```python
<h5 class="card-title"><i class="fa fa-thumb-tack" aria-hidden="true"></i>
  {{ task.name }}
  {% if task.done %}
    <i class="fa-solid fa-circle-check"></i> 
  {% else %}
    <i class="fa-solid fa-clock"></i>
  {% endif %}
</h5>

```

- Alternar el estado de la tarea
    - Formulario para alternar estado: Este formulario permite alternar entre completado y no completado enviando una solicitud POST.
    - Token CSRF: {% csrf_token %} se usa para proteger el formulario.
    - Botón de alternancia: Dependiendo del estado (task.done), se muestra el ícono de toggle-on o toggle-off.

```python
<form action="{% url 'tasks:toggle-task' task.slug %}" method="POST" style="display: inline;">
  {% csrf_token %}
  <button type="submit" class="btn btn-sm btn-outline-secondary">
      {% if task.done %}
      <i class="fa-solid fa-toggle-on"></i>
      {% else %}
      <i class="fa-solid fa-toggle-off"></i>
      {% endif %}
  </button>
</form>

```
### Task-detail
```html
{% extends "base.html" %}
{% block  title %}Supertodo: Task Detail{% endblock title %}
{% block body %}
<div class="container">
  <div class="card text-center">
    <div class="card-header fa-solid fa-ghost">
      {{ task.created_at }}
    </div>
    <div class="card-body">
      <h5 class="card-title">{{ task.name }}
        {% if task.done %}
            <i class="fa-solid fa-circle-check"></i> 
          {% else %}
            <i class="fa-solid fa-clock"></i>
          {% endif %}
      </h5>
      <p class="card-text">{{ task.description }}</p>
      <form action="{% url 'tasks:toggle-task' task.slug %}" method="POST" style="display: inline;">
        {% csrf_token %}
        <button type="submit" class="btn btn-sm btn-outline-secondary">
            {% if task.done %}
            <i class="fa-solid fa-toggle-on"></i>
            {% else %}
            <i class="fa-solid fa-toggle-off"></i>
            {% endif %}
        </button>
    </form>

    </div>
    <div class="card-footer text-body-secondary">
      <h5>Due date: {{ task.complete_before | date:"d/m/Y" }}</h5>
      <h5>Time left: {{ task.complete_before | timeuntil  }}</h5>
    </div>
  </div>
  <a href="{% url 'tasks:task-list'%}" class="btn btn-primary" >Back</a>
 

</div>
{% endblock body %}
```

- Filtros del template.
    - `date:"d/m/Y"`: sirve para darle formato a la fecha
    -`timeuntil`: muestra el tiiempo restante hasta esa fecha

<a href="https://mkdocs.aprendepython.es/third-party/webdev/django/templates/#filtros">MÁS INFO Y TIPOS DE FILTROS AQUÍ</a>

Antes de hablar de los demás templates, es mportante explicar los formularios.

## FORMULARIOS MODELO <p id="formulario"></p>
<p id="form"><p>
Los formularios modelo en Django son una forma de crear formularios que se relacionan con
modelos de la base de datos. Estos formularios se pueden utilizar para crear, editar
o eliminar registros de la base de datos.

Hay varios tipos y maneras  de crear formularios modelo en Django. Más info <a href="https://mkdocs.aprendepython.es/third-party/webdev/django/forms/#tipos-de-formularios">AQUÍ</a>

En general , para crear un formulario modelo, la sintaxis e sun poco así:

```python

from django import forms

from .models import Post

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task #aquí va el modelo que queremos vincular
        fields = ('name', 'descripton') #los campos del modelo a incluir en el formulario
```


#### IMPORTANTE. 
Los formularios estarán en un archivo que tenemos que crear que se 
llame `form.py` a la misma altura que las vistas y modelos de la aplicación.

Ahora, vamos a desglosar este caso en concreto de formulario.

### FORMULARIO DE TAREAS

```python
from django import forms

from .models import Task



class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before')
        widgets = {'complete_before': forms.DateInput(attrs={'type': 'date'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before')
```


  ```python
  {% extends "base.html" %}
{% block  title %}Supertodo: Edit Task{% endblock title %}
{% block body %}
<div class="container">
<h1>Editando tarea "{{ task.name }}"</h1>
<form method="post">
  {% csrf_token %}
  {{ form }}
  <input type="submit" value="Save Changes" class="btn btn-primary">
</form>
</div>
{% endblock body %}
  ```

### 1. Importaciones y modelo de referencia

```python
from django import forms
from .models import Task
```

- `from django import forms`: Importa el módulo de formularios de Django, que contiene ModelForm, clases de campo y widgets.
- `from .models import Task`: Importa el modelo Task, el cual representa a las tareas y es la base para los campos y estructura de ambos formularios.

### 2. Clase AddTaskForm

```python

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before')
        widgets = {'complete_before': forms.DateInput(attrs={'type': 'date'})}
```


- `class AddTaskForm(forms.ModelForm)`: Crea una clase de formulario basada en ModelForm, vinculada al modelo Task.
- `Class Meta`: Define la configuración del formulario:
- `model = Task`: Define Task como el modelo base del formulario.
- `fields = ('name', 'description', 'complete_before')`: Especifica los campos del modelo que se incluirán en el formulario.
- `widgets`: Personaliza la apariencia de los campos:
- `complete_before`: Usa un DateInput con attrs={'type': 'date'}, lo que genera un selector de fecha en HTML5 para mejorar la experiencia de usuario.

### Método __init__

```python

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['name'].widget.attrs['class'] = 'form-control'
    self.fields['description'].widget.attrs['class'] = 'form-control'
```
- Este método personalizado permite modificar atributos HTML de los campos del formulario.
- `self.fields['name'].widget.attrs['class'] = 'form-control`: Añade la clase de Bootstrap "form-control" al campo name.
- `self.fields['description'].widget.attrs['class'] = 'form-control`: Aplica el mismo estilo al campo description.
- Resultado: Mejora el estilo y el aspecto del formulario.

### 3. Clase EditTaskForm

```python
class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before')
```
- Similar a AddTaskForm, define un formulario para editar tareas.
- Al ser muy similar a AddTaskForm, omite la personalización de widgets
 y métodos, ya que se supone que el formulario de edición no requiere configuraciones especiales.

 ## Plantilla para formulario

Ubicación del archivo: `posts/templates/posts/add-task.html`
- Como se ve, solo es necesario poner `{{ form }}` y desde `form.py`, se renderizará 
el formulario con los campos.

 ```python
 {% extends "base.html" %}
{% block  title %}Supertodo: Add Task{% endblock title %}
{% block body %}
<div class="container">
<form method="post">
  {% csrf_token %}
  {{ form }}
  <input type="submit" value="Add task" class="btn btn-primary">
</form>
</div>
{% endblock body %}
 ```

Por último veamos cómo implementar la vista que debe procesar el formulario:

### 6. Vista para añadir una nueva tarea

```python
def add_task(request):
    if request.method == 'POST':
        if (form := AddTaskForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)  # Genera el slug a partir del nombre
            task.save()  # Guarda la tarea
            return redirect('tasks:task-list')
    else:
        form = AddTaskForm()  # Si no es POST, crea un formulario vacío
    return render(request, 'tasks/add-task.html', dict(form=form))
```
- Utiliza <a href="#formulario">TaskForm</a> para mandar la tarea

- Si es una solicitud POST (cuando se envía el formulario):
    - Valida el formulario.
    - Crea un slug único basado en el nombre de la tarea.
    - Guarda la tarea en la base de datos.
    - Redirige a la lista de tareas.
- Si es una solicitud GET: Muestra el formulario vacío para que el usuario pueda ingresar datos.

- Plantilla: tasks/add-task.html


### 7. Vista para editar una tarea

```python
def edit_task(request, task_slug: str):
    task = Task.objects.get(slug=task_slug)  # Busca la tarea para editar
    if request.method == 'POST':
        if (form := EditTaskForm(request.POST, instance=task)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    else:
        form = EditTaskForm(instance=task)  # Pasa la tarea actual al formulario
    return render(request, 'tasks/edit-task.html', dict(task=task, form=form))
```

- Descripción: Permite editar una tarea usando EditTaskForm.

    - Si es una solicitud POST: Valida y guarda los cambios.
    - Si es una solicitud GET: Carga la tarea en el formulario para que el usuario pueda modificarla.

- Plantilla: tasks/edit-task.html


## AÑADIR HOJA DE ESTILOS CSS <p id="css"></p>

### 1. Crear una Carpeta de Archivos Estáticos (Static)

- En Django, los archivos CSS, imágenes y JavaScript se consideran archivos estáticos. Para que Django los gestione, debes colocarlos en una carpeta específica dentro de cada aplicación o en una ubicación común del proyecto.

  Dentro de la aplicación, creamos una carpeta llamada static y dentro otra con el nombre de la aplicación para organizar mejor los archivos. La estructura sería algo como esto:

```arduino
tasks/
├── static/
│   └── tasks/
│       └── styles.css

```

### 2. Configurar el archivo settings.py

Django necesita saber dónde buscar los archivos estáticos. Por defecto, Django ya tiene configurada la variable STATIC_URL en settings.py:

```python

STATIC_URL = '/static/'
```
Si planeas usar archivos estáticos en diferentes aplicaciones, también puedes especificar un directorio central en STATICFILES_DIRS, por ejemplo:

```python

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

### 3. Cargar los Archivos Estáticos en las Plantillas

Para que una plantilla HTML pueda utilizar los archivos CSS, primero debes cargar los archivos estáticos de Django y luego vincular el archivo CSS en la etiqueta <link>.

Abrimos la plantilla HTML (por ejemplo, lask-list.html) 
y agregamos el siguiente código al inicio del archivo (esto ya lo teníamos):

```html

{% load static %}
```

En la sección <head> de tu HTML, agregamos un enlace al archivo CSS utilizando 
la etiqueta <link> y la etiqueta {% static %}:

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SUPERTODO</title>
    <link rel="stylesheet" href="{% static 'todo/styles.css' %}">
</head>
<body>
    <!-- Contenido de la página -->
</body>
</html>
```
