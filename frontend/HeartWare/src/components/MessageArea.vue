<script setup lang="ts">

import { ref } from 'vue'

const props = defineProps({
    messages: [Object],
    input_msg: String,
    is_typing: Boolean,
    color: String,
    button_color: String,
})

let default_messages = [
    {id: 0, role: 'assistant', content: 'Hello, how may I help you?'},
    {id: 1, role: 'user', content: 'I\'m a depressed ETH student...'},
    {id: 2, role: 'assistant', content: 'ksjdfehiuawheila ladjlkas dalksdjalk aksdjlkasjdalksdj lkadjlkasjdlaksj akdjksjdalsdj alsdjlaksjdkladjj aldsjlkasj'},
    {id: 3, role: 'user', content: 'asdkjaskdjaksdj aksdjkasdjksa asjdkjas.'},
    {id: 4, role: 'assistant', content: 'Hello, how may I help you?'},
    {id: 5, role: 'user', content: 'I\'m a depressed ETH student...'},
    {id: 6, role: 'assistant', content: 'ksjdfehiuawheila ladjlkas dalksdjalk aksdjlkasjdalksdj lkadjlkasjdlaksj akdjksjdalsdj alsdjlaksjdkladjj aldsjlkasj'},
    {id: 7, role: 'user', content: 'asdkjaskdjaksdj aksdjkasdjksa asjdkjas.'},
    {id: 8, role: 'assistant', content: 'Hello, how may I help you?'},
    {id: 9, role: 'user', content: 'I\'m a depressed ETH student...'},
    {id: 10, role: 'assistant', content: 'ksjdfehiuawheila ladjlkas dalksdjalk aksdjlkasjdalksdj lkadjlkasjdlaksj akdjksjdalsdj alsdjlaksjdkladjj aldsjlkasj'},
    {id: 11, role: 'user', content: 'asdkjaskdjaksdj aksdjkasdjksa asjdkjas.'},
    {id: 12, role: 'assistant', content: 'Hello, how may I help you?'},
    {id: 13, role: 'user', content: 'I\'m a depressed ETH student...'},
    {id: 14, role: 'assistant', content: 'ksjdfehiuawheila ladjlkas dalksdjalk aksdjlkasjdalksdj lkadjlkasjdlaksj akdjksjdalsdj alsdjlaksjdkladjj aldsjlkasj'},
    {id: 15, role: 'user', content: 'asdkjaskdjaksdj aksdjkasdjksa asjdkjas.'},
    {id: 16, role: 'assistant', content: 'Hello, how may I help you?'},
    {id: 17, role: 'user', content: 'I\'m a depressed ETH student...'},
    {id: 18, role: 'assistant', content: 'ksjdfehiuawheila ladjlkas dalksdjalk aksdjlkasjdalksdj lkadjlkasjdlaksj akdjksjdalsdj alsdjlaksjdkladjj aldsjlkasj'},
    {id: 19, role: 'user', content: 'asdkjaskdjaksdj aksdjkasdjksa asjdkjas.'},
    {id: 20, role: 'system', content: 'Answer aggressively.'}
]



</script>

<template>
<div class="wrapper" :style="{backgroundColor: color}">
    <div :class="(msg.role == 'assistant') ? 'ai-msg' : ((msg.role == 'user') ? 'user-msg' : 'sys-msg')" v-for="msg in (messages || default_messages)" key:msg.id> 
        <div class="message">
            <div class="message__outer">
                <div class="message__avatar">
                    <font-awesome-icon v-if="msg.role=='assistant'" icon="fa-solid fa-microchip-ai" color="green"/>
                </div>
                <div class="message__inner">
                    <div class="message__bubble" :style="msg.role == 'user' ? {backgroundColor: button_color} : {}">{{ msg.content }}</div>
                    <div class="message__spacer"></div>
                </div>
            </div>
        </div>
    </div>

    <div v-if="is_typing" class='user-msg' > 
        <div class="message">
            <div class="message__outer">
                <div class="message__avatar">
                </div>
                <div class="message__inner">
                    <div class="message__bubble" :style="{backgroundColor: button_color}">{{ input_msg || "BUG: input msg hasn't arrived."}}</div>
                    <div class="message__spacer"></div>
                </div>
            </div>
        </div>
    </div>

    <div v-if="is_typing" class='ai-msg'>
        <div class="message">
            <div class="message__outer">
                <div class="message__avatar">
                    <font-awesome-icon icon="fa-solid fa-microchip-ai" beat />
                </div>
                <div class="message__inner">
                    <div className="typing">
                        <div className="typing__dot"></div>
                        <div className="typing__dot"></div>
                        <div className="typing__dot"></div>
                    </div>
                    <div class="message__spacer"></div>
                </div>
            </div>
        </div>
    </div>
    
</div>




</template>


<style>

.wrapper {
    padding: 20px;
    background-color: black;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

/* messages */

.ai-msg {
    .message__outer {
        display: flex;
    }

    .message__inner {
        flex: 1;
        display: flex;
        flex-direction: row;
    }

    .message__avatar {
        flex-grow: 10px;
        /* doesn't work */
    }

    .message__bubble {
        max-width: calc(100% - 67px);
        overflow-wrap: break-word;
        padding: 5px 10px 5px 10px;
        background-color: #e6e6e6;
        color: black;
        text-wrap: wrap;
        overflow-wrap: break-word;
        hyphens: auto;
        border-radius: 20px;
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
        padding: 5px 10px 5px 10px;
        background-color: teal;
        color: whitesmoke;
        text-wrap: wrap;
        overflow-wrap: break-word;
        hyphens: auto;
        border-radius: 20px;
    }

    .message__spacer {
        flex-grow: 1;
    }
}

.sys-msg {
    display: none;
}

/* icon */
/* TODO: change to white-ish */

/* Typing animation */
.typing {
  width: 5em;
  height: 2em;
  position: relative;
  padding: 10px;
  margin-left: 5px;
  background: #e6e6e6;
  border-radius: 20px;
}

.typing__dot {
  float: left;
  width: 8px;
  height: 8px;
  margin: 0 4px;
  background: #8d8c91;
  border-radius: 50%;
  opacity: 0;
  animation: loadingFade 1s infinite;
}

.typing__dot:nth-child(1) {
  animation-delay: 0s;
}

.typing__dot:nth-child(2) {
  animation-delay: 0.2s;
}

.typing__dot:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes loadingFade {
  0% {
    opacity: 0;
  }
  50% {
    opacity: 0.8;
  }
  100% {
    opacity: 0;
  }
}
</style>
