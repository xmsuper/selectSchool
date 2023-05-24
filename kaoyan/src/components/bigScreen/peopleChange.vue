<template>
    <div id="main" style="width: 370px;height: 300px;"></div>
</template>

<script setup>
import { ref, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"
import * as echarts from 'echarts'
onMounted(() => {
    initeCharts()
})


const state = reactive({
    option: {
        tooltip:{
            show:true,

        },
        lineStyle: {
            color: '#00FF00'
        },
        itemStyle: {
            normal: {
                color: '#00FF00'
            }
        },
        title: {
            show: true,
            text: '近4年考研人数',
            textAlign: '',
            textStyle: {
                color: '#fff',
                fontSize: 16
            },
        },
        legend: {
            data: ['报名人数'],
            textStyle: {
                color: '#fff',
                fontSize: 12,
                padding: 2,
            },
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            data: ['2017', '2018', '2019', '2020', '2021', '2022', '2023'],
            nameTextStyle: {
                color: "#fff"
            },
            axisLabel: {
                textStyle: {
                    color: '#fff'
                },
                fontSize: 14
            },
            axisLine: {
                lineStyle: {
                    color: "rgba(255, 255, 255, 1)"
                }
            }
        },
        yAxis: {
            type: 'value',
            name: '（单位）万',
            nameTextStyle: {
                color: '#fff',
                backgroundColor: '',
            },
            axisLabel: {
                textStyle: {
                    color: '#fff'
                },
                fontSize: 14
            },
            axisLine: {
                lineStyle: {
                    color: "rgba(255, 255, 255, 1)"
                }
            }
        },
        series: [
            {
                data: [201, 238, 290, 341, 377, 457, 480],
                type: 'line',
                smooth: true,
                name: '报名人数',
            },

        ]
    }
})
const initeCharts = () => {
    let myChart = echarts.init(document.getElementById('main'))
    // 绘制图表
    myChart.setOption(state.option)
}



</script>

<style scoped></style>