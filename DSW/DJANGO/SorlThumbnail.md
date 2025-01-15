### ¿Qué es sorl-thumbnail?

**sorl-thumbnail** es un paquete que te ayuda a crear **miniaturas** (imágenes pequeñas) de imágenes más grandes en tus aplicaciones Django de forma fácil. Por ejemplo, si tienes una imagen de portada grande para un post de un blog, puedes usar este paquete para crear una versión más pequeña (miniatura) de la imagen para mostrarla en tu página web.

### Instalación:

Para instalar **sorl-thumbnail**, debes añadirlo a tu entorno virtual y a tu archivo de dependencias `requirements.txt` (si usas uno). Luego, debes instalarlo ejecutando:

```bash
pip install sorl-thumbnail
```

### Configuración:

Una vez instalado el paquete, debes agregarlo a la lista de aplicaciones instaladas en Django en el archivo `settings.py`. Esto se hace para que Django sepa que quieres usar esta funcionalidad en tu proyecto.

En tu `settings.py`, añade esta línea a `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    # ...
    'sorl.thumbnail',
    # ...
)
```

### ¿Cómo usarlo en las plantillas?

Lo más común es usar **sorl-thumbnail** para generar miniaturas de imágenes dentro de las plantillas. Esto es especialmente útil cuando tienes una imagen muy grande (como la portada de un post de un blog) y quieres mostrarla de forma más pequeña para ahorrar espacio.

Aquí te dejo un ejemplo de cómo se usa en una plantilla de Django:

1. **Carga del paquete**: Primero, necesitas cargar el paquete en tu plantilla con `{% load thumbnail %}`.
2. **Generar miniatura**: Luego, usas la etiqueta `{% thumbnail %}` para crear la miniatura de la imagen que quieres mostrar.

Por ejemplo, imagina que tienes un post con un campo `cover` que es la imagen de portada. El siguiente código en la plantilla genera una miniatura de esa imagen de 200x200 píxeles:

```html
{% load thumbnail %}

<div class="post">
  <h1>{{ post.title }}</h1>
  
  <!-- Crear miniatura de la imagen -->
  {% thumbnail post.cover "200x200" crop="center" format="PNG" as thumb %}
    <img src="{{ thumb.url }}" alt="Post cover">
  {% endthumbnail %}

  <p>{{ post.content }}</p>
</div>
```

### Explicación de los parámetros:
- **post.cover**: Es el campo que contiene la imagen del post (en este caso, la imagen de portada).
- **"200x200"**: Especifica el tamaño de la miniatura, en este caso, 200 píxeles de ancho y 200 píxeles de alto.
- **crop="center"**: Significa que la miniatura se recortará desde el centro de la imagen original para ajustarse al tamaño indicado (en este caso, 200x200).
- **format="PNG"**: Esto indica que la miniatura será generada en formato PNG.
- **as thumb**: Al usar `as thumb`, le dices a Django que almacene la miniatura generada en una variable llamada `thumb`, y luego puedes acceder a sus propiedades, como la URL, para mostrar la imagen.


