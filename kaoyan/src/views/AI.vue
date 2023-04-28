<template>
    <div class="container">
        <el-form :model="form">
            <div class="import">
                <div class="chooseMajor">请选择你要考的专业</div>
                <chooseMajor @getChildData="getChildVal"></chooseMajor>
            </div>

            <div class="chooseRegin">
                <div>请选择你想去的地区</div>
                <ul class="allRegin">
                    <li v-for="(i, k) of allRegin.arr" :class="provinceActive == k + 1 ? 'active' : ''"
                        @click="yourRegin(i[0], k)">
                        {{ i[0] }}</li>
                </ul>
            </div>
            <div class="score">
                <div class="score-title">请输入你的预估分数？</div>
                <div>
                    <el-input v-model="form.score" :rows="2" type="textarea" placeholder="请输入你的分数" />
                </div>
            </div>
            <el-button class="subbtn" @click="onsubmit">获取结果</el-button>
        </el-form>
    </div>
    <div class="search">
        <hotSearch></hotSearch>
    </div>

    <div class="recommend_result" style="width: 1400px;margin: 0px auto;">
        <p v-if="isShow" style="font-size: 20px;border-left:5px solid #f60;padding-left: 10px;">保底院校</p>
        <div v-for="i of recommend_school.item.slice(0,3)"
            style="margin: 10px auto;border:1px solid orange;padding: 20px;border-radius: 15px;">
            <el-row>
                <el-col :span="2">
                    <div>
                        <img style="width: 60px;height: 60px;" :src=i[25]>
                    </div>
                </el-col>
                <el-col :span="8" >
                    <div>
                        <div class="school_list_item_content">
                            <span>{{ i[9] }}</span>
                            <span>
                                <svg t="1678540025337" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                    xmlns="http://www.w3.org/2000/svg" p-id="2949" width="16" height="16">
                                    <path
                                        d="M512 11.65312c-225.3824 0-408.75008 183.35744-408.75008 408.75008 0 167.56736 97.51552 316.30336 179.32288 411.57632C366.53056 929.7408 471.6032 1012.34688 512 1012.34688c39.41376 0 144.51712-84.96128 229.5296-185.53856 155.94496-184.48384 179.22048-333.81376 179.22048-406.41536 0-225.3824-183.35744-408.73984-408.75008-408.73984z m-0.04096 959.71328c-42.47552-4.5568-367.73888-263.0656-367.73888-550.97344C144.20992 217.6 309.20704 52.61312 512 52.61312c202.8032 0 367.79008 164.98688 367.79008 367.79008 0 277.27872-326.53312 545.76128-367.83104 550.9632z"
                                        fill="" p-id="2950"></path>
                                    <path
                                        d="M512.69632 212.77696c-114.4832 0-207.616 93.14304-207.616 207.616 0 114.4832 93.14304 207.62624 207.616 207.62624s207.616-93.14304 207.616-207.62624c0.01024-114.47296-93.1328-207.616-207.616-207.616z m0 374.28224c-91.89376 0-166.656-74.76224-166.656-166.66624 0-91.89376 74.76224-166.656 166.656-166.656 91.904 0 166.656 74.76224 166.656 166.656 0.01024 91.904-74.752 166.66624-166.656 166.66624z"
                                        fill="" p-id="2951"></path>
                                </svg>
                                {{i[11]  }}
                                  排名：{{ i[21] }}
                            </span>
                        </div>
                        <el-breadcrumb separator="|">
                            <el-breadcrumb-item v-if="i[12]==1">985</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i[13] }}</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i[14] }}</el-breadcrumb-item>
                        </el-breadcrumb>
                    </div>
                </el-col>
                <el-col :span="14" style="display: flex;align-items: center;justify-content: space-between;">
                    <!-- 右侧=开始 -->
                    <div style="display: flex;text-align: left;justify-content:space-around;" class="school_score">
                        <p>{{ i[2] }}</p>
                        <p>总分：{{ i[3] }}</p>
                        <p>政治：{{ i[4] }} </p>
                        <p>英语：{{ i[5] }}</p>
                        <p>业务课1:{{ i[6] }}</p>
                        <p>业务课2:{{ i[7] }}</p>
                    </div>

                    <p><el-button color="#f60" style="color:#fff" @click="gotoDetail(i[24])">查看详情</el-button></p>
                    <!-- 右侧--结束 -->
                </el-col>
            </el-row>
        </div>
    </div>

    <div class="recommend_result" style="width: 1400px;margin: 0px auto;">
        <p  v-if="isShow" style="font-size: 20px;border-left:5px solid #f60;padding-left: 10px;">稳健院校</p>
        <div v-for="i of recommend_school.item.slice(3,8)"
            style="margin: 10px auto;border:1px solid orange;padding: 20px;border-radius: 15px;">
            <el-row>
                <el-col :span="2">
                    <div>
                        <img style="width: 60px;height: 60px;" :src=i[25]>
                    </div>
                </el-col>
                <el-col :span="8" >
                    <div>
                        <div class="school_list_item_content">
                            <span>{{ i[9] }}</span>
                            <span>
                                <svg t="1678540025337" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                    xmlns="http://www.w3.org/2000/svg" p-id="2949" width="16" height="16">
                                    <path
                                        d="M512 11.65312c-225.3824 0-408.75008 183.35744-408.75008 408.75008 0 167.56736 97.51552 316.30336 179.32288 411.57632C366.53056 929.7408 471.6032 1012.34688 512 1012.34688c39.41376 0 144.51712-84.96128 229.5296-185.53856 155.94496-184.48384 179.22048-333.81376 179.22048-406.41536 0-225.3824-183.35744-408.73984-408.75008-408.73984z m-0.04096 959.71328c-42.47552-4.5568-367.73888-263.0656-367.73888-550.97344C144.20992 217.6 309.20704 52.61312 512 52.61312c202.8032 0 367.79008 164.98688 367.79008 367.79008 0 277.27872-326.53312 545.76128-367.83104 550.9632z"
                                        fill="" p-id="2950"></path>
                                    <path
                                        d="M512.69632 212.77696c-114.4832 0-207.616 93.14304-207.616 207.616 0 114.4832 93.14304 207.62624 207.616 207.62624s207.616-93.14304 207.616-207.62624c0.01024-114.47296-93.1328-207.616-207.616-207.616z m0 374.28224c-91.89376 0-166.656-74.76224-166.656-166.66624 0-91.89376 74.76224-166.656 166.656-166.656 91.904 0 166.656 74.76224 166.656 166.656 0.01024 91.904-74.752 166.66624-166.656 166.66624z"
                                        fill="" p-id="2951"></path>
                                </svg>
                                {{i[11]  }}
                                  排名：{{ i[21] }}
                            </span>
                        </div>
                        <el-breadcrumb separator="|">
                            <el-breadcrumb-item v-if="i[12]==1">985</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i[13] }}</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i[14] }}</el-breadcrumb-item>
                        </el-breadcrumb>
                    </div>
                </el-col>
                <el-col :span="14" style="display: flex;align-items: center;justify-content: space-between;">
                    <!-- 右侧=开始 -->
                    <div style="display: flex;text-align: left;justify-content:space-around;" class="school_score">
                        <p>{{ i[2] }}</p>
                        <p>总分：{{ i[3] }}</p>
                        <p>政治：{{ i[4] }} </p>
                        <p>英语：{{ i[5] }}</p>
                        <p>业务课1:{{ i[6] }}</p>
                        <p>业务课2:{{ i[7] }}</p>
                    </div>

                    <p><el-button color="#f60" style="color:#fff" @click="gotoDetail(i[24])">查看详情</el-button></p>
                    <!-- 右侧--结束 -->
                </el-col>
            </el-row>
        </div>
    </div>

    <div class="recommend_result" style="width: 1400px;margin: 0px auto;">
        <p  v-if="isShow" style="font-size: 20px;border-left:5px solid #f60;padding-left: 10px;">冲刺院校</p>
        <div v-for="i of recommend_school.item.slice(8,recommend_school.item.length)"
            style="margin: 10px auto;border:1px solid orange;padding: 20px;border-radius: 15px;">
            <el-row>
                <el-col :span="2">
                    <div>
                        <img style="width: 60px;height: 60px;" :src=i[25]>
                    </div>
                </el-col>
                <el-col :span="8" >
                    <div>
                        <div class="school_list_item_content">
                            <span>{{ i[9] }}</span>
                            <span>
                                <svg t="1678540025337" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                    xmlns="http://www.w3.org/2000/svg" p-id="2949" width="16" height="16">
                                    <path
                                        d="M512 11.65312c-225.3824 0-408.75008 183.35744-408.75008 408.75008 0 167.56736 97.51552 316.30336 179.32288 411.57632C366.53056 929.7408 471.6032 1012.34688 512 1012.34688c39.41376 0 144.51712-84.96128 229.5296-185.53856 155.94496-184.48384 179.22048-333.81376 179.22048-406.41536 0-225.3824-183.35744-408.73984-408.75008-408.73984z m-0.04096 959.71328c-42.47552-4.5568-367.73888-263.0656-367.73888-550.97344C144.20992 217.6 309.20704 52.61312 512 52.61312c202.8032 0 367.79008 164.98688 367.79008 367.79008 0 277.27872-326.53312 545.76128-367.83104 550.9632z"
                                        fill="" p-id="2950"></path>
                                    <path
                                        d="M512.69632 212.77696c-114.4832 0-207.616 93.14304-207.616 207.616 0 114.4832 93.14304 207.62624 207.616 207.62624s207.616-93.14304 207.616-207.62624c0.01024-114.47296-93.1328-207.616-207.616-207.616z m0 374.28224c-91.89376 0-166.656-74.76224-166.656-166.66624 0-91.89376 74.76224-166.656 166.656-166.656 91.904 0 166.656 74.76224 166.656 166.656 0.01024 91.904-74.752 166.66624-166.656 166.66624z"
                                        fill="" p-id="2951"></path>
                                </svg>
                                {{i[11]  }}
                                  排名：{{ i[21] }}
                            </span>
                        </div>
                        <el-breadcrumb separator="|">
                            <el-breadcrumb-item v-if="i[12]==1">985</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i[13] }}</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i[14] }}</el-breadcrumb-item>
                        </el-breadcrumb>
                    </div>
                </el-col>
                <el-col :span="14" style="display: flex;align-items: center;justify-content: space-between;">
                    <!-- 右侧=开始 -->
                    <div style="display: flex;text-align: left;justify-content:space-around;" class="school_score">
                        <p>{{ i[2] }}</p>
                        <p>总分：{{ i[3] }}</p>
                        <p>政治：{{ i[4] }} </p>
                        <p>英语：{{ i[5] }}</p>
                        <p>业务课1:{{ i[6] }}</p>
                        <p>业务课2:{{ i[7] }}</p>
                    </div>

                    <p><el-button color="#f60" style="color:#fff" @click="gotoDetail(i[24])">查看详情</el-button></p>
                    <!-- 右侧--结束 -->
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"
import chooseMajor from "@/components/chooseMajor.vue";
import hotSearch from "@/components/hotSearch.vue";
import requestFn from "@/api/requestFn";
import { useRouter, useRoute } from "vue-router";

