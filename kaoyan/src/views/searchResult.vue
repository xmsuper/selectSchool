<template>
    <div class="searchView">
        <div class="tip" v-if="tips">
            <svg t="1679888078538" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                p-id="2901" width="200" height="200">
                <path
                    d="M332.350877 351.214035c-4.491228-2.694737-9.880702-0.898246-12.575438 3.592983-19.761404 35.929825-58.385965 53.894737-120.364913 53.894736-5.389474 0-8.982456 3.592982-8.982456 8.982457s3.592982 8.982456 8.982456 8.982456c67.368421 0 113.178947-21.557895 135.635088-62.877193 3.592982-4.491228 1.796491-9.880702-2.694737-12.575439zM714.105263 426.666667c5.389474 0 8.982456-3.592982 8.982456-8.982456s-3.592982-8.982456-8.982456-8.982457c-61.080702 0-100.603509-17.964912-120.364912-53.894736-2.694737-4.491228-8.084211-6.287719-12.575439-3.592983-4.491228 2.694737-6.287719 8.084211-3.592982 12.575439 23.354386 41.319298 69.164912 62.877193 136.533333 62.877193zM285.642105 449.122807c-12.575439 0-22.45614 9.880702-22.45614 22.45614v35.929825c0 12.575439 9.880702 22.45614 22.45614 22.45614s22.45614-9.880702 22.456141-22.45614v-35.929825c0-12.575439-9.880702-22.45614-22.456141-22.45614zM626.975439 449.122807c-12.575439 0-22.45614 9.880702-22.456141 22.45614v35.929825c0 12.575439 9.880702 22.45614 22.456141 22.45614s22.45614-9.880702 22.45614-22.45614v-35.929825c0-12.575439-9.880702-22.45614-22.45614-22.45614zM528.168421 662.905263c0 5.389474 3.592982 8.982456 8.982456 8.982456s8.982456-3.592982 8.982456-8.982456c0-34.133333-38.624561-61.080702-88.02807-61.080702-49.403509 0-88.02807 26.947368-88.02807 61.080702 0 5.389474 3.592982 8.982456 8.982456 8.982456s8.982456-3.592982 8.982456-8.982456c0-23.354386 31.438596-43.115789 70.063158-43.115789s70.063158 19.761404 70.063158 43.115789z"
                    fill="#777777" p-id="2902"></path>
                <path
                    d="M930.582456 578.470175c-14.37193-14.37193-30.540351-26.049123-47.607017-34.133333V224.561404v-3.592983c0-1.796491-0.898246-2.694737-1.796492-4.491228 0 0 0-0.898246-0.898245-0.898246-0.898246-1.796491-1.796491-2.694737-2.694737-3.592982L657.515789 5.389474h-0.898245c-0.898246-0.898246-1.796491-1.796491-3.592983-2.694737 0 0-0.898246 0-0.898245-0.898246-0.898246-0.898246-2.694737-0.898246-3.592983-1.796491H92.519298C62.877193 0 38.624561 24.252632 38.624561 53.894737v916.210526c0 29.642105 24.252632 53.894737 53.894737 53.894737h736.561404c29.642105 0 53.894737-24.252632 53.894737-53.894737V879.382456c17.066667-8.982456 33.235088-19.761404 47.607017-34.133333 72.757895-73.65614 72.757895-193.122807 0-266.778948zM662.905263 59.284211L819.2 206.596491H716.8c-29.642105 0-53.894737-24.252632-53.894737-53.894737V59.284211zM92.519298 988.070175c-9.880702 0-17.964912-8.084211-17.964912-17.964912V53.894737c0-9.880702 8.084211-17.964912 17.964912-17.964912h534.456141v152.701754c0 29.642105 24.252632 53.894737 53.894736 53.894737H847.045614v287.438596c-62.877193-17.066667-133.838596-1.796491-183.242105 48.505263-54.792982 54.792982-68.266667 134.736842-42.217544 202.105264l-89.824561 89.824561c-32.336842 32.336842-35.031579 82.638596-8.084211 117.670175H92.519298z m571.284211-142.821052c17.066667 17.066667 36.82807 29.642105 57.487719 39.522807l-88.02807 88.02807c-20.659649 20.659649-54.792982 20.659649-76.350877 0s-20.659649-54.792982 0-76.350877l81.740351-81.740351c7.185965 10.778947 15.270175 20.659649 25.150877 30.540351zM847.045614 970.105263c0 9.880702-8.084211 17.964912-17.964912 17.964912H668.294737l91.621052-91.621052c28.74386 5.389474 59.284211 4.491228 87.129825-2.694737v76.350877z m57.487719-150.905263c-7.185965 7.185965-14.37193 12.575439-21.557894 17.964912-11.677193 8.084211-23.354386 13.473684-35.929825 17.964913-19.761404 6.287719-39.522807 9.880702-60.182456 8.08421-12.575439-0.898246-26.049123-3.592982-38.624562-7.185965-21.557895-7.185965-42.217544-19.761404-60.182456-36.82807-9.880702-9.880702-17.964912-20.659649-24.252631-31.438596-6.287719-11.677193-11.677193-23.354386-15.270176-35.031579-14.37193-51.2-1.796491-108.687719 38.624562-149.108772 43.115789-43.115789 104.196491-54.792982 158.091228-35.929825 12.575439 4.491228 24.252632 9.880702 35.929824 17.964912 8.084211 5.389474 15.270175 10.778947 21.557895 17.964913 61.978947 59.284211 61.978947 156.294737 1.796491 215.578947z"
                    fill="#777777" p-id="2903"></path>
                <path
                    d="M879.382456 628.77193c-3.592982-3.592982-8.982456-3.592982-12.575438 0s-3.592982 8.982456 0 12.575438c38.624561 38.624561 38.624561 100.603509 0 139.228071-3.592982 3.592982-3.592982 8.982456 0 12.575438 1.796491 1.796491 4.491228 2.694737 6.287719 2.694737s4.491228-0.898246 6.287719-2.694737c45.810526-44.912281 45.810526-118.568421 0-164.378947z"
                    fill="#777777" p-id="2904"></path>
            </svg>
            <p>抱歉，没有找到您想要的院校/专业！</p>
        </div>
        <el-tabs v-else type="border-card" class="demo-tabs">
            <el-tab-pane label="院校">
                <div @click="gotoDetail(v.school_id)" v-for="(v, k) of searchSchool.arr"
                    style="border:1px solid #eee;border-radius: 15px;margin-bottom: 10px;padding: 10px 40px;">
                    <el-row>
                        <el-col :span="2">
                            <img style="width: 60px;height: 60px;" :src=v.school_name.school_img>
                        </el-col>
                        <el-col :span="22">
                            <el-row>
                                <el-col style="font-size: 18px;color:#ff6600" :span="4">
                                    {{ v.school_name.school_name }}
                                </el-col>
                                <el-col :span="1"><img style="width: 20px;height: 20px;" src="../../public/定位.png"
                                        alt=""></el-col>
                                <el-col :span="1" style="font-size: 14px;color:#888888;">{{ v.province_name }}</el-col>
                            </el-row>
                            <el-row>
                                <el-breadcrumb>
                                    <el-breadcrumb-item>{{ v.type_school_name }}</el-breadcrumb-item>
                                    <el-breadcrumb-item>{{ v.type_name }}</el-breadcrumb-item>
                                    <el-breadcrumb-item v-if="v.is_985 == 1">985</el-breadcrumb-item>
                                    <el-breadcrumb-item v-if="v.is_211 == 1">211</el-breadcrumb-item>
                                    <el-breadcrumb-item v-if="v.syl == 1">双一流</el-breadcrumb-item>
                                    <el-breadcrumb-item v-if="v.is_zihuaxian = 1">自划线</el-breadcrumb-item>
                                    <el-breadcrumb-item>{{ v.province_area }}区</el-breadcrumb-item>

                                </el-breadcrumb>
                            </el-row>
                        </el-col>
                    </el-row>
                </div>

            </el-tab-pane>
            <el-tab-pane label="专业">
                <div v-for="i of searchMajor.arr">
                    <el-row>
                        <el-col><span style="font-size: 18px;color: #ff6600;">{{ i.major_name }}</span></el-col>
                    </el-row>
                    <el-row>
                        <el-breadcrumb>
                            <el-breadcrumb-item>{{ i.level1_name }}</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i.level2_name }}类</el-breadcrumb-item>
                            <el-breadcrumb-item>专业代码{{ i.major_code }}</el-breadcrumb-item>
                        </el-breadcrumb>
                    </el-row>
                </div>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<script setup>
