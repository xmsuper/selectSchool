<template>
    <div id='hotMajor' style="width: 370px;height: 300px;">

    </div>
</template>

<script setup>
import { ref,reactive,nextTick,computed,watch,onMounted,onUpdated} from "vue" 
import * as echarts from 'echarts';
var option;

option = {
  title: {
    text: 'Referer of a Website',
    subtext: 'Fake Data',
    left: 'center'
  },
  tooltip: {
    trigger: 'item'
  },
  legend: {
    orient: 'vertical',
    left: 'left'
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: '50%',
      data: [
        { value: 1048, name: 'Search Engine' },
        { value: 735, name: 'Direct' },
        { value: 580, name: 'Email' },
        { value: 484, name: 'Union Ads' },
        { value: 300, name: 'Video Ads' }
      ],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
};
onMounted(()=>{
    var chartDom = document.getElementById('hotMajor');
var myChart = echarts.init(chartDom);
option && myChart.setOption(option);
})


</script>

<style scoped>

</style>