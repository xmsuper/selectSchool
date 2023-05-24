<template>
    <div id="chinaMap" style="width: 800px;height: 500px;"></div>
</template>
  
<script>
import * as echarts from 'echarts';
import china from '@/assets/map/china.js'
import requestFn from '@/api/requestFn.js';
export default {
    name: '',
    components: {},
    props: {},
    data() {
        return {
            school_list:[]
        };
    },
    methods: {
        init() {
            function randomData() {
                return Math.round(Math.random() * 500);
            }

            var mydata = this.school_list

            var option = {
                backgroundColor: '',
                title: { text: '院校分布图',  x: 'center',textStyle:{color:'#fff'}},
                tooltip: { trigger: 'item' },
                grid: {
                    left: 0,
                    right: 0,
                    top: 0,
                    bottom: 0,
                },
                visualMap: {
                    show: false,
                    x: 'left',
                    y: 'bottom',
                    splitList: [
                        { start: 50, end: 1000 },
                        { start: 30, end: 50 },
                        { start: 20, end: 30 },
                        { start: 10, end: 20 },
                        { start: 3, end: 10},
                        { start: 0, end: 3 },
                    ],
                    color: ['red', '#00FF00', '#66FF33', '#339900', '#33CC00', '#00CC00'],
                },
                series: [
                    {
                        name: '随机数据',
                        type: 'map',
                        map: 'china',
                        roam: true,
                        label: { show: false },
                        emphasis: { label: { show: false } },
                        data: this.school_list,
                    },
                ],
            };
            var chart = echarts.init(document.getElementById('chinaMap'));
            chart.setOption(option);
        },
    },
    mounted() {
        requestFn({
            url:'/everyProvinceNum',
            method:'get',
        }).then(data=>{
            this.school_list=data.data
        this.init();

        })
    },
};
</script>
  
<style scoped lang="less"></style>
  