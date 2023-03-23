<template>
    <div class="major">
        <div class="major_class">
            <el-row class="degree_class">
                <el-col :span="2">学位类别</el-col>
                <el-col :span="2"><svg t="1679539700485" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="2790" width="200" height="200">
                        <path
                            d="M660.2496 485.1456L385.1776 210.0992a18.048 18.048 0 0 0-25.5488 0c-7.0656 7.0656-7.0656 18.5088 0 25.5488L634.7008 510.72c0.3328 0.3328 0.3328 0.8448 0 1.1776l-276.48 276.4544a18.048 18.048 0 0 0 0 25.5488 17.98656 17.98656 0 0 0 12.7744 5.2992c4.6336 0 9.2416-1.7664 12.7744-5.2992L660.224 537.4464c14.4384-14.4128 14.4384-37.888 0.0256-52.3008z"
                            fill="#231815" p-id="2791"></path>
                    </svg></el-col>
                <el-col :span="1">全部</el-col>
                <el-col :span="19"><span @click="two_major(k.major_class, v)" v-for="(k, v) of twoClass.arr">{{ k.major_class
                }}</span></el-col>
            </el-row>
            <el-row class="spe_class">
                <el-col :span="2">门类</el-col>
                <el-col :span="2"><svg t="1679539700485" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="2790" width="200" height="200">
                        <path
                            d="M660.2496 485.1456L385.1776 210.0992a18.048 18.048 0 0 0-25.5488 0c-7.0656 7.0656-7.0656 18.5088 0 25.5488L634.7008 510.72c0.3328 0.3328 0.3328 0.8448 0 1.1776l-276.48 276.4544a18.048 18.048 0 0 0 0 25.5488 17.98656 17.98656 0 0 0 12.7744 5.2992c4.6336 0 9.2416-1.7664 12.7744-5.2992L660.224 537.4464c14.4384-14.4128 14.4384-37.888 0.0256-52.3008z"
                            fill="#231815" p-id="2791"></path>
                    </svg></el-col>
                <el-col :span="1">全部</el-col>
                <el-col :span="19">
                    <!-- 点击门类，显示专业具体名字 -->
                    <span @click="speBtn(k.level1_name, v)" v-for="(k, v) of level1_name.arr">{{ k.level1_name
                    }}</span>
                </el-col>
            </el-row>
            <el-row v-if="showClass" class="subject_class">
                <el-col :span="2">学科类别</el-col>
                <el-col :span="2"><svg t="1679539700485" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="2790" width="200" height="200">
                        <path
                            d="M660.2496 485.1456L385.1776 210.0992a18.048 18.048 0 0 0-25.5488 0c-7.0656 7.0656-7.0656 18.5088 0 25.5488L634.7008 510.72c0.3328 0.3328 0.3328 0.8448 0 1.1776l-276.48 276.4544a18.048 18.048 0 0 0 0 25.5488 17.98656 17.98656 0 0 0 12.7744 5.2992c4.6336 0 9.2416-1.7664 12.7744-5.2992L660.224 537.4464c14.4384-14.4128 14.4384-37.888 0.0256-52.3008z"
                            fill="#231815" p-id="2791"></path>
                    </svg></el-col>
                <el-col :span="1">全部</el-col>
                <el-col :span="19">
                    <span>力学</span>
                    <span>光学工程</span>
                    <span>建筑学</span>
                    <span>电子信息</span>
                    <span>土木工程</span>
                    <span>机械</span>
                </el-col>
            </el-row>
        </div>
        <div class="major_list">
            <div class="level1_name">经济学</div>
            <div>
                <div class="level2_name">理论经济学</div>
                <el-row class="list_major">
                    <el-col :span="22">
                        <span>企业经济学</span>
                        <span>专业代码：自定义专业 | 学位类别：学术型硕士</span>
                    </el-col>
                    <el-col :span="2">
                        <div>
                            <el-button type="danger">开设院校</el-button>

                        </div>
                    </el-col>
                </el-row>
            </div>
        </div>
        <!-- 分页 -->
        <el-pagination background layout="prev, pager, next" :total="1000" />
    </div>
</template>

<script setup>
import { ref, reactive, onMounted,nextTick} from "vue"
import requestFn from "@/api/requestFn";
const twoClass = reactive({ arr: [] })
const level1_name = reactive({ arr: [] })
const showClass = ref(false)
const passList=reactive({
    two_class:'',
    level1_name:'',
    level2_name:''
})
onMounted(() => {
    requestFn({
        url: '/pm_class',
        method: 'get'
    }).then(data => {
        // console.log(data.data)
        level1_name.arr = data.data
    })

    requestFn({
        url: '/showTwoClass',
        method: 'get',
    }).then(data => {
        twoClass.arr = data.data
    })
})
const two_major = (k, v) => {
    // 可以优化的点
    for(let j in passList){
        delete passList[j]
    }
    console.log(k, v)
    if (v == 0) {
        requestFn({
            url: '/pm_class',
            method: 'get'
        }).then(data => {
            // console.log(data.data)
            level1_name.arr = data.data
            nextTick(()=>{
                passList.two_class=k
                console.log(passList)
            })
        })
    } else {
        requestFn({
            url: '/am_class',
            method: 'get'
        }).then(data => {
            // console.log(data.data)
            level1_name.arr = data.data
            nextTick(()=>{
                passList.two_class=k
                console.log(passList)
                requestFn({
                    url:'/subject_class',
                    method:'post',
                    data:{
                        twoClass:passList.two_class,
                        level1_name:passList.level1_name,
                    }
                }).then(data=>{
                    console.log(data)
                })
            })
        })
    }
}

const speBtn = (k, v) => {
    console.log(k,v)
    showClass.value = true
    nextTick(()=>{
        passList.level1_name=k
        console.log(passList)
    })
}
</script>

<style scoped>
.major {
    font-size: 14px;
}

.degree_class {
    /* margin-bottom: 20px; */
    font-size: 14px;
}

.el-row {
    padding: 20px 20px;
    cursor: pointer;
}

.el-row .el-col svg {
    width: 12px;
    height: 12px;
}

.el-row .el-col span {
    margin-right: 10px;
}

.major_class {
    width: 900px;
    /* height: 400px; */
    border-radius: 15px;
    border: 1px solid #eee;
    margin: 10px auto;
}

.major_list {
    width: 900px;
    height: 400px;
    border-bottom: 1px solid #eee;
    margin: 10px auto;
}


.major_list .el-col {
    display: flex;
    flex-direction: column;
}

.major_list .el-col span:nth-of-type(1) {
    font-weight: bold;
    margin-bottom: 10px;
}

.level1_name {
    padding: 0px 10px;
    border-left: 5px solid orange;
    border-bottom: 1px solid #eee;
}

.level2_name:first-child {
    margin-top: 20px;
    /* color: red; */
    color: #f60;
    font-size: 16px;
    font-weight: bold;
    padding: 0 20px;
}

.list_major {
    border: 1px solid #eee;
    border-radius: 15px;
}
</style>