<template>
    <!-- 所有院校展示页面 -->
    <div>
            <div class="schoolListItem">
                <el-row v-for="n in schoolInfoSlice.arr">
                    <el-col :span="2">
                        <div>
                            <img style="width: 60px;height: 60px;" :src="n.school_name.school_img">
                        </div>
                    </el-col>
                    <el-col :span="14">
                        <div>
                            <div class="school_list_item_content">
                                <span>{{ n.school_name.school_name }}</span>
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
                                    {{ n.province_name }}
                                </span>
                            </div>
                            <el-breadcrumb separator="|">
                                <el-breadcrumb-item>{{ n.type_school_name }}</el-breadcrumb-item>
                                <el-breadcrumb-item>{{ n.type_name }}</el-breadcrumb-item>
                                <el-breadcrumb-item>{{ n.province_area }}</el-breadcrumb-item>
                            </el-breadcrumb>
                        </div>
                    </el-col>
                    <el-col :span="8">
                        <!-- 右侧=开始 -->
                        <div class="schoolListBtn">
                            <el-button type="warning">简章</el-button>
                            <el-button type="warning">分数线</el-button>
                            <el-button type="warning">问招办</el-button>
                        </div>
                        <!-- 右侧--结束 -->
                    </el-col>
                </el-row>

                <el-pagination v-model:current-page="curretPage" :disabled="disabled" :background="background"
                    layout="prev, pager, next, jumper" :total="maxPage" @current-change="handleCurrentChange" />

            </div>
    </div>
</template>

<script>
import { ref, onMounted, reactive, watch } from "vue"
import requestFn from '@/api/requestFn.js'
import { on } from "events"
import { slice } from "lodash"
export default {
    name: 'home',
    components: {},
    setup() {
        const background = ref(false)
        const disabled = ref(false)
        // 每页显示个数
        let pageSize = ref(10)
        // 当前页,初始当前页等于1
        let curretPage = ref(1)
        // 最大条数
        let maxPage = ref(0)
        let schoolInfo = reactive({ arr: [] })
        let schoolInfoSlice = reactive({ arr: [] })
        onMounted(() => {
            requestFn({
                url: '/allSchool',
                method: 'get',
            }).then(_d => {

                schoolInfo.arr = _d.data
                // console.log(schoolInfo.arr)
                maxPage.value = parseInt(_d.data.length)
                schoolInfoSlice.arr = schoolInfo.arr.slice((curretPage.value - 1) * pageSize.value, curretPage.value * pageSize.value)
            }).catch(error => {
                //异常发生时会自动调用这里的代码，同时第一个参数表示异常对象
                // error.response获取来自服务端的异常信息，如果服务端没有异常，则response的值为undefined
                console.log(error)
            })
        })
        // 每页条数
        // const handleSizeChange = (val) => {
        //     console.log(val)
        // }
        // 当前页数
        const handleCurrentChange = (val) => {
            // slice((当前页-1)*每页条数,当前页*每页条数)
            schoolInfoSlice.arr = schoolInfo.arr.slice((val - 1) * pageSize.value, val * pageSize.value)
        }

        return {
            maxPage, schoolInfo, curretPage, pageSize, handleCurrentChange,
            background, disabled, schoolInfoSlice
        }
    }
}
</script>

<style scoped>
.el-row {
    margin-bottom: 50px;
    border: 1px solid #eee;
    border-radius: 15px;
    padding:10px 10px


}

.schoolListItem {
    /* border: 1px solid #eee; */
    margin-left: 80px;
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
}

.school_list_item_content span:nth-of-type(2) {
    font-size: 14px;
    color: #888888;
}

.school_list_item_label span {
    float: left;
    margin-right: 10px;
}

.schoolListBtn {
    padding-top: 15px;
}

.el-pagination{
    width: 50%;
    margin: 0 auto;
}
</style>