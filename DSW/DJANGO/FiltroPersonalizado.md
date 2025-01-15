¡Claro! Vamos a explicarlo paso a paso y de manera sencilla.

### **¿Qué son los filtros personalizados?**
En Django, los filtros son una forma de modificar el contenido de una variable directamente en una plantilla. Por ejemplo, en lugar de modificar un dato en tu vista o modelo, puedes aplicar un filtro en la plantilla para formatearlo, modificarlo o realizar cálculos.

Un filtro personalizado es simplemente un filtro que tú mismo defines para hacer algo que los filtros "predefinidos" de Django no pueden hacer.

---

### **Ejemplo explicado**

Supongamos que tienes un blog y cada post tiene contenido (texto). Quieres calcular el tamaño de cada post (por número de palabras o caracteres) y mostrarlo en una plantilla.

#### **Paso 1: Crear el filtro**

En el archivo `posts/templatetags/post_extras.py`, se define el filtro personalizado llamado `post_size`.

```python
@register.filter
def post_size(post: Post, metric: str = 'by-words') -> int:
    match metric:  # Evaluamos qué métrica usar
        case 'by-words':  # Si la métrica es por palabras
            size = len(w for w in post.content.split())  # Cuenta las palabras
        case 'by-chars':  # Si la métrica es por caracteres
            size = len(post.content)  # Cuenta los caracteres
        case _:  # Si no se especifica métrica válida
            size = 0  # Devuelve 0
    return size  # Retorna el tamaño
```

#### **Explicación del filtro:**
1. **`@register.filter`**:
   - Esto convierte la función en un filtro que se puede usar en las plantillas.
   
2. **`post_size(post: Post, metric: str = 'by-words')`**:
   - Es una función que recibe dos argumentos:
     - `post`: El objeto del post que será procesado.
     - `metric`: Una métrica opcional para especificar si calcular el tamaño por palabras (`by-words`) o por caracteres (`by-chars`).
   - Por defecto, usa la métrica `by-words`.

3. **`match metric:`**:
   - Evalúa qué métrica se especificó.
     - Si es `'by-words'`, cuenta las palabras en el contenido del post.
     - Si es `'by-chars'`, cuenta los caracteres en el contenido.
     - Si no se especifica una métrica concreta, usa por defecto la que le pusimos (por palabras)

---

#### **Paso 2: Usar el filtro en la plantilla**

En la plantilla `posts/templates/posts/index.html`, puedes usar el filtro `post_size` de esta manera:

```html
{% load post_extras %} <!-- Cargamos los filtros personalizados -->

<div class="posts">
    {% for post in posts %} <!-- Iteramos sobre los posts -->
        <div class="post">
            <!--Si no especificamos, será el default por palabras porque pusimos: metric: str = 'by-words'-->
            Tamaño del post default (por palabras): {{ post|post_size }}
            Tamaño del post (por palabras): {{ post|post_size:"by-words" }}
            Tamaño del post (por caracteres): {{ post|post_size:"by-chars" }}
        </div>
    {% endfor %}
</div>
```

---

### **Actividad: Crear un filtro personalizado para agregar emojis a las películas según su clasificación**

#### **Descripción:**
Crearás un filtro personalizado para agregar un emoji a la clasificación de las películas, dependiendo de su rating (calificación). Por ejemplo:
- Si la película tiene una calificación mayor a 8, se le asigna un emoji de ⭐ (estrella).
- Si tiene una calificación mayor a 5 pero menor o igual a 8, se le asigna un emoji de 😎 (cara cool).
- Si tiene una calificación menor o igual a 5, se le asigna un emoji de 👎 (pulgar abajo).

---

### **Pasos para realizar la actividad:**

1. **Modelo de ejemplo (Película):**
   Crea un modelo de Película con campos como título, descripción y calificación:

   ```python
   from django.db import models

   class Movie(models.Model):
       title = models.CharField(max_length=200)
       description = models.TextField()
       rating = models.FloatField()

       def __str__(self):
           return self.title
   ```

2. **Crea la estructura de `templatetags`:**
   - Dentro de tu aplicación, crea una carpeta llamada `templatetags` (si no existe ya).
   - En esa carpeta, crea un archivo llamado `movie_extras.py`.

3. **Define el filtro personalizado:**
   En `movie_extras.py`, implementa el filtro para asignar el emoji basado en la calificación:

   ```python
   from django import template

   register = template.Library()

   @register.filter
   def rating_emoji(rating: float) -> str:
       """
       Agrega un emoji según la calificación de la película.
       """
       if rating > 8:
           return "⭐"  # Estrella para películas de más de 8
       elif rating > 5:
           return "😎"  # Cara cool para películas entre 5 y 8
       else:
           return "👎"  # Pulgar abajo para películas con rating 5 o menos
   ```

4. **Usa el filtro en una plantilla:**
   - Carga el filtro en tu plantilla.
   - Aplica el filtro a la calificación de cada película.

   Ejemplo de plantilla (`movies/templates/movies/index.html`):

   ```html
   {% load movie_extras %}

   <h1>Lista de Películas</h1>
   {% for movie in movies %}
       <div class="movie">
           <h2>{{ movie.title }}</h2>
           <p>{{ movie.description }}</p>
           <p>Calificación: {{ movie.rating }} {{ movie.rating|rating_emoji }}</p>
       </div>
   {% endfor %}
   ```

