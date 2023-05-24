<template>
    <!-- https://static.kaoyan.cn/json/config/schedule.json -->
    <div class="calender">
        <p><span>考研日程</span> <i>日程早掌握，计划没烦恼</i></p>
        <div class="tab">
            <div class="tab-left">
                <div :class="tabChoose=='考试报名'?'calenderActive':''" @click="currentCalender($event)">考试报名</div>
                <div :class="tabChoose=='初试时间'?'calenderActive':''" @click="currentCalender($event)">初试时间</div>
                <div :class="tabChoose=='成绩查询'?'calenderActive':''" @click="currentCalender($event)">成绩查询</div>
                <div :class="tabChoose=='复试阶段'?'calenderActive':''" @click="currentCalender($event)">复试阶段</div>
            </div>
            <div class="tab-right">
                <div :class="tabChoose=='考试报名'?'calenderDisplay':''" class="tab-1">
                    <div class="tab-1-list" v-for="(i,k) of kaoshibaoming">
                        <span>{{ k+1 }}</span><span>{{ i.title }}</span><span>{{ i.date }}</span><a href=i.url>点我查看详情>></a>
                    </div>
                </div>
                <div class="tab-2" :class="tabChoose=='初试时间'?'calenderDisplay':''">
                    <div class="tab-2-example">
                        <span>预计日期</span>
                        <span>预计时间</span>
                        <span>考试科目</span>
                    </div>
                    <div class="tab-2-list" v-for="(i,k) of chushishijian">
                        <span>{{ i.date }}</span>
                        <span>{{ i.time }}</span>
                        <span>{{ i.subject }}</span>
                    </div>
                </div>
                <div class="tab-3" :class="tabChoose=='成绩查询'?'calenderDisplay':''">
                    <div class="tab-3-list" v-for="(i,k) of guojiaxianchaxun">
                        <span>{{ k+1 }}</span><span>{{ i.title }}</span><span>{{ i.date }}</span><a href=i.url>点我查看详情>></a>
                    </div>
                </div>
                <div class="tab-4" :class="tabChoose=='复试阶段'?'calenderDisplay':''">
                    <div class="tab-4-list" v-for="(i,k) in fushijieduan">
                        <span>{{ k+1 }}</span><span>{{ i.title }}</span><span>{{ i.date }}</span><a href=i.url>点我查看详情>></a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="country">
        <p><span>国家线</span></p>
        <div class="yearVersion">
            <span :class="current_year == 2021 ? 'active' : ''" @click="chooseYear($event)">2021</span>
            <span :class="current_year == 2022 ? 'active' : ''" @click="chooseYear($event)">2022</span>
            <span :class="current_year == 2023 ? 'active' : ''" @click="chooseYear($event)">2023</span>

        </div>

        <div class="line">
            <el-table :data="newCountryLine.item" border style="width: 100%">
                <el-table-column prop="school_year" label="年级" width="180" />
                <el-table-column prop="major_name" label="专业名称" width="180" />
                <el-table-column prop="code" label="专业代码" width="180" />
                <el-table-column prop="area_type" label="考生类型" width="180" />
                <el-table-column prop="total" label="总分" width="180" />
                <el-table-column prop="single_100" label="单科分（满分=100）" width="180" />
                <el-table-column prop="total" label="单科分（满分>100）" />
            </el-table>
        </div>

        <el-pagination style="width: 1200px;margin:40px 500px" v-model:current-page="currentPage" background
            layout="prev, pager, next" :total="maxPage" :page-size="pageSize" @current-change="handleCurrentChange" />
    </div>
</template>

