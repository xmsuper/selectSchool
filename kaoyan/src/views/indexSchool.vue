<template>
    <!-- 所有院校展示页面 -->
    <div>
        <!-- 单个院校展示--后期for循环 -->
        <div>
            <!-- 左侧--开始 -->
            <div class="schoolListItem">
                <el-row>
                    <el-col :span="2">
                        <div style="width: 60px;height: 60px;background-color: red;" />
                    </el-col>
                    <el-col :span="14">
                        <div>
                            <div class="school_list_item_content">
                                <span>青岛大学</span>
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
                                    山东
                                </span>
                            </div>
                            <el-breadcrumb separator="|">
                                <el-breadcrumb-item>高等院校</el-breadcrumb-item>
                                <el-breadcrumb-item>综合类</el-breadcrumb-item>
                                <el-breadcrumb-item>A区</el-breadcrumb-item>
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


            </div>
            <!-- 左侧--结束 -->


        </div>
    </div>
</template>

<script>
import { ref,onMounted } from "vue"
import requestFn from '@/api/requestFn.js'
import { on } from "events"
export default {
    name: 'home',
    components: {},
    setup() {
        onMounted(()=>{
            requestFn({
                url:'/allschool',
                method:'get',
            }).then(_d=>{
                console.log(_d.data)
            }).catch(error=>{
                //异常发生时会自动调用这里的代码，同时第一个参数表示异常对象
                // error.response获取来自服务端的异常信息，如果服务端没有异常，则response的值为undefined
                
            })
        })
        return {

        }
    }
}
</script>

<style scoped>
.schoolListItem {
    border: 1px solid #eee;
}

.school_list_item_content {
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
}</style>