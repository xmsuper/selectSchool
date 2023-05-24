<template>
    <div class="major_class">
        <el-row class="degree_class">
            <el-col :span="2">学位类别</el-col>
            <el-col :span="2"><svg t="1679539700485" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="2790" width="200" height="200">
                    <path
                        d="M660.2496 485.1456L385.1776 210.0992a18.048 18.048 0 0 0-25.5488 0c-7.0656 7.0656-7.0656 18.5088 0 25.5488L634.7008 510.72c0.3328 0.3328 0.3328 0.8448 0 1.1776l-276.48 276.4544a18.048 18.048 0 0 0 0 25.5488 17.98656 17.98656 0 0 0 12.7744 5.2992c4.6336 0 9.2416-1.7664 12.7744-5.2992L660.224 537.4464c14.4384-14.4128 14.4384-37.888 0.0256-52.3008z"
                        fill="#231815" p-id="2791"></path>
                </svg></el-col>
            <el-col :span="2" @click="all_majorFn" :class="allbtn == true ? 'active' : ''">全部</el-col>
            <el-col :span="18"><span @click="two_major(k.major_class, v)" :class="isActive == v ? 'active' : ''"
                    v-for="(k, v) of twoClass.arr">{{
                        k.major_class
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
            <el-col :span="2"></el-col>
            <el-col :span="18">
                <!-- 点击门类，显示专业具体名字 -->
                <span @click="speBtn(k.level1_name, v)" :class="isActive1 == v ? 'active' : ''"
                    v-for="(k, v) of level1_name.arr">{{ k.level1_name
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
            <el-col :span="2"></el-col>
            <el-col :span="18">
                <span v-for="(v, k) of level2_name.arr" :class="isActive2 == k ? 'active' : ''"
                    @click="majorNameBtn(v.level2_name, k)">{{ v.level2_name
                    }}</span>
            </el-col>
        </el-row>
    </div>
</template>

<script setup>
import { ref, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"
import requestFn from "@/api/requestFn.js";
const allbtn = ref(true)
const twoClass = reactive({ arr: [] })
const level1_name = reactive({ arr: [] })
const level2_name = reactive({ arr: [] })
const showClass = ref(false)
const all_major = reactive({ arr: [] })
const passList = reactive({
    two_class: '专业型硕士',
    level1_name: '',
    level2_name: '',
    major_name: ''
})
const emit=defineEmits(['getChildData'])
onMounted(() => {
    requestFn({
        url: '/pm_class',
        method: 'get'
    }).then(data => {
        level1_name.arr = data.data
    })

    requestFn({
        url: '/showTwoClass',
        method: 'get',
    }).then(data => {
        twoClass.arr = data.data
    })
})
// 获取所有专业列表
const all_majorFn = () => {
    allbtn.value=true
    isActive.value=-1
    isActive1.value=-1
    isActive2.value=-1
    showClass.value=false
}

const isActive = ref(null)
const isActive1 = ref(null)
const isActive2 = ref(null)

// 硕士类别筛选--开始
const two_major = (v, k) => {
    allbtn.value = false
    isActive.value = k
    showClass.value = false
    passList.two_class = v
    passList.level1_name=''
    passList.level2_name=''
    isActive1.value=-1

    requestFn({
        url: '/pm_class',
        method: 'post',
        data: {
            data: passList.two_class
        }
    }).then(data => {
        level1_name.arr = data.data
    })
}
// 硕士类别筛选--结束
watch(passList, (newVal, oldVal) => {
    const notNull = Object.fromEntries(
        Object.entries(passList).filter(([k, v]) => v !== null && v !== '')
    )
    // console.log(notNull)
    emit('getChildData',notNull)
})




// leve1_name --开始
const speBtn = (k, v) => {
    allbtn.value = false
    isActive1.value = v
    isActive2.value = -1
    showClass.value = true
    passList.level1_name = k
    passList.level2_name=''
    requestFn({
        url: '/subject_class',
        method: 'post',
        data: {
            twoClass: passList.two_class,
            level1_name: passList.level1_name,
        }
    }).then(data => {
        level2_name.arr = data.data
    })
}
// leve1_name --结束

// level2_name--开始
const majorNameBtn = (v, k) => {
    allbtn.value = false
    isActive2.value = k
    passList.level2_name = v
}
// level2_name--结束

</script>

<style scoped>
.active {
    color: #ff6602;
}

.major {
    font-size: 14px;
    float: left;
    margin: 0 150px 0 180px;
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
    margin-right: 20px;
}

.el-row .el-col span:hover {
    color: #ff6602;
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
    height: 200px;
    /* border-bottom: 1px solid #eee; */
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