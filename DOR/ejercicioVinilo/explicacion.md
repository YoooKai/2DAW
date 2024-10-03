# index.js

Este es el archivo principal que se encarga de cargar las canciones y asociarlas con los elementos HTML. Además, crea una instancia del reproductor (Player).

## Importaciones

```javascript
import songs from "../assets/songs/*.mp3";  // Importa todas las canciones en formato mp3
import Player from "./player.js";           // Importa la clase Player desde el archivo player.js

```

Aquí se importan módulos externos. En este caso:

- songs es un objeto que contiene las canciones (archivos mp3) importados del directorio ../assets/songs/.
- El objeto songs se construye automáticamente con las claves que generalmente provienen de los nombres de los archivos y los valores que son las rutas a esos archivos.
Se verían: 
```javascript
{
    "song1": "/assets/songs/song1.mp3",
    "song2": "/assets/songs/song2.mp3",
    "song3": "/assets/songs/song3.mp3"
}

```

- Player es la clase que se importará desde el archivo player.js. Esta clase manejará la reproducción de canciones.

## Creación del objeto map

```javascript
const map = {};

```
Creamos un objeto vacío llamado map que se usará para asociar cada elemento del HTML con una canción.

## Iteración sobre las canciones
```javascript
let aux = 1;
for (var key of Object.keys(songs)) {
    // Asociar map[`.item-${aux}`] con la canción songs[key]
    map[`.item-${aux++}`] = songs[key];
}
```

`Object.keys(songs):`
- Object.keys() es un método que devuelve un array con las claves del objeto. 
- Object.keys(songs) devuelve un array como: **["song1.mp3", "song2.mp3", "song3.mp3"]**.

`Bucle for...of:`
- Usamos este bucle para iterar sobre cada clave (nombre del archivo mp3).
- Cada vez que pasa por el bucle, la variable key es el nombre de un archivo de canción.

`Asociación map:`

- En cada iteración, estamos asociando una clase CSS (.item-1, .item-2, etc.) con la ruta de la canción (songs[key]).

- obj['nombre'] = 'Juan'; // Asigna el valor 'Juan' a la propiedad 'nombre'

- Esto es esencialmente para mapear el HTML con las canciones. Así, el elemento con la clase .item-1 estará asociado con song1.mp3.

- Map se vería así:
```javascript
map = {
    '.item-1': 'ruta/a/song1.mp3',
    '.item-2': 'ruta/a/song2.mp3',
    '.item-3': 'ruta/a/song3.mp3'
};

```



## Creación de la instancia Player
```javascript
const player = new Player(map);
```
Finalmente, creamos una instancia del reproductor (Player) y le pasamos el objeto map. Esta instancia manejará la interacción entre las canciones y los elementos del DOM (HTML).