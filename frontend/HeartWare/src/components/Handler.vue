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
const button_color = ref("teal");

const change_color = (color_input: string) => {
  color.value = color_input;
  switch (color_input) {
    case '#490009': // red
      button_color.value = '#b40000';
      break;
    case '#503c00': // orange
      button_color.value = '#c98300';
      break;
    case '#3b531f': // green
      button_color.value = 'green';
      break;
    case '#183D3D': // teal
      button_color.value = 'teal';
      break;
    case '#19376D': // blue
      button_color.value = '#2222da';
      break;
    case '#451952': // purple
      button_color.value = 'purple';
      break;
    default:
      console.log(`something wrong with color`);
      button_color.value = 'teal';
  }
};

</script>

<template>
  <MessageArea :messages="indexed_conv" :input_msg="rsp" :is_typing="typing" :color="color" :button_color="button_color"/>
  <InputArea v-on:response="send_to_llm" :is_typing="typing" :color="color" :button_color="button_color"/>
  <Color v-on:color="change_color"/>
</template>

<style></style>