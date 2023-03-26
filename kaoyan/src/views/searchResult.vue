<template>
    <div class="searchView">
        <el-tabs type="border-card" class="demo-tabs">
            <el-tab-pane label="院校">
                <el-row>
                    <el-col :span="2">
                        <img style="width: 60px;height: 60px;" src="https://static.kaoyan.cn/image/logo/5_log.jpg" alt="">
                    </el-col>
                    <el-col :span="22">
                        <el-row>
                            <el-col style="font-size: 18px;color:#ff6600" :span="2">
                                清华大学
                            </el-col>
                            <el-col :span="1"><img style="width: 20px;height: 20px;" src="../../public/定位.png"
                                    alt=""></el-col>
                            <el-col :span="1" style="font-size: 14px;color:#888888;">北京</el-col>
                        </el-row>
                        <el-row>
                            <el-breadcrumb>
                                <el-breadcrumb-item>高等院校</el-breadcrumb-item>
                                <el-breadcrumb-item>综合类</el-breadcrumb-item>
                                <el-breadcrumb-item>985</el-breadcrumb-item>
                                <el-breadcrumb-item>211</el-breadcrumb-item>
                            </el-breadcrumb>
                        </el-row>
                    </el-col>
                </el-row></el-tab-pane>
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
import { ref, reactive,onMounted,watch } from "vue"
import { useRoute, useRouter } from 'vue-router'
import requestFn from "@/api/requestFn";
const route = useRoute()
const kw = route.query
const keyword=ref(kw)
const searchMajor = reactive({ arr: [] })
onMounted(() => {
    requestFn({
        url: '/searchResult',
        method: 'post',
        data: { keyword: kw }
    }).then(data => {
        console.log(data.data)
    }).catch(error => [
        console.log(error.error)
    ])
    requestFn({
        url: '/searchMajor',
        method: 'post',
        data: { keyword: kw }
    }).then(data => {
        // console.log(data.data)
        searchMajor.arr = data.data
    }).catch(error => [
        console.log(error.error)
    ])
}),
watch(keyword.value, (newVal,oldVal) => {
    console.log(newVal,oldVal)
    // requestFn({
    //     url: '/searchResult',
    //     method: 'post',
    //     data: { keyword: kw }
    // }).then(data => {
    //     console.log(data.data)
    // }).catch(error => [
    //     console.log(error.error)
    // ])
    // requestFn({
    //     url: '/searchMajor',
    //     method: 'post',
    //     data: { keyword: kw }
    // }).then(data => {
    //     console.log(data.data)
    //     searchMajor.arr = data.data
    // }).catch(error => [
    //     console.log(error.error)
    // ])
})

</script>

<style scoped>
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