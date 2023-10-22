<script setup lang="ts">
import MessageArea from "./MessageArea.vue";
import InputArea from "./InputArea.vue";
import Color from "./Color.vue";
import { ref, watch, computed } from "vue";
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

const props = defineProps({ color: String });

const rsp = ref("");
const typing = ref(false);

// localStorage.clear(); //TODO -------------------------------------------------------------------------------------------------------------------------------------------------

const socket = new WebSocket("ws://localhost:8000/chat");
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
  if (text !== "" || typing.value) {
    socket.send(text);
    typing.value = true;
    rsp.value = text;
  }
};

watch(conversation, (conv) => {
  console.log(conv);
  indexed_conv.value = conv.map((item, index): Message => {
    return {
      id: index + 1,
      role: item.role,
      content: item.content,
    };
  });
});

const button_color = computed(() => {
  switch (props.color) {
    case "#490009": // red
      return "#b40000";
      break;
    case "#503c00": // orange
      return "#c98300";
      break;
    case "#3b531f": // green
      return "green";
      break;
    case "#183D3D": // teal
      return "teal";
      break;
    case "#19376D": // blue
      return "#2222da";
      break;
    case "#451952": // purple
      return "purple";
      break;
    default:
      console.log(`something wrong with color`);
      return "teal";
  }
});
</script>

<template>
  <MessageArea
    :messages="indexed_conv"
    :input_msg="rsp"
    :is_typing="typing"
    :color="color"
    :button_color="button_color"
  />
  <InputArea
    id = "floor"
    v-on:response="send_to_llm"
    :is_typing="typing"
    :color="color"
    :button_color="button_color"
  />
</template>

<style>
  #floor {
    float: bottom;
  }
</style>
