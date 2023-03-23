<template>
    <!-- 轮播图 -->
    <el-carousel :interval="4000" type="card" height="200px">
    <el-carousel-item v-for="i of slogan.arr">
        <img :src=i alt="">
    </el-carousel-item>
  </el-carousel>

  <div class="nav_middle">
    <el-row :gutter="24">
    <el-col :span="4">
        <div>
            <div><img src="../../public/考研政策.png"></div>
            <span>考研政策</span>
        </div>
    </el-col>
    <el-col :span="4">
        <div>
            <div><img src="../../public/心仪院校.png"></div>
            <span>心仪院校</span>
        </div>
    </el-col>
    <el-col :span="4">
        <div>
            <div><img src="../../public/向往专业.png"></div>
            <span>向往专业</span>
        </div>
    </el-col>
    <el-col :span="4">
        <div>
            <div><img src="../../public/历年真题.png"></div>
            <span>历年真题</span>
        </div>
    </el-col>
    <el-col :span="4">
        <div>
            <div><img src="../../public/复试备考.png"></div>
            <span>复试备考</span>
        </div>
    </el-col>
    <el-col :span="4">
        <div>
            <div><img src="../../public/心仪院校.png"></div>
            <span>考研政策</span>
        </div>
    </el-col>
  </el-row>

  </div>


</template>

<script setup>
import { ref,reactive,onMounted,watch} from 'vue';
const slogan=reactive({arr:[
    'https://news.ycwb.com/pic/2019-11/23/f0ef853a-eb59-4d19-ad1e-5d9b68f99755.jpg',
    'https://p1.itc.cn/q_70/images03/20211222/9d8ce62e045f43abb5eaf5b3d918919f.png',
    'https://pic2.zhimg.com/v2-b75713850547f70b6fb9473878592421_r.jpg',
    'https://cdn2.kybimg.com/forum/201302/17/133227n7dx8yha5wi5wxww.jpg'
]})


</script>

<style scoped>
.el-carousel{
    clear: both;
    width: 1200px;
    margin:10px auto;
    height:300px;
    background-color: #fafafa;
}
.el-carousel__item{
    height: 300px;overflow: hidden;
}
.el-carousel__item img{
    width: 100%;
    height: 100%;
}
/* .el-carousel__container{
    height: 400px;
} */
.nav_middle{
    width: 1200px;
    margin: 10px auto;
    background-color: #fafafa;
}
.el-row .el-col div{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    /* background-color: red; */
}
.el-row .el-col img{
    width: 100px;
    height: 100px;
}
</style>