const isShow=ref(false)
const router = useRouter()
const provinceActive = ref(null)
const form = reactive({
    score: '',
    province_name: '',
    school_info: {}

})
const inputInfo = reactive({
    region: '',
    class: '',
    major_class1: '',
    major_class2: '',
    score: ''
})
watch(form, () => {
    inputInfo.region = form.province_name,
        inputInfo.class = form.school_info.two_class,
        inputInfo.major_class1 = form.school_info.level1_name,
        inputInfo.major_class2 = form.school_info.level2_name,
        inputInfo.score = form.score
})

const gotoDetail = (e) => {
    router.push({
        // path:'/schoolDetail/'+e,
        name: 'schoolDetail',
        params: {
            school_id: e,
        }
    })
}


const recommend_school = reactive({ item: [] })
const onsubmit = () => {
    isShow.value=true
    const objvalue = Object.values(inputInfo)
    if (objvalue.filter(Boolean).length < 5) {
        alert('请选择并输入完整的信息')
    } else {
        requestFn({
            url: '/recommend',
            method: 'post',
            data: {
                region: inputInfo.region,
                class: inputInfo.class,
                major_class1: inputInfo.major_class1,
                major_class2: inputInfo.major_class2,
                score: inputInfo.score
            }
        }).then(res => {
            recommend_school.item = res.data
            console.log(recommend_school)
        })
    }


}
const allRegin = reactive({ arr: [] })
onMounted(() => {
    requestFn({
        url: '/regin',
        method: 'get'
    }).then(data => {
        allRegin.arr = (eval("(" + data.data + ")"))
    })
})

