<script setup lang="ts">
import MessageArea from "./MessageArea.vue";
import InputArea from "./InputArea.vue";
import Color from "./Color.vue";
import { ref, watch } from "vue";
import { useStorage } from "@vueuse/core";

interface Message {
  id: number;
  role: string;
  content: string;
}

interface Argument {
  role: string;
  content: string;
}

const rsp = ref('')
const typing = ref(false)

localStorage.clear(); //TODO -------------------------------------------------------------------------------------------------------------------------------------------------

const socket = new WebSocket("wss://lluminaries.serveo.net/chat");
const awaitConnection = (s: WebSocket) => {
  return new Promise((resolve): void => {
    if (s.readyState !== s.OPEN) {
      socket.onopen = (_: any) => {
        resolve(null);
      };
    } else {
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
  typing.value = false;
};

const send_to_llm = (text: string) => {
  if (text !== '' || typing.value) {
    socket.send(text);
    typing.value = true;
    rsp.value = text;
  }
};

watch(conversation, (conv) => {
  console.log(conv)
  indexed_conv.value = conv.map((item, index): Message => {
    return {
      id: index + 1,
      role: item.role,
      content: item.content,
    };
  });
});

const color = ref("#222222");

const change_color = (color_input: string) => {
  color.value = color_input;
};

</script>

<template>
  <MessageArea :messages="indexed_conv" :input_msg="rsp" :is_typing="typing" :color="color"/>
  <InputArea v-on:response="send_to_llm" :is_typing="typing" :color="color"/>
  <Color v-on:color="change_color"/>
</template>

<style></style>