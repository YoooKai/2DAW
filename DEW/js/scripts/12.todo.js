const todoList = [{
    name: 'make dinner',
    dueDate: '2022-12-22'
  }, {
    name: 'wash dishes',
    dueDate: '2022-12-22'
  }];
  
  renderTodoList();
  
  function renderTodoList() {
    let todoListHTML = '';
    todoList.forEach((todoObject, index) => {
      const { name, dueDate } = todoObject;
      const html = `
        <div>${name}</div>
        <div>${dueDate}</div>
        <button class="delete-todo-button js-delete-todo-btn">Delete</button> 
      `;
      todoListHTML += html;

    });
    
  
    document.querySelector('.js-todo-list')
      .innerHTML = todoListHTML;
      //debe estar aquí cuando los botones se hayan puesto en la pag, y con Selectorall, selecciona todos los delete
      document.querySelectorAll('.js-delete-todo-btn').forEach((deleteBtn, index) => {
        deleteBtn.addEventListener('click', () => {
          todoList.splice(index, 1);
          renderTodoList();
        });
      });
  }
  
  document.querySelector('.js-add-todo-btn').addEventListener('click', () => {
    addTodo();
  });



  function addTodo() {
    const inputElement = document.querySelector('.js-name-input');
    const name = inputElement.value;
  
    const dateInputElement = document.querySelector('.js-due-date-input');
    const dueDate = dateInputElement.value;
  
    todoList.push({
      //name: name,
      //dueDate: dueDate,
      name,
      dueDate
    });
  
    inputElement.value = '';
  
    renderTodoList();
  }