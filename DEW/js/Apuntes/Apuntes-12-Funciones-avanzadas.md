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