<script setup>
import { ref, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"
import chooseMajor from "@/components/chooseMajor.vue";
import requestFn from "@/api/requestFn.js";
const countryLine = reactive({ item: [] })
const newCountryLine = reactive({ item: [] })
const newArray = reactive({ item: [] })
const current_year = ref(2023)
const tabPosition = ref('left')


onMounted(() => {
    requestFn({
        url: '/contryLine',
        method: 'post',
        data: {
            year: 2023
        }
    }).then(data => {
        countryLine.item = data.data
        maxPage.value = countryLine.item.length
        newCountryLine.item = data.data.slice((currentPage.value - 1) * pageSize.value, currentPage.value * pageSize.value)

    })
})


const handleCurrentChange = (val) => {
    newCountryLine.item = countryLine.item.slice((val - 1) * pageSize.value, val * pageSize.value)
}


const chooseYear = (e) => {
    current_year.value = e.target.innerText
    requestFn({
        url: '/contryLine',
        method: 'post',
        data: {
            year: e.target.innerText
        }
    }).then(data => {
        countryLine.item = data.data
        maxPage.value = countryLine.item.length
        newCountryLine.item = data.data.slice((currentPage.value - 1) * pageSize.value, currentPage.value * pageSize.value)
    })
}


const pageSize = ref(10)
const currentPage = ref(1)
const maxPage = ref(0)

const tabChoose = ref('考试报名')
const currentCalender=(e)=>{
    console.log(e.target.innerText);
    tabChoose.value=e.target.innerText;
}


const kaoshibaoming=[{'title': '院校学科专场咨询会', 'date': '2023年5月-10月', 'url': 'https://m.kaoyan.cn/live'}, {'title': '预报名', 'date': '预计2023年9月24日-9月27日', 'url': 'https://kaoyan.eol.cn/e_ky/zt/app/2020kybm/index.html'}, {'title': '正式报名', 'date': '预计2023年10月5日-10月25日', 'url': 'https://kaoyan.eol.cn/e_ky/zt/app/2020kybm/index.html'}, {'title': '报名确认', 'date': '预计2023年10月28日-11月5日', 'url': 'https://kaoyan.eol.cn/e_ky/zt/app/2020kyqr/index.html'}, {'title': '准考证下载', 'date': '预计2023年12月14日-12月26日', 'url': 'https://www.kaoyan.cn/article/211588'}]
const chushishijian=[{'subject': '思想政治理论/管理类综合能力', 'date': '2023.12.23', 'time': '08:30-11:30'}, {'subject': '外国语', 'date': '2023.12.23', 'time': '14:00-17:00'}, {'subject': '业务课一', 'date': '2023.12.24', 'time': '08:30-11:30'}, {'subject': '业务课二', 'date': '2023.12.24', 'time': '14:00-17:00'}, {'subject': '超过三小时或有特殊要求的科目', 'date': '2023.12.25', 'time': '--'}]
const guojiaxianchaxun=[{'title': '国家线查询', 'date': '2023年3月', 'url': 'https://kaoyan.eol.cn/e_ky/zt/app/2020cjcx/index.html'}, {'title': '调剂查询', 'date': '2023年3月31日', 'url': 'https://yz.chsi.com.cn/yztj/'}]
const fushijieduan=[{'title': '复试录取通知', 'date': '2023年4月30日以后', 'url': 'https://yz.chsi.com.cn/kyzx/kp/202103/20210319/1773474721.html'}]
</script>

<style scoped lang="less">
.calenderActive{
    color: #fff;
    background-color: #ff6602;
}
.calenderDisplay{
    display:block !important;
}
.country {
    .active {
        border: 1px solid orange;
        color: orange;
    }

    p {
        width: 1200px;
        margin: 0px auto;
        border-left: 5px solid orange;

        span {
            font-size: 20px;
            font-weight: bold;
            margin-left: 5px;
        }
    }

    .line {
        width: 1200px;
        margin: 0px auto;
    }

    .yearVersion {
        width: 1200px;
        display: flex;
        margin: 10px auto;

        span {
            width: 50px;
            height: 30px;
            text-align: center;
            margin-right: 20px;
            font-size: 16px;
            line-height: 32px;
            // border: 1px solid red;
        }
    }
}

.calender {
    width: 1200px;
    margin: 0px auto;


    p {
        width: 1200px;
        margin: 0px auto;
        border-left: 5px solid orange;
        text-align: left;
        padding-left: 10px;
    }

    span {
        font-size: 20px;
        font-weight: bold;
        color: #000;
        margin-right: 30px;
    }

    i {
        font-style: normal;
        font-size: 14px;
        color: rgba(0, 0, 0, .64);
    }

    .tab {
        margin: 30px 0px;
        display: flex;
        box-shadow: 1px 1px 1px 1px #eee,1px 1px 1px 1px #eee,1px 1px 1px 1px #eee,1px 1px 1px 1px #eee,;
        .tab-left {
            background-color: #f8f8f8;

            div {
                font-size: 16px;
                // color:#fff;
                text-align: center;
                width: 150px;
                height: 50px;
                line-height: 50px;
                &:hover{
                    background-color: #ff6602;
                    color:#fff;

                }
            }
        }

        .tab-right {
            background-color:#fff;
            width: 1050px;
            box-shadow: #ff6602;

            .tab-1 {
                display: none;
                .tab-1-list {
                    margin-left: 20px;

                    display: flex;
                    align-items: center;
                    padding: 10px;
                    a{
                        color: #ff6602;
                    }
                    span {
                        &:nth-of-type(1) {
                            font-style: normal;
                            display: inline-block;
                            width: 20px;
                            height: 20px;
                            background: #f5f6f7;
                            text-align: center;
                            line-height: 20px;
                            border-radius: 50%;
                            margin-right: 20px;
                            font-size: 13px;
                            font-weight: 700;
                            color: #999;
                        }

                        &:nth-of-type(2) {
                            width: 184px;
                            font-size: 13px;
                            font-weight: 500;
                            color: #333;
                        }

                        &:nth-of-type(3) {
                            width: 232px;
                            font-size: 13px;
                            font-weight: 400;
                            color: #999;
                        }
                    }
                }
            }

            .tab-2 {

                display: none;
                .tab-2-example{
                    float: left;
                    display: flex;
                    flex-direction: column;
                    // background-color: red;
                    width:120px;

                    span{
                        &:nth-of-type(3){
                            padding:32px 0px;
                        }
                        display: block;
                        width: 100%;
                        height: 44px;
                        background: #fafafa;
                        text-align: center;
                        line-height: 44px;
                        font-size: 13px;
                        font-weight: 500;
                        color: #666;
                        border-bottom: 1px solid #eee;
                        border-right: 1px solid #eee;
                        border-left: 1px solid #eee;
                    }
                }
                .tab-2-list {
                    float: left;
                    display: flex;
                    flex-direction: column;
                    background-color: red;
                    width:186px;
                    span {
                        &:nth-of-type(3){
                            padding:32px 0px;
                        }
                        display: block;
                        width: 100%;
                        height: 44px;
                        background: #fafafa;
                        text-align: center;
                        line-height: 44px;
                        font-size: 13px;
                        font-weight: 500;
                        color: #666;
                        border-bottom: 1px solid #eee;
                        border-right: 1px solid #eee;
                        border-left: 1px solid #eee;
                    }
                }
            }
            .tab-3{
                display: none;
                .tab-3-list {
                    display: flex;
                    align-items: center;
                    padding: 10px;
                    a{
                        color: #ff6602;
                    }
                    span {
                        &:nth-of-type(1) {
                            margin-left: 20px;
                            font-style: normal;
                            display: inline-block;
                            width: 20px;
                            height: 20px;
                            background: #f5f6f7;
                            text-align: center;
                            line-height: 20px;
                            border-radius: 50%;
                            margin-right: 20px;
                            font-size: 13px;
                            font-weight: 700;
                            color: #999;
                        }

                        &:nth-of-type(2) {
                            width: 184px;
                            font-size: 13px;
                            font-weight: 500;
                            color: #333;
                        }

                        &:nth-of-type(3) {
                            width: 232px;
                            font-size: 13px;
                            font-weight: 400;
                            color: #999;
                        }
                    }
                }
            }
            .tab-4{
                display: none;
                .tab-4-list {
                    display: flex;
                    align-items: center;
                    padding: 10px;
                    a{
                        color: #ff6602;
                    }
                    span {
                        &:nth-of-type(1) {
                            margin-left: 20px;

                            font-style: normal;
                            display: inline-block;
                            width: 20px;
                            height: 20px;
                            background: #f5f6f7;
                            text-align: center;
                            line-height: 20px;
                            border-radius: 50%;
                            margin-right: 20px;
                            font-size: 13px;
                            font-weight: 700;
                            color: #999;
                        }

                        &:nth-of-type(2) {
                            width: 184px;
                            font-size: 13px;
                            font-weight: 500;
                            color: #333;
                        }

                        &:nth-of-type(3) {
                            width: 232px;
                            font-size: 13px;
                            font-weight: 400;
                            color: #999;
                        }
                    }
                }
            }
        }
    }
}</style>