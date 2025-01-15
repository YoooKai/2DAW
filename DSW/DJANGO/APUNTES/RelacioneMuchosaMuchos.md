### Resumen de **Relaciones Muchos a Muchos en Django**:

Las **relaciones muchos a muchos** son utilizadas cuando un modelo puede estar relacionado con muchos otros modelos y viceversa. Esto se logra con el campo `ManyToManyField` en Django.

#### **Ejemplo básico: Relacionar Posts con Etiquetas**
Supongamos que tienes un blog con **posts** y cada post puede tener varias **etiquetas** (y cada etiqueta puede pertenecer a varios posts). Para gestionar esta relación, usamos `ManyToManyField`.

**Modelos básicos:**
1. **Label (Etiqueta)**: Cada etiqueta tiene un nombre y un slug único.
2. **Post**: Cada post tiene un título, contenido y muchas etiquetas asociadas.

**Código:**
```python
# labels/models.py
class Label(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)

# posts/models.py
class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(max_length=256)
    labels = models.ManyToManyField(
        'labels.Label',
        related_name='posts',
        blank=True,
    )
```

**Operaciones comunes:**
1. **Crear objetos**: Crear etiquetas y posts.
2. **Relaciones**:
   - Un post puede tener muchas etiquetas.
   - Una etiqueta puede estar asociada con muchos posts.
3. **Consultas**:
   - Para obtener todas las etiquetas de un post: `post_python.labels.all()`
   - Para obtener todos los posts de una etiqueta: `label_ai.posts.all()`

**Ejemplo:**
```python
label_tech = Label.objects.create(name='Technology', slug='tech')
label_ai = Label.objects.create(name='AI', slug='ai')

post_python = Post.objects.create(title='Python', content='Great programming language')
post_midjourney = Post.objects.create(title='Midjourney', content='Image generation AI')

post_python.labels.add(label_tech, label_ai)
post_midjourney.labels.add(label_tech)
```

#### **Relaciones Muchos a Muchos con un Modelo Intermedio**

En algunos casos, además de la relación muchos a muchos, necesitamos almacenar **información adicional** en la relación misma. Para ello, Django permite definir un **modelo intermedio**.

En este caso, supongamos que queremos registrar **la razón por la que una etiqueta fue asignada a un post** (por ejemplo, "Etiqueta aplicada porque el post habla de tecnología").

**Cómo hacerlo:**
1. Definimos un modelo intermedio llamado `Reason`, que conecta `Post` y `Label`, y agrega el campo `labelled_because` (razón del etiquetado).
2. Usamos el parámetro `through` en `ManyToManyField` para indicar que la relación pasa por el modelo intermedio.

**Código:**
```python
# reasons/models.py
class Reason(models.Model):
    post = models.ForeignKey('posts.Post', related_name='seals', on_delete=models.CASCADE)
    label = models.ForeignKey('labels.Label', related_name='seals', on_delete=models.CASCADE)
    labelled_because = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.post} ⇔ {self.label} ({self.labelled_because})'

# posts/models.py
class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(max_length=256)
    labels = models.ManyToManyField(
        'labels.Label',
        related_name='posts',
        through='reasons.Reason',  # Especifica el modelo intermedio
        blank=True,
    )

    def __str__(self):
        return self.title
```

**Operaciones sobre el modelo intermedio:**
1. Crear la relación entre los posts y las etiquetas con razones adicionales.
2. Realizar consultas como: obtener todas las razones por las que un post tiene una etiqueta.

**Ejemplo:**
```python
reason_python_tech = Reason.objects.create(
    post=post_python,
    label=label_tech,
    labelled_because='Post sobre programación y tecnología'
)

reason_midjourney_tech = Reason.objects.create(
    post=post_midjourney,
    label=label_tech,
    labelled_because='Post sobre imágenes generadas por AI'
)

# Consultar razones de un post
post_python.seals.all()
```


### **Práctica 1: Relaciones Muchos a Muchos (sin intermediario)**

#### **Contexto: Superhéroes y Equipos**
Estás creando una base de datos para gestionar superhéroes y los equipos a los que pertenecen. Un superhéroe puede pertenecer a varios equipos, y un equipo puede tener varios superhéroes.

#### **Modelos que necesitas:**
1. **Hero:** Cada superhéroe tiene un nombre y un alias.
2. **Team:** Cada equipo tiene un nombre y una base de operaciones.

#### **Requisitos:**
1. Define los modelos y crea la relación muchos a muchos entre ellos.
2. Crea varios superhéroes y equipos:
   - **Superhéroes:** Iron Man, Spider-Man, Thor.
   - **Equipos:** Avengers, Guardians of the Galaxy.
