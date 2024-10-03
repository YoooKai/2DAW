//creo array vacío donde se meterán los valores del input
const todoList = [];

function addTodo() {
    //meto el input en una variable
    const inputElement = document.querySelector('.js-name-input');
    //guardo el valor (texto que metamos en caja de texto)en otra variable
    const name = inputElement.value;
    //meto el valor en el array vacío, ahí se van añadiendo todos
    todoList.push(name);
    //muestro en consola el array
    console.log(todoList);

    //VACIAR/resetear el cuadro de texto después de hacer lo anterior
    inputElement.value = '';
}