<template>
    <div class="container">
        <el-form :model="form">
            <div class="import">
                <div class="chooseMajor">请选择你要考的专业</div>
                <chooseMajor @getChildData="getChildVal"></chooseMajor>
            </div>

            <div class="chooseRegin">
                <div>请选择你想去的地区</div>
                <ul class="allRegin">
                    <li v-for="(i, k) of allRegin.arr" :class="provinceActive == k + 1 ? 'active' : ''"
                        @click="yourRegin(i[0], k)">
                        {{ i[0] }}</li>
                </ul>
            </div>
            <div class="score">
                <div class="score-title">请输入你的预估分数？</div>
                <div style="background-color: #fff;">
                    <!-- <el-input v-model="form.score" :rows="2" type="textarea" placeholder="请输入你的分数" /> -->
                    <el-input-number v-model="form.score" :min="1" :max="500"  placeholder="请输入你的分数" />
                </div>
            </div>
            <div class="scoreSchool">
                <div class="score-title">请输你的目标院校：</div>
                <el-cascader style="margin-left: 14px;" v-model="form.scoreSchool" :options="school_name_choose" @change="handleChangeJilian" />

            </div>
            <el-button class="subbtn" @click="onsubmit">获取结果</el-button>
        </el-form>
    </div>
    <div class="search">
        <hotSearch></hotSearch>
    </div>

    <div class="recommend_result" style="width: 1200px;margin-left: 100px;margin-top: 30px;">
        <p v-if="isShow" style="font-size: 20px;border-left:5px solid #f60;padding-left: 10px;">保底院校</p>
        <div v-for="i of recommend_school.item.slice(0, 3)"
            style="margin: 10px auto;border:1px solid orange;padding: 20px;border-radius: 15px;">
            <el-row>
                <el-col :span="2">
                    <div>
                        <img style="width: 60px;height: 60px;" :src=i[26]>
                    </div>
                </el-col>
                <el-col :span="6">
                    <div>
                        <div class="school_list_item_content">
                            <span>{{ i[9] }}</span>
                            <span>
                                <svg t="1678540025337" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                    xmlns="http://www.w3.org/2000/svg" p-id="2949" width="16" height="16">
                                    <path
                                        d="M512 11.65312c-225.3824 0-408.75008 183.35744-408.75008 408.75008 0 167.56736 97.51552 316.30336 179.32288 411.57632C366.53056 929.7408 471.6032 1012.34688 512 1012.34688c39.41376 0 144.51712-84.96128 229.5296-185.53856 155.94496-184.48384 179.22048-333.81376 179.22048-406.41536 0-225.3824-183.35744-408.73984-408.75008-408.73984z m-0.04096 959.71328c-42.47552-4.5568-367.73888-263.0656-367.73888-550.97344C144.20992 217.6 309.20704 52.61312 512 52.61312c202.8032 0 367.79008 164.98688 367.79008 367.79008 0 277.27872-326.53312 545.76128-367.83104 550.9632z"
                                        fill="" p-id="2950"></path>
                                    <path
                                        d="M512.69632 212.77696c-114.4832 0-207.616 93.14304-207.616 207.616 0 114.4832 93.14304 207.62624 207.616 207.62624s207.616-93.14304 207.616-207.62624c0.01024-114.47296-93.1328-207.616-207.616-207.616z m0 374.28224c-91.89376 0-166.656-74.76224-166.656-166.66624 0-91.89376 74.76224-166.656 166.656-166.656 91.904 0 166.656 74.76224 166.656 166.656 0.01024 91.904-74.752 166.66624-166.656 166.66624z"
                                        fill="" p-id="2951"></path>
                                </svg>
                                {{ i[22] }}
                                排名：{{ i[21] }}
                            </span>
                        </div>
                        <el-breadcrumb separator="|">
                            <el-breadcrumb-item v-if="i[12] == 1">211</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i[13] }}</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i[14] }}</el-breadcrumb-item>
                        </el-breadcrumb>
                    </div>
                </el-col>
                <el-col :span="16" style="display: flex;align-items: center;justify-content: space-between;">
                    <!-- 右侧=开始 -->
                    <div style="display: flex;text-align: left;justify-content:space-around;" class="school_score">
                        <p>{{ i[2] }}</p>
                        <!-- <p>总分：{{ i[3] }}</p> -->
                        <p>政治：{{ i[4] }} </p>
                        <p>英语：{{ i[5] }}</p>
                        <p>业务课1: {{ i[6] }}</p>
                        <p>业务课2: {{ i[7] }}</p>
                    </div>

                    <p>
                        <el-button color="#f60" style="color:#fff" @click="gotoDetail(i[24])">查看详情</el-button>
                        <el-button color="#f60" style="color:#fff" @click="joinCompare(i[24])">加入对比</el-button>
                    </p>
                    <!-- 右侧--结束 -->
                </el-col>
            </el-row>
        </div>
    </div>

    <div class="recommend_result" style="width: 1200px;margin-left: 100px;margin-top: 30px;">
        <p v-if="isShow" style="font-size: 20px;border-left:5px solid #f60;padding-left: 10px;">稳健院校</p>
        <div v-for="i of recommend_school.item.slice(3, 8)"
            style="margin: 10px auto;border:1px solid orange;padding: 20px;border-radius: 15px;">
            <el-row>
                <el-col :span="2">
                    <div>
                        <img style="width: 60px;height: 60px;" :src=i[26]>
                    </div>
                </el-col>
                <el-col :span="6">
                    <div>
                        <div class="school_list_item_content">
                            <span>{{ i[9] }}</span>
                            <span>
                                <svg t="1678540025337" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                    xmlns="http://www.w3.org/2000/svg" p-id="2949" width="16" height="16">
                                    <path
                                        d="M512 11.65312c-225.3824 0-408.75008 183.35744-408.75008 408.75008 0 167.56736 97.51552 316.30336 179.32288 411.57632C366.53056 929.7408 471.6032 1012.34688 512 1012.34688c39.41376 0 144.51712-84.96128 229.5296-185.53856 155.94496-184.48384 179.22048-333.81376 179.22048-406.41536 0-225.3824-183.35744-408.73984-408.75008-408.73984z m-0.04096 959.71328c-42.47552-4.5568-367.73888-263.0656-367.73888-550.97344C144.20992 217.6 309.20704 52.61312 512 52.61312c202.8032 0 367.79008 164.98688 367.79008 367.79008 0 277.27872-326.53312 545.76128-367.83104 550.9632z"
                                        fill="" p-id="2950"></path>
                                    <path
                                        d="M512.69632 212.77696c-114.4832 0-207.616 93.14304-207.616 207.616 0 114.4832 93.14304 207.62624 207.616 207.62624s207.616-93.14304 207.616-207.62624c0.01024-114.47296-93.1328-207.616-207.616-207.616z m0 374.28224c-91.89376 0-166.656-74.76224-166.656-166.66624 0-91.89376 74.76224-166.656 166.656-166.656 91.904 0 166.656 74.76224 166.656 166.656 0.01024 91.904-74.752 166.66624-166.656 166.66624z"
                                        fill="" p-id="2951"></path>
                                </svg>
                                {{ i[22] }}
                                排名：{{ i[21] }}
                            </span>
                        </div>
                        <el-breadcrumb separator="|">
                            <el-breadcrumb-item v-if="i[12] == 1">985</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i[13] }}</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i[14] }}</el-breadcrumb-item>
                        </el-breadcrumb>
                    </div>
                </el-col>
                <el-col :span="16" style="display: flex;align-items: center;justify-content: space-between;">
                    <!-- 右侧=开始 -->
                    <div style="display: flex;text-align: left;justify-content:space-around;" class="school_score">
                        <p>{{ i[2] }}</p>
                        <!-- <p>总分：{{ i[3] }}</p> -->
                        <p>政治：{{ i[4] }} </p>
                        <p>英语：{{ i[5] }}</p>
                        <p>业务课1: {{ i[6] }}</p>
                        <p>业务课2: {{ i[7] }}</p>
                    </div>

                    <p>
                        <el-button color="#f60" style="color:#fff" @click="gotoDetail(i[24])">查看详情</el-button>
                        <el-button color="#f60" style="color:#fff" @click="joinCompare(i[24])">加入对比</el-button>
                    </p>
                    <!-- 右侧--结束 -->
                </el-col>
            </el-row>
        </div>
    </div>

    <div class="recommend_result" style="width: 1200px;margin-left: 100px;margin-top: 30px;">
        <p v-if="isShow" style="font-size: 20px;border-left:5px solid #f60;padding-left: 10px;">冲刺院校</p>
        <div v-for="i of recommend_school.item.slice(8, recommend_school.item.length)"
            style="margin: 10px auto;border:1px solid orange;padding: 20px;border-radius: 15px;">
            <el-row>
                <el-col :span="2">
                    <div>
                        <img style="width: 60px;height: 60px;" :src=i[26]>
                    </div>
                </el-col>
                <el-col :span="6">
                    <div>
                        <div class="school_list_item_content">
                            <span>{{ i[9] }}</span>
                            <span>
                                <svg t="1678540025337" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                    xmlns="http://www.w3.org/2000/svg" p-id="2949" width="16" height="16">
                                    <path
                                        d="M512 11.65312c-225.3824 0-408.75008 183.35744-408.75008 408.75008 0 167.56736 97.51552 316.30336 179.32288 411.57632C366.53056 929.7408 471.6032 1012.34688 512 1012.34688c39.41376 0 144.51712-84.96128 229.5296-185.53856 155.94496-184.48384 179.22048-333.81376 179.22048-406.41536 0-225.3824-183.35744-408.73984-408.75008-408.73984z m-0.04096 959.71328c-42.47552-4.5568-367.73888-263.0656-367.73888-550.97344C144.20992 217.6 309.20704 52.61312 512 52.61312c202.8032 0 367.79008 164.98688 367.79008 367.79008 0 277.27872-326.53312 545.76128-367.83104 550.9632z"
                                        fill="" p-id="2950"></path>
                                    <path
                                        d="M512.69632 212.77696c-114.4832 0-207.616 93.14304-207.616 207.616 0 114.4832 93.14304 207.62624 207.616 207.62624s207.616-93.14304 207.616-207.62624c0.01024-114.47296-93.1328-207.616-207.616-207.616z m0 374.28224c-91.89376 0-166.656-74.76224-166.656-166.66624 0-91.89376 74.76224-166.656 166.656-166.656 91.904 0 166.656 74.76224 166.656 166.656 0.01024 91.904-74.752 166.66624-166.656 166.66624z"
                                        fill="" p-id="2951"></path>
                                </svg>
                                {{ i[22] }}
                                排名：{{ i[21] }}
                            </span>
                        </div>
                        <el-breadcrumb separator="|">
                            <el-breadcrumb-item v-if="i[12] == 1">985</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i[13] }}</el-breadcrumb-item>
                            <el-breadcrumb-item>{{ i[14] }}</el-breadcrumb-item>
                        </el-breadcrumb>
                    </div>
                </el-col>
                <el-col :span="16" style="display: flex;align-items: center;justify-content: space-between;">
                    <!-- 右侧=开始 -->
                    <div style="display: flex;text-align: left;justify-content:space-around;" class="school_score">
                        <p>{{ i[2] }}</p>
                        <!-- <p>总分：{{ i[3] }}</p> -->
                        <p>政治：{{ i[4] }} </p>
                        <p>英语：{{ i[5] }}</p>
                        <p>业务课1: {{ i[6] }}</p>
                        <p>业务课2: {{ i[7] }}</p>
                    </div>

                    <p>
                        <el-button color="#f60" style="color:#fff" @click="gotoDetail(i[24])">查看详情</el-button>
                        <el-button color="#f60" style="color:#fff" @click="joinCompare(i[24])">加入对比</el-button>

                    </p>
                    <!-- 右侧--结束 -->
                </el-col>
            </el-row>
        </div>
    </div>

    <el-badge v-if="isShowDuibi" @click="zhankai" :value="compareSchoolValue"
        style="position:fixed;bottom:100px;right: 40px;" class="item" type="primary">
        <div class=""
            style="width:80px;height: 80px;font-size: 14px;display: flex;border-radius: 15px;border: 1px solid #f60;">
            <span style="margin: auto;">展开对比</span>
        </div>
    </el-badge>


    <el-dialog v-model="dialogTableVisible" width="80%" title="院校对比">
        <!-- 加入对比 -->
        <div class="schoolCompare">
            <ul style="display: flex;">
                <li>
                    <div style="">
                        <p></p>
                        <p>学校名称</p>
                        <p>所在省份</p>
                        <p>是否985</p>
                        <p>是否211</p>
                        <p>是否双一流</p>
                        <p>是否自划线</p>
                        <p>招生类型</p>
                        <p>学校排名</p>
                        <p>复试线</p>
                        <p>招生人数</p>
                    </div>
                </li>
                <li v-for="i of compareSchoolList.item">
                    <div style="">
                        <p @click="gotoDetail(i.school_id)"><img style="width: 30px;height: auto;" :src=i.school_img alt="">
                        </p>
                        <p>{{ i.school_name }}</p>
                        <p>{{ i.province_name }}</p>
                        <p v-if="i.is_985 == 1" :class="i.is_985 == 1 ? 'active' : ''">985</p>
                        <p v-else>--</p>
                        <p v-if="i.is_211 == 1" :class="i.is_211 == 1 ? 'active' : ''">211</p>
                        <p v-else>--</p>
                        <p v-if="i.syl == 1" :class="i.syl == 1 ? 'active' : ''">双一流</p>
                        <p v-else>--</p>
                        <p v-if="i.is_zihuaxian == 1" :class="i.zihuaxian == 1 ? 'active' : ''">✓</p>
                        <p v-else>×</p>
                        <p>{{ i.learn_type }}</p>
                        <p>{{ i.rank }}</p>

                        <p>{{ i.total }}</p>
                        <p>{{ i.recruit_number }}</p>
                        <p @click="cancelJoin(i.school_id)"><svg style="width: 30px;height: 30px;" t="1682820374879"
                                class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                                p-id="2590" width="200" height="200">
                                <path d="M872.802928 755.99406 872.864326 755.99406 872.864326 755.624646Z" fill="#f81f03"
                                    p-id="2591"></path>
                                <path
                                    d="M927.846568 511.997953c0-229.315756-186.567139-415.839917-415.838893-415.839917-229.329059 0-415.85322 186.524161-415.85322 415.839917 0 229.300406 186.524161 415.84094 415.85322 415.84094C741.278405 927.838893 927.846568 741.29836 927.846568 511.997953M512.007675 868.171955c-196.375529 0-356.172979-159.827125-356.172979-356.174002 0-196.374506 159.797449-356.157629 356.172979-356.157629 196.34483 0 356.144326 159.783123 356.144326 356.157629C868.152001 708.34483 708.352505 868.171955 512.007675 868.171955"
                                    fill="#f81f03" p-id="2592"></path>
                                <path
                                    d="M682.378947 642.227993 553.797453 513.264806 682.261267 386.229528c11.661597-11.514241 11.749602-30.332842 0.234337-41.995463-11.514241-11.676947-30.362518-11.765975-42.026162-0.222057L511.888971 471.195665 385.223107 344.130711c-11.602246-11.603269-30.393217-11.661597-42.025139-0.059352-11.603269 11.618619-11.603269 30.407544-0.059352 42.011836l126.518508 126.887922L342.137823 639.104863c-11.662621 11.543917-11.780301 30.305213-0.23536 41.96988 5.830799 5.89015 13.429871 8.833179 21.086248 8.833179 7.53972 0 15.136745-2.8847 20.910239-8.569166l127.695311-126.311801L640.293433 684.195827c5.802146 5.8001 13.428847 8.717546 21.056572 8.717546 7.599072 0 15.165398-2.917446 20.968567-8.659217C693.922864 672.681586 693.950494 653.889591 682.378947 642.227993"
                                    fill="#f81f03" p-id="2593"></path>
                            </svg></p>
                    </div>
                </li>
            </ul>
        </div>
    </el-dialog>
