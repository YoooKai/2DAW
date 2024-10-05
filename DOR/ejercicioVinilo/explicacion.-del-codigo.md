## Proyecto SpotifyVinilo
### Explcación del código.

#### ÍNDICE
- <a href="#index">index.js</a>
- <a href="#player">player.js</a>
- <a href="#song">song.js </a>

<h1 id="index">index.js</h1>

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



<h1 id="player">player.js</h1>
Este archivo contiene la definición de la clase Player, que es responsable de gestionar la lógica de la reproducción de canciones.

## Importaciones
```javascript
import Song, { play_song } from './song.js';
```
Aquí estamos importando:

- **Song**: Clase que representa una canción individual.
- **play_song**: Función que controla la lógica de reproducción de una canción (como play/pause).

## Definición de la clase Player
```javascript
export default class Player {
    constructor(map) {
        let aux = 1;

        for (var [key, value] of Object.entries(map)) {
            const s_key = key; // La clave, como ".item-1", ".item-2"
            const s_value = value; // La canción asociada (por ejemplo, "path/to/song.mp3")
            const s_cover = `.cv${aux}`; // La clase CSS para la portada, como ".cv1", ".cv2"
            const song = new Song(s_key, s_value, s_cover); // Crea una instancia de Song
            play_song(song); // Asocia la interacción del usuario con la reproducción de la canción
            aux++;
        }
    }
}

```
`export default class Player`

- La clase Player es exportada como la exportación por defecto del archivo. Esto significa que cuando otro archivo quiera importar esta clase, simplemente hará import Player from './player.js' sin necesidad de utilizar llaves {}.
- Una clase es una estructura de JavaScript que permite crear objetos con propiedades y métodos asociados. Aquí, la clase Player gestiona la lógica para vincular canciones con elementos en la página y controlar la reproducción.

`constructor(map)`

- El constructor es un método especial de las clases en JavaScript que se ejecuta automáticamente cuando se crea una instancia de la clase.

- Aquí, el constructor recibe un parámetro llamado map. Este parámetro es un objeto que contiene una relación entre claves (que corresponden a los elementos del HTML) y valores (las rutas de las canciones).

Por ejemplo, map podría verse así:

```javascript
const map = {
    '.item-1': 'path/to/song1.mp3',
    '.item-2': 'path/to/song2.mp3',
    '.item-3': 'path/to/song3.mp3',
};
```
` El bucle for` 

```javascript
Copiar código
for (var [key, value] of Object.entries(map)) {
```
Esta es una forma de recorrer un objeto en JavaScript. 

La función `Object.entries()` devuelve un array de pares [clave, valor] de las entradas del objeto map.

Por ejemplo, si map es:

```javascript
{
    '.item-1': 'path/to/song1.mp3',
    '.item-2': 'path/to/song2.mp3',
}
```
Entonces, Object.entries(map) generaría un array como:

```javascript

[
    ['.item-1', 'path/to/song1.mp3'],
    ['.item-2', 'path/to/song2.mp3']
]
```
- La sintaxis `[key, value]` utiliza desestructuración (desempaquetado) para asignar directamente la clave (ej. '.item-1') a key y el valor (ej. 'path/to/song1.mp3') a value.

- en python se vería:
```python
for key, value in map.items():
    print(key, value)
```
`Las variables dentro del bucle`

**const s_key = key;**

- `s_key` almacena la clave obtenida del map. En este caso, las claves son las clases CSS como .item-1, .item-2, que corresponden a elementos en el HTML.
const s_value = value;

- `s_value` almacena el valor de la ruta de la canción. Es decir, para .item-1, la ruta podría ser path/to/song1.mp3.

**const s_cover = .cv${aux};**

- Esta línea utiliza interpolación de cadenas para crear una clase CSS para la portada de la canción. Por ejemplo, cuando **aux es 1, s_cover será .cv1.** Cuando aux es 2, s_cover será .cv2, y así sucesivamente.

**const song = new Song(s_key, s_value);**

Aquí se crea una nueva instancia de la clase Song (que está importada de otro archivo **song.js**).

Song es una clase que representa cada canción, y recibe dos parámetros:

- s_key: la clase del HTML que identifica a un elemento.
- s_value: la ruta del archivo de audio.


Por ejemplo:

```javascript
const song = new Song('.item-1', 'path/to/song1.mp3');
```

Este objeto **Song** se encarga de gestionar cosas como el elemento HTML de la canción y su reproducción.

`play_song(song);`

Una vez que se crea la instancia song, se llama a la función **play_song**(también importada de otro archivo).

- La función **play_song(song)** asocia la reproducción de la canción con la interacción del usuario. Es decir, configura para que cuando se haga clic en el elemento correspondiente, la canción comience o se pause.

`aux++`

Finalmente, se incrementa la variable aux en 1. Esto es para que, en la siguiente iteración del bucle, se use la clase CSS correspondiente a la siguiente portada (ej. .cv2, .cv3, etc.).

<h1 id="song">song.js</h1>

El fichero song.js define la clase **Song** y una función llamada **play_song**. 

## Clase Song
```javascript
export default class Song {
    constructor(k_song, v_song, c_song) {
        this.element = document.querySelector(k_song);
        this.audio = new Audio(v_song);
        this.album = document.querySelector(c_song);
        this.vinyl = this.element.querySelector('.vinyl');
    }
}
```
## Constructor
El constructor de la clase **Song** toma tres parámetros:

