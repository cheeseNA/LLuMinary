<script setup lang="ts">
import MessageArea from './MessageArea.vue';

let id = 0

const messages = ref([{id: id++, role: 'ai', text: 'Hey, how can I help you?'}])
const newMessage = ref('')

function addMessage() {
    console.log('added message')
    sendMsgToAI()
    messages.value.push({ id: id++, role: 'user', text: newMessage.value })
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
    <MessageArea />
</template>

<style></style>