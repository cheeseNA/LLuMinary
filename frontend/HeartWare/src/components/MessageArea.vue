<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps({
    messages: [Object]
})

let default_messages = [
    {id: 0, role: 'ai', content: 'Hello, how may I help you?'},
    {id: 1, role: 'user', content: 'I\'m a depressed ETH student...'},
    {id: 2, role: 'ai', content: 'ksjdfehiuawheila ladjlkas dalksdjalk aksdjlkasjdalksdj lkadjlkasjdlaksj akdjksjdalsdj alsdjlaksjdkladjj aldsjlkasj'},
    {id: 3, role: 'user', content: 'asdkjaskdjaksdj aksdjkasdjksa asjdkjas.'}
]

const message_class = ref('')

</script>


<template>
<div class="wrapper">
    <div :class="(msg.role == 'ai') ? 'ai-msg' : 'user-msg'" v-for="msg in (messages || default_messages)" key:msg.id> 
        <div class="message">
            <div class="message__outer">
                <div class="message__avatar"></div>
                <div class="message__inner">
                    <div class="message__bubble">{{ msg.content }}</div>
                    <div class="message__spacer"></div>
                </div>
            </div>
        </div>
    </div>
</div>




</template>


<style>

.wrapper {
    padding: 10px;
    border-radius: 5px;
    background-color: black;
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.ai-msg {
    .message__outer {
        display: flex;
    }

    .message__inner {
        flex: 1;
        display: flex;
        flex-direction: row;
    }

    .message__bubble {
        max-width: calc(100% - 67px);
        overflow-wrap: break-word;
        padding: 5px;
        background-color: lightgray;
        color: black;
        text-wrap: wrap;
        overflow-wrap: break-word;
        hyphens: auto;
        border: solid darkgray 1px;
        border-radius: 5px;
    }

    .message__spacer {
        flex-grow: 1;
    }
}

.user-msg {
    .message__outer {
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
        padding: 5px;
        background-color: teal;
        color: whitesmoke;
        text-wrap: wrap;
        overflow-wrap: break-word;
        hyphens: auto;
        border: solid darkslategray 1px;
        border-radius: 5px;
    }

    .message__spacer {
        flex-grow: 1;
    }
}
</style>