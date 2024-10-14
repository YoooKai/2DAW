# apuntes 4

Cursos: DESARROLLO WEB EN ENTORNO SERVIDOR - DSW  (https://www.notion.so/DESARROLLO-WEB-EN-ENTORNO-SERVIDOR-DSW-c4519a74ee854698beb23cb3c6625ffe?pvs=21)
Hecho: No

Es una práctica común que al inicial un proyecto poner un startproject main en lugar de poner nanobits.

```python
slug = models.SlugField(max_length=120, unique=True)
updated_at = models.DateTimeField(auto_now=True)

          
```

```python
#decorador en admin.py
@admin.register(Post)
class POstAdmin(admin.ModelAdmin):
	pass
	
	
```

j -l 

pone lo que tenemos en el fichero just

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen.png)

personalizar admin

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%201.png)

PONERLE CSS

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%202.png)

linkear 

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%203.png)

importar funcionalidades de static

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%204.png)

los ficheros estáticos los sirve el servidor web. Pero si le paso una ruta con código python o django, se lo manda a django.

EN producción, los sirve un servidor web los ficheros estáticos. NO tenemos en nuestra máquina un servidor de desarrollo que devuelva los ficheros estçaticos. Pero ello nos vamos a url. Para eso vamos a [urls.py](http://urls.py) de nanobits.

AÑadimos cómo devolver los estáticos (no hay que procesarlos, solo devolverlos):

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%205.png)

```python
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

LA HERENCIA DE PLANTILLAS

defino lo común en un sitio, y hago que todas las plantillas hereden de ella.

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%206.png)

esqueleto común de todas las plantillas

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%207.png)

home html

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%208.png)

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%209.png)

detail

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2010.png)

También el title en base

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2011.png)

nanobits es un default si no lo usas

en home: 

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2012.png)

CUANDO SALE [manage.py](http://manage.py) 

error el puerto está en uso

tenemos que localizar el proceso que está ejecutando en ese puerto

1- buscar proceso

ps aux 

encontrar ese pid

hacer un:

kill <pid>

FORM

url

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2013.png)

vista

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2014.png)

Plantilla

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2015.png)

VISTAS

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2016.png)

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2017.png)

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2018.png)

Importar el slug y que lo añada así:

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2019.png)

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2020.png)

LA MANERA DJANGO

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2021.png)

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2022.png)

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2023.png)

VISTAS

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2024.png)

DJango automaticamente valida los campos

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2025.png)

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2026.png)

PERO SI TENEMOS UN MODELO, PODEMOS CREAR UN MODELO FORMULARIO

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2027.png)

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2028.png)

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2029.png)

![imagen.png](apuntes%204%20118c98e1579d80989895cdc020bddd3f/imagen%2030.png)