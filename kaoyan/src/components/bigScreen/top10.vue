<template>
    <div id="top10" style="width: 370px;height: 300px;">

    </div>
</template>

<script setup>
import { ref, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"

import * as echarts from 'echarts';
import requestFn from '@/api/requestFn'
const newArray = []

var option;
const data = [];
for (let i = 0; i < 11; ++i) {
    data.push(Math.round(Math.random() * 1));
}
option = {
    grid:{
            left:'30%'
        },
    color: ["#003366", "#006699", "#4cabce", "#e5323e"],
    title: {
        show: true,
        text: '热搜TOP10',
        textAlign: '',
        textStyle: {
            color: '#fff',
            fontSize: 16
        },
    },
    legend:{
        
    },
    xAxis: {
        max: 'dataMax',
        nameTextStyle: {
            color: '#fff',
            backgroundColor: '',
            // padding:10
            width: 100
        },
        axisLabel: {
            textStyle: {
                color: '#fff'
            },
            fontSize: 14
        },
    },
    yAxis: {
        // align:'right',

        type: 'category',
        data: newArray,
        inverse: true,
        animationDuration: 300,
        animationDurationUpdate: 300,
        max: 10, // only the largest 3 bars will be displayed
        nameTextStyle: {
            color: '#fff',
            backgroundColor: '',
            // padding:10
            width: 100
        },
        axisLabel: {
            textStyle: {
                color: '#fff'
            },
            fontSize: 10
        },
        axisLine: {
            lineStyle: {
                color: "rgba(255, 255, 255, 1)"
            }
        }
    },
    series: [
        {
            realtimeSort: true,
            name: '搜索指数',
            type: 'bar',
            data: data,
            label: {
                show: true,
                position: 'right',
                valueAnimation: true,
                color: '#fff'
            },
            itemStyle: {
                normal: {
                    //这里是颜色
                    color: function (params) {
                        //注意，如果颜色太少的话，后面颜色不会自动循环，最好多定义几个颜色
                        var colorList = ['#00A3E0', '#FFA100', '#ffc0cb', '#CCCCCC', '#BBFFAA', '#749f83', '#ca8622', '#eee', 'red', 'blue'];
                        return colorList[params.dataIndex]
                    }
                }
            }
        }
    ],
    legend: {
        show:false,
        itemStyle: {
            color: 'red',
        },
        textStyle: {
            color: '#fff',
            fontSize: 12,
            padding: 2,
        },
    },
    animationDuration: 0,
    animationDurationUpdate: 3000,
    animationEasing: 'linear',
    animationEasingUpdate: 'linear'
};



const initeCharts = () => {
    let myChart = echarts.init(document.getElementById('top10'))
    setTimeout(function () {
        run();
    }, 0);
    setInterval(function () {
        run();
    }, 3000);
    function run() {
        for (var i = 0; i < data.length; ++i) {
            if (Math.random() > 0.9) {
                data[i] += Math.round(Math.random() * 2000);
            } else {
                data[i] += Math.round(Math.random() * 200);
            }
        }
        myChart.setOption({
            series: [
                {
                    type: 'bar',
                    data
                }
            ]
        });
    }
    // 绘制图表
    myChart.setOption(option)
}


onMounted(() => {
    requestFn({
        url: '/hotSchool',
        method: 'get'
    }).then(data => {
        // console.log(data.data)
        data.data.forEach(item => {
            newArray.push(item.school_name.school_name)
        });
        initeCharts()

    })
})




</script>

<style scoped></style>