<script setup>
import {ref} from 'vue'

let id = 0

const messages = ref([{id: id++, role: 'ai', text: 'Hey, how can I help you?'}])
const newMessage = ref('')

function addMessage() {
    console.log('added message')
    sendMsgToAI()
    messages.value.push({id: id++, role: 'user', text: newMessage.value })
    newMessage.value = ''
    fetchAIresponse()
}

function sendMsgToAI() {
    // TODO
}

function fetchAIresponse() {
    // TODO
}


</script>


<template>

<div class="wrapper">
    <form @submit.prevent="addMessage">
        <input v-model="newMessage">
        <button>Send</button>    
    </form>

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