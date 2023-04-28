<template>
  <div class="home">
    <div class="container">
      <schoolLocation @getSchoolCondition="getSchoolValue"></schoolLocation>
      <indexSchool :chooseCondition="chooseCondition"></indexSchool>
    </div>
    <div class="hotSearch">
      <hotSearch></hotSearch>
    </div>
  </div>
</template>

<script setup>
import { watch, toRaw, onMounted, reactive, ref } from 'vue';
import schoolLocation from '@/components/schoolLocation.vue'
import indexSchool from '@/components/indexSchool.vue'
import hotSearch from '@/components/hotSearch.vue'
import store from '@/store'
const chooseCondition = reactive({
  Location: '',
  SchoolType: '',
  SchoolTs: ''
})
const getSchoolValue = (value) => {
  chooseCondition.Location = toRaw(value).Location
  chooseCondition.SchoolType = toRaw(value).SchoolType
  chooseCondition.SchoolTs = toRaw(value).SchoolTs
}
watch(chooseCondition, () => {
  console.log(chooseCondition)
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
