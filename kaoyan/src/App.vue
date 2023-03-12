<template>

  <RouterView></RouterView>
</template>

<script>
import home from '@/views/home.vue'
import { defineComponent } from 'vue';
export default defineComponent({
  name:'App',
  components:{home},
  setup() {


    return {

    }

  }
})
</script>

<style scoped></style>
