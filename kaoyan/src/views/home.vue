<template>
  <div class="home">
    <div class="container">
      <schoolLocation></schoolLocation>
      <indexSchool></indexSchool>
    </div>
    <div class="hotSearch">
      <hotSearch></hotSearch>
    </div>
  </div>
</template>

<script>
import { defineComponent, DefineComponent,onMounted} from 'vue';
import schoolLocation from '@/components/schoolLocation.vue'
import indexSchool from '@/components/indexSchool.vue'
import hotSearch from '@/components/hotSearch.vue'
import store from '@/store'
export default defineComponent({
  components: { indexSchool, schoolLocation,hotSearch },
  setup() {
    onMounted(() => {
      // store.dispatch('showAllSchool')
    })

    return {

    }

  }
})
</script>

<style scoped>
.home {
  display: flex;
}

.container {
  width: 1000px;
}

.hotSearch {
  float: right;
  border: 1px solid #eee;
  width: 300px;
  height: 800px;
  /* background-color: red; */
  margin-left: 50px;
  border-radius: 15px;
}
</style>
