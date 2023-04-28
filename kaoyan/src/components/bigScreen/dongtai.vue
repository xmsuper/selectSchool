<template>
    <div id="countryLine" style="width: 400px;height: 300px;">

    </div>
</template>

<script setup>
import { ref, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"
import * as echarts from 'echarts';
import requestFn from "@/api/requestFn";


const total_zhexue=reactive({item:[]})
const total_jinrong=reactive({item:[]})
const total_dianzixinxi=reactive({item:[]})
const total_lixue=reactive({item:[]})
const total_lishixue=reactive({item:[]})
const total_1=[0,5,10]
onMounted(() => {
    requestFn({
        url:'/countryLineBigScreen',
        method:'get'
    }).then(data=>{
        data.data.forEach((item,index)=>{
            if([0,5,10].includes(index)){
                total_zhexue.item.push(item)
            }
            if([1,6,11].includes(index)){
                total_jinrong.item.push(item)
            }
            if([2,7,12].includes(index)){
                total_dianzixinxi.item.push(item)
            }
            if([3,8,13].includes(index)){
                total_lixue.item.push(item)
            }
            if([4,9,14].includes(index)){
                total_lishixue.item.push(item)
            }

        })

        const option = {
            grid:{top:'20%'},
        title: {
            text: '近3年国家线变化趋势',
            textStyle:{
                color:'#fff',
            }
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: ['哲学', '金融', '电子信息', '理学', '历史学'],
            top:'8%',
            textStyle: {
                    color: '#fff'
                }
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['2021', '2022', '2023'],
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
        },
        yAxis: {
            type: 'value',
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
        },
        series: [
            {
                name: '哲学',
                type: 'line',
                // stack: 'Total',
                data:total_zhexue.item
            },
            {
                name: '金融',
                type: 'line',
                // stack: 'Total',
                data: total_jinrong.item
            },
            {
                name: '电子信息',
                type: 'line',
                // stack: 'Total',
                data: total_dianzixinxi.item
            },
            {
                name: '理学',
                type: 'line',
                // stack: 'Total',
                data: total_lixue.item
            },
            {
                name: '历史学',
                type: 'line',
                // stack: 'Total',
                data: total_lishixue.item
            }
        ]
    };
    var chartDom = document.getElementById('countryLine');
var myChart = echarts.init(chartDom);
option && myChart.setOption(option);


    })




})


</script>

<style scoped></style>