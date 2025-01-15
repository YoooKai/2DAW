
### **Validación en Django**

Cuando creas formularios en Django, puedes añadir validaciones para asegurarte de que los datos introducidos por los usuarios son correctos. Django te permite hacer dos tipos de validaciones: **validación individual** (de un solo campo) y **validación cruzada** (entre varios campos).

### **1. Validación Individual**

La **validación individual** se realiza cuando quieres verificar los datos de un solo campo de forma independiente. Esto se hace con un método especial llamado `clean_<nombre_campo>()`, donde `<nombre_campo>` es el nombre del campo del formulario.

**Ejemplo:**

Supón que tienes un formulario de registro de usuario y quieres asegurarte de que no haya dos usuarios con el mismo correo electrónico. Para hacerlo, en el campo `email` del formulario, puedes crear el método `clean_email()` para validar que el correo no se repita.

```python
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()  # Modelo de usuario
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data['email']  # Obtenemos el valor del campo email
        if self._meta.model.objects.filter(email=email).count() > 0:  # Comprobamos si el email ya existe
            raise ValidationError('A user with that email already exists.')  # Si existe, lanzamos un error
        return email  # Si no existe, devolvemos el email
```

En este ejemplo:
- El método `clean_email()` se encarga de verificar si ya hay un usuario con el mismo correo electrónico.
- Si ya existe, se lanza un error con `ValidationError`.
- Si no existe, el correo se devuelve para que el formulario lo use.

### **2. Validación Cruzada**

La **validación cruzada** es cuando la validación depende de más de un campo. Por ejemplo, si quieres que el nombre del usuario (`first_name`) sea igual al nombre de usuario (`username`), pero con la primera letra en mayúscula, necesitarías comparar estos dos campos. En este caso, usamos el método `clean()`.

**Ejemplo:**

Continuando con el ejemplo anterior, si quieres que el `first_name` coincida con el `username`, pero con la primera letra en mayúscula, puedes usar `clean()`:

```python
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def clean(self):
        username = self.cleaned_data['username']  # Obtenemos el valor de username
        first_name = self.cleaned_data['first_name']  # Obtenemos el valor de first_name
        if first_name != username.title():  # Comprobamos si first_name no es igual a username con la primera letra en mayúscula
            raise ValidationError('First name must be like username as title.')  # Si no coinciden, lanzamos un error
```

Aquí:
- El método `clean()` se utiliza para hacer la validación cruzada entre `username` y `first_name`.
- Si `first_name` no es igual a `username` en formato de título (primera letra en mayúscula), lanzamos un `ValidationError`.

### **Acceso a Errores en la Plantilla**

Cuando los formularios tienen errores de validación, puedes acceder a esos errores en la plantilla de Django para mostrarlos al usuario.

Para acceder a los errores **no relacionados con campos específicos** (errores generados por validaciones cruzadas, por ejemplo), puedes usar:

```html
{{ form.non_field_errors }}
```

Esto mostrará los errores que no están asociados con un campo específico del formulario, como los errores generados en el método `clean()`.


## Otro ej

Mis disculpas por la confusión. Aquí te dejo un ejemplo **nuevo** para que puedas practicar tanto la **validación individual** como la **validación cruzada** con un caso diferente.

### **Actividad: Formulario de Pedido de Compra**
Vamos a crear un formulario de pedido para una tienda online donde se deben cumplir las siguientes validaciones:

1. **Validación individual**: El campo `phone_number` debe tener exactamente 10 caracteres (validación de longitud).
2. **Validación cruzada**: La cantidad (`quantity`) de un producto debe ser mayor o igual a 1 y no puede exceder el stock disponible en el inventario.

### **Pasos para la actividad:**

1. **Modelo del Pedido y Producto**:
   Supongamos que tienes dos modelos: uno para `Product` (producto) y otro para `Order` (pedido).

   ```python
   # models.py

   from django.db import models

   class Product(models.Model):
       name = models.CharField(max_length=255)
       description = models.TextField()
       price = models.DecimalField(max_digits=10, decimal_places=2)
       stock = models.PositiveIntegerField()  # Cantidad disponible en stock

       def __str__(self):
           return self.name

   class Order(models.Model):
       product = models.ForeignKey(Product, on_delete=models.CASCADE)
       quantity = models.PositiveIntegerField()
       phone_number = models.CharField(max_length=15)
       customer_name = models.CharField(max_length=255)
       order_date = models.DateTimeField(auto_now_add=True)

       def __str__(self):
           return f'Order for {self.product.name} by {self.customer_name}'
   ```

2. **Formulario para el Pedido (OrderForm)**:
   Ahora, vamos a crear el formulario para crear un pedido de compra. Aquí se implementarán las validaciones que hemos mencionado:

   ```python
   # forms.py

   from django import forms
   from django.core.exceptions import ValidationError
   from .models import Order, Product

   class OrderForm(forms.ModelForm):
       class Meta:
           model = Order
           fields = ['product', 'quantity', 'phone_number', 'customer_name']

       # Validación individual: El número de teléfono debe tener exactamente 10 caracteres
      def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) != 10:
            raise ValidationError

       # Validación cruzada: La cantidad no puede ser mayor que el stock disponible
       def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        quantity = cleaned_data.get('quantity')

        # Validación cruzada
        if product and quantity:
            if quantity < 1:
                raise ValidationError('La cantidad debe ser al menos 1.')
            if quantity > product.stock:
                raise ValidationError(f'No hay suficiente stock. Solo quedan {product.stock} unidades disponibles.')

        return cleaned_data
   ```

   - **`clean_phone_number()`**: Esta es una validación individual que asegura que el número de teléfono tiene exactamente 10 caracteres.
   - **`clean()`**: Esta es una validación cruzada que compara la cantidad del pedido con el stock disponible del producto. Si la cantidad es mayor que el stock, lanza un error.


### Otro ejemplo

```python
class EventForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()

    def clean(self):
        cleaned_data = super().clean()  # Llamada a super().clean() para obtener todos los datos limpios
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError('Start date must be before end date.')
        return cleaned_data

```