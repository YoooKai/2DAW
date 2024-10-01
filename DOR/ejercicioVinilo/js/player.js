//el Player toma el objeto map de canciones, crea instancias de Song y llama a una 
//función play_song para permitir la reproducción de la canción

import song, {play_song} from './song.js';

export default class Player {
    constructor(map){
        Object.entries(map);
        let aux = 1;
        for (var[key, value] of Objects.entries(map)) {
            //crea la instancia para song
            //invoca la funcion para reporducir la cancion
            const song = [key, value];
            play_song(song);
            aux ++;
        }
    }
}

