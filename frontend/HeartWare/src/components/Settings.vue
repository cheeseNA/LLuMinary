<script setup lang="ts">
import { ref, watch } from "vue";
import Color from "./Color.vue";

const emit = defineEmits({ color: String, backgroundColor: String });
const extended = ref(false);
const enabled = ref(false);
const color = ref("blue");
watch(color, (c) => {
  emit("color", c);
});

const deleteConversation = () => {
  localStorage.clear();
};
</script>

<template>
  <font-awesome-icon
    @click="
      () => {
        enabled = !enabled;
        extended = !extended;
      }
    "
    :class="{ settings: true, rotater: enabled }"
    :icon="['fas', 'gear']"
    color="color"
  />
  <div :class="{ sidebar: extended, minimized: !extended }">
    <Color @color="(c) => (color = c)" />
    <font-awesome-icon
      @click="deleteConversation"
      :icon="['fas', 'trash']"
      :class="{ settings: true }"
    />
  </div>
</template>

<style>
.minimized {
  /* width: 0px; */
  opacity: 0%;
  transition-duration: 0.6s;
  display: none;
}
.sidebar {
  display: flex;
  justify-content: center;
  opacity: 100%;
  transition-duration: 0.6s;
}

.rotater {
  transform: rotate(180deg);
}
.settings {
  opacity: 60%;
  transition-duration: 0.9s;
}
.settings:hover {
  opacity: 100%;
  transition-duration: 0.6s;
}
</style>
