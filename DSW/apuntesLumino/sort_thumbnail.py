# Paquete de Django a instalar: sorl-thumbnail
# Asegúrate de agregar "sorl.thumbnail" en INSTALLED_APPS en settings.py

# Esto es avatar.html

{% load thumbnail %}

{% thumbnail user.profile.avatar size crop="center" format="PNG" as avatar %}
    <img src="{{ avatar.url }}" alt="Avatar">
{% endthumbnail %}

# En la plantilla principal:

{% include "user/includes/avatar.html" with user=target_user size="200x200" %}
