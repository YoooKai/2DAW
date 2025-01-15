### Pasos para integrar **Bootstrap** en un proyecto Django

**Bootstrap** es una popular librería de herramientas frontend que facilita el diseño y la creación de interfaces de usuario responsivas. A continuación, te explicaré los pasos para instalar y configurar Bootstrap en tu proyecto Django utilizando `npm` y ficheros estáticos.

#### 1. **Instalación de Paquetes con `npm`**
Bootstrap y sus dependencias se pueden instalar mediante `npm` (Node Package Manager). Este comando descarga los archivos necesarios para usar Bootstrap y otras dependencias en tu proyecto.

1. Abre la terminal y navega hasta el directorio de tu proyecto Django.
2. Ejecuta el siguiente comando para instalar Bootstrap y **Bootstrap Icons**:
   ```bash
   npm install bootstrap bootstrap-icons
   ```

Este comando hará lo siguiente:
- **Instalar Bootstrap** y **Bootstrap Icons**.
- Crear una carpeta `node_modules` que contiene los archivos de estas librerías y sus dependencias.
- Crear los archivos `package.json` y `package-lock.json` para gestionar las versiones de los paquetes.

#### 2. **Excluir `node_modules` del Control de Versiones**
Es recomendable que no subas la carpeta `node_modules` a tu repositorio de control de versiones (como Git), ya que los paquetes se pueden volver a instalar en cualquier momento a través de `npm install`.

Para hacer esto, añade la carpeta `node_modules` al archivo `.gitignore` de tu proyecto.

**.gitignore:**
```
node_modules/
```

#### 3. **Configuración de Archivos Estáticos en Django**
En Django, los archivos estáticos (como CSS, JS, imágenes, etc.) deben ser configurados para que puedan ser accesibles en las plantillas.

1. Abre el archivo `settings.py` de tu proyecto Django.
2. Agrega la siguiente línea para incluir la carpeta `node_modules` como una fuente de archivos estáticos:
   ```python
   STATICFILES_DIRS = [BASE_DIR / 'node_modules']
   ```

Esto indica a Django que también busque archivos estáticos dentro de la carpeta `node_modules` para cargarlos correctamente.

#### 4. **Cargar Archivos Estáticos en las Plantillas**
Ahora, necesitas referenciar los archivos CSS y JS de Bootstrap en tus plantillas HTML para que se carguen correctamente en el navegador.

1. Abre el archivo base de tus plantillas, por ejemplo `shared/templates/base.html`.
2. Asegúrate de cargar los archivos estáticos utilizando el tag `{% load static %}` al principio del archivo.
3. Dentro de la sección `<head>`, agrega los enlaces a los archivos CSS de Bootstrap y Bootstrap Icons:
   ```html
   {% load static %}
   
   <!DOCTYPE html>
   <html>
     <head>
       <meta charset="utf-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1" />
       <title>Mi Proyecto</title>
       <!-- Cargar Bootstrap CSS -->
       <link rel="stylesheet" href="{% static 'bootstrap/dist/css/bootstrap.min.css' %}">
       <!-- Cargar Bootstrap Icons CSS -->
       <link rel="stylesheet" href="{% static 'bootstrap-icons/font/bootstrap-icons.min.css' %}">
       <!-- Cargar CSS personalizado -->
       <link rel="stylesheet" href="{% static 'css/custom.css' %}">
     </head>
   
     <body>
       <div class="container">
         {% block content %}
         {% endblock %}
       </div>
   
       <!-- Cargar Bootstrap JS -->
       <script type="text/javascript" src="{% static 'bootstrap/dist/js/bootstrap.bundle.min.js' %}"></script>
     </body>
   </html>
   ```

#### 5. **Utilización de Bootstrap en las Plantillas**
Una vez que has configurado correctamente los archivos CSS y JS de Bootstrap, puedes comenzar a usar las clases y componentes de Bootstrap en tus plantillas Django. 

Por ejemplo, podrías usar un **navbar** de Bootstrap en el bloque `{% block content %}`:

```html
{% block content %}
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Mi Blog</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" href="#">Inicio</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Blog</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Contacto</a>
        </li>
      </ul>
    </div>
  </nav>
{% endblock %}
```
