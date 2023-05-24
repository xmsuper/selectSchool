<template>
    <div id="schoolDestributed" style="width: 370px;height: 300px;">

    </div>
</template>

<script setup>
import { ref, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"
import * as echarts from 'echarts';
import requestFn from "@/api/requestFn.js";

const school_percent = reactive({ item: [] })
const school_class = ['985', '211', '双一流', '科研院所', '高等院校']
var option;



onMounted(() => {

    requestFn({
        url: '/schooltypePercent',
        method: 'get'
    }).then(data => {
        data.data.forEach((item, index) => {
            school_percent.item.push({
                value: item, name: school_class[index]
            })
        });
        option = {
            title:{
                text:'院校分类',
                textStyle:{
                    color:'#fff'
                }
            },
            grid:{
                top:'50%'
            },
            tooltip: {
                top:'10%',
                trigger: 'item'
            },
            legend: {
                top: '20%',
                left: '',
                orient:'vertical',
                textStyle: {
                    color: '#fff'
                }
            },
            series: [
                {
                    name: 'Access From',
                    type: 'pie',
                    radius: ['40%', '70%'],
                    avoidLabelOverlap: false,
                    itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                    },
                    label: {
                        show: false,
                        position: 'center',
                    },
                    emphasis: {
                        label: {
                            show: true,
                            fontSize: 40,
                            fontWeight: 'bold'
                        }
                    },

                    labelLine: {
                        show: false
                    },
                    data: school_percent.item
                }
            ]
        };
        var chartDom = document.getElementById('schoolDestributed');
        var myChart = echarts.init(chartDom);
        option && myChart.setOption(option);

    })


})
</script>

<style scoped></style>