<script setup lang="ts">
import MessageArea from "./MessageArea.vue";
import InputArea from "./InputArea.vue";
import { ref, watch } from "vue";
import { useStorage } from "@vueuse/core";

interface Message {
  id: number;
  role: string;
  text: string;
}

interface Argument {
  role: string;
  content: string;
}
localStorage.clear();

const waiting = ref(true);
const socket = new WebSocket("wss://lluminaries.serveo.net/chat");
const awaitConnection = (s: WebSocket) => {
  return new Promise((resolve): void => {
    if (s.readyState !== s.OPEN) {
      socket.onopen = (_: any) => {
        waiting.value = false;
        resolve(null);
      };
    } else {
      waiting.value = false;
      resolve(null);
    }
  });
};
await awaitConnection(socket);

const tmp = localStorage.getItem("conversation");
if (tmp === null) {
  socket.send("");
  localStorage.setItem("conversation", "[]");
} else {
  socket.send(tmp);
}

const conversation = useStorage(
  "conversation",
  Array<Argument>(),
  localStorage,
);
const indexed_conv = ref(Array<Message>());

socket.onmessage = (e: MessageEvent) => {
  const raw_data = e.data;
  conversation.value = JSON.parse(raw_data);
};

const send_to_llm = (text: string) => {
  socket.send(text);
};

watch(conversation, (conv) => {
  indexed_conv.value = conv.map((item, index): Message => {
    return {
      id: index + 1,
      role: item.role,
      text: item.content,
    };
  });
});
console.log("This finishes");
</script>

<template>
  <p v-if="waiting">Waiting right now...</p>
  <p v-else>Connection made</p>
  <p>{{ conversation }}</p>
  <!-- <MessageArea :messages="indexed_conv" /> -->
  <!-- <InputArea v-on:response="send_to_llm" /> -->
  <!-- <ul> -->
  <!--   <li v-for="t in conversation">{{ t }}</li> -->
  <!-- </ul> -->
</template>

<style></style>