3. Relaciona a los superhéroes con sus equipos:
   - Iron Man y Spider-Man son miembros de los Avengers.
   - Thor pertenece tanto a los Avengers como a los Guardians of the Galaxy.
4. Consulta todos los equipos a los que pertenece Thor.

---


```python
from django.db import models

# Modelo de superhéroe
class Hero(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.alias} ({self.name})"

# Modelo de equipo
class Team(models.Model):
    name = models.CharField(max_length=100)
    base_of_operations = models.CharField(max_length=100)
    heroes = models.ManyToManyField(
        'heroes.Hero',  # Relación con el modelo Hero
        related_name='teams',  # Nombre inverso para acceder desde Hero
        blank=True,
    )

    def __str__(self):
        return f"{self.name} - Base: {self.base_of_operations}"

# Crear superhéroes
iron_man = Hero.objects.create(name='Tony Stark', alias='Iron Man')
spider_man = Hero.objects.create(name='Peter Parker', alias='Spider-Man')
thor = Hero.objects.create(name='Thor', alias='Thor')

# Crear equipos
avengers = Team.objects.create(name='Avengers', base_of_operations='New York')
guardians_of_the_galaxy = Team.objects.create(name='Guardians of the Galaxy', base_of_operations='Knowhere')

# Relacionar héroes con equipos
avengers.heroes.add(iron_man, spider_man)
guardians_of_the_galaxy.heroes.add(thor)
avengers.heroes.add(thor)  

# Consultar los equipos de Thor
thor_teams = thor.teams.all()

```

### **Práctica 2: Relaciones Muchos a Muchos (con intermediario)**

#### **Contexto: Librería y Prestamos**
Estás gestionando una librería. Los clientes pueden pedir prestados libros, pero cada préstamo necesita registrar información adicional: cuándo se realizó el préstamo y cuándo se debe devolver el libro.

#### **Modelos que necesitas:**
1. **Book:** Cada libro tiene un título y un autor.
2. **Customer:** Cada cliente tiene un nombre y un correo electrónico.
3. **Loan:** Es el modelo intermedio que contiene:
   - El cliente que pidió prestado el libro.
   - El libro que pidió prestado.
   - La fecha del préstamo (`borrowed_date`).
   - La fecha de devolución (`due_date`).




#### **Requisitos:**
1. Define los modelos y configura el modelo intermedio (`Loan`).
2. Crea varios clientes y libros:
   - **Clientes:** Alice, Bob.
   - **Libros:** "El Principito" (Antoine de Saint-Exupéry), "1984" (George Orwell).
3. Registra varios préstamos:
   - Alice pidió prestado "El Principito" el 1 de enero de 2025 y debe devolverlo el 15 de enero de 2025.
   - Bob pidió prestado "1984" el 2 de enero de 2025 y debe devolverlo el 16 de enero de 2025.
4. Consulta:
   - Todos los libros que Alice tiene en préstamo.
   - Todos los clientes que pidieron prestado "1984".

---
```python
from django.db import models

# Modelo de libro
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title} by {self.author}'

# Modelo de cliente
class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Modelo intermedio: préstamo
class Loan(models.Model):
    book = models.ForeignKey(
        'books.Book',
        related_name='loans',
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        'customers.Customer',
        related_name='loans',
        on_delete=models.CASCADE
    )
    borrowed_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return f'{self.customer.name} borrowed "{self.book.title}" on {self.borrowed_date}'

# Crear clientes
alice = Customer.objects.create(name='Alice', email='alice@example.com')
bob = Customer.objects.create(name='Bob', email='bob@example.com')

# Crear libros
el_principito = Book.objects.create(title='El Principito', author='Antoine de Saint-Exupéry')
go1984 = Book.objects.create(title='1984', author='George Orwell')

# Crear préstamos
loan_1 = Loan.objects.create(
    book=el_principito,
    customer=alice,
    borrowed_date='2025-01-01',
    due_date='2025-01-15',
)
loan_2 = Loan.objects.create(
    book=go1984,
    customer=bob,
    borrowed_date='2025-01-05',
    due_date='2025-01-16',
)

# Consultar libros que tiene Alice en préstamo
alice_books = Loan.objects.filter(customer=alice).values_list('book__title', flat=True)

# Consultar clientes que pidieron prestado "1984"
book_customers = Loan.objects.filter(book=go1984).values_list('customer__name', flat=True)

```
`values_list()`

El método values_list() se utiliza en consultas de Django para obtener una lista de tuplas con los valores de ciertos campos de los modelos. Es útil cuando quieres seleccionar solo algunos campos específicos de la base de datos en lugar de cargar toda la instancia del modelo.

El parámetro `flat=True` se utiliza cuando solo se solicita un único campo en la consulta. En ese caso, flat=True hace que Django devuelva una lista simple con los valores de ese campo, en lugar de una lista de tuplas.