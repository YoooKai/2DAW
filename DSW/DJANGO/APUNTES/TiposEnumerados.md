### ¿Qué son los tipos enumerados?

Los tipos enumerados son una forma estructurada de definir un conjunto fijo de valores para un campo. Esto es útil cuando deseas limitar las opciones posibles de ese campo y trabajar con etiquetas más legibles en lugar de simples valores.

---

### Ejemplo en detalle:

El código que diste define un modelo llamado `Post` que utiliza una clase interna llamada `Category` de tipo `TextChoices`. La clase `Category` define las categorías válidas para los posts del blog.

#### **Clase interna `Category`**
```python
class Category(models.TextChoices):
    SOCIETY = 'SOC', 'Society'
    EDUCATION = 'EDU', 'Education'
    HEALTH = 'HLT', 'Health'
    CULTURE = 'CUL', 'Culture'
    TECH = 'TEC', 'Technology'
```

- **Clave**: `'SOC'`, `'EDU'`, etc., son los valores almacenados en la base de datos.
- **Etiqueta**: `'Society'`, `'Education'`, etc., son las etiquetas descriptivas que se mostrarán en formularios o interfaces.

#### **Campo `category`**
```python
category = models.CharField(
    max_length=3,
    choices=Category,
    default=Category.SOCIETY
)
```

- `max_length=3`: El campo `category` permite hasta 3 caracteres, ya que los valores como `'SOC'` tienen 3 letras.
- `choices=Category`: Limita los valores permitidos a los definidos en `Category`.
- `default=Category.SOCIETY`: Si no se especifica una categoría, el valor predeterminado será `'SOC'`.

---

### Funciones útiles

Django proporciona métodos y propiedades útiles para trabajar con estos tipos enumerados:

#### **Opciones y metadatos de `TextChoices`**
1. `Post.Category.choices`  
   Devuelve una lista de pares (`clave`, `etiqueta`), como:
   ```python
   [('SOC', 'Society'), ('EDU', 'Education'), ('HLT', 'Health'), ('CUL', 'Culture'), ('TEC', 'Technology')]
   ```

2. `Post.Category.labels`  
   Devuelve una lista con las etiquetas descriptivas:
   ```python
   ['Society', 'Education', 'Health', 'Culture', 'Technology']
   ```

3. `Post.Category.values`  
   Devuelve una lista con los valores almacenados en la base de datos:
   ```python
   ['SOC', 'EDU', 'HLT', 'CUL', 'TEC']
   ```

4. `Post.Category.names`  
   Devuelve los nombres de las opciones tal como están definidas en la clase:
   ```python
   ['SOCIETY', 'EDUCATION', 'HEALTH', 'CULTURE', 'TECH']
   ```

---

### Operaciones con un objeto de tipo `Post`

Supongamos que tienes un objeto `post` de este modelo:

1. `post.category`  
   Muestra el valor almacenado, por ejemplo, `'SOC'`.

2. `post.category.label`  
   Muestra la etiqueta legible asociada al valor, por ejemplo, `'Society'`.

3. `post.get_category_display()`  
   También devuelve la etiqueta descriptiva, como `'Society'`.

---

### Comprobaciones y buenas prácticas

#### **Forma correcta de comparar categorías**

Para verificar si un post pertenece a una categoría específica, usa la constante de la clase interna `Category`:

```python
from posts.models import Post

if post.category == Post.Category.EDUCATION:
    # Realizar acciones específicas
```

#### **Forma incorrecta**
Evita comparar con los valores directamente, como:

```python
if post.category == 'EDU':  # No es recomendado
    # Realizar acciones
```

Esto es incorrecto porque:
- Es menos legible y más propenso a errores.
- Si cambias el valor de `'EDU'` en el futuro, deberías actualizarlo manualmente en todo tu código.

---

## OTRO EJEMPLO

```python
class Product(models.Model):
    class Category(models.TextChoices):
        ELECTRONICS: 'ELC', 'Electronics'
        CLOTHING: 'CLT', 'Clothing'
        GROCERIES: 'GRC', 'Groceries'
        FURNITURE: 'FNT', 'Furniture''
        TOYS: 'TOY', 'Toys'

    name = models.CharField(max_length=100)
    price = DecimalField(max_digits=10, decimal_places=2)

    category = models.CharField(
        max_length=3,
        choices=Category,
        default=Category.GROCERIES
    )

    def __str__(self):
        return f"{self.name} ({self.get_category_display()}) - ${self.price}"

```
#### Función que devuelva los productos de una categoría específica

```python
from django.shortcuts import render
from shop.models import Product

def products_by_category(request, category_name):
    products = Product.objects.filter(category=category)
    return render(request, 'products.html', {'products': products})
```