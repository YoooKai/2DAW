### `base.html`:
```html
{% include "includes/messages.html" %}
```

---

### `includes/messages.html`:
```html
{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
        {{ message }}
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
    {% endfor %}
</ul>
{% endif %}
```

---

### Código en `views.py` (por ejemplo, en `add_lesson`):
```python
from django.contrib import messages

def add_lesson(request):
    # Lógica para agregar lección
    if success_condition:  # Cambia esto según la lógica de tu vista
        messages.add_message(request, messages.SUCCESS, 'Changes were successfully saved')
    else:
        messages.add_message(request, messages.ERROR, 'Something went wrong')
    return redirect('some-view-name')  # Redirige a la vista correspondiente
```
