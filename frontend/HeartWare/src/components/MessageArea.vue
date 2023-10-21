<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps({
    messages: [Object]
})

let default_messages = [
    {id: 0, role: 'ai', content: 'Hello, how may I help you?'},
    {id: 1, role: 'user', content: 'I\'m a depressed ETH student...'}
]

const message_class = ref('')

</script>


<template>

<div class="wrapper">
    <div class="message">
        <div class="message__outer">
            <div class="message__avatar"></div>
            <div class="message__inner">
                <div :class="(msg.role == 'ai') ? 'ai-msg' : 'user-msg'" v-for="msg in (messages || default_messages)" key:msg.id> 
                    <!-- like message__bubble -->
                    {{ msg.content }}
                </div>
            <div class="message__spacer"></div>
            </div>
        </div>
    </div>
</div>



</template>


<style>

/* .message__outer {
  display: flex;
}

.message__inner {
  flex: 1;
  display: flex;
  flex-direction: row-reverse;
}

.message__bubble {
  max-width: calc(100% - 67px);
  overflow-wrap: break-word;
} */

.wrapper {
    display: grid;
    grid-gap: 5px;
}



.ai-msg {
    border: 1px;
    border-style: solid;
    border-color: black;
    border-radius: 5px;
    border-collapse: collapse;

    text-align: left;
    color: black;
    padding: 5px;
}

.user-msg {
    border: 1px;
    border-style: solid;
    border-color: black;
    border-radius: 5px;
    border-collapse: collapse;

    text-align: right;
    color: blue;
    padding: 5px;
}
</style>