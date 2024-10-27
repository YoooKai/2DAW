# TRIBU

Red social similar a twitter.

Debe tener 3 Aplicaciones:
- shared (contiene el login, usuarios...)
- echos (es como los tweets)
- waves (es como los comentarios de los tweets)

### Modelo Echo
- id
- content
- created_at
- updated_at
- user(fk)

### Modelo Wave
- id
- content
- created_at
- updated_at
- user(fk)

### URL
- `/echos/` - todos los echos, echo-list
- `/echos/pk` - echo concreto, echo-detail
- `/echos/pk/edit` - editar echo concreto
- `/echos/pk/delete` - eliminar echo concreto
- `/echos/add/` - añadir un echo
- `/echos/@username` - ver los echos de usuario concreto
- `/echos/pk/waves/add` - añadir un wave a un echo concreto
- `/echos/pk/waves/` - todos los waves de un echo concreto
- `/waves/pk/edit` - editar un wave concreto
- `/waves/pk/delete` - eliminar un wave concreto
