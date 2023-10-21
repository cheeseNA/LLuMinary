<script setup>
import {ref} from 'vue';
</script>


<template>

<!-- <div class="wrapper">
    
</div> -->

<div class="d-flex justify-content-center">
  <div class="container container-child">
    <div class="card">
      <div class="card-body">
        <div class="text-left"><span class="badge badge-pill badge-secondary" title="2020-01-01 09:00:00">Hello</span></div>
        <div class="text-right"><span class="badge badge-pill badge-primary" title="2020-01-01 09:00:00">World</span></div>
      </div>
      <div class="card-footer">
        <div class="input-group input-group-sm">
          <input type="text" class="form-control" placeholder="Your message..." autofocus />
          <div class="input-group-append">
            <button type="button" class="btn btn-primary"><i class="fa fa-paper-plane-o fa-fw"></i><span class="d-none d-sm-inline"> Send</span></button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

</template>


<style>
/* .wrapper {
    display: grid;
}

.ai-msg {

}

.user-msg {

} */

.d-flex {
    height: 100%;
  }

  .card {
    height: 100%;
  }

  .card-body {
    overflow-y: auto;
  }

  .badge {
    font-weight: 400;
  }
</style>