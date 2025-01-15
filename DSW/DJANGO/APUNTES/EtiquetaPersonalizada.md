### ¿Qué son las etiquetas personalizadas en Django?

Django tiene un sistema de **etiquetas de plantilla** que puedes usar para añadir lógica o contenido dinámico en tus plantillas HTML. Estas etiquetas son como pequeñas funciones que puedes llamar en tu HTML para realizar tareas específicas. Por ejemplo, una etiqueta puede mostrar una lista de objetos de la base de datos o realizar cálculos.

**Etiquetas personalizadas** son aquellas que tú creas cuando necesitas una funcionalidad que no está incluida en Django.

---

### ¿Qué son las **inclusion tags**?

Las **inclusion tags** son un tipo especial de etiquetas personalizadas que:
1. **Realizan algún procesamiento de datos.**
2. **Renderizan una plantilla con esos datos.**

Por ejemplo, imagina que quieres mostrar una lista de publicaciones (`posts`) en una página, pero solo las que tienen una valoración mayor a cierto número.

---

### Cómo funcionan las **inclusion tags**

1. **Modelo de datos**:
   - Se define un modelo que contiene los datos. En este caso, un modelo llamado `Post` con atributos como `title`, `content` y `rating`.

   ```python
   class Post(models.Model):
       title = models.CharField(max_length=256)
       content = models.TextField(max_length=256)
       rating = models.FloatField(default=0)
   ```

2. **Plantilla para renderizar los datos**:
   - Crea una plantilla HTML para mostrar la información. En este caso, una lista de títulos y contenido de publicaciones.

   ```html
   <!-- posts/templates/posts/includes/list.html -->
   {% for post in posts %}
       <h1>{{ post.title }}</h1>
       <p>{{ post.content }}</p>
   {% endfor %}
   ```

3. **Definición de la etiqueta personalizada**:
   - Crea un archivo en `templatetags` para definir la lógica de la etiqueta.
   - La etiqueta `post_list` filtra las publicaciones con una valoración (`rating`) mayor o igual a un valor dado (`min_rating`) y pasa estos datos a la plantilla.

   ```python
   from django import template
   from posts.models import Post

   register = template.Library()

   @register.inclusion_tag('posts/includes/list.html')
   def post_list(min_rating: int = 0):
       posts = Post.objects.filter(rating__gte=min_rating)
       return {'posts': posts}
   ```

   **Nota:** 
   - El archivo `post_extras.py` debe estar en una carpeta llamada `templatetags`.
   - Usamos `@register.inclusion_tag` para registrar la etiqueta y especificar qué plantilla debe usar.

4. **Uso de la etiqueta personalizada**:
   - Ahora puedes usar la etiqueta en cualquier plantilla cargando el archivo donde la definiste (`post_extras.py`) y llamándola con su nombre (`post_list`).

   ```html
   <!-- posts/templates/posts/index.html -->
   {% load post_extras %}

   <div class="posts">
       {% post_list 5 %}  <!-- Muestra posts con rating >= 5 -->
   </div>
   ```

---

### ¿Qué pasa con los argumentos?

En este ejemplo:
- `post_list` tiene un argumento `min_rating` con un valor por defecto (`0`).
- Cuando llamas a `{% post_list 5 %}`, le estás pasando el valor `5` para filtrar publicaciones con un rating mayor o igual a `5`.

También puedes definir argumentos **nominales** (es decir, con nombre). Por ejemplo:

```python
@register.inclusion_tag('posts/includes/list.html')
def post_list(min_rating: int = 0, max_posts: int = 10):
    posts = Post.objects.filter(rating__gte=min_rating)[:max_posts]
    return {'posts': posts}
```

Y lo llamarías así:

```html
{% post_list 5 max_posts=3 %}
```

Esto mostrará solo 3 publicaciones con rating >= 5.

---

`__gte`: Es un operador de filtro que significa "greater than or equal" (mayor o igual).

Django proporciona una serie de operadores que puedes usar con los campos del modelo para realizar consultas avanzadas.

Algunos ejemplos comunes:

`field__gte:` Mayor o igual (greater than or equal).
`field__lte:` Menor o igual (less than or equal).
`field__exact:` Igual a un valor.
`field__icontains:` Contiene una cadena de texto (sin importar mayúsculas o minúsculas).
`field__in:` Dentro de una lista de valores.


¡Claro que sí! Aquí tienes otro ejemplo diferente:

---

### Actividad: Crear una Etiqueta Personalizada para Mostrar los Comentarios Recientes de un Blog

Imagina que tienes un blog y quieres mostrar en la barra lateral los **comentarios más recientes**, limitando la cantidad de comentarios mostrados.

#### Modelo

El modelo `Comentario` tiene los siguientes campos:

- `autor`: Nombre del autor del comentario.
- `contenido`: Texto del comentario.
- `fecha`: Fecha en que se hizo el comentario.
- `publicado_en`: Una relación con el modelo `Post`, que representa la publicación del blog asociada al comentario.

#### Pasos

1. **Define el modelo**: Crea el modelo `Comentario` con los campos mencionados en tu aplicación (por ejemplo, en `blog/models.py`).
```python
class Comentario(models.Model):
    autor = models.CharField(max_length=100)  # Si usas usuarios autenticados, reemplázalo con User
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    publicado_en = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")

    def __str__(self):
        
```

2. **Crea la plantilla**: Diseña una plantilla llamada `blog/includes/comentarios_recientes.html` que muestre los comentarios recientes. Por ejemplo:
   ```html
   <ul>
       {% for comentario in comentarios %}
           <li>
               <strong>{{ comentario.autor }}</strong> comentó en 
               <a href="{{ comentario.publicado_en.get_absolute_url }}">{{ comentario.publicado_en.title }}</a>:
               <p>{{ comentario.contenido }}</p>
               <small>{{ comentario.fecha }}</small>
           </li>
       {% endfor %}
   </ul>
   ```

3. **Define la etiqueta personalizada**: Escribe la función para la etiqueta personalizada en `blog/templatetags/blog_extras.py`. Esta etiqueta debería:

   - Ordenar los comentarios por fecha, mostrando los más recientes primero.
   - Limitar la cantidad de comentarios mostrados (por ejemplo, a los 5 más recientes).

   ```python
   from django import template
   from blog.models import Comentario

   register = template.Library()

   @register.inclusion_tag('blog/includes/comentarios_recientes.html')
   def comentarios_recientes(limite=5):
       comentarios = Comentario.objects.order_by('-fecha')[:limite]
       return {'comentarios': comentarios}
   ```

4. **Usa la etiqueta en una plantilla**: En `blog/templates/blog/index.html`, utiliza la etiqueta para mostrar los comentarios recientes en la barra lateral.

   ```html
   {% load blog_extras %}

   <div class="sidebar">
       <h3>Comentarios recientes</h3>
       {% comentarios_recientes 5 %}
   </div>
   ```

#### Reglas

- Asegúrate de ordenar los comentarios por `fecha` en orden descendente.
- Usa el argumento `limite` para controlar cuántos comentarios se muestran.

---

### Resultado Esperado

Cuando uses la etiqueta en tu plantilla, debería mostrar los últimos 5 comentarios publicados, incluyendo el autor, un fragmento del contenido, y un enlace al post donde se publicó el comentario.

Por ejemplo:
```html
<h3>Comentarios recientes</h3>
<ul>
    <li>
        <strong>Juan</strong> comentó en <a href="/post/python-tutorial/">Python Tutorial</a>:
        <p>Muy útil, gracias por compartir.</p>
        <small>2025-01-10</small>
    </li>
    <!-- Más comentarios -->
</ul>
```

---