- `k_song`: es el selector CSS del elemento asociado a la canción (por ejemplo, .item-1, .item-2).
- `v_song`: es la ruta del archivo de audio (por ejemplo, "song1.mp3").
- `c_song`: es el selector CSS de la portada del álbum (por ejemplo, .cv1, .cv2).

## Propiedades del constructor

`this.element`: 
Selecciona el elemento del DOM usando el selector `k_song` (por ejemplo, .item-1). Esto asigna el nodo del HTML que contiene la canción.

```javascript
this.element = document.querySelector(k_song);
```
Si k_song es .item-1, seleccionará el elemento HTML que tiene la clase .item-1.

`this.audio:` Crea un nuevo objeto Audio que carga el archivo de sonido (v_song), como "song1.mp3".

```javascript
this.audio = new Audio(v_song);
```
Este objeto permite reproducir, pausar y controlar el audio.

`this.album`: Selecciona el elemento del DOM que corresponde a la portada del álbum, usando c_song como selector (por ejemplo, .cv1 para la primera canción).

```javascript
this.album = document.querySelector(c_song);
```

`this.vinyl`: Dentro de this.element (que representa .item-1, .item-2, etc.), selecciona el subelemento que tiene la clase .vinyl. Este será el disco de vinilo en la interfaz.

```javascript
this.vinyl = this.element.querySelector('.vinyl');
```

### Cuando llamas a new Song(s_key, s_value, s_cover):
- s_key toma el valor de la clave en el objeto map (por ejemplo, ".item-1").
- s_value toma el valor asociado a esa clave, que es la ruta del archivo de la canción (por ejemplo, "song1.mp3").
- s_cover toma el valor de la clase CSS que construimos para la portada (por ejemplo, ".cv1").
- Esos valores se pasan al constructor de la clase Song. En el constructor, `k_song` es el parámetro que recibe el valor de `s_key`, `v_song` recibe el valor de `s_value`, y `c_song` recibe el valor de `s_cover`.

## Nombres más descriptivos:
- k_song → `songElementSelector`: Porque esto representa el selector CSS del elemento que representa la canción en el DOM.
- v_song → `songFilePath`: Porque este valor es la ruta del archivo de la canción (el mp3).
- c_song → `coverElementSelector`: Porque esto representa el selector CSS para la portada del álbum.

## Función play_song
```javascript
export function play_song(song) {
    song.element.onclick = () => {
        if (song.audio.paused) {
            song.vinyl.style.transform = 'translate(-50%, 0)';
            song.audio.play();
        } else {
            song.vinyl.style.transform = 'translate(-100%, 0)';
            song.audio.pause();
        }
    }
}
```

- Esta función controla lo que ocurre cuando el usuario hace clic en el elemento asociado a una canción.

## Asignación del evento onclick

Cuando el usuario hace clic en song.element (que corresponde a una de las cajas con .item-1, .item-2, etc.), la función chequea si la canción está pausada o no.

```javascript
Copiar código
song.element.onclick = () => {
    // Código que se ejecuta al hacer clic
}
```
## Comprobación del estado de la canción

- Si la canción está pausada (song.audio.paused es true), entonces:

Cambia la posición del vinilo visualmente (mueve el vinilo usando CSS transform), lo que simula que el disco se está reproduciendo.

```javascript
song.vinyl.style.transform = 'translate(-50%, 0)';
```
## Reproduce la canción:

```javascript
song.audio.play();
```
- Si la canción ya está sonando, el código hace lo contrario:
Cambia la posición del vinilo para parecer que se ha detenido:

```javascript
song.vinyl.style.transform = 'translate(-100%, 0)';
```


```javascript

song.audio.pause();
```




## Este código en Python se vería algo así:
```python
# Simulación de la clase Song en Python
class Song:
    def __init__(self, key_song, value_song):
        self.element = key_song  # Representación del selector de HTML
        self.audio = value_song  # Ruta de la canción
        self.is_playing = False  # Estado de la canción (reproduciendo o no)

    def play_song(self):
        if not self.is_playing:
            print(f"Playing {self.audio}")
            self.is_playing = True
        else:
            print(f"Pausing {self.audio}")
            self.is_playing = False

# Clase Player que recibe un diccionario similar a 'map' en JS
class Player:
    def __init__(self, song_map):
        aux = 1

        # Recorre el diccionario con clave-valor como lo haría Object.entries()
        for key, value in song_map.items():
            s_key = key  # En JS es el selector CSS como '.item-1'
            s_value = value  # Ruta de la canción como 'song1.mp3'
            s_cover = f"cv{aux}"  # Clase de la portada en CSS, como '.cv1'

            # Crea una instancia de Song
            song = Song(s_key, s_value)
            self.play_song(song)  # Simula la reproducción de la canción
            aux += 1

    def play_song(self, song):
        song.play_song()  # Llama al método play_song de la clase Song


# Simulamos el objeto 'map' de JavaScript en Python como un diccionario
songs = {
    ".item-1": "song1.mp3",
    ".item-2": "song2.mp3",
    ".item-3": "song3.mp3"
}

# Creamos una instancia de Player y le pasamos el diccionario 'songs'
player = Player(songs)

```
