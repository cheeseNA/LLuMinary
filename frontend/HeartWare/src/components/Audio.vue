<script setup lang="ts">
import type { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { timestamp } from "@vueuse/core";
import { onMounted, ref } from "vue"

const audio_sources = [
  '/Arabesque.mp3',
  '/ClaireDeLune.mp3'
]

let track_index = 0
const player = new Audio()
const playing = ref(false)
let first_interaction = true
let fade_intervall = 200

// function loadTrack() {
//     player.src = audio_sources[track_index]
//     player.load()
//     player.play()
// }

function mmTrack() {
  if (!playing.value) {
    if (first_interaction) {
      player.src = audio_sources[track_index]
      player.load()
      player.volume = 0
      player.play()
      first_interaction = false
    }
    // player.play()
    var fadein = setInterval(
    function() {
      // Reduce volume by 0.05 as long as it is above 0
      // This works as long as you start with a multiple of 0.05!
      if (player.volume <= 0.95) {
        player.volume += 0.05
      }
      else {
        // Stop the setInterval when 1 is reached
        // console.log('max reached...')
        player.volume = 1
        clearInterval(fadein);
      }
    }, fade_intervall);
    playing.value = true
  } else {
    // player.pause()
    var fadeout = setInterval(
    function() {
      // Reduce volume by 0.05 as long as it is above 0
      // This works as long as you start with a multiple of 0.05!
      if (player.volume >= 0.05) {
        player.volume -= 0.05
      }
      else {
        // Stop the setInterval when 0 is reached
        // console.log('silence reached...')
        player.volume = 0
        clearInterval(fadeout);
      }
    }, fade_intervall);
    // player.volume = 0
    playing.value = false
  }
}
 
// function nextTrack() {
//   player.pause()
//   track_index = (track_index + 1) % audio_sources.length
//   loadTrack()
// }

// function prevTrack() {
//   player.pause()
//   track_index = (track_index - 1 + audio_sources.length) % audio_sources.length
//   loadTrack()
// }


// onMounted(() => {
//   loadTrack()
// })

</script>

<template>
  <div class = "player">
    <!-- <button @click="prevTrack">Previous</button> -->
    <font-awesome-icon class="but" @click="mmTrack" icon="fa-solid fa-music" />
    <!-- <button @click="nextTrack">Next</button> -->
  </div>
</template>

<style>


.but {
  font-size: 25px;
  color: white;
  opacity: 60%;
  transition-duration: 0.9s;
  padding: 5px;
}
.but:hover {
  opacity: 100%;
  transition-duration: 0.6s;
}

</style>
