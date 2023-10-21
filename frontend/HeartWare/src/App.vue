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
  </Suspense>
</template>

<style scoped></style>
