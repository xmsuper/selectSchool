<template>
    <div class="container" v-for="(v,k) of school_info.arr">
        <div class="intro">
            <el-row :gutter="300">
                <el-col :span="8">
                    <img src="https://static-data.eol.cn/upload/svideo/1591237744_8048_thumb.png" alt="">
                </el-col>
                <el-col :span="16">
                    <el-card>
                        {{v.intro  }}
                    </el-card>
                    </el-col>
            </el-row>
        </div>
        <div class="basicInfo">
            <div class="info">基本信息</div>
            <el-row :gutter="0" class="rank">
                <el-col :span="4">
                    <span><i>{{ v.num_doctor }}</i>个</span>
                    <span><img src="../../public/博士.png">     博士点</span>
                </el-col>
                <el-col :span="2"></el-col>
                <el-col :span="4">
                    <span><i>{{ v.num_master }}</i>个</span>
                    <span><img src="../../public/硕士.png">硕士点</span>
                </el-col>
                <el-col :span="2"></el-col>
                <el-col :span="4">
                    <span><i>{{v.num_subject}}</i>个</span>
                    <span><img src="../../public/国家重点学科.png">国家重点学科</span>
                </el-col>
                <el-col :span="2"></el-col>
                <el-col :span="4">
                    <span><i>{{v.num_lab}}</i>个</span>
                    <span><img src="../../public/国家实验室.png">重点实验室</span>
                </el-col>   
            </el-row>
            <el-row class="infoCard">
                <div>
                    <span><img src="../../public/创建时间.png"></span>
                    <span>创建时间:</span>
                    <span>{{v.create_date}}年</span>
                </div>
                <div>
                    <span><img src="../../public/隶属于.png"></span>
                    <span>隶属于:</span>
                    <span>{{ v.belongsTo}}</span>
                </div>
                <div>
                    <span><img src="../../public/占地面积.png"></span>
                    <span>占地面积(亩):</span>
                    <span>{{ v.school_space }}</span>
                </div>
                <div>
                    <span><img src="../../public/学校地址.png"></span>
                    <span>学校地址:</span>
                    <span>山东省青岛市宁夏路308号</span>
                </div>
            </el-row>
        </div>
    </div>
</template>

<script setup>
import requestFn from "@/api/requestFn";
import { ref,reactive,nextTick,computed,watch,onMounted,onUpdated,toRaw} from "vue" 
import { useRoute,useRouter } from "vue-router";
const school_info=reactive({arr:[]})// 接受父路由的参数

// 方法1
// const route=useRoute()
// console.log(route.params)

// 方法2
const props=defineProps({
    school_id:{
        type:String,
        required:true
    }
})
onMounted(()=>{
    requestFn({
        url:'/singSchoolInfo',
        method:'post',
        data:{
            school_id:props.school_id
        }
    }).then(data=>{
        console.log(data.data)
 school_info.arr=data.data
    })
})

</script>

<style scoped>
.container{
    width: 1200px;
    margin:0 auto;
    /* background-color: red; */
    margin-bottom: 80px;
}
.intro{
    margin-top: 20px;
}
/* .intro .el-row .el-col:nth-of-type(1){
    width: 460px;height: 259px;
} */
.intro .el-row .el-col:nth-of-type(1) img{
    width: 460px;height: 259px;border-radius: 15px;

}
/* .intro .el-row .el-col:nth-of-type(2){
    width: 720px;
    height: 260px;
    overflow: hidden;
} */
.intro .el-row .el-col:nth-of-type(2) .el-card{
    width: 700px;height: 260px;font-size: 16px;overflow: hidden;
    text-overflow:ellipsis;
}
.basicInfo{
    margin-top: 20px;
}
.rank{
    /* background-color: red; */
    width: 1200px;
}
.info{
    height: 30px;border-left: 5px solid #ff6600;font-size: 20px;
    line-height: 30px;margin-bottom: 20px;
}
.rank .el-col{
    display: flex;flex-direction: column;
    align-items: center;justify-content: center;
    font-size: 14px;
}
.rank .el-col span{
    margin-top: 10px;
}
.rank .el-col i{
    font-size: 22px;
}
.rank img{
    width: 22px;height: 22px;
}


.infoCard{
    margin-top: 50px;
    border:1px solid #eee;
    width: 1200px;
    /* height: 200px; */
    display: flex;flex-direction: column;
}
.infoCard div img{
    width: 16px;height: 16px;
}
.infoCard div {
    font-size: 16px;
    display: flex;
    margin:20px 10px;
}
.infoCard div span{
    margin-right: 10px;
}
</style>