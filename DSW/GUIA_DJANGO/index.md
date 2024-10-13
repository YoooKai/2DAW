# Guía de Inicio con Django

Esta guía la hice para no olvidarme de cómo configurar un entorno de desarrollo con Django paso a paso.

## Antes que nada: Crear un directorio para el proyecto

Primero, crea un directorio donde se alojará tu proyecto y ubícate dentro de este:

```bash
mkdir proyecto && cd proyecto
```
## 1. Crear entorno virtual
Es buena práctica trabajar con un entorno virtual para aislar las dependencias del proyecto. 
```pyhton
python -m venv .venv --prompt questlog
```
Este comando creará un entorno virtual en la carpeta .venv y establecerá questlog como su nombre para que sea más fácil identificarlo en tu terminal.
## 2. Actvar el entorno virtual
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
django-admin startproject questlog .
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
./manage.py startapp todo
```
Esto creará una nueva carpeta todo con la estructura básica de una aplicación Django. Recuerda agregar la nueva app a INSTALLED_APPS en settings.py.

# MODELS
Los modelos son la representación conceptual abstracta de los datos que queremos represnetar en la tabla.
- Cada módulo se define como una clase en python y cada atributo representa un campo de la tabla.

- Cuando se define un modelo y se reistra, django crea automáticamente las tablas de la base de datos mediante migraciones.
- Djangog proporciona herramientas para manejar las operaciones CRUD(crear, leer, actualizar, eliminar), simplificando la interacción con la base de datos.

## 1. Creamos un primer modelo.

Se vería algo como esto.
Para saber las caracterśiticas de los tipos de datos, se puede acudir a la documentación de Django.

También es importante para más adelante añadirle un método str, para controlar cómo se representará el objeto cuando se convierta en un string.

```python
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add = True)
    due_date = models.DateTimeField()
    slug = models.SlugField('max_length=150', unique=True)

    def __str__(self):
        return self.title
    
```

## 2. Hacer migraciones.
Como hemos modificado la estructura de la aplcación, tenemos que aplicar migraciones en la terminal.

```python
./manage.py make migrations
```
```python
./manage.py make migrate
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
    

admin.site.register(ToDoItem, TaskAdmin)

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
    'todo.apps.TodoConfig',
]
```

## 5. Configurar la zona horaria.
En el mismo fichero de settings.py, para configurar la hora de Canarias, vamos a la línea `TIME_ZONE = 'UTC'` y la cambamos por:

`TIME_ZONE = 'Atlantic/Canary'`

## 6. Probar y crear una tarea en la interfaz adminisrativa.
Recordar que para entrar, escribimos:
`./manage.py runserver`
