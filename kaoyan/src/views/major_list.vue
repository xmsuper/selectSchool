<template>
    <el-backtop :right="100" :bottom="100" />
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
        <div class="major_list" v-for="i of newLevel1Name.item" :key="i">
            <div class="level1_name" style="border: 1px solid orange;margin-top: 20px;border-radius: 15px;">
                <p style="margin-top:10px;border-left: 5px solid orange;padding-left: 5px;font-size: 20px;font-weight: bold;">{{ i }}</p>
                <div class="level2_name" v-for="j,k of level2_name_fn(i)" :key="j">
                    <!-- <p>经济学</p> -->
                        <div class="major_name_list" style="margin-top: 10px;display: flex;justify-content: space-between;">
                            <div class="major_list_detail">
                                <p style="color:red">{{j.major_name}}</p>
                                <span style="margin-right: 20px;">专业代码：{{j.major_code}}</span>
                                <span>学位类别:{{ j.major_class }}</span>
                            </div>
                            <div>
                                <el-button color="#f60" style="color:#fff" @click="kaisheyuanxiao(j)" >开设院校</el-button>
                            </div>
                        </div>
                </div>
            </div>
        </div>
        <!-- 分页 -->
        <el-pagination v-model:current-page="currentPage" background layout="prev, pager, next" :total="maxPage"
            :page-size="pageSize" @current-change="handleCurrentChange" />
    </div>
    <hotSearch></hotSearch>
</template>

<script setup>
import { ref, reactive, onMounted, nextTick,computed,watch } from "vue"
import requestFn from "@/api/requestFn.js";
import hotSearch from "@/components/hotSearch.vue";
import router from "@/router/index.js";
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
// 分页---开始
const pageSize = ref(20)
const currentPage = ref(1)
const maxPage = ref(0)
const all_major_slice = reactive({ arr: [] })
const handleCurrentChange = (val) => {
    all_major_slice.arr = all_major.arr.slice((val - 1) * pageSize.value, val * pageSize.value)
}
// 分页---结束

const class1 = reactive({ item: [] })
const newLevel1Name = reactive({ item: [] })
const newLeve21Name = reactive({ item: [] })
const newMjorName = reactive({ item: [] })
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

    // 获取全部的专业-开始
    requestFn({
        url: '/detail_major_list',
        method: 'get',
    }).then(data => {
        all_major.arr = data.data
        // console.log(all_major.arr)
        maxPage.value = all_major.arr.length
        for (let i of all_major.arr) {
            class1.item.push(i.level1_name)
        }
        newLevel1Name.item=[...new Set(class1.item)]
        all_major_slice.arr = all_major.arr.slice((currentPage.value - 1) * pageSize.value, currentPage.value * pageSize.value)
    })
    // 获取全部的专业-结束

})
// 获取所有专业列表
const all_majorFn = () => {
    allbtn.value = true
    isActive.value = -1
    isActive1.value = -1
    isActive2.value = -1
    requestFn({
        url: '/detail_major_list',
        method: 'get'
    }).then(data => {
        all_major.arr = data.data
    })
}

const isActive = ref(null)
const isActive1 = ref(null)
const isActive2 = ref(null)

// 专业型硕士筛选-开始
const two_major = (k, v) => {
    allbtn.value = false
    isActive.value = v
    showClass.value = false
    // 可以优化的点
    for (let j in passList) {
        delete passList[j]
    }
    if (v == 0) {
        requestFn({
            url: '/pm_class',
            method: 'get'
        }).then(data => {
            level1_name.arr = data.data
            nextTick(() => {
                passList.two_class = k
                requestFn({
                    url: '/detail_major_list',
                    method: 'post',
                    data: {
                        twoClass: passList.two_class,
                    }
                }).then(data => {
                    all_major.arr = data.data
                    maxPage.value = all_major.arr.length
                    all_major_slice.arr = all_major.arr.slice((currentPage.value - 1) * pageSize.value, currentPage.value * pageSize.value)
                })
            })
        })
    } else {
        requestFn({
            url: '/am_class',
            method: 'get'
        }).then(data => {
            level1_name.arr = data.data
            nextTick(() => {
                passList.two_class = k
                // console.log(passList)
                requestFn({
                    url: '/detail_major_list',
                    method: 'post',
                    data: {
                        twoClass: passList.two_class,
                    }
                }).then(data => {
                    all_major.arr = data.data
                    maxPage.value = all_major.arr.length
                    all_major_slice.arr = all_major.arr.slice((currentPage.value - 1) * pageSize.value, currentPage.value * pageSize.value)
                })
            })
        })
    }
}
// 专业型硕士筛选-结束

// level1_name-开始
const speBtn = (k, v) => {
    allbtn.value = false
    isActive1.value = v
    isActive2.value = -1
    showClass.value = true
    nextTick(() => {
        passList.level1_name = k
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

        // 请求筛选的数据
        requestFn({
            url: '/detail_major_list',
            method: 'post',
            data: {
                level1_name: passList.level1_name,
            }
        }).then(data => {
            all_major.arr = data.data
            maxPage.value = all_major.arr.length
            all_major_slice.arr = all_major.arr.slice((currentPage.value - 1) * pageSize.value, currentPage.value * pageSize.value)
        })

    })
}
// level1_name--结束

// 专业筛选--开始
const majorNameBtn = (v, k) => {
    allbtn.value = false
    isActive2.value = k
    nextTick(() => {
        passList.level2_name = v
        // console.log(passList)
        requestFn({
            url: '/detail_major_list',
            method: 'post',
            data: {
                twoClass: passList.two_class,
                level1_name: passList.level1_name,
                level2_name: passList.level2_name,
            }
        }).then(data => {
            all_major.arr = data.data
            maxPage.value = all_major.arr.length
            all_major_slice.arr = all_major.arr.slice((currentPage.value - 1) * pageSize.value, currentPage.value * pageSize.value)
        })
    })
}
// 专业筛选--结束

const kaisheyuanxiao=(e)=>{
    console.log(e)
    router.push({
        path:'/major_list_select',
        query:{
            major_name:e.major_name,
            major_code:e.major_code,
            major_class:e.major_class,
        }
    })

}


const myMap={}

const newLevel2Name=reactive({item:[]})
const level2_name_fn = (e)=>{
  return [...new Set(all_major.arr.filter(item=>item.level1_name===e))]

}


</script>

<style scoped>
.active {
    color: #ff6602;
}

.el-pagination.is-background .el-pager li.is-active {
    background-color: red;
}

.el-pagination {
    margin: 0px 35%;
    margin-bottom: 200px;
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
    /* height: 200px; */
    /* border-bottom: 1px solid #eee; */
    margin: 10px auto;
    /* background-color: red; */
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
    /* border-left: 5px solid orange; */
    border-bottom: 1px solid #eee;
}


.level2_name {
    width: 800px;
    font-weight: 600;
    font-size: 16px;
    color: #f60;
    padding: 8px 15px;
    display: inline-block;
    position: relative;
    border: 1px solid #eee;
    border-bottom: none;
}

.list_major {
    border: 1px solid #eee;
    border-radius: 15px;
}

.major_name {
    padding: 15px;
    border: 1px solid #eee;
}

.major_name_list {
    /* padding: 15px 0; */
    border-bottom: 1px dashed #eee;
    position: relative;
    cursor: pointer;
}

.major_list-title {
    font-size: 16px;
    color: #000;
    margin-bottom: 10px;
    font-weight: 600;
    transition: all .4s;
}

.major_list_detail {
    padding-bottom: 10px;
}

.major_list_detail span {
    font-size: 14px;
    color: #555555;
}
</style>