<template>
  <Loader v-if="isLoading"></Loader>
  <navHeader></navHeader>
  <RouterView></RouterView>
</template>

<script setup>
import home from '@/views/home.vue'
import { computed, onMounted } from 'vue';
import navHeader from './components/navHeader.vue';
import store from './store';
import Loader from './components/Loader.vue';

//此时是flase
const isLoading = computed(() => store.state.loading)

</script>

<style scoped></style>