const yourRegin = (v, k) => {
    provinceActive.value = k + 1
    form.province_name = v
}
const getChildVal = (e) => {
    form.school_info = e
}
</script>

<style scoped lang="less">
.school_score p{
    margin-right: 10px;
}
.active {
    color: #ff6602
}

.subbtn {
    width: 160px;
    height: 38px;
    background: #ff6602;
    border-radius: 6px 6px 6px 6px;
    font-size: 14px;
    font-family: PingFang SC-Regular, PingFang SC !important;
    font-weight: 400;
    color: #fff;
    margin-top: 30px;
}

.chooseMajor {
    width: 1200px;
    /* margin: 20px auto; */
    width: 880px;
    height: 68px;
    background: #fff9f2;
    border-radius: 4px 4px 4px 4px;
    text-align: center;
    line-height: 68px;
    font-size: 20px;
    font-family: PingFang SC-Medium, PingFang SC !important;
    font-weight: 500;
    color: #f60;
    margin-bottom: 23px;
}

.chooseRegin {
    width: 900px;
    /* margin: 10px auto; */
}

.chooseRegin div {
    width: 1200px;
    margin: 20px auto;
    width: 880px;
    height: 68px;
    background: #fff9f2;
    border-radius: 4px 4px 4px 4px;
    text-align: center;
    line-height: 68px;
    font-size: 20px;
    font-family: PingFang SC-Medium, PingFang SC !important;
    font-weight: 500;
    color: #f60;
    margin-bottom: 23px;
}

