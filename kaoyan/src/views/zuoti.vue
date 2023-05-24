<template>
    <div class="timu" v-for="(i, k) of tiku.item" :key="k">
        <h2>{{ i.subject }}</h2>
        <div class="options" style="margin-top: 30px;" >
            <el-radio-group :disabled="disabledItem[k]" v-model="selectedOptions[k]" @change="chooseOptions($event, i.id,k)" @click="disableFn(k)" style="display: flex;
                        flex-flow: column nowrap;
                        align-items: flex-start;">
                <el-radio label="A">{{ i.optionsA }}</el-radio>
                <el-radio label="B">{{ i.optionsB }}</el-radio>
                <el-radio label="C">{{ i.optionsC }}</el-radio>
                <el-radio label="D">{{ i.optionsD }}</el-radio>
            </el-radio-group>
            <el-button v-show="isShowBtn.item[k]" color="#f60" style="color: #fff;margin-top: 20px;" @click="isShowExplation.item[k]=!isShowExplation.item[k]">查看解析</el-button>
        </div>
        <p style="font-size: 14px;margin-top: 20px;" v-if="isShowExplation.item[k]">{{ i.answer }}</p>
        <p style="font-size: 14px;margin-top: 20px;"  v-if="isShowExplation.item[k]">{{ i.explation }}</p>
    </div>
</template>

<script setup>
import { ref, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"
import requestFn from '@/api/requestFn.js'
import { ElMessage } from 'element-plus'
const tiku = reactive({ item: [] })
let selectedOptions = reactive({ item: [] })
let disabledItem=[]
let isShowBtn=reactive({item:[]})
const disableFn=(k)=>{
    disabledItem[k]=true
}

onMounted(() => {
    requestFn({
        url: '/zuoti',
        method: 'get'
    }).then(res => {
        tiku.item = res.data
        for (let i = 1; i <= tiku.item.length; i++) {
            selectedOptions.item.push('A')
            disabledItem.push(false)
            isShowBtn.item.push(false)
            isShowExplation.item.push(false)
        }
    })
})

const isShowExplation = reactive({item:[]})
const chooseOptions = (event, id,k) => {
    requestFn({
        url: '/checkAnswer',
        method: 'post',
        data: {
            id: id,
            chooseVal: event
        }
    }).then(res => {
        console.log(res.data)

        if (res.data.code == 200) {
            ElMessage({
                message: '回答正确！',
                type: 'success',
            })
            isShowBtn.item[k]=false
        } else {
            ElMessage.error('回答错误！')
            isShowBtn.item[k]=true
        }
    })
}




</script>

<style scoped lang="less">
.timu {
    width: 1200px;
    margin: 20px auto;
    border: 1px solid #eee;
    padding: 30px;
}
</style>