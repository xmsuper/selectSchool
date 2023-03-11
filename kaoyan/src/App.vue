<template>
  <indexSchool></indexSchool>
  <RouterView></RouterView>
</template>

<script>
import indexSchool from './views/indexSchool.vue';
import { defineComponent } from 'vue';
export default defineComponent({
  name:'App',
  components:{indexSchool},
  setup() {


    return {

    }

  }
})
</script>

<style lang="scss" scoped></style>