import navHeader from "@/components/navHeader.vue";
import { ref, reactive, onMounted, watch, nextTick } from "vue"
import { useRoute, useRouter } from 'vue-router'
import requestFn from "@/api/requestFn";
const route = useRoute()
const router = useRouter()
const kw = route.query
const keyword = ref(kw)
const tips = ref(false)
const searchMajor = reactive({ arr: [] })
const searchSchool = reactive({ arr: [] })
// 路由带参跳转
const gotoDetail=(e)=>{
    router.push({
        // path:'/schoolDetail/'+e,
        name:'schoolDetail',
        params:{
            school_id:e,
        }
    })
}
// 监听路由的变化
// console.log(router.currentRoute.value.query)
watch(() => router.currentRoute.value.query, (newVal) => {
    // console.log(newVal.keyword)
    requestFn({
        url: '/searchResult',
        method: 'post',
        data: { keyword: newVal }
    }).then(data => {
        // console.log(data.data)
        searchSchool.arr = data.data
        requestFn({
            url: '/searchMajor',
            method: 'post',
            data: { keyword: newVal }
        }).then(data => {
            // console.log(data.data)
            searchMajor.arr = data.data
            if (searchSchool.arr.length == 0 && searchMajor.arr.length == 0) {
                tips.value = true
            } else {
                tips.value = false
            }

        }).catch(error => [
            console.log(error.error)
        ])

        // 下次在做分页
    }).catch(error => [
        console.log(error.error)
    ])
})

