export default class Song {
    constructor (key,value,c_song){
        this.element = document.querySelector(key);
        this.audio = new Audio(value);
        this.album = document.querySelector(c_song);

    }
}

export function play_song(song){
    song.element.onclick = () => {
        if(song.audio.paused){
            song.audio.play();
        }
        else{
            song.audio.pause();
        }
    }
}
