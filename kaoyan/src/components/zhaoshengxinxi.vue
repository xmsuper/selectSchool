<template>
    <div class="syl_jianshe" v-if="syl_build_new.arr.length==0?false:true">
        <p><i>双一流建设</i></p>
        <div>
            <span v-for="i of syl_build_new.arr" :key="i.school_id">
                <svg t="1680425673984" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2841" width="200" height="200"><path d="M512 624a112 112 0 1 0 0-224 112 112 0 0 0 0 224z" p-id="2842" fill="#fb2105"></path></svg>
                {{ i }}
            </span>
        </div>

    </div>
</template>


<script setup>
import requestFn from "@/api/requestFn";
import { ref,reactive,nextTick,computed,watch,onMounted,onUpdated} from "vue" 
import { useRoute,useRouter } from "vue-router";
const route=useRoute()
// console.log(route.params.school_id)
const syl_build=reactive({arr:[]})
const syl_build_new=reactive({arr:[]})
onMounted(()=>{
    requestFn({
        url:'/syl_jianshe',
        method:'post',
        data:{
            school_id:route.params.school_id
        }
    }).then(data=>{
        // console.log(typeof(data.data))
        syl_build.arr=data.data
        syl_build_new.arr=syl_build.arr[0].syl_jianshe.split("  ").slice(0,-1)
    })
})
</script>

<style scoped>
.syl_jianshe{
    width: 1200px;margin: 10px auto;
}
.syl_jianshe svg{
    width: 20px;height: 20px;
}
.syl_jianshe span{
    display: block;
    font-size: 16px;
    font-weight: bold;
    color: #555555;
    width: 276px;height: 24px;float:left;margin-top: 10px;
}
.syl_jianshe p{
    width: 100%;font-size: 20px;font-weight: bold;
    height: 30px;
    border-left: 5px solid #ff6600;
}
.syl_jianshe p i{
    margin-left: 10px;
}

</style>