<template>
  <div class="header_title"  style="width: 1200px;margin: 0px auto;">
    <h1 style="font-size:30px;border-bottom: 1px solid #eee;padding-bottom: 10px;">{{ route.query.major_name }}</h1>
    <p><span>学术类别：<i>{{ route.query.major_class }}</i></span>   <span>专业代码：<i>{{ route.query.major_code }}</i></span></p>
  </div>
  <div style="width: 1200px;margin: 0px auto;">
    <div v-for="i of recommend_school_new.item"
            style="margin: 10px auto;border:1px solid orange;padding: 20px;border-radius: 15px;">
            <el-row>
                <el-col :span="2">
                    <div>
                        <img style="width: 60px;height: 60px;" :src=i.school_img>
                    </div>
                </el-col>
                <el-col :span="8">
                    <div>
                        <div class="school_list_item_content" >
                            <span style="font-size: 18px;">{{ i.school_name }}</span>
                            <span style="margin-left: 20px;">
                                <svg t="1678540025337" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                    xmlns="http://www.w3.org/2000/svg" p-id="2949" width="16" height="16">
                                    <path
                                        d="M512 11.65312c-225.3824 0-408.75008 183.35744-408.75008 408.75008 0 167.56736 97.51552 316.30336 179.32288 411.57632C366.53056 929.7408 471.6032 1012.34688 512 1012.34688c39.41376 0 144.51712-84.96128 229.5296-185.53856 155.94496-184.48384 179.22048-333.81376 179.22048-406.41536 0-225.3824-183.35744-408.73984-408.75008-408.73984z m-0.04096 959.71328c-42.47552-4.5568-367.73888-263.0656-367.73888-550.97344C144.20992 217.6 309.20704 52.61312 512 52.61312c202.8032 0 367.79008 164.98688 367.79008 367.79008 0 277.27872-326.53312 545.76128-367.83104 550.9632z"
                                        fill="" p-id="2950"></path>
                                    <path
                                        d="M512.69632 212.77696c-114.4832 0-207.616 93.14304-207.616 207.616 0 114.4832 93.14304 207.62624 207.616 207.62624s207.616-93.14304 207.616-207.62624c0.01024-114.47296-93.1328-207.616-207.616-207.616z m0 374.28224c-91.89376 0-166.656-74.76224-166.656-166.66624 0-91.89376 74.76224-166.656 166.656-166.656 91.904 0 166.656 74.76224 166.656 166.656 0.01024 91.904-74.752 166.66624-166.656 166.66624z"
                                        fill="" p-id="2951"></path>
                                </svg>
                                {{ i.province }}
                                排名：{{ i.rank }}
                            </span>
                        </div>
                        <el-breadcrumb separator="|" style="margin-top: 20px;">
                            <el-breadcrumb-item v-if="i.is_211== 1">211</el-breadcrumb-item>
                            <el-breadcrumb-item v-if="i.is_985== 1">985</el-breadcrumb-item>
                            <el-breadcrumb-item v-if="i.is_zihuaxian== 1">自划线</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i.school_type }}</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i.school_type_final }}</el-breadcrumb-item>
                        </el-breadcrumb>
                    </div>
                </el-col>
                <el-col :span="14">
                    <el-button @click="gotoDetail(i.school_id)" color="#f60" style="float: right;color:#fff">查看详情</el-button>
                </el-col>
            </el-row>
        </div>
  </div>

    <el-pagination style="margin-left:460px;padding: 50px;" v-model:current-page="curretPage" :disabled="disabled" :background="background"
                layout="prev, pager, next, jumper" :total="maxPage" @current-change="handleCurrentChange" />
</template>

<script setup>
import {ref,reactive,onMounted,computed,watch} from 'vue';
import { useRoute,useRouter } from 'vue-router';
import requestFn from '@/api/requestFn';
const router=useRouter()
const route=useRoute()
const recommend_school=reactive({item:[]})


// 每页显示个数
let pageSize = ref(10)
// 当前页,初始当前页等于1
let curretPage = ref(1)
// 最大条数
let maxPage = ref(0)
const gotoDetail = (e) => {
    router.push({
        // path:'/schoolDetail/'+e,
        path: '/schoolDetail/' + e + '/schoolView',
        params: {
            school_id: e,
        }
    })
}

const recommend_school_new=reactive({item:[]})
onMounted(()=>{
    requestFn({
        url:'/kaisheyuanxiao',
        method:'post',
        data:{
            major_name:route.query.major_name,
            major_code:route.query.major_code,
            major_class:route.query.major_class
        }
    }).then(res=>{
        console.log(res.data)
        recommend_school.item=res.data
        maxPage.value=recommend_school.item.length
        recommend_school_new.item = recommend_school.item.slice((curretPage.value - 1) * pageSize.value, curretPage.value * pageSize.value)

    })
})

// 当前页数
const handleCurrentChange = (val) => {
    // slice((当前页-1)*每页条数,当前页*每页条数)
    recommend_school_new.item = recommend_school.item.slice((val - 1) * pageSize.value, val * pageSize.value)
}

</script>

<style lang="less" scoped>

.header_title{
    p{
        padding:30px 0px;
        span{
            font-size: 14px;
        }
    }
}


</style>
