<template>
    <div class="bigScreen">
        <div class="header" style="width: 100%;height: 100px;padding-top:20px;">
            <p style="width: 200px;margin: 0px auto;font-size: 20px;color: #82ddf1;">数据分析</p>
        </div>
        <div class="bottom">
            <div class="left">
                <div class="people">
                    <peopleChange></peopleChange>
                </div>

                <div class="top10">
                    <top10></top10>
                </div>

                <div class="schoolDestributed">
                    <schoolDistributed></schoolDistributed>
                </div>
            </div>
            <div class="middle">
                <div class="intro">
                    <div>
                        <p>1065</p>
                        <p>收录院校（单位：所）</p>
                    </div>
                    <div>
                        <p>39976</p>
                        <p>收录专业（单位：条）</p>
                    </div>
                    <div>
                        <p>5</p>
                        <p>用户数量（单位：个）</p>
                    </div>
                </div>

                <div class="chinaMap">
                    <chinaMap></chinaMap>
                </div>
            </div>
            <div class="right">
                <div class="hotMajor">
                    <hotMajor></hotMajor>

                </div>
                <div class="dongtai">
                    <dongtai></dongtai>

                </div>
                <div class="hotWord" style="width:360px;height: 300px;margin-top: 20px;">
                    <img style="width: 360px;height: 250px;" src="http://127.0.0.1:8000/media/wordcloud/wordcloud.png" alt="">
                </div>
            </div>
        </div>

    </div>
</template>

<script setup>
import { ref, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"
import peopleChange from "@/components/bigScreen/peopleChange.vue";
import chinaMap from '@/components/bigScreen/chinaMap.vue'
import top10 from "@/components/bigScreen/top10.vue";
import schoolDistributed from "@/components/bigScreen/schoolDistributed.vue";
import hotMajor from "@/components/bigScreen/hotMajor.vue";
import dongtai from "@/components/bigScreen/dongtai.vue";
import requestFn from "@/api/requestFn";

const img_url=ref('')
onMounted(()=>{
    requestFn({
        url:'/wordCloud',
        method:'get'
    }).then(res=>{
        img_url.value='http://127.0.0.1:8000/'+res.data.wordcloud
        console.log(img_url.value)
    })
})
</script>

<style scoped lang="less">
.bigScreen {

    position: relative;
    background-image: url(../../public/大屏背景.jpg);
    // width: 1200px;
    height: 1100px;
    margin: 20px auto;
    z-index: 0;

    .bottom {
        display: flex;
        justify-content: space-between;

        // align-items: center;
        .left {
            z-index: 10;
            padding: 20px;
            // background-color: red;

            .people {
                width: 370px;
                height: 300px;
                // border: 1px solid lightblue;
                // padding: 10px;
            }

            .top10 {
                // border: 1px solid lightblue;
            }


            .schoolDestributed {
                // border: 1px solid lightblue;

            }


        }

        .middle {
            // width: 370px;
            height: 300px;

            // background-color: aqua;
            .intro {
                // width: 30px;
                display: flex;
                font-size: 20px;
                color: #fff;
                // border: 1px solid lightblue;


                div {
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    margin:0 10px;
                    p{
                        &:nth-of-type(2){
                            font-size: 14px;
                        }
                    }
                }
            }

            .chinaMap {
                position: absolute;
                // width: 500px;
                top: 20%;
                left: 50%;
                margin-left: -400px;
                z-index: 1;

            }
        }

        .right {
            z-index: 10;
            width: 370px;
            height: 800px;
            // background-color: pink;
        }
    }



}</style>