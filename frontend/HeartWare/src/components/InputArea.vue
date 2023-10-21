<script setup lang="ts">
import { ref } from 'vue'
const input = ref("");
const emit = defineEmits(["response"]);

const props = defineProps({
    is_typing: Boolean,
    color: String,
})

</script>

<template>
  <div class="chat-input-container" :style='{backgroundColor: color}'>
    <input v-model="input" type="text" class="chat-input" placeholder="Type your message...">
    <button v-on:click="emit('response', input); input=''" class="send-button" :disabled="is_typing">Send</button>
  </div>
</template>

<style>
  /* Chat input container */
  .chat-input-container {
    display: flex;
    align-items: center;
    width: 100%;
    background-color: black;
    padding: 10px;
  }

  /* Chat input field */
  .chat-input {
    flex: 1;
    border: none;
    border-radius: 5px;
    padding: 10px;
  }

  /* Send button */
  .send-button {
    background-color: teal;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    margin-left: 10px;
    cursor: pointer;
  }

  input {
    /* outline-color: white;
    outline-offset: -5px; */
    outline-color: teal;
  }
</style>
