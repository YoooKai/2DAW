# Apuntes de JavaScript - Funciones y Callbacks

## Hoisting en funciones

-  **hoisting**: las funciones declaradas con function se "elevan", por lo que puedes llamarlas antes de que estén definidas en el código.
- Este comportamiento no ocurre con las funciones almacenadas en variables.

```javascript
greetings(); // Llamada antes de la definición, gracias al hoisting

function greetings() {
    console.log('hello');
}

greetings(); // Llamada después de la definición
```

## Funciones almacenadas en variables
En JavaScript, las funciones también son un tipo de valor, por lo que puedes almacenarlas en variables.

```javascript
const num = 2;

// Función almacenada en una variable
const funcion1 = function greetings() {
    console.log('hello2');
};

console.log(funcion1); // Imprime la función
console.log(typeof funcion1); // Imprime "function"
funcion1(); // Llama a la función almacenada
```

## Funciones anónimas
Cuando una función no tiene nombre, se denomina función anónima. El nombre no es necesario si ya estamos almacenando la función en una variable.

```javascript
const funcion2 = function() {
    console.log('hello3');
};
funcion2(); // Llama a la función anónima
```

## Funciones dentro de objetos
También puedes almacenar funciones dentro de objetos. Esto es útil para organizar el código.

```javascript
Copiar código
const object1 = {
    num: 2,
    fun: function greetings() {
        console.log('hello4');
    }
};

object1.fun(); // Llama a la función dentro del objeto
```

## Parámetros en funciones
Puedes pasar parámetros a una función y utilizarlos dentro de la misma.

```javascript
function display(param) {
    console.log(param);
}

display(2); // Imprime 2
```

### Pasar funciones como parámetros (Callbacks)
En JavaScript, las funciones pueden ser pasadas como argumentos a otras funciones. Esto se denomina un callback.

```javascript
Copiar código
function run(param) {
    param(); // Llama a la función pasada como argumento
}

run(function() {
    console.log('hello5');
});
```
## Código asíncrono: setTimeout y setInterval

**setTimeout**

Esta función ejecuta una función después de un tiempo específico (en milisegundos). Es asíncrona, lo que significa que no bloquea la ejecución del código posterior.

```javascript
setTimeout(function() {
    console.log('timeout');
}, 3000); // Ejecuta después de 3 segundos

console.log('next line'); // Se ejecuta antes que el timeout
```
**setInterval**

Esta función ejecuta repetidamente una función cada cierto intervalo de tiempo.

```javascript
setInterval(function() {
    console.log('Interval');
}, 3000); // Ejecuta cada 3 segundos

console.log('next line 2');
```


## Recorrer un array: forEach
forEach es una manera moderna y concisa de iterar sobre los elementos de un array. Se le puede pasar una función callback que recibirá los elementos de forma individual.

```javascript
[
    'make dinner',
    'wash dishes',
    'watch anime'
].forEach(function(value) {
    console.log(value);
});
```
Puedes también obtener el índice de cada elemento pasándolo como segundo parámetro al callback.

```javascript
[
    'make dinner',
    'wash dishes',
    'watch anime'
].forEach(function(value, index) {
    if(value === 'wash dishes') {
        return; // Salta la iteración actual
    }
    console.log(value);
    console.log(index);
});
```
**Importante sobre forEach**

- No puedes usar continue o break en un forEach. Para saltar una iteración, usas return.
- Si necesitas romper un bucle, es mejor usar un bucle for tradicional.


## Función Flecha

### Versión normal vs. Arrow function
```javascript
// Versión normal
const regularFunction = function(param, param2) {
    console.log('hello');
    return 5;
};

// Arrow function
const arrowFunction = (param, param2) => {
    console.log('hello');
    return 5;
};
arrowFunction();
```
Ambas versiones usan parámetros y return de manera similar.
Sin embargo, las arrow functions tienen ciertos atajos que las funciones regulares no.

## Arrow function con un solo parámetro
Si una función flecha tiene un solo parámetro, se pueden omitir los paréntesis.

```javascript
const oneParam = param => {
    console.log(param + 1);
};
oneParam(2);
```

## Arrow function en una sola línea
Si la función flecha tiene una sola línea de código, puedes poner la lógica al lado de la flecha, eliminando las llaves y el return.

```javascript
const oneLine = () => 2 + 3;
```
## Práctica con funciones flecha

Es buena práctica usar una función flecha cuando se pasa como argumento a otra función, ya que mejora la legibilidad.

```javascript
[
    'make dinner',
    'wash dishes',
    'watch anime'
].forEach((value, index) => {
    if(value === 'wash dishes'){
        return;
    }
    console.log(value);
    console.log(index);
});
```

## Shorthand method en objetos
Podemos definir métodos en objetos de forma abreviada.

```javascript
const object2 = {
    // Definición tradicional de un método
    method: () => {

    },
    // Definición abreviada (shorthand method)
    method (){

    }
};
```

## Event Listener
El Event Listener permite ejecutar código cuando interactuamos con un elemento, como al hacer clic en un botón.

**Añadir un listener a un botón**

```javascript
const buttonElement = document.querySelector('.js-btn');

const eventListener = () => {
    console.log('click');
};

// Añadimos un evento de click
buttonElement.addEventListener('click', eventListener);
```
``addEventListener``permite múltiples listeners para un mismo evento.

## Remover un listener
Se puede eliminar un listener con removeEventListener.

```javascript
buttonElement.removeEventListener('click', eventListener);
```

## Métodos de Arrays
``Filter``

El método filter crea un nuevo array. Si la función que se le pasa devuelve true, el elemento es añadido al nuevo array. Si devuelve false, no se incluye.

```javascript
Copiar código
console.log([1, -3, 5].filter((value) => {
    return value >= 0;
}));
// Resultado: [1, 5]
```

`Map`

El método map también crea un nuevo array. Lo que devuelva la función se añade al nuevo array.

```javascript
Copiar código
console.log([1, 3, 4].map((value) => value * 2));
// Resultado: [2, 6, 8]
```

## Closure
Closure significa que si una función tiene acceso a un valor, siempre tendrá acceso a ese valor en su entorno actual.
