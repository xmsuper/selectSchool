<template>
    <div class="MajorOption">
        <span style="    font-size: 16px;color: #f60;line-height: 22px;">注：箭头头后数字为院线复试线与国家线的差值</span>
        <!-- type --开始 -->
        <el-dropdown style="border-radius: 15px;">
            <span class="el-dropdown-link" style="margin-left: 100px;" :v-model="schoolType">
                {{ schoolType }}
                <el-icon class="el-icon--right">
                    <arrow-down />
                </el-icon>
            </span>
            <template #dropdown>
                <el-dropdown-menu>
                    <el-dropdown-item @click="chooseType($event)">全部</el-dropdown-item>
                    <el-dropdown-item @click="chooseType($event)">专业型硕士</el-dropdown-item>
                    <el-dropdown-item @click="chooseType($event)">学术型硕士 </el-dropdown-item>
                </el-dropdown-menu>
            </template>
        </el-dropdown>
        <!-- type --结束 -->

        <!-- 专业筛选-开始 -->
        <el-dropdown style="margin-left: 200px;">
            <span class="el-dropdown-link" :v-model="schoolMajor">
                {{ schoolMajor }}
                <el-icon class="el-icon--right">
                    <arrow-down />
                </el-icon>
            </span>
            <template #dropdown>
                <el-dropdown-menu style="width:200px;height:300px;overflow: hidden;overflow-y: scroll;">
                    <el-dropdown-item v-for="(v, k) of singleSchoolSore.arr" @click="chooseMajor(v.major_name, k)">{{
                        v.major_name }}</el-dropdown-item>
                </el-dropdown-menu>
            </template>
        </el-dropdown>
        <!-- 专业筛选-开始 -->


        <!-- 表格  --开始 -->
        <el-table :data="tableData.arr" border style="width: 100%">
            <el-table-column prop="learnType" label="硕士类型" width="180" />
            <el-table-column prop="major_code" label="专科代码" width="180" />
            <el-table-column prop="major_name" label="专业名称" />
            <el-table-column prop="total" label="总分" />
            <el-table-column prop="politics" label="政治" />
            <el-table-column prop="english" label="英语" />
            <el-table-column prop="procourse" label="专业课一" />
            <el-table-column prop="procourese2" label="专业课二" />
            <el-table-column prop="remark" label="备注" />
        </el-table>
        <!-- 表格  --结束 -->

        <!-- 分页 -->
        <!-- <el-pagination layout="prev, pager, next" :total="50" @current-change="handleCurrentChange" /> -->
        <el-pagination v-model:current-page="currentPage" background layout="prev, pager, next" :total="maxPage"
            :page-size="pageSize" @current-change="handleCurrentChange" />
    </div>
</template>

<script setup>
import { ArrowDown } from '@element-plus/icons-vue'
import { ref, reactive, onMounted, watch } from 'vue'
import requestFn from '@/api/requestFn.js';
import { useRoute, useRouter } from 'vue-router';
const schoolType = ref('全部')
const schoolMajor = ref('全部')
const singleSchoolSore = reactive({ arr: [] })
const route = useRoute()
const tableData = reactive({ arr: [] })
const tableData_slice = reactive({ arr: [] })
const tableData_slice_change=reactive({arr:[]})
const pageSize = ref(10)
const currentPage = ref(1)
const maxPage = ref(0)
const pm = reactive({ arr: [] })
const am = reactive({ arr: [] })
const chooseCon = reactive({
    type: '',
    major: ''
})
onMounted(() => {
    // schoolType.value='专业型硕士'
    requestFn({
        url: '/allSchoolMajor',
        method: 'post',
        data: {
            school_id: route.params.school_id
        }
    }).then(data => {
        for (let i of data.data) {
            if (i.learnType == '学术型硕士') {
                am.arr.push(i)
            } else {
                pm.arr.push(i)
            }
        }
        singleSchoolSore.arr = pm.arr,
            tableData_slice.arr = data.data
        maxPage.value = tableData_slice.arr.length
        tableData.arr = tableData_slice.arr.slice((currentPage.value - 1) * pageSize.value, currentPage.value * pageSize.value)
    })
})

const chooseMajor = (v, k) => {
    // console.log(v, k)
    currentPage.value=1
    schoolMajor.value = v
    chooseCon.major = v
}
const chooseType = (e) => {
    schoolMajor.value = '全部'
    schoolType.value = e.target.innerHTML.replace('<!--v-if-->', '')
    switch (schoolType.value.trim()) {
        case '专业型硕士':
        currentPage.value=1
            chooseCon.type = '专业型硕士'
            chooseCon.major = ''
            // console.log(pm.arr)
            singleSchoolSore.arr = pm.arr
            break
        case '学术型硕士':
        currentPage.value=1
            chooseCon.type = '学术型硕士'
            chooseCon.major = ''
            // console.log(am.arr)
            singleSchoolSore.arr = am.arr
            break
        case '全部':
        currentPage.value=1
        singleSchoolSore.arr = pm.arr

            maxPage.value = tableData_slice.arr.length
            tableData.arr = tableData_slice.arr.slice((currentPage.value - 1) * pageSize.value, currentPage.value * pageSize.value)
            break
    }
}

watch(chooseCon, (newVal, oldVal) => {
    const chooseConFilter = Object.fromEntries(
        Object.entries(chooseCon).filter(([k, v]) => v != null && v !== '')
    )
    console.log(chooseConFilter)
    if (newVal != chooseConFilter) {
        requestFn({
            url: '/chooseMajor',
            method: 'post',
            data: {
                data: chooseConFilter,
                school_id: route.params.school_id
            }
        }).then(data => {
            tableData_slice_change.arr = data.data
            maxPage.value = tableData_slice_change.arr.length
            tableData.arr = tableData_slice_change.arr.slice((currentPage.value - 1) * pageSize.value, currentPage.value * pageSize.value)
        })
    }

})


const handleCurrentChange = (val) => {
    console.log(val)
    tableData.arr = tableData_slice.arr.slice((val - 1) * pageSize.value, val * pageSize.value)
}


</script>
<style scoped>
.example-showcase .el-dropdown-link {
    cursor: pointer;
    color: var(--el-color-primary);
    display: flex;
    align-items: center;
}

.MajorOption {
    width: 1200px;
    /* background-color: red; */
    margin: 10px auto;
    margin-top: 50px;
}

.el-table {
    margin-top: 50px;
}

.el-pagination {

    margin: 20px 35%;
}
</style>