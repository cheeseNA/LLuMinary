<script setup lang="ts">
import Handler from "./components/Handler.vue";
import Settings from "./components/Settings.vue";
import { ref, watch } from "vue";
const color = ref("blue");
</script>

<template>
  <Suspense>
    <Settings
      @color="
        (c) => {
          color = c;
        }
      "
    />
    <Handler :color="color" />
    <template #fallback>Awaiting Websocket...</template>
  </Suspense>
</template>

<style scoped></style>
