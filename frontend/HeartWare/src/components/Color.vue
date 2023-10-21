<script setup lang="ts">
// this vue file is for the color picker
// list four color buttons

import { ref, watch } from "vue";
const emit = defineEmits({ color: String });
const color = ref("blue");

watch(color, (c: string) => {
  emit("color", c);
  let tmp = "";
  switch (c) {
    case "#490009": // red
      tmp = "#270005";
      break;
    case "#503c00": // orange
      tmp = "#352700";
      break;
    case "#3b531f": // green
      tmp = "#1f2c10";
      break;
    case "#183D3D": // teal
      tmp = "#102929";
      break;
    case "#19376D": // blue
      tmp = "#132953";
      break;
    case "#451952": // purple
      tmp = "#270e2e";
      break;
    default:
      console.log(`something wrong with color`);
      tmp = "teal";
  }
  document.body.style.backgroundColor = tmp;
});
</script>
<template>
  <div class="color-picker">
    <label class="orange">
      <input type="radio" name="color" value="#490009" v-model="color" />

      <div class="button"><span></span></div>
    </label>

    <label class="amber">
      <input type="radio" name="color" value="#503c00" v-model="color" />

      <div class="button"><span></span></div>
    </label>

    <label class="lime">
      <input type="radio" name="color" value="#3b531f" v-model="color" />

      <div class="button"><span></span></div>
    </label>

    <label class="teal">
      <input type="radio" name="color" value="#183D3D" v-model="color" />

      <div class="button"><span></span></div>
    </label>

    <label class="blue">
      <input type="radio" name="color" value="#19376D" v-model="color" />

      <div class="button"><span></span></div>
    </label>

    <label class="indigo">
      <input type="radio" name="color" value="#451952" v-model="color" />

      <div class="button"><span></span></div>
    </label>
  </div>
</template>

<style>
.color-picker {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 10px;
  margin-bottom: 10px;
}

input[type="radio"] {
  display: none;
}

.button {
  display: inline-block;
  position: relative;
  width: 50px;
  height: 50px;
  margin: 10px;
  cursor: pointer;
}

.button span {
  display: block;
  position: absolute;
  width: 30px;
  height: 30px;
  padding: 0;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  -o-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  border-radius: 100%;
  background: #eeeeee;
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.26);
  transition: ease 0.3s;
}

.orange .button span {
  background: #52000a;
}

.amber .button span {
  background: #503c00;
}

.lime .button span {
  background: #3b531f;
}

.teal .button span {
  background: #183d3d;
}

.blue .button span {
  background: #19376d;
}

.indigo .button span {
  background: #471a55;
}

.layer {
  display: block;
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background: transparent;
  /*transition: ease .3s;*/
  z-index: -1;
}

.orange input:checked ~ .layer {
  background: #270005;
}

.amber input:checked ~ .layer {
  background: #352700;
}

.lime input:checked ~ .layer {
  background: #1f2c10;
}

.teal input:checked ~ .layer {
  background: #102929;
}

.blue input:checked ~ .layer {
  background: #132953;
}

.indigo input:checked ~ .layer {
  background: #270e2e;
}
</style>
