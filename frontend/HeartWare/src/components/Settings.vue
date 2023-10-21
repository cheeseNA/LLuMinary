<script setup lang="ts">
import { ref } from "vue";

const extended = ref(false);
</script>

<template>
  <div v-if="extended"></div>
  <div v-else>
    <font-awesome-icon :icon="['fas', 'gear']" />
  </div>
</template>

<style></style>