onMounted(() => {
    requestFn({
        url: '/searchResult',
        method: 'post',
        data: { keyword: kw }
    }).then(data => {
        // console.log(data.data)
        searchSchool.arr = data.data
        requestFn({
            url: '/searchMajor',
            method: 'post',
            data: { keyword: kw }
        }).then(data => {
            // console.log(data.data)
            searchMajor.arr = data.data
            if (searchSchool.arr.length == 0 && searchMajor.arr.length == 0) {
                tips.value = true
            } else {
                tips.value = false
            }
        }).catch(error => [
            console.log(error.error)
        ])

        // 下次在做分页
    }).catch(error => [
        console.log(error.error)
    ])

})

</script>

<style scoped>
.tip {
    width: 1200px;
    height: 800px;
    border: 1px solid #ff6600;
    border-radius: 15px;
}

.tip svg {
    margin-top: 10%;
    margin-left: 40%;
}

.tip p {
    text-align: center;
    font-size: 22px;
    margin-top: 10px;
    color: #ff6600;
}

.el-tab-pane:nth-of-type(2) {
    /* border:1px solid red; */
}

.el-tab-pane:nth-of-type(2) div {
    /* border: 1px solid #eee; */
    margin-top: 10px;
    /* border:1px solid red; */

}

.searchView {
    width: 1200px;
    margin: 20px auto;
}

.el-breadcrumb {
    margin-top: 15px;
}
</style>