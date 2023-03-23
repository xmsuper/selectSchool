<template>
  <Loader v-if="isLoading"></Loader>
  <navHeader></navHeader>
    <RouterView></RouterView>

</template>

<script>
import home from '@/views/home.vue'
import { defineComponent,computed,onMounted} from 'vue';
import navHeader from './components/navHeader.vue';
import store from './store';
import Loader from './components/Loader.vue';
export default defineComponent({
  name:'App',
  components:{navHeader,Loader},
  setup() {
    //此时是flase
    const isLoading=computed(()=>store.state.loading)

    return {
      isLoading
    }

  }
})
</script>

<style scoped></style>
