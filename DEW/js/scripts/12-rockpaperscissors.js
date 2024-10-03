//Almacenamiento del marcador en localStorage

let score = JSON.parse(localStorage.getItem('score')) || {
    wins: 0,
    losses: 0,
    ties: 0
};

// Actualizar el marcador visualmente
updateScoreElement();


// Callback: Es la función que se ejecuta cada cierto intervalo de tiempo (en este caso, 1 segundo).
// Delay: Especifica el tiempo entre cada ejecución, en milisegundos.


let isAutoPlaying = false;
let intervalId;


function autoPlay() {
    if(!isAutoPlaying){
        //darle un id
        intervalId = setInterval(() => {
            const playerMove = pickComputerMove();
            playGame(playerMove);
        }, 1000);
        isAutoPlaying = true;
    }else{
        //parar el intervalo con esa id
        clearInterval(intervalId); 
        isAutoPlaying = false;
    } 
}

document.querySelector('.js-rock-btn')
.addEventListener('click', () => {
    playGame('rock');
})

document.querySelector('.js-paper-btn')
.addEventListener('click', () => {
    playGame('paper');
})

document.querySelector('.js-scissors-btn')
.addEventListener('click', () => {
    playGame('scissors');
})


// Función para jugar el juego: playGame()
function playGame(playerMove) {
const computerMove = pickComputerMove();
let result = '';

// Condiciones para determinar el resultado

if (playerMove === 'scissors') {
    if (computerMove === 'rock') {
        result = 'You lose.'
    } else if (computerMove === 'paper') {
        result = 'You win.';
    } else if (computerMove === 'scissors') {
        result = 'Tie.';
    } 
    
} else if (playerMove === 'paper') {
if (computerMove === 'rock') {
    result = 'You win.'
} else if (computerMove === 'paper') {
    result = 'Tie.';
} else if (computerMove === 'scissors') {
    result = 'You lose.';
} 

} else if (playerMove === 'rock') {
    if (computerMove === 'rock') {
    result = 'Tie.';
} else if (computerMove === 'paper') {
    result = 'You lose.';
} else if (computerMove === 'scissors') {
    result = 'You win.';
}
}

//Actualizar el marcador basado en el resultado

if (result === 'You win.') {
    score.wins += 1;
} else if (result === 'You lose.') {
    score.losses += 1;
} else if (result === 'Tie.') {
    score.ties += 1;
}


//Guardar el marcador en localStorage
localStorage.setItem('score',JSON.stringify(score));


updateScoreElement();

//Actualizar la interfaz con el resultado y movimientos, muestra info
document.querySelector('.js-result').innerHTML = result;
document.querySelector('.js-moves').innerHTML = 

`You
<img src="img/${playerMove}-emoji.png" alt="">
<img src="img/${computerMove}-emoji.png" alt="">
Computer

`

}

// Actualizar el marcador en la interfaz
function updateScoreElement() {
document.querySelector('.js-score')
.innerHTML =`Wins: ${score.wins} Losses: ${score.losses} Ties: ${score.ties}`;
}

// Función para que pc elija un movimiento aleatorio

let computerMove = '';

function pickComputerMove() {
const randomNumber = Math.random();

if (randomNumber >= 0 && randomNumber < 1/3) {
    computerMove = 'rock';

} else if (randomNumber >= 1/3 && randomNumber < 2/3) {
    computerMove = 'paper';
} else if (randomNumber >= 2/3 && randomNumber < 1) {
    computerMove = 'scissors';
}

return computerMove;

}
