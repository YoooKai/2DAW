

### Uso del template tag:

```html
{% modal "leave" "user.leave" title="Destroy account" body="This action will delete your account and all your data.<br>Are you sure?" btn-classes="btn btn-danger" btn-icon="bi bi-exclamation-triangle-fill" %}
```

---

### Archivo `shared_extras.py`:

```python
from django.template import Library
from django.urls import reverse

register = Library()

@register.inclusion_tag('modal.html')
def modal(
    btn_text,
    url,
    url_args=None,
    title='Attention',
    body='Are you sure you want to leave this account?',
    action='Continue',
    btn_classes='btn',
    btn_icon=''
):
    """
    Template tag para generar un modal reutilizable.

    Args:
        btn_text (str): Texto del botón.
        url (str): Nombre de la vista para el botón de acción.
        url_args (list, optional): Argumentos para construir la URL.
        title (str): Título del modal.
        body (str): Cuerpo del mensaje en el modal.
        action (str): Texto del botón de acción.
        btn_classes (str): Clases CSS para estilizar el botón.
        btn_icon (str): Icono CSS para el botón.

    Returns:
        dict: Contexto para el modal.
    """
    return {
        'modal_id': f'modal-{url.replace(":", "-")}',
        'title': title,
        'body': body,
        'action': action,
        'url': reverse(url, args=url_args or []),
        'btn_text': btn_text,
        'btn_classes': btn_classes,
        'btn_icon': btn_icon
    }
```

---

### Plantilla `modal.html`:

```html
<div id="{{ modal_id }}" class="modal fade" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">{{ title }}</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <p>{{ body|safe }}</p>
            </div>
            <div class="modal-footer">
                <a href="{{ url }}" class="{{ btn_classes }}">
                    {% if btn_icon %}
                        <i class="{{ btn_icon }}"></i>
                    {% endif %}
                    {{ action }}
                </a>
            </div>
        </div>
    </div>
</div>

<!-- Botón para activar el modal -->
<button type="button" data-bs-toggle="modal" data-bs-target="#{{ modal_id }}" class="{{ btn_classes }}">
    {% if btn_icon %}
        <i class="{{ btn_icon }}"></i>
    {% endif %}
    {{ btn_text }}
</button>
```

