<script setup lang="ts">
import MessageArea from "./MessageArea.vue";
import InputArea from "./InputArea.vue";
import { ref } from "vue";
import { useStorage } from "@vueuse/core";

interface Message {
  id: number;
  role: string;
  text: string;
}
localStorage.clear();
if (localStorage.getItem("conversation") === null) {
  localStorage.setItem("conversation", "[]");
}
const conversation = useStorage("conversation", Array<Message>(), localStorage);
conversation.value.push({ id: 1, role: "user", text: "hello" });
conversation.value.forEach((item, index) => {
  item.id = index + 1;
});
</script>

<template>
  <p>{{ conversation }}</p>
  <!-- <ul> -->
  <!--   <li v-for="t in conversation">{{ t }}</li> -->
  <!-- </ul> -->
</template>

<style></style>