</template>

<script setup>
import { ref, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"
import chooseMajor from "@/components/chooseMajor.vue";
import hotSearch from "@/components/hotSearch.vue";
import requestFn from "@/api/requestFn.js";
import { useRouter, useRoute } from "vue-router";
import { ElMessage } from 'element-plus'


const isShow = ref(false)
const isShowDuibi = ref(false)
const router = useRouter()
const provinceActive = ref(null)
const form = reactive({
    score: '',
    scoreSchool: '',
    province_name: '',
    school_info: {}

})
const inputInfo = reactive({
    region: '',
    class: '',
    major_class1: '',
    major_class2: '',
    score: '',
    scoreSchool: '',
})
watch(form, () => {
    inputInfo.region = form.province_name,
        inputInfo.class = form.school_info.two_class,
        inputInfo.major_class1 = form.school_info.level1_name,
        inputInfo.major_class2 = form.school_info.level2_name,
        inputInfo.score = form.score,
        inputInfo.scoreSchool = form.scoreSchool
    
})

const gotoDetail = (e) => {
    router.push({
        // path:'/schoolDetail/'+e,
        path: '/schoolDetail/' + e + '/schoolView',
        params: {
            school_id: e,
        }
    })
}


const recommend_school = reactive({ item: [] })
const onsubmit = () => {
    recommend_school.item.length=0
    isShow.value = true
    const objvalue = Object.values(inputInfo)
    if (objvalue.filter(Boolean).length < 6) {
        isShow.value = false
        ElMessage.error('请输入完整信息！')
    } else {
        requestFn({
            url: '/recommend',
            method: 'post',
            data: {
                region: inputInfo.region,
                class: inputInfo.class,
                major_class1: inputInfo.major_class1,
                major_class2: inputInfo.major_class2,
                score: inputInfo.score,
                scoreSchool: inputInfo.scoreSchool
            }
        }).then(res => {
            if(res.data.msg){
                ElMessage.error(`目标院校没有--${inputInfo.major_class2}--这项专业`)
                isShow.value=false
            }else{
                recommend_school.item = res.data
            console.log(recommend_school)
            }

        })
    }


}


const handleChangeJilian = (e) => {
    form.scoreSchool = e['1']
}



const allRegin = reactive({ arr: [] })
onMounted(() => {
    requestFn({
        url: '/regin',
        method: 'get'
    }).then(data => {
        allRegin.arr = (eval("(" + data.data + ")"))
    })


})

const yourRegin = (v, k) => {
    provinceActive.value = k + 1
    form.province_name = v
}
const getChildVal = (e) => {
    form.school_info = e
}
const compareSchoolValue = ref(0)
const compareSchool = reactive({ item: [] })
const joinCompare = (e) => {
    if (compareSchool.item.includes(e)) {
        ElMessage.error('已经加入了!')
    } else {
        if (compareSchool.item.length < 5) {
            // isCunzai.value=false
            compareSchool.item.push(e)
            compareSchoolValue.value = compareSchool.item.length
            sessionStorage.setItem('joinCompare', compareSchool.item)
            isShowDuibi.value = true
        }
        else {
            ElMessage.error('最多添加5个!')
        }

    }
}


const cancelJoin = (id) => {
    const inx = compareSchool.item.indexOf(id)
    compareSchool.item.splice(inx, 1)
    sessionStorage.setItem('joinCompare', compareSchool.item)
    requestFn({
        url: '/showCompare',
        method: 'post',
        data: {
            compareSchool: compareSchool.item,
            major_name: inputInfo.major_class2
        }
    }).then(res => {
        console.log(res.data)
        compareSchoolList.item = res.data
    })
    compareSchoolValue.value = compareSchool.item.length
}

const dialogTableVisible = ref(false)
const compareSchoolList = reactive({ item: [] })
const zhankai = () => {
    dialogTableVisible.value = true
    requestFn({
        url: '/showCompare',
        method: 'post',
        data: {
            compareSchool: compareSchool.item,
            major_name: inputInfo.major_class2
        }
    }).then(res => {
        console.log(res.data)
        compareSchoolList.item = res.data
    })
}









let school_name_choose = [{ 'value': '北京', 'label': '北京', 'children': [{ 'value': '清华大学', 'label': '清华大学' }, { 'value': '中国地震局地球物理研究所', 'label': '中国地震局地球物理研究所' }, { 'value': '北京协和医学院', 'label': '北京协和医学院' }, { 'value': '应急管理部国家自然灾害防治研究院', 'label': '应急管理部国家自然灾害防治研究院' }, { 'value': '中国气象科学研究院', 'label': '中国气象科学研究院' }, { 'value': '中国地质科学院', 'label': '中国地质科学院' }, { 'value': '华北计算技术研究所（中电太极（集团）有限公司）', 'label': '华北计算技术研究所（中电太极（集团）有限公司）' }, { 'value': '中国原子能科学研究院', 'label': '中国原子能科学研究院' }, { 'value': '中国农业科学院', 'label': '中国农业科学院' }, { 'value': '北京交通大学', 'label': '北京交通大学' }, { 'value': '中国空间技术研究院（航天五院）', 'label': '中国空间技术研究院（航天五院）' }, { 'value': '中国建筑设计研究院', 'label': '中国建筑设计研究院' }, { 'value': '中国工程物理研究院', 'label': '中国工程物理研究院' }, { 'value': '北京工业大学', 'label': '北京工业大学' }, { 'value': '核工业北京地质研究院', 'label': '核工业北京地质研究院' }, { 'value': '中国水利水电科学研究院', 'label': '中国水利水电科学研究院' }, { 'value': '北京林业大学', 'label': '北京林业大学' }, { 'value': '中国青年政治学院', 'label': '中国青年政治学院' }, { 'value': '中国矿业大学（北京）', 'label': '中国矿业大学（北京）' }, { 'value': '钢铁研究总院', 'label': '钢铁研究总院' }, { 'value': '北京中医药大学', 'label': '北京中医药大学' }, { 'value': '中共北京市委党校', 'label': '中共北京市委党校' }, { 'value': '北京服装学院', 'label': '北京服装学院' }, { 'value': '外交学院', 'label': '外交学院' }, { 'value': '北京工商大学', 'label': '北京工商大学' }, { 'value': '北方工业大学', 'label': '北方工业大学' }, { 'value': '中共中央党校', 'label': '中共中央党校' }, { 'value': '国际关系学院', 'label': '国际关系学院' }, { 'value': '北京印刷学院', 'label': '北京印刷学院' }, { 'value': '中央民族大学', 'label': '中央民族大学' }, { 'value': '中国科学院电工研究所', 'label': '中国科学院电工研究所' }, { 'value': '北京邮电大学', 'label': '北京邮电大学' }, { 'value': '北京大学', 'label': '北京大学' }, { 'value': '陆军装甲兵学院', 'label': '陆军装甲兵学院' }, { 'value': '中国科学院大学', 'label': '中国科学院大学' }, { 'value': '北京师范大学', 'label': '北京师范大学' }, { 'value': '对外经济贸易大学', 'label': '对外经济贸易大学' }, { 'value': '北京外国语大学', 'label': '北京外国语大学' }, { 'value': '中国人民大学', 'label': '中国人民大学' }, { 'value': '北京航空航天大学', 'label': '北京航空航天大学' }, { 'value': '北京理工大学', 'label': '北京理工大学' }, { 'value': '中国政法大学', 'label': '中国政法大学' }, { 'value': '首都师范大学', 'label': '首都师范大学' }, { 'value': '中国农业大学', 'label': '中国农业大学' }, { 'value': '华北电力大学', 'label': '华北电力大学' }, { 'value': '北京体育大学', 'label': '北京体育大学' }, { 'value': '首都医科大学', 'label': '首都医科大学' }, { 'value': '中国人民公安大学', 'label': '中国人民公安大学' }, { 'value': '北京电影学院', 'label': '北京电影学院' }, { 'value': '中央戏剧学院', 'label': '中央戏剧学院' }, { 'value': '北京物资学院', 'label': '北京物资学院' }, { 'value': '煤炭科学研究总院', 'label': '煤炭科学研究总院' }, { 'value': '中国传媒大学', 'label': '中国传媒大学' }, { 'value': '中国地质大学（北京）', 'label': '中国地质大学（北京）' }, { 'value': '北京信息科技大学', 'label': '北京信息科技大学' }, { 'value': '北京科技大学', 'label': '北京科技大学' }, { 'value': '北京化工大学', 'label': '北京化工大学' }, { 'value': '北京建筑大学', 'label': '北京建筑大学' }, { 'value': '北京第二外国语学院', 'label': '北京第二外国语学院' }, { 'value': '北京语言大学', 'label': '北京语言大学' }, { 'value': '中央财经大学', 'label': '中央财经大学' }, { 'value': '中央音乐学院', 'label': '中央音乐学院' }, { 'value': '中央美术学院', 'label': '中央美术学院' }, { 'value': '中国戏曲学院', 'label': '中国戏曲学院' }, { 'value': '北京舞蹈学院', 'label': '北京舞蹈学院' }, { 'value': '首都经济贸易大学', 'label': '首都经济贸易大学' }, { 'value': '中国科学院数学与系统科学研究院', 'label': '中国科学院数学与系统科学研究院' }, { 'value': '中国科学院系统科学研究所', 'label': '中国科学院系统科学研究所' }, { 'value': '中国科学院北京力学研究所', 'label': '中国科学院北京力学研究所' }, { 'value': '中国科学院物理研究所', 'label': '中国科学院物理研究所' }, { 'value': '中国科学院高能物理研究所', 'label': '中国科学院高能物理研究所' }, { 'value': '中国科学院声学研究所', 'label': '中国科学院声学研究所' }, { 'value': '中国科学院理论物理研究所', 'label': '中国科学院理论物理研究所' }, { 'value': '中国科学院国家天文台', 'label': '中国科学院国家天文台' }, { 'value': '中国科学院北京自然科学史研究所', 'label': '中国科学院北京自然科学史研究所' }, { 'value': '中国科学院北京化学研究所', 'label': '中国科学院北京化学研究所' }, { 'value': '中国科学院生态环境研究中心', 'label': '中国科学院生态环境研究中心' }, { 'value': '中国科学院北京古脊椎动物与古人类研究所', 'label': '中国科学院北京古脊椎动物与古人类研究所' }, { 'value': '中国科学院地质与地球物理研究所', 'label': '中国科学院地质与地球物理研究所' }, { 'value': '中国科学院大气物理研究所', 'label': '中国科学院大气物理研究所' }, { 'value': '中国科学院北京地理科学与资源研究所', 'label': '中国科学院北京地理科学与资源研究所' }, { 'value': '中国科学院遥感应用研究所', 'label': '中国科学院遥感应用研究所' }, { 'value': '中国科学院地理科学与资源研究所', 'label': '中国科学院地理科学与资源研究所' }, { 'value': '中国科学院北京空间科学与应用研究中心', 'label': '中国科学院北京空间科学与应用研究中心' }, { 'value': '中国科学院遥感与数字地球研究所', 'label': '中国科学院遥感与数字地球研究所' }, { 'value': '中国科学院北京动物研究所', 'label': '中国科学院北京动物研究所' }, { 'value': '中国科学院植物研究所', 'label': '中国科学院植物研究所' }, { 'value': '冶金自动化研究设计院', 'label': '冶金自动化研究设计院' }, { 'value': '中国科学院生物物理研究所', 'label': '中国科学院生物物理研究所' }, { 'value': '中国科学院北京微生物研究所', 'label': '中国科学院北京微生物研究所' }, { 'value': '中国机械科学研究总院', 'label': '中国机械科学研究总院' }, { 'value': '北京机械工业自动化研究所', 'label': '北京机械工业自动化研究所' }, { 'value': '中国科学院遗传与发育生物学研究所', 'label': '中国科学院遗传与发育生物学研究所' }, { 'value': '北京机电研究所', 'label': '北京机电研究所' }, { 'value': '中国农业机械化科学研究院', 'label': '中国农业机械化科学研究院' }, { 'value': '核工业北京化工冶金研究院', 'label': '核工业北京化工冶金研究院' }, { 'value': '北京应用物理与计算数学研究所', 'label': '北京应用物理与计算数学研究所' }, { 'value': '中国航空研究院', 'label': '中国航空研究院' }, { 'value': '北京航空精密机械研究所', 'label': '北京航空精密机械研究所' }, { 'value': '中国科学院北京心理研究所', 'label': '中国科学院北京心理研究所' }, { 'value': '中国科学院计算技术研究所', 'label': '中国科学院计算技术研究所' }, { 'value': '中国科学院技术科学部（计算数学与科学工程研究所）', 'label': '中国科学院技术科学部（计算数学与科学工程研究所）' }, { 'value': '中国科学院工程热物理研究所', 'label': '中国科学院工程热物理研究所' }, { 'value': '中国科学院北京半导体研究所', 'label': '中国科学院北京半导体研究所' }, { 'value': '中国科学院北京电子学研究所', 'label': '中国科学院北京电子学研究所' }, { 'value': '中国科学院北京自动化研究所', 'label': '中国科学院北京自动化研究所' }, { 'value': '北京航空材料研究院', 'label': '北京航空材料研究院' }, { 'value': '中国航空制造技术研究院', 'label': '中国航空制造技术研究院' }, { 'value': '中国科学院北京软件研究所', 'label': '中国科学院北京软件研究所' }, { 'value': '中国航空规划设计研究总院有限公司', 'label': '中国航空规划设计研究总院有限公司' }, { 'value': '中国科学院北京文献情报中心', 'label': '中国科学院北京文献情报中心' }, { 'value': '中国科学院微电子研究所', 'label': '中国科学院微电子研究所' }, { 'value': '航空工业总公司第六二八研究所', 'label': '航空工业总公司第六二八研究所' }, { 'value': '北京长城计量测试技术研究所', 'label': '北京长城计量测试技术研究所' }, { 'value': '华北计算机系统工程研究所', 'label': '华北计算机系统工程研究所' }, { 'value': '北京真空电子技术研究所', 'label': '北京真空电子技术研究所' }, { 'value': '中国科学院科技政策与管理科学研究所', 'label': '中国科学院科技政策与管理科学研究所' }, { 'value': '中国社会科学院大学', 'label': '中国社会科学院大学' }, { 'value': '华北光电技术研究所', 'label': '华北光电技术研究所' }, { 'value': '中国现代国际关系研究院', 'label': '中国现代国际关系研究院' }, { 'value': '中国财政科学研究院', 'label': '中国财政科学研究院' }, { 'value': '中国人民银行金融研究所', 'label': '中国人民银行金融研究所' }, { 'value': '国际贸易经济合作研究院', 'label': '国际贸易经济合作研究院' }, { 'value': '中国北方车辆研究所', 'label': '中国北方车辆研究所' }, { 'value': '中国林业科学研究院', 'label': '中国林业科学研究院' }, { 'value': '中国电力科学研究院', 'label': '中国电力科学研究院' }, { 'value': '中国建筑科学研究院', 'label': '中国建筑科学研究院' }, { 'value': '中国城市规划设计研究院', 'label': '中国城市规划设计研究院' }, { 'value': '中国建筑技术研究院', 'label': '中国建筑技术研究院' }, { 'value': '中国环境科学研究院', 'label': '中国环境科学研究院' }, { 'value': '中冶集团建筑研究总院', 'label': '中冶集团建筑研究总院' }, { 'value': '北京橡胶工业研究设计院', 'label': '北京橡胶工业研究设计院' }, { 'value': '中国制浆造纸研究院', 'label': '中国制浆造纸研究院' }, { 'value': '中国铁道科学研究院', 'label': '中国铁道科学研究院' }, { 'value': '交通运输部公路科学研究所', 'label': '交通运输部公路科学研究所' }, { 'value': '中国艺术研究院', 'label': '中国艺术研究院' }, { 'value': '中国电影艺术研究中心', 'label': '中国电影艺术研究中心' }, { 'value': '中国疾病预防控制中心', 'label': '中国疾病预防控制中心' }, { 'value': '中国兵器科学研究院（生产工艺自动化研究所）', 'label': '中国兵器科学研究院（生产工艺自动化研究所）' }, { 'value': '中国中医科学院', 'label': '中国中医科学院' }, { 'value': '中国运载火箭技术研究院', 'label': '中国运载火箭技术研究院' }, { 'value': '中国航天工业总公司第一研究院（第一总体设计部）', 'label': '中国航天工业总公司第一研究院（第一总体设计部）' }, { 'value': '北京生物制品研究所', 'label': '北京生物制品研究所' }, { 'value': '中国航天工业总公司第一研究院（北京11所）', 'label': '中国航天工业总公司第一研究院（北京11所）' }, { 'value': '中国航天系统科学与工程研究院', 'label': '中国航天系统科学与工程研究院' }, { 'value': '中国航天工业总公司第一研究院（13所）', 'label': '中国航天工业总公司第一研究院（13所）' }, { 'value': '中国航天工业总公司第一研究院（14所）', 'label': '中国航天工业总公司第一研究院（14所）' }, { 'value': '中国航天工业总公司第一研究院（15所）', 'label': '中国航天工业总公司第一研究院（15所）' }, { 'value': '中国航天工业总公司第一研究院（702所）', 'label': '中国航天工业总公司第一研究院（702所）' }, { 'value': '中国航天工业总公司第一研究院（703所）', 'label': '中国航天工业总公司第一研究院（703所）' }, { 'value': '中国航天工业总公司第一研究院（704所）', 'label': '中国航天工业总公司第一研究院（704所）' }, { 'value': '中国航天工业总公司第一研究院（103所）', 'label': '中国航天工业总公司第一研究院（103所）' }, { 'value': '中日友好临床医学研究所', 'label': '中日友好临床医学研究所' }, { 'value': '中国航天工业总公司第一研究院（067基地、11所）', 'label': '中国航天工业总公司第一研究院（067基地、11所）' }, { 'value': '中国航天科工集团第二研究院', 'label': '中国航天科工集团第二研究院' }, { 'value': '中国航天工业总公司第二研究院（第二总体设计部）', 'label': '中国航天工业总公司第二研究院（第二总体设计部）' }, { 'value': '北京医院', 'label': '北京医院' }, { 'value': '中国建筑材料科学研究院', 'label': '中国建筑材料科学研究院' }, { 'value': '国家海洋环境预报研究中心', 'label': '国家海洋环境预报研究中心' }, { 'value': '中国计量科学研究院', 'label': '中国计量科学研究院' }, { 'value': '中国测绘科学研究院', 'label': '中国测绘科学研究院' }, { 'value': '中国舰船研究院', 'label': '中国舰船研究院' }, { 'value': '中国石化石油化工科学研究院', 'label': '中国石化石油化工科学研究院' }, { 'value': '北京矿冶研究总院', 'label': '北京矿冶研究总院' }, { 'value': '北京有色金属研究总院（有研科技集团有限公司）', 'label': '北京有色金属研究总院（有研科技集团有限公司）' }, { 'value': '北京市科学技术研究院城市安全与环境科学研究所', 'label': '北京市科学技术研究院城市安全与环境科学研究所' }, { 'value': '北京市生态环境保护科学研究院', 'label': '北京市生态环境保护科学研究院' }, { 'value': '北京市心肺血管疾病研究所', 'label': '北京市心肺血管疾病研究所' }, { 'value': '北京市市政工程研究院', 'label': '北京市市政工程研究院' }, { 'value': '北京市结核病胸部肿瘤研究所', 'label': '北京市结核病胸部肿瘤研究所' }, { 'value': '北京市创伤骨科研究所', 'label': '北京市创伤骨科研究所' }, { 'value': '北京市中医研究所', 'label': '北京市中医研究所' }, { 'value': '首都儿科研究所', 'label': '首都儿科研究所' }, { 'value': '中国中医药科技开发交流中心', 'label': '中国中医药科技开发交流中心' }, { 'value': '陆军防化学院', 'label': '陆军防化学院' }, { 'value': '空军指挥学院', 'label': '空军指挥学院' }, { 'value': '中国地震局地震预测研究所', 'label': '中国地震局地震预测研究所' }, { 'value': '中国地震局地质研究所', 'label': '中国地震局地质研究所' }, { 'value': '北京农学院', 'label': '北京农学院' }, { 'value': '中国航天科工集团第三研究院', 'label': '中国航天科工集团第三研究院' }, { 'value': '中国石油大学（北京）', 'label': '中国石油大学（北京）' }, { 'value': '中国科学院理化技术研究所', 'label': '中国科学院理化技术研究所' }, { 'value': '中国科学院过程工程研究所', 'label': '中国科学院过程工程研究所' }, { 'value': '首都体育学院', 'label': '首都体育学院' }, { 'value': '中国音乐学院', 'label': '中国音乐学院' }, { 'value': '北京联合大学', 'label': '北京联合大学' }, { 'value': '中国科学技术信息研究所', 'label': '中国科学技术信息研究所' }, { 'value': '国家纳米科学中心', 'label': '国家纳米科学中心' }, { 'value': '中国石油勘探开发研究院', 'label': '中国石油勘探开发研究院' }, { 'value': '北京化工研究院', 'label': '北京化工研究院' }, { 'value': '北京市科学技术研究院资源环境研究所', 'label': '北京市科学技术研究院资源环境研究所' }, { 'value': '中国食品发酵工业研究院', 'label': '中国食品发酵工业研究院' }, { 'value': '中国科学院北京基因组研究所（国家生物信息中心）', 'label': '中国科学院北京基因组研究所（国家生物信息中心）' }, { 'value': '中国科学院青藏高原研究所', 'label': '中国科学院青藏高原研究所' }, { 'value': '中国科学院兰州文献情报中心', 'label': '中国科学院兰州文献情报中心' }, { 'value': '中国科学院光电研究院（总部）', 'label': '中国科学院光电研究院（总部）' }, { 'value': '中国科学院研究生院信息科学与工程学院', 'label': '中国科学院研究生院信息科学与工程学院' }, { 'value': '解放军医学院', 'label': '解放军医学院' }, { 'value': '北京国家会计学院', 'label': '北京国家会计学院' }, { 'value': '国家行政学院', 'label': '国家行政学院' }, { 'value': '北京城市学院', 'label': '北京城市学院' }, { 'value': '北京石油化工学院', 'label': '北京石油化工学院' }, { 'value': '北京电子科技学院', 'label': '北京电子科技学院' }, { 'value': '中国食品药品检定研究院', 'label': '中国食品药品检定研究院' }, { 'value': '中国劳动关系学院', 'label': '中国劳动关系学院' }, { 'value': '中华女子学院', 'label': '中华女子学院' }, { 'value': '中国科学院微生物研究所', 'label': '中国科学院微生物研究所' }, { 'value': '中国科学院信息工程研究所', 'label': '中国科学院信息工程研究所' }, { 'value': '中国科学院空间应用工程与技术中心', 'label': '中国科学院空间应用工程与技术中心' }, { 'value': '中国科学院自然科学史研究所', 'label': '中国科学院自然科学史研究所' }, { 'value': '中国科学院化学研究所', 'label': '中国科学院化学研究所' }, { 'value': '中国科学院古脊椎动物与古人类研究所', 'label': '中国科学院古脊椎动物与古人类研究所' }, { 'value': '中国科学院国家空间科学中心', 'label': '中国科学院国家空间科学中心' }, { 'value': '中国科学院动物研究所', 'label': '中国科学院动物研究所' }, { 'value': '中国科学院心理研究所', 'label': '中国科学院心理研究所' }, { 'value': '中国科学院半导体研究所', 'label': '中国科学院半导体研究所' }, { 'value': '中国科学院自动化研究所', 'label': '中国科学院自动化研究所' }, { 'value': '中国科学院软件研究所', 'label': '中国科学院软件研究所' }, { 'value': '中国科学院文献情报中心', 'label': '中国科学院文献情报中心' }, { 'value': '中国科学院科技战略咨询研究院', 'label': '中国科学院科技战略咨询研究院' }, { 'value': '中国科学院杭州高等研究院', 'label': '中国科学院杭州高等研究院' }, { 'value': '中国电子科技集团公司信息科学研究院', 'label': '中国电子科技集团公司信息科学研究院' }] }, { 'value': '天津', 'label': '天津', 'children': [{ 'value': '天津理工大学', 'label': '天津理工大学' }, { 'value': '天津外国语大学', 'label': '天津外国语大学' }, { 'value': '河北工业大学', 'label': '河北工业大学' }, { 'value': '天津科技大学', 'label': '天津科技大学' }, { 'value': '天津工业大学', 'label': '天津工业大学' }, { 'value': '天津大学', 'label': '天津大学' }, { 'value': '南开大学', 'label': '南开大学' }, { 'value': '天津师范大学', 'label': '天津师范大学' }, { 'value': '天津医科大学', 'label': '天津医科大学' }, { 'value': '天津音乐学院', 'label': '天津音乐学院' }, { 'value': '中国民航大学', 'label': '中国民航大学' }, { 'value': '天津中医药大学', 'label': '天津中医药大学' }, { 'value': '天津财经大学', 'label': '天津财经大学' }, { 'value': '天津体育学院', 'label': '天津体育学院' }, { 'value': '天津城建大学', 'label': '天津城建大学' }, { 'value': '天津美术学院', 'label': '天津美术学院' }, { 'value': '中钢集团天津地质研究院有限公司', 'label': '中钢集团天津地质研究院有限公司' }, { 'value': '国家海洋技术中心', 'label': '国家海洋技术中心' }, { 'value': '天津航海仪器研究所', 'label': '天津航海仪器研究所' }, { 'value': '航天科工集团三院8357所', 'label': '航天科工集团三院8357所' }, { 'value': '航天科工集团三院8358所', 'label': '航天科工集团三院8358所' }, { 'value': '天津商业大学', 'label': '天津商业大学' }, { 'value': '陆军军事交通学院', 'label': '陆军军事交通学院' }, { 'value': '天津职业技术师范大学', 'label': '天津职业技术师范大学' }, { 'value': '天津农学院', 'label': '天津农学院' }, { 'value': '武警指挥学院', 'label': '武警指挥学院' }, { 'value': '武警后勤学院', 'label': '武警后勤学院' }, { 'value': '海军勤务学院', 'label': '海军勤务学院' }, { 'value': '中国科学院天津工业生物技术研究所', 'label': '中国科学院天津工业生物技术研究所' }] }, { 'value': '河北', 'label': '河北', 'children': [{ 'value': '燕山大学', 'label': '燕山大学' }, { 'value': '河北地质大学', 'label': '河北地质大学' }, { 'value': '河北大学', 'label': '河北大学' }, { 'value': '河北师范大学', 'label': '河北师范大学' }, { 'value': '石家庄铁道大学', 'label': '石家庄铁道大学' }, { 'value': '华北电力大学保定校区', 'label': '华北电力大学保定校区' }, { 'value': '河北农业大学', 'label': '河北农业大学' }, { 'value': '河北工程大学', 'label': '河北工程大学' }, { 'value': '华北理工大学', 'label': '华北理工大学' }, { 'value': '河北科技大学', 'label': '河北科技大学' }, { 'value': '河北医科大学', 'label': '河北医科大学' }, { 'value': '河北经贸大学', 'label': '河北经贸大学' }, { 'value': '中国科学院渗流流体力学研究所', 'label': '中国科学院渗流流体力学研究所' }, { 'value': '中国科学院遗传与发育生物学研究所农业资源研究中心', 'label': '中国科学院遗传与发育生物学研究所农业资源研究中心' }, { 'value': '石家庄通信测控技术研究所（54所）', 'label': '石家庄通信测控技术研究所（54所）' }, { 'value': '承德医学院', 'label': '承德医学院' }, { 'value': '河北北方学院', 'label': '河北北方学院' }, { 'value': '河北科技师范学院', 'label': '河北科技师范学院' }, { 'value': '中国人民警察大学', 'label': '中国人民警察大学' }, { 'value': '中国船舶集团有限公司第七一八研究所', 'label': '中国船舶集团有限公司第七一八研究所' }, { 'value': '陆军步兵学院', 'label': '陆军步兵学院' }, { 'value': '河北传媒学院', 'label': '河北传媒学院' }, { 'value': '北华航天工业学院', 'label': '北华航天工业学院' }, { 'value': '河北金融学院', 'label': '河北金融学院' }, { 'value': '防灾科技学院', 'label': '防灾科技学院' }, { 'value': '华北科技学院', 'label': '华北科技学院' }, { 'value': '中央司法警官学院', 'label': '中央司法警官学院' }, { 'value': '河北建筑工程学院', 'label': '河北建筑工程学院' }, { 'value': '河北中医学院', 'label': '河北中医学院' }] }, { 'value': '山西', 'label': '山西', 'children': [{ 'value': '太原科技大学', 'label': '太原科技大学' }, { 'value': '山西师范大学', 'label': '山西师范大学' }, { 'value': '太原理工大学', 'label': '太原理工大学' }, { 'value': '山西大学', 'label': '山西大学' }, { 'value': '山西财经大学', 'label': '山西财经大学' }, { 'value': '山西农业大学', 'label': '山西农业大学' }, { 'value': '中北大学', 'label': '中北大学' }, { 'value': '山西医科大学', 'label': '山西医科大学' }, { 'value': '中国科学院山西煤炭化学研究所', 'label': '中国科学院山西煤炭化学研究所' }, { 'value': '中国辐射防护研究院', 'label': '中国辐射防护研究院' }, { 'value': '中国北方自动控制技术研究所', 'label': '中国北方自动控制技术研究所' }, { 'value': '中国日用化学工业研究院', 'label': '中国日用化学工业研究院' }, { 'value': '山西省中医药研究院', 'label': '山西省中医药研究院' }, { 'value': '山西中医药大学', 'label': '山西中医药大学' }, { 'value': '长治医学院', 'label': '长治医学院' }, { 'value': '太原师范学院', 'label': '太原师范学院' }, { 'value': '山西大同大学', 'label': '山西大同大学' }] }, { 'value': '辽宁', 'label': '辽宁', 'children': [{ 'value': '中国刑事警察学院', 'label': '中国刑事警察学院' }, { 'value': '渤海大学', 'label': '渤海大学' }, { 'value': '辽宁师范大学', 'label': '辽宁师范大学' }, { 'value': '辽宁大学', 'label': '辽宁大学' }, { 'value': '大连理工大学', 'label': '大连理工大学' }, { 'value': '东北大学', 'label': '东北大学' }, { 'value': '大连海事大学', 'label': '大连海事大学' }, { 'value': '大连海洋大学', 'label': '大连海洋大学' }, { 'value': '东北财经大学', 'label': '东北财经大学' }, { 'value': '沈阳工业大学', 'label': '沈阳工业大学' }, { 'value': '辽宁工业大学', 'label': '辽宁工业大学' }, { 'value': '大连外国语大学', 'label': '大连外国语大学' }, { 'value': '大连交通大学', 'label': '大连交通大学' }, { 'value': '沈阳体育学院', 'label': '沈阳体育学院' }, { 'value': '鲁迅美术学院', 'label': '鲁迅美术学院' }, { 'value': '沈阳航空航天大学', 'label': '沈阳航空航天大学' }, { 'value': '辽宁工程技术大学', 'label': '辽宁工程技术大学' }, { 'value': '辽宁石油化工大学', 'label': '辽宁石油化工大学' }, { 'value': '沈阳化工大学', 'label': '沈阳化工大学' }, { 'value': '大连工业大学', 'label': '大连工业大学' }, { 'value': '沈阳农业大学', 'label': '沈阳农业大学' }, { 'value': '中国医科大学', 'label': '中国医科大学' }, { 'value': '锦州医科大学', 'label': '锦州医科大学' }, { 'value': '大连医科大学', 'label': '大连医科大学' }, { 'value': '辽宁中医药大学', 'label': '辽宁中医药大学' }, { 'value': '沈阳药科大学', 'label': '沈阳药科大学' }, { 'value': '沈阳音乐学院', 'label': '沈阳音乐学院' }, { 'value': '中国科学院大连化学物理研究所', 'label': '中国科学院大连化学物理研究所' }, { 'value': '中国科学院沈阳应用生态研究所', 'label': '中国科学院沈阳应用生态研究所' }, { 'value': '中国科学院沈阳计算技术研究所', 'label': '中国科学院沈阳计算技术研究所' }, { 'value': '中国科学院金属研究所', 'label': '中国科学院金属研究所' }, { 'value': '中国科学院沈阳自动化研究所', 'label': '中国科学院沈阳自动化研究所' }, { 'value': '沈阳铸造研究所', 'label': '沈阳铸造研究所' }, { 'value': '中国航空研究院601研究所', 'label': '中国航空研究院601研究所' }, { 'value': '中国航空研究院626所', 'label': '中国航空研究院626所' }, { 'value': '沈阳理工大学', 'label': '沈阳理工大学' }, { 'value': '辽宁科技大学', 'label': '辽宁科技大学' }, { 'value': '沈阳建筑大学', 'label': '沈阳建筑大学' }, { 'value': '沈阳师范大学', 'label': '沈阳师范大学' }, { 'value': '沈阳化工研究院', 'label': '沈阳化工研究院' }, { 'value': '沈阳大学', 'label': '沈阳大学' }, { 'value': '大连大学', 'label': '大连大学' }, { 'value': '大连测控技术研究所', 'label': '大连测控技术研究所' }, { 'value': '中共辽宁省委党校', 'label': '中共辽宁省委党校' }, { 'value': '中国航空研究院606研究所', 'label': '中国航空研究院606研究所' }, { 'value': '大连民族大学', 'label': '大连民族大学' }, { 'value': '沈阳工程学院', 'label': '沈阳工程学院' }, { 'value': '鞍山师范学院', 'label': '鞍山师范学院' }, { 'value': '沈阳医学院', 'label': '沈阳医学院' }] }, { 'value': '吉林', 'label': '吉林', 'children': [{ 'value': '长春工业大学', 'label': '长春工业大学' }, { 'value': '长春理工大学', 'label': '长春理工大学' }, { 'value': '东北电力大学', 'label': '东北电力大学' }, { 'value': '吉林大学', 'label': '吉林大学' }, { 'value': '东北师范大学', 'label': '东北师范大学' }, { 'value': '北华大学', 'label': '北华大学' }, { 'value': '延边大学', 'label': '延边大学' }, { 'value': '吉林农业大学', 'label': '吉林农业大学' }, { 'value': '长春中医药大学', 'label': '长春中医药大学' }, { 'value': '吉林师范大学', 'label': '吉林师范大学' }, { 'value': '吉林财经大学', 'label': '吉林财经大学' }, { 'value': '吉林艺术学院', 'label': '吉林艺术学院' }, { 'value': '中国科学院长春应用化学研究所', 'label': '中国科学院长春应用化学研究所' }, { 'value': '中国科学院长春光学精密机械与物理研究所', 'label': '中国科学院长春光学精密机械与物理研究所' }, { 'value': '吉林建筑大学', 'label': '吉林建筑大学' }, { 'value': '长春生物制品研究所', 'label': '长春生物制品研究所' }, { 'value': '中共吉林省委党校（吉林省行政学院）', 'label': '中共吉林省委党校（吉林省行政学院）' }, { 'value': '空军航空大学', 'label': '空军航空大学' }, { 'value': '长春师范大学', 'label': '长春师范大学' }, { 'value': '吉林体育学院', 'label': '吉林体育学院' }, { 'value': '中国科学院东北地理与农业生态研究所', 'label': '中国科学院东北地理与农业生态研究所' }, { 'value': '中国科学院国家天文台长春人造卫星观测站', 'label': '中国科学院国家天文台长春人造卫星观测站' }, { 'value': '吉林外国语大学', 'label': '吉林外国语大学' }, { 'value': '长春工程学院', 'label': '长春工程学院' }, { 'value': '吉林化工学院', 'label': '吉林化工学院' }, { 'value': '长春大学', 'label': '长春大学' }, { 'value': '吉林工程技术师范学院', 'label': '吉林工程技术师范学院' }] }, { 'value': '黑龙江', 'label': '黑龙江', 'children': [{ 'value': '黑龙江大学', 'label': '黑龙江大学' }, { 'value': '哈尔滨工程大学', 'label': '哈尔滨工程大学' }, { 'value': '东北林业大学', 'label': '东北林业大学' }, { 'value': '哈尔滨医科大学', 'label': '哈尔滨医科大学' }, { 'value': '哈尔滨工业大学', 'label': '哈尔滨工业大学' }, { 'value': '东北农业大学', 'label': '东北农业大学' }, { 'value': '佳木斯大学', 'label': '佳木斯大学' }, { 'value': '哈尔滨商业大学', 'label': '哈尔滨商业大学' }, { 'value': '黑龙江八一农垦大学', 'label': '黑龙江八一农垦大学' }, { 'value': '哈尔滨师范大学', 'label': '哈尔滨师范大学' }, { 'value': '哈尔滨理工大学', 'label': '哈尔滨理工大学' }, { 'value': '东北石油大学', 'label': '东北石油大学' }, { 'value': '齐齐哈尔大学', 'label': '齐齐哈尔大学' }, { 'value': '黑龙江中医药大学', 'label': '黑龙江中医药大学' }, { 'value': '中国航空工业空气动力研究院', 'label': '中国航空工业空气动力研究院' }, { 'value': '哈尔滨船舶锅炉涡轮机研究所', 'label': '哈尔滨船舶锅炉涡轮机研究所' }, { 'value': '黑龙江省中医药科学院', 'label': '黑龙江省中医药科学院' }, { 'value': '黑龙江省社会科学院', 'label': '黑龙江省社会科学院' }, { 'value': '黑龙江省科学院', 'label': '黑龙江省科学院' }, { 'value': '中共黑龙江省委党校', 'label': '中共黑龙江省委党校' }, { 'value': '机械科学研究院哈尔滨焊接研究所', 'label': '机械科学研究院哈尔滨焊接研究所' }, { 'value': '中国地震局工程力学研究所', 'label': '中国地震局工程力学研究所' }, { 'value': '黑龙江科技大学', 'label': '黑龙江科技大学' }, { 'value': '牡丹江师范学院', 'label': '牡丹江师范学院' }, { 'value': '哈尔滨体育学院', 'label': '哈尔滨体育学院' }, { 'value': '黑龙江东方学院', 'label': '黑龙江东方学院' }, { 'value': '牡丹江医学院', 'label': '牡丹江医学院' }, { 'value': '哈尔滨音乐学院', 'label': '哈尔滨音乐学院' }, { 'value': '齐齐哈尔医学院', 'label': '齐齐哈尔医学院' }, { 'value': '黑龙江工程学院', 'label': '黑龙江工程学院' }] }, { 'value': '上海', 'label': '上海', 'children': [{ 'value': '上海海事大学', 'label': '上海海事大学' }, { 'value': '上海理工大学', 'label': '上海理工大学' }, { 'value': '上海海洋大学', 'label': '上海海洋大学' }, { 'value': '东华大学', 'label': '东华大学' }, { 'value': '上海大学', 'label': '上海大学' }, { 'value': '复旦大学', 'label': '复旦大学' }, { 'value': '同济大学', 'label': '同济大学' }, { 'value': '华东理工大学', 'label': '华东理工大学' }, { 'value': '华东师范大学', 'label': '华东师范大学' }, { 'value': '上海财经大学', 'label': '上海财经大学' }, { 'value': '上海交通大学', 'label': '上海交通大学' }, { 'value': '上海师范大学', 'label': '上海师范大学' }, { 'value': '上海外国语大学', 'label': '上海外国语大学' }, { 'value': '华东政法大学', 'label': '华东政法大学' }, { 'value': '海军军医大学', 'label': '海军军医大学' }, { 'value': '上海音乐学院', 'label': '上海音乐学院' }, { 'value': '上海体育学院', 'label': '上海体育学院' }, { 'value': '上海戏剧学院', 'label': '上海戏剧学院' }, { 'value': '上海对外经贸大学', 'label': '上海对外经贸大学' }, { 'value': '上海中医药大学', 'label': '上海中医药大学' }, { 'value': '中国科学院上海天文台', 'label': '中国科学院上海天文台' }, { 'value': '中国科学院上海有机化学研究所', 'label': '中国科学院上海有机化学研究所' }, { 'value': '中国科学院上海硅酸盐研究所', 'label': '中国科学院上海硅酸盐研究所' }, { 'value': '中国科学院分子植物科学卓越创新中心', 'label': '中国科学院分子植物科学卓越创新中心' }, { 'value': '中国科学院分子细胞科学卓越创新中心', 'label': '中国科学院分子细胞科学卓越创新中心' }, { 'value': '中国科学院上海药物研究所', 'label': '中国科学院上海药物研究所' }, { 'value': '上海材料研究所', 'label': '上海材料研究所' }, { 'value': '上海发电设备成套设计研究院', 'label': '上海发电设备成套设计研究院' }, { 'value': '上海核工程研究设计院', 'label': '上海核工程研究设计院' }, { 'value': '中国科学院上海光学精密机械研究所', 'label': '中国科学院上海光学精密机械研究所' }, { 'value': '中国科学院上海技术物理研究所', 'label': '中国科学院上海技术物理研究所' }, { 'value': '上海生物制品研究所', 'label': '上海生物制品研究所' }, { 'value': '上海市计算技术研究所', 'label': '上海市计算技术研究所' }, { 'value': '上海国际问题研究院', 'label': '上海国际问题研究院' }, { 'value': '上海社会科学院', 'label': '上海社会科学院' }, { 'value': '中共上海市委党校', 'label': '中共上海市委党校' }, { 'value': '中国科学院上海微系统与信息技术研究所', 'label': '中国科学院上海微系统与信息技术研究所' }, { 'value': '中国航空研究院640所', 'label': '中国航空研究院640所' }, { 'value': '上海航天技术研究院', 'label': '上海航天技术研究院' }, { 'value': '上海化工研究院', 'label': '上海化工研究院' }, { 'value': '上海船舶运输科学研究所', 'label': '上海船舶运输科学研究所' }, { 'value': '电信科学技术第一研究所（上海）', 'label': '电信科学技术第一研究所（上海）' }, { 'value': '中国医药工业研究总院', 'label': '中国医药工业研究总院' }, { 'value': '中国船舶工业集团公司第七○八研究所（中国船舶及海洋工程设计研究院）', 'label': '中国船舶工业集团公司第七○八研究所（中国船舶及海洋工程设计研究院）' }, { 'value': '上海船舶设备研究所', 'label': '上海船舶设备研究所' }, { 'value': '上海船用柴油机研究所', 'label': '上海船用柴油机研究所' }, { 'value': '上海船舶电子设备研究所（七二六研究所）', 'label': '上海船舶电子设备研究所（七二六研究所）' }, { 'value': '中国科学院上海应用物理研究所', 'label': '中国科学院上海应用物理研究所' }, { 'value': '上海电力大学', 'label': '上海电力大学' }, { 'value': '上海工程技术大学', 'label': '上海工程技术大学' }, { 'value': '上海应用技术大学', 'label': '上海应用技术大学' }, { 'value': '上海国家会计学院', 'label': '上海国家会计学院' }, { 'value': '上海政法学院', 'label': '上海政法学院' }, { 'value': '上海立信会计金融学院', 'label': '上海立信会计金融学院' }, { 'value': '上海电机学院', 'label': '上海电机学院' }, { 'value': '上海第二工业大学', 'label': '上海第二工业大学' }, { 'value': '上海海关学院', 'label': '上海海关学院' }, { 'value': '上海科技大学', 'label': '上海科技大学' }, { 'value': '中国科学院上海高等研究院', 'label': '中国科学院上海高等研究院' }, { 'value': '上海健康医学院', 'label': '上海健康医学院' }, { 'value': '上海商学院', 'label': '上海商学院' }, { 'value': '中国科学院上海巴斯德研究所', 'label': '中国科学院上海巴斯德研究所' }, { 'value': '中国科学院脑科学与智能技术卓越创新中心', 'label': '中国科学院脑科学与智能技术卓越创新中心' }, { 'value': '中国科学院微小卫星创新研究院', 'label': '中国科学院微小卫星创新研究院' }, { 'value': '华东计算技术研究所', 'label': '华东计算技术研究所' }] }, { 'value': '江苏', 'label': '江苏', 'children': [{ 'value': '常州大学', 'label': '常州大学' }, { 'value': '陆军工程大学', 'label': '陆军工程大学' }, { 'value': '南京农业大学', 'label': '南京农业大学' }, { 'value': '南京大学', 'label': '南京大学' }, { 'value': '河海大学', 'label': '河海大学' }, { 'value': '南京艺术学院', 'label': '南京艺术学院' }, { 'value': '南京工业大学', 'label': '南京工业大学' }, { 'value': '南京财经大学', 'label': '南京财经大学' }, { 'value': '南京中医药大学', 'label': '南京中医药大学' }, { 'value': '扬州大学', 'label': '扬州大学' }, { 'value': '南京林业大学', 'label': '南京林业大学' }, { 'value': '南京航空航天大学', 'label': '南京航空航天大学' }, { 'value': '江苏大学', 'label': '江苏大学' }, { 'value': '南京医科大学', 'label': '南京医科大学' }, { 'value': '南京邮电大学', 'label': '南京邮电大学' }, { 'value': '南京理工大学', 'label': '南京理工大学' }, { 'value': '苏州大学', 'label': '苏州大学' }, { 'value': '江苏师范大学', 'label': '江苏师范大学' }, { 'value': '东南大学', 'label': '东南大学' }, { 'value': '江南大学', 'label': '江南大学' }, { 'value': '苏州科技大学', 'label': '苏州科技大学' }, { 'value': '南通大学', 'label': '南通大学' }, { 'value': '江苏科技大学', 'label': '江苏科技大学' }, { 'value': '中国矿业大学', 'label': '中国矿业大学' }, { 'value': '南京信息工程大学', 'label': '南京信息工程大学' }, { 'value': '徐州医科大学', 'label': '徐州医科大学' }, { 'value': '中国药科大学', 'label': '中国药科大学' }, { 'value': '南京体育学院', 'label': '南京体育学院' }, { 'value': '中国科学院紫金山天文台', 'label': '中国科学院紫金山天文台' }, { 'value': '中国科学院南京地质古生物研究所', 'label': '中国科学院南京地质古生物研究所' }, { 'value': '中国科学院南京地理与湖泊研究所', 'label': '中国科学院南京地理与湖泊研究所' }, { 'value': '中国科学院南京土壤研究所', 'label': '中国科学院南京土壤研究所' }, { 'value': '中国航空研究院609研究所', 'label': '中国航空研究院609研究所' }, { 'value': '中国科学院南京天文仪器研制中心', 'label': '中国科学院南京天文仪器研制中心' }, { 'value': '南京电子器件研究所', 'label': '南京电子器件研究所' }, { 'value': '国网电力科学研究院', 'label': '国网电力科学研究院' }, { 'value': '南京水利科学研究院', 'label': '南京水利科学研究院' }, { 'value': '中国船舶科学研究中心（即702所）', 'label': '中国船舶科学研究中心（即702所）' }, { 'value': '江苏自动化研究所', 'label': '江苏自动化研究所' }, { 'value': '江苏省植物研究所', 'label': '江苏省植物研究所' }, { 'value': '江苏省血吸虫病防治研究所', 'label': '江苏省血吸虫病防治研究所' }, { 'value': '南京电子技术研究所', 'label': '南京电子技术研究所' }, { 'value': '海军指挥学院', 'label': '海军指挥学院' }, { 'value': '中共江苏省委党校', 'label': '中共江苏省委党校' }, { 'value': '空军勤务学院', 'label': '空军勤务学院' }, { 'value': '中国科学院南京天文光学技术研究所', 'label': '中国科学院南京天文光学技术研究所' }, { 'value': '南京师范大学', 'label': '南京师范大学' }, { 'value': '淮阴工学院', 'label': '淮阴工学院' }, { 'value': '南京审计大学', 'label': '南京审计大学' }, { 'value': '江苏理工学院', 'label': '江苏理工学院' }, { 'value': '南京工程学院', 'label': '南京工程学院' }, { 'value': '江苏海洋大学', 'label': '江苏海洋大学' }, { 'value': '盐城工学院', 'label': '盐城工学院' }, { 'value': '江苏警官学院', 'label': '江苏警官学院' }, { 'value': '西交利物浦大学', 'label': '西交利物浦大学' }, { 'value': '中国科学院苏州纳米技术与纳米仿生研究所', 'label': '中国科学院苏州纳米技术与纳米仿生研究所' }, { 'value': '中国科学院苏州生物医学工程技术研究所', 'label': '中国科学院苏州生物医学工程技术研究所' }] }, { 'value': '浙江', 'label': '浙江', 'children': [{ 'value': '浙江财经大学', 'label': '浙江财经大学' }, { 'value': '温州医科大学', 'label': '温州医科大学' }, { 'value': '中国计量大学', 'label': '中国计量大学' }, { 'value': '杭州师范大学', 'label': '杭州师范大学' }, { 'value': '浙江工业大学', 'label': '浙江工业大学' }, { 'value': '温州大学', 'label': '温州大学' }, { 'value': '宁波大学', 'label': '宁波大学' }, { 'value': '浙江师范大学', 'label': '浙江师范大学' }, { 'value': '浙江大学', 'label': '浙江大学' }, { 'value': '杭州电子科技大学', 'label': '杭州电子科技大学' }, { 'value': '浙江理工大学', 'label': '浙江理工大学' }, { 'value': '浙江中医药大学', 'label': '浙江中医药大学' }, { 'value': '浙江工商大学', 'label': '浙江工商大学' }, { 'value': '中国美术学院', 'label': '中国美术学院' }, { 'value': '自然资源部第二海洋研究所', 'label': '自然资源部第二海洋研究所' }, { 'value': '杭州医学院', 'label': '杭州医学院' }, { 'value': '中共浙江省委党校', 'label': '中共浙江省委党校' }, { 'value': '浙江海洋大学', 'label': '浙江海洋大学' }, { 'value': '浙江农林大学', 'label': '浙江农林大学' }, { 'value': '杭州应用声学研究所', 'label': '杭州应用声学研究所' }, { 'value': '中国科学院宁波材料技术与工程研究所', 'label': '中国科学院宁波材料技术与工程研究所' }, { 'value': '宁波诺丁汉大学', 'label': '宁波诺丁汉大学' }, { 'value': '浙江万里学院', 'label': '浙江万里学院' }, { 'value': '湖州师范学院', 'label': '湖州师范学院' }, { 'value': '浙江传媒学院', 'label': '浙江传媒学院' }, { 'value': '绍兴文理学院', 'label': '绍兴文理学院' }, { 'value': '浙江科技学院', 'label': '浙江科技学院' }, { 'value': '温州肯恩大学', 'label': '温州肯恩大学' }, { 'value': '西湖大学', 'label': '西湖大学' }, { 'value': '台州学院', 'label': '台州学院' }, { 'value': '嘉兴学院', 'label': '嘉兴学院' }, { 'value': '宁波工程学院', 'label': '宁波工程学院' }, { 'value': '浙江警察学院', 'label': '浙江警察学院' }, { 'value': '浙大城市学院', 'label': '浙大城市学院' }, { 'value': '丽水学院', 'label': '丽水学院' }, { 'value': '浙江音乐学院', 'label': '浙江音乐学院' }] }, { 'value': '安徽', 'label': '安徽', 'children': [{ 'value': '安徽理工大学', 'label': '安徽理工大学' }, { 'value': '安徽大学', 'label': '安徽大学' }, { 'value': '合肥工业大学', 'label': '合肥工业大学' }, { 'value': '中国科学技术大学', 'label': '中国科学技术大学' }, { 'value': '安徽师范大学', 'label': '安徽师范大学' }, { 'value': '安徽工业大学', 'label': '安徽工业大学' }, { 'value': '皖南医学院', 'label': '皖南医学院' }, { 'value': '蚌埠医学院', 'label': '蚌埠医学院' }, { 'value': '安徽财经大学', 'label': '安徽财经大学' }, { 'value': '安徽农业大学', 'label': '安徽农业大学' }, { 'value': '安徽医科大学', 'label': '安徽医科大学' }, { 'value': '安徽中医药大学', 'label': '安徽中医药大学' }, { 'value': '中国科学院等离子体物理研究所', 'label': '中国科学院等离子体物理研究所' }, { 'value': '中国科学院安徽光学精密机械研究所', 'label': '中国科学院安徽光学精密机械研究所' }, { 'value': '中钢集团马鞍山矿山研究院', 'label': '中钢集团马鞍山矿山研究院' }, { 'value': '陆军炮兵防空兵学院', 'label': '陆军炮兵防空兵学院' }, { 'value': '安徽工程大学', 'label': '安徽工程大学' }, { 'value': '安庆师范大学', 'label': '安庆师范大学' }, { 'value': '淮北师范大学', 'label': '淮北师范大学' }, { 'value': '安徽建筑大学', 'label': '安徽建筑大学' }, { 'value': '中国科学院合肥物质科学研究院', 'label': '中国科学院合肥物质科学研究院' }, { 'value': '中国科学院合肥物质科学研究院固体物理研究所', 'label': '中国科学院合肥物质科学研究院固体物理研究所' }, { 'value': '合肥学院', 'label': '合肥学院' }, { 'value': '合肥师范学院', 'label': '合肥师范学院' }, { 'value': '安徽科技学院', 'label': '安徽科技学院' }, { 'value': '阜阳师范大学', 'label': '阜阳师范大学' }] }, { 'value': '福建', 'label': '福建', 'children': [{ 'value': '集美大学', 'label': '集美大学' }, { 'value': '华侨大学', 'label': '华侨大学' }, { 'value': '闽南师范大学', 'label': '闽南师范大学' }, { 'value': '厦门大学', 'label': '厦门大学' }, { 'value': '福建师范大学', 'label': '福建师范大学' }, { 'value': '福州大学', 'label': '福州大学' }, { 'value': '福建医科大学', 'label': '福建医科大学' }, { 'value': '福建中医药大学', 'label': '福建中医药大学' }, { 'value': '福建农林大学', 'label': '福建农林大学' }, { 'value': '中国科学院福建物质结构研究所', 'label': '中国科学院福建物质结构研究所' }, { 'value': '自然资源部第三海洋研究所', 'label': '自然资源部第三海洋研究所' }, { 'value': '厦门国家会计学院', 'label': '厦门国家会计学院' }, { 'value': '闽江学院', 'label': '闽江学院' }, { 'value': '厦门理工学院', 'label': '厦门理工学院' }, { 'value': '泉州师范学院', 'label': '泉州师范学院' }, { 'value': '福建工程学院', 'label': '福建工程学院' }, { 'value': '中国科学院城市环境研究所', 'label': '中国科学院城市环境研究所' }, { 'value': '莆田学院', 'label': '莆田学院' }] }, { 'value': '江西', 'label': '江西', 'children': [{ 'value': '江西中医药大学', 'label': '江西中医药大学' }, { 'value': '江西财经大学', 'label': '江西财经大学' }, { 'value': '江西农业大学', 'label': '江西农业大学' }, { 'value': '南昌大学', 'label': '南昌大学' }, { 'value': '华东交通大学', 'label': '华东交通大学' }, { 'value': '南昌航空大学', 'label': '南昌航空大学' }, { 'value': '江西理工大学', 'label': '江西理工大学' }, { 'value': '景德镇陶瓷大学', 'label': '景德镇陶瓷大学' }, { 'value': '江西师范大学', 'label': '江西师范大学' }, { 'value': '中国航空研究院602研究所', 'label': '中国航空研究院602研究所' }, { 'value': '东华理工大学', 'label': '东华理工大学' }, { 'value': '赣南师范大学', 'label': '赣南师范大学' }, { 'value': '江西科技师范大学', 'label': '江西科技师范大学' }, { 'value': '井冈山大学', 'label': '井冈山大学' }, { 'value': '南昌工程学院', 'label': '南昌工程学院' }, { 'value': '宜春学院', 'label': '宜春学院' }, { 'value': '赣南医学院', 'label': '赣南医学院' }] }, { 'value': '山东', 'label': '山东', 'children': [{ 'value': '山东理工大学', 'label': '山东理工大学' }, { 'value': '青岛农业大学', 'label': '青岛农业大学' }, { 'value': '山东大学', 'label': '山东大学' }, { 'value': '山东师范大学', 'label': '山东师范大学' }, { 'value': '山东农业大学', 'label': '山东农业大学' }, { 'value': '山东中医药大学', 'label': '山东中医药大学' }, { 'value': '济南大学', 'label': '济南大学' }, { 'value': '烟台大学', 'label': '烟台大学' }, { 'value': '山东建筑大学', 'label': '山东建筑大学' }, { 'value': '青岛科技大学', 'label': '青岛科技大学' }, { 'value': '鲁东大学', 'label': '鲁东大学' }, { 'value': '聊城大学', 'label': '聊城大学' }, { 'value': '曲阜师范大学', 'label': '曲阜师范大学' }, { 'value': '山东第一医科大学', 'label': '山东第一医科大学' }, { 'value': '齐鲁工业大学', 'label': '齐鲁工业大学' }, { 'value': '中国石油大学（华东）', 'label': '中国石油大学（华东）' }, { 'value': '青岛大学', 'label': '青岛大学' }, { 'value': '中国海洋大学', 'label': '中国海洋大学' }, { 'value': '山东科技大学', 'label': '山东科技大学' }, { 'value': '青岛理工大学', 'label': '青岛理工大学' }, { 'value': '潍坊医学院', 'label': '潍坊医学院' }, { 'value': '山东艺术学院', 'label': '山东艺术学院' }, { 'value': '国家海洋局第一海洋研究所', 'label': '国家海洋局第一海洋研究所' }, { 'value': '海军潜艇学院', 'label': '海军潜艇学院' }, { 'value': '滨州医学院', 'label': '滨州医学院' }, { 'value': '中国科学院海洋研究所', 'label': '中国科学院海洋研究所' }, { 'value': '山东非金属材料研究所', 'label': '山东非金属材料研究所' }, { 'value': '中共山东省委党校（山东行政学院）', 'label': '中共山东省委党校（山东行政学院）' }, { 'value': '山东体育学院', 'label': '山东体育学院' }, { 'value': '山东工艺美术学院', 'label': '山东工艺美术学院' }, { 'value': '山东财经大学', 'label': '山东财经大学' }, { 'value': '山东交通学院', 'label': '山东交通学院' }, { 'value': '济宁医学院', 'label': '济宁医学院' }, { 'value': '山东政法学院', 'label': '山东政法学院' }, { 'value': '山东工商学院', 'label': '山东工商学院' }, { 'value': '海军航空大学', 'label': '海军航空大学' }, { 'value': '临沂大学', 'label': '临沂大学' }, { 'value': '山东产业技术研究院', 'label': '山东产业技术研究院' }, { 'value': '中国科学院青岛生物能源与过程研究所', 'label': '中国科学院青岛生物能源与过程研究所' }, { 'value': '滨州学院', 'label': '滨州学院' }, { 'value': '自然资源部第一海洋研究所', 'label': '自然资源部第一海洋研究所' }, { 'value': '中国科学院烟台海岸带研究所', 'label': '中国科学院烟台海岸带研究所' }] }, { 'value': '河南', 'label': '河南', 'children': [{ 'value': '河南理工大学', 'label': '河南理工大学' }, { 'value': '郑州大学', 'label': '郑州大学' }, { 'value': '河南中医药大学', 'label': '河南中医药大学' }, { 'value': '信阳师范学院', 'label': '信阳师范学院' }, { 'value': '郑州轻工业大学', 'label': '郑州轻工业大学' }, { 'value': '河南大学', 'label': '河南大学' }, { 'value': '中原工学院', 'label': '中原工学院' }, { 'value': '河南师范大学', 'label': '河南师范大学' }, { 'value': '华北水利水电大学', 'label': '华北水利水电大学' }, { 'value': '河南财经政法大学', 'label': '河南财经政法大学' }, { 'value': '河南农业大学', 'label': '河南农业大学' }, { 'value': '新乡医学院', 'label': '新乡医学院' }, { 'value': '河南科技大学', 'label': '河南科技大学' }, { 'value': '河南工业大学', 'label': '河南工业大学' }, { 'value': '中钢集团洛阳耐火材料研究院', 'label': '中钢集团洛阳耐火材料研究院' }, { 'value': '郑州机械研究所', 'label': '郑州机械研究所' }, { 'value': '中国电波传播研究所', 'label': '中国电波传播研究所' }, { 'value': '中国航空工业第613研究所', 'label': '中国航空工业第613研究所' }, { 'value': '郑州烟草研究院', 'label': '郑州烟草研究院' }, { 'value': '河南科技学院', 'label': '河南科技学院' }, { 'value': '中国空空导弹研究院', 'label': '中国空空导弹研究院' }, { 'value': '郑州机电工程研究所', 'label': '郑州机电工程研究所' }, { 'value': '南阳师范学院', 'label': '南阳师范学院' }, { 'value': '安阳师范学院', 'label': '安阳师范学院' }, { 'value': '洛阳师范学院', 'label': '洛阳师范学院' }, { 'value': '郑州航空工业管理学院', 'label': '郑州航空工业管理学院' }, { 'value': '中国人民解放军战略支援部队信息工程大学', 'label': '中国人民解放军战略支援部队信息工程大学' }] }, { 'value': '湖北', 'label': '湖北', 'children': [{ 'value': '湖北大学', 'label': '湖北大学' }, { 'value': '武汉大学', 'label': '武汉大学' }, { 'value': '三峡大学', 'label': '三峡大学' }, { 'value': '华中科技大学', 'label': '华中科技大学' }, { 'value': '空军预警学院', 'label': '空军预警学院' }, { 'value': '海军工程大学', 'label': '海军工程大学' }, { 'value': '武汉体育学院', 'label': '武汉体育学院' }, { 'value': '武汉工程大学', 'label': '武汉工程大学' }, { 'value': '湖北工业大学', 'label': '湖北工业大学' }, { 'value': '华中农业大学', 'label': '华中农业大学' }, { 'value': '中南财经政法大学', 'label': '中南财经政法大学' }, { 'value': '武汉科技大学', 'label': '武汉科技大学' }, { 'value': '中国地质大学（武汉）', 'label': '中国地质大学（武汉）' }, { 'value': '湖北中医药大学', 'label': '湖北中医药大学' }, { 'value': '武汉理工大学', 'label': '武汉理工大学' }, { 'value': '武汉纺织大学', 'label': '武汉纺织大学' }, { 'value': '长江大学', 'label': '长江大学' }, { 'value': '华中师范大学', 'label': '华中师范大学' }, { 'value': '中南民族大学', 'label': '中南民族大学' }, { 'value': '武汉音乐学院', 'label': '武汉音乐学院' }, { 'value': '湖北美术学院', 'label': '湖北美术学院' }, { 'value': '湖北汽车工业学院', 'label': '湖北汽车工业学院' }, { 'value': '中国科学院武汉岩土力学研究所', 'label': '中国科学院武汉岩土力学研究所' }, { 'value': '中国科学院武汉物理与数学研究所', 'label': '中国科学院武汉物理与数学研究所' }, { 'value': '中国科学院测量与地球物理研究所', 'label': '中国科学院测量与地球物理研究所' }, { 'value': '中国科学院武汉植物园', 'label': '中国科学院武汉植物园' }, { 'value': '中钢集团武汉安全环保研究院', 'label': '中钢集团武汉安全环保研究院' }, { 'value': '中国科学院水生生物研究所', 'label': '中国科学院水生生物研究所' }, { 'value': '中国科学院武汉病毒研究所', 'label': '中国科学院武汉病毒研究所' }, { 'value': '武汉材料保护研究所', 'label': '武汉材料保护研究所' }, { 'value': '长江科学院', 'label': '长江科学院' }, { 'value': '武汉邮电科学研究院', 'label': '武汉邮电科学研究院' }, { 'value': '武汉生物制品研究所', 'label': '武汉生物制品研究所' }, { 'value': '湖北师范大学', 'label': '湖北师范大学' }, { 'value': '湖北民族大学', 'label': '湖北民族大学' }, { 'value': '中国地震局地震研究所', 'label': '中国地震局地震研究所' }, { 'value': '中国舰船研究设计中心（701所）', 'label': '中国舰船研究设计中心（701所）' }, { 'value': '湖北省社会科学院', 'label': '湖北省社会科学院' }, { 'value': '江汉大学', 'label': '江汉大学' }, { 'value': '武汉轻工大学', 'label': '武汉轻工大学' }, { 'value': '中国航空研究院610所', 'label': '中国航空研究院610所' }, { 'value': '武汉数字工程研究所', 'label': '武汉数字工程研究所' }, { 'value': '武汉船用电力推进装置研究所', 'label': '武汉船用电力推进装置研究所' }, { 'value': '华中光电技术研究所', 'label': '华中光电技术研究所' }, { 'value': '武汉船舶通信研究所', 'label': '武汉船舶通信研究所' }, { 'value': '武汉第二船舶设计研究所', 'label': '武汉第二船舶设计研究所' }, { 'value': '中共湖北省委党校', 'label': '中共湖北省委党校' }, { 'value': '黄冈师范学院', 'label': '黄冈师范学院' }, { 'value': '湖北经济学院', 'label': '湖北经济学院' }, { 'value': '湖北科技学院', 'label': '湖北科技学院' }, { 'value': '湖北医药学院', 'label': '湖北医药学院' }, { 'value': '湖北文理学院', 'label': '湖北文理学院' }, { 'value': '中国科学院精密测量科学与技术创新研究院', 'label': '中国科学院精密测量科学与技术创新研究院' }, { 'value': '中国航天科技集团第四研究院第四十二所', 'label': '中国航天科技集团第四研究院第四十二所' }] }, { 'value': '湖南', 'label': '湖南', 'children': [{ 'value': '湖南科技大学', 'label': '湖南科技大学' }, { 'value': '南华大学', 'label': '南华大学' }, { 'value': '中南大学', 'label': '中南大学' }, { 'value': '吉首大学', 'label': '吉首大学' }, { 'value': '湖南工业大学', 'label': '湖南工业大学' }, { 'value': '湖南师范大学', 'label': '湖南师范大学' }, { 'value': '湖南大学', 'label': '湖南大学' }, { 'value': '长沙理工大学', 'label': '长沙理工大学' }, { 'value': '中国人民解放军国防科技大学', 'label': '中国人民解放军国防科技大学' }, { 'value': '湘潭大学', 'label': '湘潭大学' }, { 'value': '湖南工程学院', 'label': '湖南工程学院' }, { 'value': '湖南农业大学', 'label': '湖南农业大学' }, { 'value': '中南林业科技大学', 'label': '中南林业科技大学' }, { 'value': '湖南中医药大学', 'label': '湖南中医药大学' }, { 'value': '长沙矿冶研究院', 'label': '长沙矿冶研究院' }, { 'value': '长沙矿山研究院', 'label': '长沙矿山研究院' }, { 'value': '中国科学院亚热带农业生态研究所', 'label': '中国科学院亚热带农业生态研究所' }, { 'value': '中共湖南省委党校', 'label': '中共湖南省委党校' }, { 'value': '湖南省中医药研究院', 'label': '湖南省中医药研究院' }, { 'value': '湖南人文科技学院', 'label': '湖南人文科技学院' }, { 'value': '邵阳学院', 'label': '邵阳学院' }, { 'value': '湖南理工学院', 'label': '湖南理工学院' }, { 'value': '湖南工商大学', 'label': '湖南工商大学' }, { 'value': '衡阳师范学院', 'label': '衡阳师范学院' }, { 'value': '湖南城市学院', 'label': '湖南城市学院' }] }, { 'value': '广东', 'label': '广东', 'children': [{ 'value': '中共广东省委党校（广东行政学院）', 'label': '中共广东省委党校（广东行政学院）' }, { 'value': '五邑大学', 'label': '五邑大学' }, { 'value': '广东外语外贸大学', 'label': '广东外语外贸大学' }, { 'value': '广东财经大学', 'label': '广东财经大学' }, { 'value': '广州医科大学', 'label': '广州医科大学' }, { 'value': '华南理工大学', 'label': '华南理工大学' }, { 'value': '汕头大学', 'label': '汕头大学' }, { 'value': '广州大学', 'label': '广州大学' }, { 'value': '暨南大学', 'label': '暨南大学' }, { 'value': '广东工业大学', 'label': '广东工业大学' }, { 'value': '广州中医药大学', 'label': '广州中医药大学' }, { 'value': '深圳大学', 'label': '深圳大学' }, { 'value': '中山大学', 'label': '中山大学' }, { 'value': '华南农业大学', 'label': '华南农业大学' }, { 'value': '华南师范大学', 'label': '华南师范大学' }, { 'value': '广东医科大学', 'label': '广东医科大学' }, { 'value': '仲恺农业工程学院', 'label': '仲恺农业工程学院' }, { 'value': '广州体育学院', 'label': '广州体育学院' }, { 'value': '广州美术学院', 'label': '广州美术学院' }, { 'value': '中国科学院广州化学研究所', 'label': '中国科学院广州化学研究所' }, { 'value': '中国科学院南海海洋研究所', 'label': '中国科学院南海海洋研究所' }, { 'value': '中国科学院华南植物园', 'label': '中国科学院华南植物园' }, { 'value': '中国科学院广州能源研究所', 'label': '中国科学院广州能源研究所' }, { 'value': '中国科学院广州地球化学研究所', 'label': '中国科学院广州地球化学研究所' }, { 'value': '广东省社会科学院', 'label': '广东省社会科学院' }, { 'value': '广东省心血管病研究所', 'label': '广东省心血管病研究所' }, { 'value': '广东海洋大学', 'label': '广东海洋大学' }, { 'value': '广东药科大学', 'label': '广东药科大学' }, { 'value': '南方医科大学', 'label': '南方医科大学' }, { 'value': '星海音乐学院', 'label': '星海音乐学院' }, { 'value': '广东技术师范大学', 'label': '广东技术师范大学' }, { 'value': '中国科学院广州生物医药与健康研究院', 'label': '中国科学院广州生物医药与健康研究院' }, { 'value': '广东金融学院', 'label': '广东金融学院' }, { 'value': '佛山科学技术学院', 'label': '佛山科学技术学院' }, { 'value': '南方科技大学', 'label': '南方科技大学' }, { 'value': '深圳北理莫斯科大学', 'label': '深圳北理莫斯科大学' }, { 'value': '东莞理工学院', 'label': '东莞理工学院' }, { 'value': '深圳技术大学', 'label': '深圳技术大学' }, { 'value': '广东以色列理工学院', 'label': '广东以色列理工学院' }, { 'value': '广东石油化工学院', 'label': '广东石油化工学院' }, { 'value': '肇庆学院', 'label': '肇庆学院' }, { 'value': '中国科学院深圳先进技术研究院', 'label': '中国科学院深圳先进技术研究院' }, { 'value': '深圳理工大学', 'label': '深圳理工大学' }] }, { 'value': '重庆', 'label': '重庆', 'children': [{ 'value': '重庆大学', 'label': '重庆大学' }, { 'value': '重庆医科大学', 'label': '重庆医科大学' }, { 'value': '西南政法大学', 'label': '西南政法大学' }, { 'value': '重庆交通大学', 'label': '重庆交通大学' }, { 'value': '四川外国语大学', 'label': '四川外国语大学' }, { 'value': '重庆邮电大学', 'label': '重庆邮电大学' }, { 'value': '重庆师范大学', 'label': '重庆师范大学' }, { 'value': '四川美术学院', 'label': '四川美术学院' }, { 'value': '陆军军医大学', 'label': '陆军军医大学' }, { 'value': '西南大学', 'label': '西南大学' }, { 'value': '重庆工商大学', 'label': '重庆工商大学' }, { 'value': '重庆理工大学', 'label': '重庆理工大学' }, { 'value': '中共重庆市委党校', 'label': '中共重庆市委党校' }, { 'value': '陆军勤务学院', 'label': '陆军勤务学院' }, { 'value': '重庆科技学院', 'label': '重庆科技学院' }, { 'value': '重庆三峡学院', 'label': '重庆三峡学院' }, { 'value': '重庆文理学院', 'label': '重庆文理学院' }, { 'value': '中国科学院重庆绿色智能技术研究院', 'label': '中国科学院重庆绿色智能技术研究院' }] }, { 'value': '四川', 'label': '四川', 'children': [{ 'value': '成都理工大学', 'label': '成都理工大学' }, { 'value': '西南医科大学', 'label': '西南医科大学' }, { 'value': '四川大学', 'label': '四川大学' }, { 'value': '西南财经大学', 'label': '西南财经大学' }, { 'value': '西南科技大学', 'label': '西南科技大学' }, { 'value': '西南石油大学', 'label': '西南石油大学' }, { 'value': '四川农业大学', 'label': '四川农业大学' }, { 'value': '四川师范大学', 'label': '四川师范大学' }, { 'value': '成都中医药大学', 'label': '成都中医药大学' }, { 'value': '西南交通大学', 'label': '西南交通大学' }, { 'value': '电子科技大学', 'label': '电子科技大学' }, { 'value': '西华大学', 'label': '西华大学' }, { 'value': '西华师范大学', 'label': '西华师范大学' }, { 'value': '中国科学院成都有机化学有限公司', 'label': '中国科学院成都有机化学有限公司' }, { 'value': '成都体育学院', 'label': '成都体育学院' }, { 'value': '中国科学院成都山地灾害与环境研究所', 'label': '中国科学院成都山地灾害与环境研究所' }, { 'value': '四川音乐学院', 'label': '四川音乐学院' }, { 'value': '西南民族大学', 'label': '西南民族大学' }, { 'value': '中国科学院成都生物研究所', 'label': '中国科学院成都生物研究所' }, { 'value': '中国核动力研究设计院', 'label': '中国核动力研究设计院' }, { 'value': '核工业西南物理研究院', 'label': '核工业西南物理研究院' }, { 'value': '中国航空研究院611所', 'label': '中国航空研究院611所' }, { 'value': '中国航空研究院624所', 'label': '中国航空研究院624所' }, { 'value': '西南通信研究所（30所）', 'label': '西南通信研究所（30所）' }, { 'value': '西南技术物理研究所（209所）', 'label': '西南技术物理研究所（209所）' }, { 'value': '邮电部邮电科学研究院（成都五所）', 'label': '邮电部邮电科学研究院（成都五所）' }, { 'value': '四川抗菌素工业研究所', 'label': '四川抗菌素工业研究所' }, { 'value': '四川省社会科学院', 'label': '四川省社会科学院' }, { 'value': '中共四川省委党校（四川行政学院）', 'label': '中共四川省委党校（四川行政学院）' }, { 'value': '中国空气动力研究与发展中心', 'label': '中国空气动力研究与发展中心' }, { 'value': '中国科学院光电技术研究所', 'label': '中国科学院光电技术研究所' }, { 'value': '成都信息工程大学', 'label': '成都信息工程大学' }, { 'value': '四川轻化工大学', 'label': '四川轻化工大学' }, { 'value': '中国民用航空飞行学院', 'label': '中国民用航空飞行学院' }, { 'value': '川北医学院', 'label': '川北医学院' }, { 'value': '中国科学院成都文献情报中心', 'label': '中国科学院成都文献情报中心' }, { 'value': '西南自动化研究所', 'label': '西南自动化研究所' }, { 'value': '电信科学技术第五研究所', 'label': '电信科学技术第五研究所' }, { 'value': '绵阳师范学院', 'label': '绵阳师范学院' }, { 'value': '四川警察学院', 'label': '四川警察学院' }, { 'value': '成都医学院', 'label': '成都医学院' }, { 'value': '成都大学', 'label': '成都大学' }, { 'value': '中国科学院成都有机化学研究所', 'label': '中国科学院成都有机化学研究所' }, { 'value': '中国科学院成都计算机应用研究所', 'label': '中国科学院成都计算机应用研究所' }, { 'value': '攀枝花学院', 'label': '攀枝花学院' }] }, { 'value': '陕西', 'label': '陕西', 'children': [{ 'value': '中共陕西省委党校', 'label': '中共陕西省委党校' }, { 'value': '西北政法大学', 'label': '西北政法大学' }, { 'value': '西安石油大学', 'label': '西安石油大学' }, { 'value': '西安邮电大学', 'label': '西安邮电大学' }, { 'value': '西北工业大学', 'label': '西北工业大学' }, { 'value': '西安科技大学', 'label': '西安科技大学' }, { 'value': '西北大学', 'label': '西北大学' }, { 'value': '西安交通大学', 'label': '西安交通大学' }, { 'value': '长安大学', 'label': '长安大学' }, { 'value': '西安理工大学', 'label': '西安理工大学' }, { 'value': '西安电子科技大学', 'label': '西安电子科技大学' }, { 'value': '西安建筑科技大学', 'label': '西安建筑科技大学' }, { 'value': '西北农林科技大学', 'label': '西北农林科技大学' }, { 'value': '西安工业大学', 'label': '西安工业大学' }, { 'value': '西安工程大学', 'label': '西安工程大学' }, { 'value': '空军军医大学', 'label': '空军军医大学' }, { 'value': '陕西科技大学', 'label': '陕西科技大学' }, { 'value': '陕西中医药大学', 'label': '陕西中医药大学' }, { 'value': '陕西师范大学', 'label': '陕西师范大学' }, { 'value': '延安大学', 'label': '延安大学' }, { 'value': '西安外国语大学', 'label': '西安外国语大学' }, { 'value': '西安体育学院', 'label': '西安体育学院' }, { 'value': '西安音乐学院', 'label': '西安音乐学院' }, { 'value': '西安美术学院', 'label': '西安美术学院' }, { 'value': '中国科学院水土保持与生态环境研究中心', 'label': '中国科学院水土保持与生态环境研究中心' }, { 'value': '中国科学院西安光学精密机械研究所', 'label': '中国科学院西安光学精密机械研究所' }, { 'value': '中国航空研究院603所', 'label': '中国航空研究院603所' }, { 'value': '中国航空研究院623所', 'label': '中国航空研究院623所' }, { 'value': '中国航空研究院631所', 'label': '中国航空研究院631所' }, { 'value': '中国航空研究院618所', 'label': '中国航空研究院618所' }, { 'value': '西安近代化学研究所（204所）', 'label': '西安近代化学研究所（204所）' }, { 'value': '西安应用光学研究所（205所）', 'label': '西安应用光学研究所（205所）' }, { 'value': '邮电部邮电科学研究院（西安四所）', 'label': '邮电部邮电科学研究院（西安四所）' }, { 'value': '西安机电信息技术研究所（212所）', 'label': '西安机电信息技术研究所（212所）' }, { 'value': '陕西应用物理化学研究所（213）', 'label': '陕西应用物理化学研究所（213）' }, { 'value': '中国兵器科学研究院（陕西机械电器研究所）', 'label': '中国兵器科学研究院（陕西机械电器研究所）' }, { 'value': '中国兵器科学研究院（陕西青华机电研究所）', 'label': '中国兵器科学研究院（陕西青华机电研究所）' }, { 'value': '中国兵器科学研究院（西安应用电子研究所）', 'label': '中国兵器科学研究院（西安应用电子研究所）' }, { 'value': '空军工程大学', 'label': '空军工程大学' }, { 'value': '火箭军工程大学', 'label': '火箭军工程大学' }, { 'value': '武警工程大学', 'label': '武警工程大学' }, { 'value': '西北核技术研究所', 'label': '西北核技术研究所' }, { 'value': '西藏民族大学', 'label': '西藏民族大学' }, { 'value': '陕西理工大学', 'label': '陕西理工大学' }, { 'value': '西安财经大学', 'label': '西安财经大学' }, { 'value': '中国科学院国家授时中心', 'label': '中国科学院国家授时中心' }, { 'value': '西安热工研究院有限公司', 'label': '西安热工研究院有限公司' }, { 'value': '中国科学院地球环境研究所', 'label': '中国科学院地球环境研究所' }, { 'value': '西北机电工程研究所（202所）', 'label': '西北机电工程研究所（202所）' }, { 'value': '西安现代控制技术研究所', 'label': '西安现代控制技术研究所' }, { 'value': '西安航天精密机电研究所（航天16所）', 'label': '西安航天精密机电研究所（航天16所）' }, { 'value': '航天动力技术研究院', 'label': '航天动力技术研究院' }, { 'value': '西安微电子技术研究所', 'label': '西安微电子技术研究所' }, { 'value': '中国航天科技集团有限公司第六研究院第十一研究所', 'label': '中国航天科技集团有限公司第六研究院第十一研究所' }, { 'value': '中国飞行试验研究院', 'label': '中国飞行试验研究院' }, { 'value': '西安精密机械研究所', 'label': '西安精密机械研究所' }, { 'value': '西京学院', 'label': '西京学院' }, { 'value': '西安医学院', 'label': '西安医学院' }, { 'value': '宝鸡文理学院', 'label': '宝鸡文理学院' }, { 'value': '榆林学院', 'label': '榆林学院' }] }, { 'value': '内蒙古', 'label': '内蒙古', 'children': [{ 'value': '内蒙古大学', 'label': '内蒙古大学' }, { 'value': '内蒙古农业大学', 'label': '内蒙古农业大学' }, { 'value': '内蒙古师范大学', 'label': '内蒙古师范大学' }, { 'value': '内蒙古工业大学', 'label': '内蒙古工业大学' }, { 'value': '内蒙古科技大学', 'label': '内蒙古科技大学' }, { 'value': '内蒙古医科大学', 'label': '内蒙古医科大学' }, { 'value': '内蒙古民族大学', 'label': '内蒙古民族大学' }, { 'value': '内蒙古金属材料研究所（52所）', 'label': '内蒙古金属材料研究所（52所）' }, { 'value': '内蒙古财经大学', 'label': '内蒙古财经大学' }, { 'value': '赤峰学院', 'label': '赤峰学院' }, { 'value': '内蒙古艺术学院', 'label': '内蒙古艺术学院' }, { 'value': '呼伦贝尔学院', 'label': '呼伦贝尔学院' }] }, { 'value': '广西', 'label': '广西', 'children': [{ 'value': '广西大学', 'label': '广西大学' }, { 'value': '桂林电子科技大学', 'label': '桂林电子科技大学' }, { 'value': '桂林理工大学', 'label': '桂林理工大学' }, { 'value': '广西医科大学', 'label': '广西医科大学' }, { 'value': '广西中医药大学', 'label': '广西中医药大学' }, { 'value': '广西师范大学', 'label': '广西师范大学' }, { 'value': '广西艺术学院', 'label': '广西艺术学院' }, { 'value': '广西民族大学', 'label': '广西民族大学' }, { 'value': '广西科技大学', 'label': '广西科技大学' }, { 'value': '南宁师范大学', 'label': '南宁师范大学' }, { 'value': '桂林医学院', 'label': '桂林医学院' }, { 'value': '广西财经学院', 'label': '广西财经学院' }, { 'value': '右江民族医学院', 'label': '右江民族医学院' }, { 'value': '北部湾大学', 'label': '北部湾大学' }] }, { 'value': '海南', 'label': '海南', 'children': [{ 'value': '海南大学', 'label': '海南大学' }, { 'value': '海南师范大学', 'label': '海南师范大学' }, { 'value': '海南热带海洋学院', 'label': '海南热带海洋学院' }, { 'value': '海南医学院', 'label': '海南医学院' }, { 'value': '三亚学院', 'label': '三亚学院' }, { 'value': '中国科学院深海科学与工程研究所', 'label': '中国科学院深海科学与工程研究所' }] }, { 'value': '贵州', 'label': '贵州', 'children': [{ 'value': '贵州中医药大学', 'label': '贵州中医药大学' }, { 'value': '贵州大学', 'label': '贵州大学' }, { 'value': '贵州医科大学', 'label': '贵州医科大学' }, { 'value': '遵义医科大学', 'label': '遵义医科大学' }, { 'value': '贵州师范大学', 'label': '贵州师范大学' }, { 'value': '中国科学院地球化学研究所', 'label': '中国科学院地球化学研究所' }, { 'value': '贵州财经大学', 'label': '贵州财经大学' }, { 'value': '贵州民族大学', 'label': '贵州民族大学' }, { 'value': '黔南民族师范学院', 'label': '黔南民族师范学院' }, { 'value': '贵阳学院', 'label': '贵阳学院' }, { 'value': '铜仁学院', 'label': '铜仁学院' }, { 'value': '中国航天科工集团第十研究院', 'label': '中国航天科工集团第十研究院' }] }, { 'value': '云南', 'label': '云南', 'children': [{ 'value': '云南大学', 'label': '云南大学' }, { 'value': '昆明医科大学', 'label': '昆明医科大学' }, { 'value': '中国科学院云南天文台', 'label': '中国科学院云南天文台' }, { 'value': '昆明理工大学', 'label': '昆明理工大学' }, { 'value': '西南林业大学', 'label': '西南林业大学' }, { 'value': '云南中医药大学', 'label': '云南中医药大学' }, { 'value': '云南师范大学', 'label': '云南师范大学' }, { 'value': '云南财经大学', 'label': '云南财经大学' }, { 'value': '云南农业大学', 'label': '云南农业大学' }, { 'value': '云南民族大学', 'label': '云南民族大学' }, { 'value': '中国科学院昆明动物研究所', 'label': '中国科学院昆明动物研究所' }, { 'value': '中国科学院昆明植物研究所', 'label': '中国科学院昆明植物研究所' }, { 'value': '中国科学院西双版纳热带植物园', 'label': '中国科学院西双版纳热带植物园' }, { 'value': '昆明物理研究所（211所）', 'label': '昆明物理研究所（211所）' }, { 'value': '昆明贵金属研究所', 'label': '昆明贵金属研究所' }, { 'value': '大理大学', 'label': '大理大学' }, { 'value': '云南艺术学院', 'label': '云南艺术学院' }, { 'value': '云南警官学院', 'label': '云南警官学院' }, { 'value': '昆明学院', 'label': '昆明学院' }] }, { 'value': '西藏', 'label': '西藏', 'children': [{ 'value': '西藏大学', 'label': '西藏大学' }, { 'value': '西藏藏医药大学', 'label': '西藏藏医药大学' }, { 'value': '西藏农牧学院', 'label': '西藏农牧学院' }] }, { 'value': '甘肃', 'label': '甘肃', 'children': [{ 'value': '西北民族大学', 'label': '西北民族大学' }, { 'value': '兰州大学', 'label': '兰州大学' }, { 'value': '甘肃农业大学', 'label': '甘肃农业大学' }, { 'value': '西北师范大学', 'label': '西北师范大学' }, { 'value': '中国科学院近代物理研究所', 'label': '中国科学院近代物理研究所' }, { 'value': '中国科学院兰州化学物理研究所', 'label': '中国科学院兰州化学物理研究所' }, { 'value': '中国科学院兰州地质研究所', 'label': '中国科学院兰州地质研究所' }, { 'value': '兰州理工大学', 'label': '兰州理工大学' }, { 'value': '兰州交通大学', 'label': '兰州交通大学' }, { 'value': '甘肃中医药大学', 'label': '甘肃中医药大学' }, { 'value': '兰州生物制品研究所', 'label': '兰州生物制品研究所' }, { 'value': '中国地震局兰州地震研究所', 'label': '中国地震局兰州地震研究所' }, { 'value': '兰州财经大学', 'label': '兰州财经大学' }, { 'value': '甘肃政法大学', 'label': '甘肃政法大学' }, { 'value': '中国科学院寒区旱区环境与工程研究所', 'label': '中国科学院寒区旱区环境与工程研究所' }, { 'value': '天华化工机械及自动化研究设计院', 'label': '天华化工机械及自动化研究设计院' }, { 'value': '中国空间技术研究院510所', 'label': '中国空间技术研究院510所' }, { 'value': '天水师范学院', 'label': '天水师范学院' }, { 'value': '中国科学院西北生态环境资源研究院', 'label': '中国科学院西北生态环境资源研究院' }, { 'value': '河西学院', 'label': '河西学院' }] }, { 'value': '青海', 'label': '青海', 'children': [{ 'value': '青海师范大学', 'label': '青海师范大学' }, { 'value': '中国科学院青海盐湖研究所', 'label': '中国科学院青海盐湖研究所' }, { 'value': '青海民族大学', 'label': '青海民族大学' }, { 'value': '青海大学', 'label': '青海大学' }, { 'value': '中国科学院西北高原生物研究所', 'label': '中国科学院西北高原生物研究所' }] }, { 'value': '宁夏', 'label': '宁夏', 'children': [{ 'value': '北方民族大学', 'label': '北方民族大学' }, { 'value': '宁夏大学', 'label': '宁夏大学' }, { 'value': '宁夏医科大学', 'label': '宁夏医科大学' }, { 'value': '宁夏师范学院', 'label': '宁夏师范学院' }] }, { 'value': '新疆', 'label': '新疆', 'children': [{ 'value': '新疆大学', 'label': '新疆大学' }, { 'value': '新疆农业大学', 'label': '新疆农业大学' }, { 'value': '石河子大学', 'label': '石河子大学' }, { 'value': '新疆医科大学', 'label': '新疆医科大学' }, { 'value': '新疆师范大学', 'label': '新疆师范大学' }, { 'value': '新疆财经大学', 'label': '新疆财经大学' }, { 'value': '中国科学院新疆理化技术研究所', 'label': '中国科学院新疆理化技术研究所' }, { 'value': '塔里木大学', 'label': '塔里木大学' }, { 'value': '喀什大学', 'label': '喀什大学' }, { 'value': '伊犁师范大学', 'label': '伊犁师范大学' }, { 'value': '中科院新疆生态与地理研究所', 'label': '中科院新疆生态与地理研究所' }, { 'value': '昌吉学院', 'label': '昌吉学院' }, { 'value': '新疆艺术学院', 'label': '新疆艺术学院' }, { 'value': '中国科学院新疆生态与地理研究所', 'label': '中国科学院新疆生态与地理研究所' }, { 'value': '中国科学院新疆天文台', 'label': '中国科学院新疆天文台' }] }, { 'value': '台湾', 'label': '台湾', 'children': [] }, { 'value': '香港', 'label': '香港', 'children': [{ 'value': '香港中文大学（深圳）', 'label': '香港中文大学（深圳）' }, { 'value': '北京师范大学-香港浸会大学联合国际学院', 'label': '北京师范大学-香港浸会大学联合国际学院' }, { 'value': '香港恒生大学', 'label': '香港恒生大学' }, { 'value': '香港科技大学', 'label': '香港科技大学' }, { 'value': '香港城市大学', 'label': '香港城市大学' }, { 'value': '香港科技大学（广州）', 'label': '香港科技大学（广州）' }, { 'value': '香港中文大学', 'label': '香港中文大学' }, { 'value': '香港大学', 'label': '香港大学' }, { 'value': '香港理工大学', 'label': '香港理工大学' }, { 'value': '香港浸会大学', 'label': '香港浸会大学' }, { 'value': '香港教育大学', 'label': '香港教育大学' }, { 'value': '香港都会大学', 'label': '香港都会大学' }, { 'value': '香港岭南大学', 'label': '香港岭南大学' }, { 'value': '香港树仁大学', 'label': '香港树仁大学' }, { 'value': '香港珠海学院', 'label': '香港珠海学院' }, { 'value': '香港演艺学院', 'label': '香港演艺学院' }] }, { 'value': '澳门', 'label': '澳门', 'children': [{ 'value': '澳门大学', 'label': '澳门大学' }, { 'value': '澳门城市大学', 'label': '澳门城市大学' }, { 'value': '澳门理工大学', 'label': '澳门理工大学' }, { 'value': '澳门科技大学', 'label': '澳门科技大学' }, { 'value': '澳门旅游学院', 'label': '澳门旅游学院' }] }]
</script>

<style scoped lang="less">
.active {
    color: #f60
}

.school_score p {
    margin-right: 10px;
}

.active {
    color: #ff6602
}

.subbtn {
    width: 160px;
    height: 38px;
    background: #ff6602;
    border-radius: 6px 6px 6px 6px;
    font-size: 14px;
    font-family: PingFang SC-Regular, PingFang SC !important;
    font-weight: 400;
    color: #fff;
    margin-top: 30px;
    margin-left: 15px;
}

.chooseMajor {
    width: 1200px;
    /* margin: 20px auto; */
    width: 880px;
    height: 68px;
    background: #fff9f2;
    border-radius: 4px 4px 4px 4px;
    text-align: center;
    line-height: 68px;
    font-size: 20px;
    font-family: PingFang SC-Medium, PingFang SC !important;
    font-weight: 500;
    color: #f60;
    margin-bottom: 23px;
}

.chooseRegin {
    width: 900px;
    /* margin: 10px auto; */
}
.scoreSchool{
    width: 900px;
}
.chooseRegin div,.score div,.scoreSchool div {
    width: 1200px;
    margin: 20px auto;
    width: 880px;
    height: 68px;
    background: #fff9f2;
    border-radius: 4px 4px 4px 4px;
    text-align: center;
    line-height: 68px;
    font-size: 20px;
    font-family: PingFang SC-Medium, PingFang SC !important;
    font-weight: 500;
    color: #f60;
    margin-bottom: 23px;
}

.allRegin {
    height: 80px;
    width: 900px;
    /* margin: 20px auto; */
    font-size: 14px;
    /* background-color:red; */
    border: 1px solid #eee;
    border-radius: 15px;
    padding: 10px 10px;
}

.recommend_result {
    margin-bottom: 50px !important;
    width: 800px;
}

.allRegin li {
    cursor: pointer;
    margin-right: 20px;
    float: left;
    margin-top: 10px;
}

.allRegin li:hover {
    color: #f60;
}

.score {
    width: 900px;
    /* margin: 20px auto; */
}

.score-title {
    width: 1200px;
    margin: 20px auto;
    // width: 880px;
    height: 68px;
    background: #fff9f2;
    border-radius: 4px 4px 4px 4px;
    text-align: center;
    line-height: 68px;
    font-size: 20px;
    font-family: PingFang SC-Medium, PingFang SC !important;
    font-weight: 500;
    color: #f60;
    margin-bottom: 23px;
}

.search {
    position: absolute;
    right: 100px;
    top: 250px;
    /* background-color: red; */
}

.import {
    /* background: black; */
    width: 900px;
}

.container {
    margin-left: 100px;
}


.loveSchool {
    overflow: hidden;

    h1 {
        margin: 30px;
    }

    .el-row {
        padding: 30px 50px;
    }
}

.schoolListItem {
    padding: 30px 100px;
    /* border: 1px solid #eee; */
    margin-left: 100px;
    position: relative;
}

.school_list_item_content {
    /* margin-left:-20px; */
    margin-bottom: 20px;
}

.school_list_item_content span:nth-of-type(1) {
    margin-right: 10px;
    font-size: 18px;
    font-weight: 700;
}

.schoolCompare {
    ul {
        li {
            div {
                display: flex;
                align-items: center;
                flex-direction: column;

                p {
                    padding: 30px;
                    font-size: 14px;
                    width: 120px;
                    height: 30px;
                    text-align: center;
                }
            }
        }
    }
}
</style>