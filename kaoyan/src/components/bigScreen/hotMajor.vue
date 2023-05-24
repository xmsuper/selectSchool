<template>
    <div id='hotMajor' style="width: 360px;height: 300px;">

    </div>
</template>

<script setup>
import { ref,reactive,nextTick,computed,watch,onMounted,onUpdated} from "vue" 
import * as echarts from 'echarts';
var option;

option = {
  title: {
    text: '专业',
    subtext: 'Major Data',
    left: 'center',
       textStyle: {
                    color: '#fff'
                }
  },
  tooltip: {
    trigger: 'item'
  },
  legend: {
    orient: 'vertical',
    left: 'left',
       textStyle: {
                    color: '#fff'
                }
  },
  series: [
    {
      // name: 'Access From',
      type: 'pie',
      radius: '50%',
      
      data: [
        { value: 1048, name: '工科' },
        { value: 735, name: '理科' },
        { value: 580, name: '经济学' },
        { value: 484, name: '法学' },
        { value: 300, name: '军事学' }
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