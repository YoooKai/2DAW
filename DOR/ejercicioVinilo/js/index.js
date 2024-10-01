//importamos canciones y asociamos cada selector 
import songs from '../assets/songs/*.mp3';
import player from './player.js';


const map = { };

let aux = 1;
for (var key of Object.keys(songs)) {
    //asociar map[`.item-${aux}`] con la canción song [key]
    map[`.item-` + aux] = songs[key];
    aux++;
}
console.log(map);
//crear objeto player y pasar por el objeto map
const player = new player(map); 

//object.keys(nombreObjeto) nos quedamos con un array de las claves, o sea, las propiedades del objeto
