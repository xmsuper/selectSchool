<template>
    <div class="demo-input-size">
        <el-row :gutter="24">
            <el-col :span="4">
                <RouterLink to="/">
                    <img style="width: 116px;height: 35px;margin-left: 50px;" src="../../public/下载.png" alt="">
                </RouterLink>
            </el-col>
            <el-col :span="5">
                <!-- <span>距离2023考研 倒计时40天</span> -->
                <van-count-down :time="time" format="DD 天 HH 时 mm 分 ss 秒" />
            </el-col>
            <el-col :span="9">
                <el-input v-model="input" class="w-10 m-5" placeholder="查专业" :suffix-icon="Search" />
            </el-col>
            <el-col :span="6">
                <el-button v-if="!isLogin"  style="margin-left: 50px;" type="danger" @click="LoginAlertFn">登录/注册</el-button>
                <el-button v-else  style="margin-left: 50px;" type="danger">欢迎您，同学xxxx</el-button>
            </el-col>
        </el-row>

        <el-row :gutter="24">
            <el-col :span="6">
                <div>AI择校</div>
            </el-col>
            <el-col :span="6">
                <div><RouterLink to="/major_list">查专业</RouterLink></div>
            </el-col>
            <el-col :span="6">
                <div>
                    <RouterLink to="/home">查院校</RouterLink>
                </div>
            </el-col>
            <el-col :span="6">
                <div>考研工具箱</div>
            </el-col>
        </el-row>

        <!-- 登录弹出框 -->
        <el-dialog v-model="LoginAlert" title="智慧考研" width="30%" center>
            <ul class="tab-main">
                <li @click="curID = 0" :class="{ 'cur': curID === 0}">登录</li>
                <li @click="curID = 1" :class="{ 'cur': curID === 1}">注册</li>
            </ul>
            <div class="tab-item">
                <!-- 盒子1--开始 -->
                <div v-if="curID === 0">
                    <el-form ref="ruleFormRef" :model="ruleForm" status-icon  label-width="120px"
                        class="demo-ruleForm">
                        <el-form-item label="用户名" prop="pass">
                            <el-input v-model="ruleForm.username"  type="text" autocomplete="off" />
                        </el-form-item>
                        <el-form-item label="密码" prop="checkPass">
                            <el-input v-model="ruleForm.password" type="password" autocomplete="off" />
                        </el-form-item>
                        <el-form-item>
                            <el-button type="danger" @click="submitForm(ruleForm)">登录</el-button>
                            <el-button @click="resetForm(ruleFormRef)">重置</el-button>
                        </el-form-item>
                    </el-form>
                </div>
                <!-- 盒子1--结束 -->

                <!-- 盒子2---开始 -->
                <div v-if="curID === 1">
                    <el-form ref="ruleFormRef2" :model="ruleForm2" status-icon  label-width="120px"
                        class="demo-ruleForm">
                        <el-form-item label="请输入用户名">
                            <el-input v-model="ruleForm2.username" type="password" autocomplete="off"/>
                        </el-form-item>
                        <el-form-item label="请输入密码" prop="checkPass">
                            <el-input v-model="ruleForm2.password" type="password" autocomplete="off" />
                        </el-form-item>
                        <el-form-item label="请再次输入密码" prop="age">
                            <el-input v-model="ruleForm2.password2" type="password" />
                        </el-form-item>
                        <el-form-item>
                            <el-button type="danger" @click="submitForm2(ruleForm2)">注册</el-button>
                            <el-button @click="resetForm(ruleFormRef)">重置</el-button>
                        </el-form-item>
                    </el-form>
                </div>
                <!-- 盒子2--结束 -->
            </div>
        </el-dialog>
        <!-- 登录弹出框结束 -->
    </div>
</template>

<script setup>
import type from 'element-plus'
import requestFn from '@/api/requestFn.js'
import {ref, reactive, onMounted,getCurrentInstance,computed} from 'vue';
import { Search } from '@element-plus/icons-vue'
import {useRoute,useRouter} from 'vue-router'
import store from '@/store';
const router=useRouter()
const isLogin=computed(()=>store.state.isLogin)
let curID = ref(0)
const input = ref('')
const ruleFormRef=ref()
const LoginAlert = ref(false)
const {proxy}=getCurrentInstance()
// console.log(proxy)
const ruleForm = reactive({
    username:'',
    password:''
})
const ruleForm2=reactive({
    username:'',
    password:'',
    password2:''
})
const LoginAlertFn=()=>{
    LoginAlert.value=true
}
// 登录
const submitForm=(e)=>{
    requestFn({
        url:'/Login',
        method:'post',
        data:{
            username:e.username,
            password:e.password
        }
    }).then(data=>{
        // console.log(data.data.content)
        if(data.data.code==200){
            // store.state.isLogin
            console.log(store.state.isLogin)
            store.commit('setLogin',true)
            console.log(store.state.isLogin)
            LoginAlert.value=false
            router.push('/')
        }

    }).catch(erro=>{
        console.log(erro)
    })

}

// 注册
const submitForm2 = (e) => {
    if(e.password==e.password2){
        requestFn({
            url:'/Register',
            method:'post',
            data:{
                username:e.username,
                password:e.password
            }
        }).then(data=>{
            console.log(data.data)
        }).catch(error=>{
            console.log(error)
        })
    }else{
        console.log('两次密码不一致')
    }
}

const resetForm = (formEl) => {
  if (!formEl) return
  formEl.resetFields()
}

let cur_time=new Date().getTime()
let fina_time=new Date('2023/12/24')
let diff=Math.abs(cur_time-fina_time.getTime())
// console.log(diff)
const time=ref(diff)
</script>

<style lang="less" scoped>
.el-dialog{
    border-radius: 20px;
}
.tab-item{
    div{
        margin-left: -10px;
    }
}
.tab-main{
    display: flex;
    justify-content:center;
    margin-bottom: 50px;
    // align-items:flex-start;
    li{
        margin-right: 40px;
        text-align: center;
        border-radius: 5px;
        border: 1px solid #eee;
        width: 50px;
        font-size: 18px;
        font-weight: bold;
    }
}
.el-tabs {
    background-color: blue;
}

.el-tab-pane {
    background-color: red;
}

.demo-input-size {
    width: 1200px;
    // margin-top: 50px;
    margin:50px auto;
    // background-color: red;
    .el-row {
        &:nth-of-type(1) {}
    }

    .el-row {
        &:nth-of-type(2) {
            margin: 30px 0;
            // background-color: red;
            padding: 20px 100px;

            .el-col {

                // background-color: white;
                div {
                    width: 30%;
                    text-align: center;
                    font-size: 18px;
                    font-weight: bold;
                    // background-color: blue;
                }

                div:hover {
                    cursor: pointer;
                    border-bottom: 3px solid orange;
                }
            }
        }
    }
}

.dialog-footer button:first-child {
    margin-right: 10px;
}
.van-count-down{
    color: red;
    font-size: 16px;
    font-weight: 900;
}
</style>
