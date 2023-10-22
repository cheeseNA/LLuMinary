<script setup lang="ts">
import Handler from "./components/Handler.vue";
import Settings from "./components/Settings.vue";
import { ref, watch } from "vue";
const color = ref("#222222");
</script>

<template>
  <div class="homepage">
    <div class="settings_cell"><Settings
      @color="
        (c) => {
          color = c;
        }
      "
    /></div>
    <div class="cell">
      <Suspense>
        <Handler :color="color" />
        <template #fallback>Awaiting Websocket...</template>
      </Suspense>
    </div>
    <div class="cell"></div>
  </div>
</template>

<style scoped>
  .homepage {
    display: grid;
    grid-template-areas:
      "div div div";
    grid-template-columns: 1fr 8fr 1fr;
    /* grid-template-rows: repeat(3, minmax(auto, 1fr)); */
    grid-template-rows: auto;
  }

  .settings_cell {
    min-height: 0;
    min-width: 0;
  }
</style>
