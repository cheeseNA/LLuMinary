<script setup lang="ts">
import { ref } from "vue";

const extended = ref(false);
const
</script>

<template>
  <div v-if="extended"></div>
  <div v-else>
    <p :class="settings">Placeholder</p>
  </div>
</template>

<style>
.settings {
}
</style>
