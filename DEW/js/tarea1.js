// 1. Implementar el control de 3 variables (a, b, c) para que se muestre un mensaje de error cuando se
// produzca alguna de las siguientes situaciones:
// a) Al menos una de las 3 variables es negativa
// b) Las tres variables son iguales a 0
// c) Las suma de las 3 variables es mayor que 10 Y las tres variables son diferentes
let a = 7
let b = 54
 let c = -3

if (a || b || c < 0) {
    console.log('ERROR. Una de las variables tiene un valor negativo.');
} else if (a === 0 && b === 0 && c === 0) {
    console.logg('ERROR. Todas las variables son iguales a 0.');
} else if (((a + b + c) > 10) && (a !== b && a !== c && b !== c)) {
    console.log('ERROR. La suma de los números es mayor a 10 y las tres variables no son distintas.');
}
