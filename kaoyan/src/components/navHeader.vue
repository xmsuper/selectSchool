<template>
    <div class="demo-input-size">
        <el-row :gutter="24">
            <el-col :span="8">
                <RouterLink to="/">
                    <img style="width: 116px;height: 35px;margin-left: 50px;" src="../../public/下载.png" alt="">
                </RouterLink>
            </el-col>
            <el-col :span="8">
                <el-input v-model="input" class="w-10 m-5" placeholder="查专业" :suffix-icon="Search" />
            </el-col>
            <el-col :span="8">
                <el-button style="margin-left: 50px;" type="danger" @click="LoginAlert = true">登录/注册</el-button>
            </el-col>
        </el-row>

        <el-row :gutter="24">
            <el-col :span="6">
                <div>AI择校</div>
            </el-col>
            <el-col :span="6">
                <div>查专业</div>
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
import {ref, reactive, onMounted } from 'vue';
import { Search } from '@element-plus/icons-vue'
let curID = ref(0)
const input = ref('')
const ruleFormRef=ref()
const LoginAlert = ref(false)
const ruleForm = reactive({
    username:'',
    password:''
})
const ruleForm2=reactive({
    username:'',
    password:'',
    password2:''
})
// 登录
const submitForm=(e)=>{
    console.log(e.username,e.password)
    requestFn({
        url:'/Login',
        method:'post',
        data:{
            username:e.username,
            password:e.password
        }
    }).then(data=>{
        console.log(data)
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
    margin-top: 50px;

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
</style>
