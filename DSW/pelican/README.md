1. Instalación de Pelican y Markdown

Primero, asegúrate de tener Python instalado en tu sistema (recomendado versión 3.6 o superior). Luego, instala Pelican y Markdown con el siguiente comando:

pip install pelican markdown

    Markdown es opcional pero muy recomendable, ya que facilita la escritura de contenido en formato de texto plano.

2. Crear una nueva estructura de proyecto de Pelican

Navega a la carpeta donde quieres crear tu sitio web y genera un nuevo proyecto de Pelican con el siguiente comando:

pelican-quickstart

Este comando te pedirá que respondas algunas preguntas para configurar tu proyecto, como el nombre del sitio, la URL, el idioma y otras opciones. Por ejemplo:

Where do you want to create your new web site? [.] .
What will be the title of this web site? Mi Sitio Pelican
Who will be the author of this web site? Mi Nombre
What is the default language? [en] es
Do you want to specify a URL prefix? e.g., https://example.com (Y/n) n
Do you want to enable article pagination? (Y/n) y
How many articles per page do you want? [10] 5

Después de responder, Pelican generará una estructura de directorios básica para tu sitio web.
3. Estructura de archivos generada

Al ejecutar pelican-quickstart, Pelican crea la siguiente estructura de directorios y archivos en tu carpeta:

.
├── content/             # Carpeta para tus archivos de contenido (Markdown o reStructuredText)
├── output/              # Carpeta donde se generarán los archivos HTML
├── pelicanconf.py       # Archivo de configuración de Pelican
├── publishconf.py       # Archivo de configuración para publicación
└── tasks.py             # Script opcional para automatizar tareas (si elegiste esa opción)

4. Crear contenido

Los archivos de contenido, como los artículos y las páginas, se almacenan en la carpeta content/. Cada artículo debe guardarse en un archivo separado con formato Markdown (.md) o reStructuredText (.rst).

Por ejemplo, puedes crear un archivo content/primer-articulo.md con el siguiente contenido en Markdown:

Title: Mi Primer Artículo
Date: 2024-01-01
Category: Blog
Tags: inicio, pelican
Slug: primer-articulo
Author: Mi Nombre
Summary: Un breve resumen de mi primer artículo.

Este es el contenido completo de mi primer artículo. ¡Bienvenido a mi sitio web hecho con Pelican!

5. Generar el sitio web estático

Para generar tu sitio web, navega a la carpeta raíz del proyecto (donde está pelicanconf.py) y ejecuta el siguiente comando:

pelican content

Este comando genera los archivos HTML estáticos en la carpeta output/, que se puede subir directamente a un servidor web.
6. Vista previa local

Pelican incluye un servidor de desarrollo para que puedas ver tu sitio web localmente. Ejecuta el siguiente comando:

pelican --listen

Después, abre tu navegador y ve a http://localhost:8000 para ver el sitio web en tu máquina.
7. Personalización y Temas

Pelican soporta temas que puedes usar para cambiar el diseño de tu sitio. Existen muchos temas en la comunidad de Pelican que puedes encontrar en el repositorio de temas de Pelican.

Para instalar un tema:

    Descarga el tema y colócalo en una carpeta llamada themes/.

    En el archivo pelicanconf.py, agrega la línea para activar el tema:

    THEME = 'themes/nombre_del_tema'

8. Publicar el sitio web

Una vez que tengas el sitio listo, puedes publicarlo subiendo el contenido de la carpeta output/ a un servidor web. Si usas GitHub Pages, puedes configurar Pelican para generar el sitio directamente en tu repositorio.
Resumen de los comandos básicos

    Generar el sitio web: pelican content
    Vista previa en local: pelican --listen
    Regenerar el sitio automáticamente (cuando cambies el contenido): pelican -r -l

¡Con estos pasos ya deberías tener un sitio web estático básico funcionando con Pelican!