.allRegin {
    height: 80px;
    width: 900px;
    /* margin: 20px auto; */
    font-size: 14px;
    /* background-color:red; */
    border: 1px solid #eee;
    border-radius: 15px;
    padding: 10px 10px;
}

.recommend_result{
    margin-bottom: 50px !important;
}
.allRegin li {
    cursor: pointer;
    margin-right: 20px;
    float: left;
    margin-top: 10px;
}

.allRegin li:hover {
    color: #f60;
}

.score {
    width: 900px;
    /* margin: 20px auto; */
}

.score-title {
    width: 1200px;
    margin: 20px auto;
    width: 880px;
    height: 68px;
    background: #fff9f2;
    border-radius: 4px 4px 4px 4px;
    text-align: center;
    line-height: 68px;
    font-size: 20px;
    font-family: PingFang SC-Medium, PingFang SC !important;
    font-weight: 500;
    color: #f60;
    margin-bottom: 23px;
}

.search {
    position: absolute;
    right: 100px;
    top: 250px;
    /* background-color: red; */
}

.import {
    /* background: black; */
    width: 900px;
}

.container {
    margin-left: 100px;
}


.loveSchool {
    overflow: hidden;

    h1 {
        margin: 30px;
    }

    .el-row {
        padding: 30px 50px;
    }
}

.schoolListItem {
    padding: 30px 100px;
    /* border: 1px solid #eee; */
    margin-left: 100px;
    position: relative;
}

.school_list_item_content {
    /* margin-left:-20px; */
    margin-bottom: 20px;
}

.school_list_item_content span:nth-of-type(1) {
    margin-right: 10px;
    font-size: 18px;
    font-weight: 700;
}</style>