<script lang="ts" setup>
import { ref } from "vue";
const input = ref("");
const emit = defineEmits(["response"]);
</script>

<template>
  <input v-model="input" type="text" />
  <button v-on:click="emit('response', input)">Send</button>
</template>

<style></style>
