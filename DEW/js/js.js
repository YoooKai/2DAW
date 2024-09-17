//-------Curso Javascript------------// 
//Es lo que hace la página web interactiva, como por ejemplo añadir un producto al carrito al hacer click a un botón.
// Para calcular el porcentaje de algo en js, se multiplica el total por 0.num, por ejem, 10% sería total * 0.1
//Tipos de datos
//Integer: 1, 2, 3, 4
//Floats: 1.1, 2,6, 6.3 - A veces no es accurate el cálculo de floats

//cALCULAR flotantes de manera accurate con dinero:
//sumar en monedas, en céntimos, y convertir de nuevo a dólares:
//  20.95  7.99
(2095 + 799) / 100

//REDONDEAR NÚMERO: 
Math.round(2.2)
//2

//consigue el porcentaje de tax
Math.round((2097 + 677) * 0.1) / 100

//En consola para pegar texto se debe escribir: allow pasting
Math,round((1899 + 799 + 487) * 0.1) / 100 

// STRINGS
alert('hey') // hace un popup
'some ' + 'text' + 3 //combinar strings, concatenación, y convierte nums en strings
typeof 2 //nos dice el tipo de dato que es
//number

//combinar cadenas con nums, utilizamos corchetes para elegir orden de operaciones
'$' + (2095 + 799) / 100
// $28.94

'Items(' + (1 + 1) + '):$' + (2096 + 600) / 100
'Items (2): $28.94'

//se pueden usar comillas simples o dobles, mejor usar simples excepto que dentro hayan ya comillas simples
"I'm learning JavaScript"
// o se pueden escape characters: \" o \'
'I\'m learning JavaScript'
//para hacer un salto de línea: \n
alert('some\ntext');
//template strings: permiten INTERPOLATION, más simple que concatenar
`hello`
`Items (${1 + 1}): $${(2097 + 799) / 100}`
// 'Items (2): $28.94'

//Cadenas multilínea: se usan template strings
`some
text`

//VARIABLES




