<template>
    <div class="container">


        <div class="syl_jianshe" v-if="syl_build_new.arr.length == 0 ? false : true">
            <p><i>双一流建设</i></p>
            <div>
                <span v-for="i of syl_build_new.arr" :key="i.school_id">
                    <svg t="1680425673984" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="2841" width="200" height="200">
                        <path d="M512 624a112 112 0 1 0 0-224 112 112 0 0 0 0 224z" p-id="2842" fill="#fb2105"></path>
                    </svg>
                    {{ i }}
                </span>
            </div>

        </div>

        <div class="shuoshizhuanye">
            <p><i>硕士专业</i></p>
            <div v-for="i of departNameqc.arr">
                <h2>{{ i }}</h2>
                <ul>
                    <li v-for="v of filterArray(i)">
                       <router-link :to="{name:'majorDetail',query:{depart_id:`${v.depart_id}`,special_id:`${v.special_id}`}}">{{ v.special_code }} {{ v.special_name }}</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>


<script setup>
import requestFn from "@/api/requestFn";
import { ref, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"
import { useRoute, useRouter } from "vue-router";
const route = useRoute()
const router=useRouter()
// console.log(route.params.school_id)
const syl_build = reactive({ arr: [] })
const syl_build_new = reactive({ arr: [] })
const shuoshizhuanye = reactive({ arr: [] })
const departName = reactive({ arr: [] })
const departNameqc = reactive({ arr: [] })
const isxuanran = reactive({ arr: [] })
onMounted(() => {
    requestFn({
        url: '/syl_jianshe',
        method: 'post',
        data: {
            school_id: route.params.school_id
        }
    }).then(data => {
        // console.log(typeof(data.data))
        syl_build.arr = data.data
        syl_build_new.arr = syl_build.arr[0].syl_jianshe.split("  ").slice(0, -1)
    })
    requestFn({
        url: '/shuoshizhuanye',
        method: 'post',
        data: {
            data: route.params.school_id
        }
    }).then(data => {
        // console.log(data.data)
        shuoshizhuanye.arr = data.data
        // console.log(shuoshizhuanye.arr)
        for (let i of shuoshizhuanye.arr) {
            departName.arr.push(i.depart_name)
        }
        departNameqc.arr = [...new Set(departName.arr)]
        // 数组里面是个对象
        // shuoshizhuanye.arr.filter(shuoshizhuanye.arr=>)

    })
})

const filterArray=(a)=>{
    isxuanran.arr.length=0
    for(let i of shuoshizhuanye.arr){
        if(i.depart_name==a){
            isxuanran.arr.push(i)
        }
    }
    return isxuanran.arr
}

const toMajorDetail=(school_id,depart_id,special_id)=>{
    // console.log(school_id,depart_id,special_id)
    // router.push({
    //     path:'/schoolDetail/'+school_id+'/'+depart_id+'/'+school_id,
    // })
}
</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
}

.syl_jianshe {
    width: 1200px;
    margin: 10px auto;
}

.syl_jianshe svg {
    width: 20px;
    height: 20px;
}

.syl_jianshe span {
    display: block;
    font-size: 16px;
    font-weight: bold;
    color: #555555;
    width: 276px;
    height: 24px;
    float: left;
    margin-top: 10px;
}

.syl_jianshe p,
.shuoshizhuanye p {
    width: 100%;
    font-size: 20px;
    font-weight: bold;
    height: 30px;
    border-left: 5px solid #ff6600;
}

.syl_jianshe p i,
.shuoshizhuanye p i {
    margin-left: 10px;
}


.shuoshizhuanye {
    width: 1200px;
    margin: 20px auto;
    border: 1px solid #eee;
    padding: 20px 20px;
    /* background-color: red; */
}

.shuoshizhuanye div{
    margin-top: 20px;
    padding:20px 20px;
    border:1px solid #eee;
}

.shuoshizhuanye ul li {
    margin-top: 10px;
    display: inline-block;
    width: 50%;
    cursor: pointer;
    font-size: 14px;
    color: #555;
    margin-bottom: 15px;
    /* padding: 0px 10px; */
}
</style>