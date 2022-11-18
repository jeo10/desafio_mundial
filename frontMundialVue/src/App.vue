<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <RouterView />
</template>

<style scoped>

</style>

<script>
  export default {
    created() {
      this.$router.push('/')
    }
  }
</script>