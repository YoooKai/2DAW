### Uso de **Crispy Forms** en Django con **Bootstrap**

**django-crispy-forms** es un paquete que facilita la renderización de formularios de manera más elegante y flexible, especialmente cuando se utiliza con frameworks CSS como **Bootstrap**. Aquí te explico cómo instalar y usar **crispy-forms** para integrar formularios con **Bootstrap 5** en tu proyecto Django.

---

### 1. **Instalación**

Para usar **crispy-forms** con **Bootstrap 5** en Django, lo primero es integrar Bootstrap en tu proyecto (esto lo puedes hacer usando `npm`, como vimos en la respuesta anterior).

Luego, para integrar `crispy-forms` con Bootstrap 5, puedes instalar el paquete `crispy-bootstrap5`, que instalará tanto el paquete `crispy-forms` como las dependencias necesarias para trabajar con Bootstrap 5.

1. **Instalación de `crispy-bootstrap5`**:
   En tu terminal, dentro del entorno virtual de tu proyecto Django, ejecuta el siguiente comando:
   ```bash
   pip install crispy-bootstrap5
   ```

2. **Actualizar `requirements.txt`**:
   Asegúrate de añadir la nueva dependencia a tu archivo `requirements.txt` para mantener un control de las dependencias de tu proyecto.

---

### 2. **Configuración de Django**

Una vez que hayas instalado `crispy-bootstrap5`, necesitas configurarlo en el archivo `settings.py` de tu proyecto Django.

1. **Añadir a `INSTALLED_APPS`**:
   Agrega `'crispy_forms'` y `'crispy_bootstrap5'` en el listado de aplicaciones instaladas.
   
   ```python
   INSTALLED_APPS = [
       # ...
       'crispy_forms',
       'crispy_bootstrap5',
       # ...
   ]
   ```

2. **Configurar el template pack**:
   Django-crispy-forms te permite especificar qué "template pack" quieres usar. En este caso, usaremos **Bootstrap 5**. Añade las siguientes líneas:
   
   ```python
   CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
   CRISPY_TEMPLATE_PACK = 'bootstrap5'
   ```

Esto permitirá que Django use **Bootstrap 5** para renderizar los formularios.

---

### 3. **Uso en Formularios**

Ahora que tienes todo configurado, puedes comenzar a usar **crispy-forms** en tus formularios. A continuación, te muestro cómo crear un formulario de inicio de sesión (login) y uno de registro (signup) utilizando **Bootstrap 5** con **crispy-forms**.

#### 3.1 **Formulario de Login (Inicio de sesión)**

1. **Formulario en `accounts/forms.py`**:
   Crea un formulario `LoginForm` utilizando **crispy-forms**:
   
   ```python
   from crispy_bootstrap5.bootstrap5 import FloatingField
   from crispy_forms.helper import FormHelper
   from crispy_forms.layout import Layout, Submit
   from django import forms

   class LoginForm(forms.Form):
       username = forms.CharField()
       password = forms.CharField(widget=forms.PasswordInput)

       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.helper = FormHelper()
           self.helper.attrs = dict(novalidate=True)  # Añadir novalidate para evitar validación de HTML
           self.helper.layout = Layout(
               FloatingField('username'),  # Renderiza el campo 'username' con el diseño de floating label
               FloatingField('password'),  # Renderiza el campo 'password' con el diseño de floating label
               Submit('login', 'Login', css_class='w-100 mt-2 mb-2'),  # Botón de submit
           )
   ```

2. **Plantilla HTML en `accounts/templates/accounts/login.html`**:
   En tu plantilla, utiliza el tag `{% crispy form %}` para renderizar el formulario de manera más limpia con el estilo de Bootstrap 5.

   ```html
   {% load crispy_forms_tags %}
   
   <div class="row justify-content-center mt-5">
     <div class="col-md-4">
       <div class="card border-dark">
         <h4 class="card-header">
           Login
         </h4>
         <div class="card-body">
           {% crispy form %}
         </div>
         <div class="card-footer">
           Don't have an account? <a href="{% url 'signup' %}">Sign up</a> here.
         </div>
       </div>
     </div>
   </div>
   ```

   Esto renderizará el formulario con el estilo de Bootstrap y usará los campos flotantes (`FloatingField`) de Bootstrap 5 para los inputs.

---

#### 3.2 **Formulario de Registro (Signup)**

1. **Formulario en `accounts/forms.py`**:
   Crea un formulario `SignupForm` usando **crispy-forms**:
   
   ```python
   class SignupForm(forms.ModelForm):
       class Meta:
           model = get_user_model()
           fields = ('username', 'password', 'first_name', 'last_name', 'email')
           required = ('username', 'password', 'first_name', 'last_name', 'email')
           widgets = dict(password=forms.PasswordInput)
           help_texts = dict(username=None)

       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)

           for field in self.Meta.required:
               self.fields[field].required = True

           self.helper = FormHelper()
           self.helper.attrs = dict(novalidate=True)
           self.helper.layout = Layout(
               FloatingField('username'),
               FloatingField('password'),
               FloatingField('first_name'),
               FloatingField('last_name'),
               FloatingField('email'),
               Submit('signup', 'Sign up', css_class='btn-info w-100 mt-2 mb-2'),
           )

       def save(self, *args, **kwargs):
           user = super().save(commit=False)
           user.set_password(self.cleaned_data['password'])  # Set the password hash
           user = super().save(*args, **kwargs)
           return user
   ```

2. **Plantilla HTML en `accounts/templates/accounts/signup.html`**:
   En la plantilla de registro, renderiza el formulario con `crispy`:

   ```html
   {% load crispy_forms_tags %}
   
   <div class="row justify-content-center mt-5">
     <div class="col-md-4">
       <div class="card border-dark">
         <h4 class="card-header">
           Sign up
         </h4>
         <div class="card-body">
           {% crispy form %}
         </div>
         <div class="card-footer">
           Already have an account? <a href="{% url 'login' %}">Login</a> here.
         </div>
       </div>
     </div>
   </div>
   ```

