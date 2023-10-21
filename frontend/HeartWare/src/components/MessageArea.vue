<script setup lang="ts">
import {ref} from 'vue'






</script>


<template>

<form @submit.prevent="addMessage">
    <input v-model="newMessage">
    <button>Send</button>    
</form>

<div class="wrapper">
    <ul>
        <li v-for="msg in messages" :key="msg.id">
            {{ msg.text }}
        </li>
    </ul>
</div>

</template>


<style>
.wrapper {
    /* display: grid; */
}

.ai-msg {

}

.user-msg {
    
}
</style>