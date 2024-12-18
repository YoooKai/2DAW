



### **1. `settings.py`**

Aquí está la configuración mejorada:

```python
import os
from prettyconf import config

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    },
}

# Configuración de envío de correos
EMAIL_HOST = 'smtp-relay.brevo.com'  # Asegúrate del hostname correcto
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

# Directorio donde se guardarán los certificados
CERTIFICATES_DIR = MEDIA_ROOT, 'certificates'
```

---

### **2. URL Configuration**

En tu archivo `urls.py`, agrega la URL de la vista para generar el certificado.

```python
from django.urls import path
from . import views

urlpatterns = [
    # Otras rutas...
    path('subject/certificate/', views.request_certificate, name='request-certificate'),
]
```

---

### **3. Vista en `views.py`**

Corrige la vista `request_certificate` para validar si el usuario tiene **nota**, y en ese caso, dispara la tarea en segundo plano:

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .tasks import deliver_certificate
from django.http import HttpResponse

@login_required
def request_certificate(request):
    # Verificar si el usuario tiene una inscripción con nota
    if request.user.enrollment_set.filter(mark__isnull=False).exists():
        # Generar la URL base para generar PDF correctamente
        base_url = request.build_absolute_uri('/')
        deliver_certificate.delay(base_url, request.user)
        return render(request, 'subjects/certificate/request_sent.html')
    else:
        return HttpResponse("You do not have a grade yet to request a certificate.", status=400)
```

---

### **4. Tarea en `tasks.py`**

La tarea `deliver_certificate` generará el PDF y enviará el correo:

```python
from django_rq import job
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from weasyprint import HTML
import datetime
import os

@job
def deliver_certificate(base_url, student):
    # Renderizar el HTML del certificado
    rendered = render_to_string(
        'subjects/certificate/certificate.html',
        {
            'student': student,
            'today': datetime.date.today(),
        }
    )

    # Generar el PDF usando WeasyPrint
    output_path = os.path.join(settings.CERTIFICATES_DIR, f'{student.username}_grade_certificate.pdf')
    os.makedirs(settings.CERTIFICATES_DIR, exist_ok=True)
    HTML(string=rendered, base_url=base_url).write_pdf(output_path)

    # Renderizar el correo
    email_body = render_to_string(
        'subjects/certificate/email.md',
        {'student': student}
    )

    # Configurar y enviar el correo
    email = EmailMessage(
        subject='Grade Certificate',
        body=email_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[student.email],
    )
    email.content_subtype = 'html'  # Asegurar que el contenido sea HTML
    email.attach_file(output_path)
    email.send()
```

---

### **5. Templates**

#### Template para el certificado (`certificate.html`)
Este es el archivo que se convertirá en PDF:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Grade Certificate</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin: 50px; }
        h1 { color: #4CAF50; }
        p { font-size: 18px; }
        .signature { margin-top: 50px; font-style: italic; }
    </style>
</head>
<body>
    <h1>Certificate of Completion</h1>
    <p>This is to certify that <strong>{{ student }}</strong></p>
    <p>has successfully completed the course with a grade.</p>
    <p>Date: {{ today }}</p>
    <div class="signature">LUMINO Team</div>
</body>
</html>
```

---

#### Template para el cuerpo del correo (`email.md`)
```html
{% load user_extras %}
<p>Dear {{ student.username }},</p>
<p>As you requested, attached is your certificate containing the grade you received in the LUMINO course.</p>
<p>Kind regards,</p>
<p><strong>LUMINO Team</strong></p>
```

---

#### Mensaje de que se ha mandado el email
Your certificate request has been processed!</h3>
You will receive an email shortly with your grade certificate attached.


---

### **6. Configuración del entorno (.env)**

Crea un archivo `.env` en tu directorio raíz con tus credenciales:

```
EMAIL_HOST_USER=sdelquin@gmail.com
EMAIL_HOST_PASSWORD=6pVXSbOkfEvyZ3R8
DEFAULT_FROM_EMAIL=sdelquin@gmail.com
```

---

### **7. Ejecutar el worker de Redis**

Para que la tarea en segundo plano funcione, debes ejecutar el worker de Redis con el siguiente comando:

```bash
python manage.py rqworker
```

---

### **8. Requisitos**

Asegúrate de instalar las dependencias necesarias:

```bash
pip install django-rq weasyprint prettyconf
```

---

### **Resumen del flujo**

1. El usuario accede a la vista `request_certificate`.  
2. La vista verifica si tiene una **nota asignada**.  
3. Si tiene nota, dispara la tarea `deliver_certificate` usando **django-rq**.  
4. La tarea genera un **PDF** con **WeasyPrint** y lo adjunta al correo.  
5. El correo se envía usando **Brevo SMTP**.

---
