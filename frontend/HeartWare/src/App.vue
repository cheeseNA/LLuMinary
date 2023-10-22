<script setup lang="ts">
import Handler from "./components/Handler.vue";
import Settings from "./components/Settings.vue";
import { ref, watch } from "vue";
const color = ref("#222222");
</script>

<template>
  <Suspense>
    <Handler :color="color" />
    <template #fallback>Awaiting Websocket...</template>
  </Suspense>
  <Settings
      @color="
        (c) => {
          color = c;
        }
      "
    />
</template>

<style scoped></style>
