//el Player toma el objeto map de canciones, crea instancias de Song y llama a una 
//función play_song para permitir la reproducción de la canción

import Song, {play_song} from './song.js';

export default class Player {
    constructor(map){
        Object.entries(map);
        let aux = 1;
        for (var[key, value] of Object.entries(map)) {
            //crea la instancia para song
            //invoca la funcion para reporducir la cancion
            const song = new Song(key, value, '.album');
            play_song(song);
            aux ++;
        }
    }
}

