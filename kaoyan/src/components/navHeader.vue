<template>
    <div class="demo-input-size">
        <el-row :gutter="24">
            <el-col :span="4">
                <RouterLink to="/">
                    <img style="width: 120px;height: 40px;margin-left: 50px;" src="../assets/logo.png" alt="">
                </RouterLink>
            </el-col>
            <el-col :span="5">
                <!-- <span>距离2023考研 倒计时40天</span> -->
                <van-count-down :time="time" format="DD 天 HH 时 mm 分 ss 秒" />
            </el-col>
            <el-col :span="9">
                <el-input v-model="input" class="w-10 m-5" placeholder="查专业" :suffix-icon="Search" @keydown="beginSearch" />
            </el-col>
            <el-col :span="6">
                <el-button v-if="!isLogin" style="margin-left: 50px;" type="danger" @click="LoginAlertFn">登录/注册</el-button>
                <p style="font-size: 20px;" v-else>
                    <router-link to="/personal">
                        <img v-if="imgURL" :src=imgURL alt="" class="avator">
                        <img v-else src="../assets/头像.svg" class="avator" alt="">
                        欢迎您{{ currentUser }}同学</router-link>

                </p>
            </el-col>
        </el-row>

        <el-row :gutter="24">
            <el-col :span="6">
                <RouterLink to="/AI">
                    <div @click="chooseNav($event)" :class="isActive == 'AI择校' ? 'active' : ''">院校推荐</div>
                </RouterLink>
            </el-col>
            <el-col :span="6">
                <RouterLink to="/major_list">
                    <div @click="chooseNav($event)" :class="isActive == '查专业' ? 'active' : ''">查专业</div>
                </RouterLink>
            </el-col>
            <el-col :span="6">
                <RouterLink to="/home">
                    <div @click="chooseNav($event)" :class="isActive == '查院校' ? 'active' : ''">查院校</div>
                </RouterLink>
            </el-col>
            <el-col :span="6">
                <router-link to="/tools">
                    <div @click="chooseNav($event)" :class="isActive == '工具箱' ? 'active' : ''">工具箱</div>
                </router-link>
            </el-col>
        </el-row>

        <!-- 登录弹出框 -->
        <el-dialog v-model="LoginAlert" title="智慧考研" width="30%" center>
            <ul class="tab-main">
                <li @click="curID = 0" :class="{ 'cur': curID === 0 }">登录</li>
                <li @click="curID = 1" :class="{ 'cur': curID === 1 }">注册</li>
            </ul>
            <div class="tab-item">
                <!-- 盒子1--开始 -->
                <div v-if="curID === 0">
                    <el-form ref="ruleFormRef" :model="ruleForm" status-icon label-width="120px" class="demo-ruleForm">
                        <el-form-item label="用户名" prop="pass">
                            <el-input v-model="ruleForm.username" type="text" autocomplete="off" />
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
                <!-- 注册 -->
                <div v-if="curID === 1">
                    <el-form ref="ruleFormRef2" :model="ruleForm2" status-icon :rules="rules" label-width="120px"
                        class="demo-ruleForm">
                        <el-form-item label="请输入用户名">
                            <el-input v-model="ruleForm2.username" type="text" autocomplete="off" />
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
import { ElMessage } from 'element-plus'
import requestFn from '@/api/requestFn.js'
import { ref, reactive, onMounted, getCurrentInstance, computed, watch } from 'vue';
import { Search } from '@element-plus/icons-vue'
import { useRoute, useRouter } from 'vue-router'
// import { FormInstance, FormRules } from 'element-plus'
import store from '@/store';
const isActive = ref('查专业')
const router = useRouter()
const isLogin = computed(() => store.state.isLogin)
let curID = ref(0)
const input = ref('')
const ruleFormRef = ref()
const ruleFormRef2 = ref()
const LoginAlert = ref(false)

const currentUser = ref('')
const { proxy } = getCurrentInstance()


const beginSearch = (event) => {
    if (event.keyCode == 13) {
        router.push({
            path: '/searchResult',
            query: {
                keyword: input.value
            }
        })
    }
}

const imgURL = ref()
try {
    imgURL.value = 'http://127.0.0.1:8000/' + store.state.userInfo[0][8]

} catch (err) {
    imgURL.value =false

}

onMounted(() => {
    const cur_username = localStorage.getItem('username')
    if (localStorage.getItem('username')) {
        requestFn({
            url: '/getPrivate',
            method: 'post',
            data: {
                username: cur_username,
            }
        }).then(res => {
            store.state.isLogin = true
            store.commit('setUserInfo', res.data)
            store.state.current_user = res.data[0][0]
            currentUser.value = res.data[0][0]
            // console.log(store.state.userInfo[0][8],'当前头像值')
            if(store.state.userInfo[0][8]!=''||null){
                imgURL.value = 'http://127.0.0.1:8000' + store.state.userInfo[0][8]
                
            }else{
                imgURL.value=false
            }
        }).catch(error => {
            if (error.code == 403) {
                ElMessage.error(`发生错误, ${error.msg}.`)
                sessionStorage.clear()
                localStorage.clear()
                setTimeout(() => {
                    router.push('/')
                }, 2000)
            }
        })
    } else {
        // ElMessage.error('您还没有登录！')
                sessionStorage.clear()
                localStorage.clear()
    }

})

const ruleForm = reactive({
    username: '',
    password: ''
})
const ruleForm2 = reactive({
    username: '',
    password: '',
    password2: ''
})
const LoginAlertFn = () => {
    LoginAlert.value = true
}
// 登录
const submitForm = (e) => {
    requestFn({
        url: '/Login',
        method: 'post',
        data: {
            username: e.username,
            password: e.password
        }
    }).then(data => {
        console.log(data.data)
        if (data.data.code == 200) {
            ElMessage({
                message: '登录成功！',
                type: 'success',
            })
            localStorage.setItem('token', data.data.token)
            localStorage.setItem('username', data.data.current_user)
            store.commit('setLogin', true)
            store.commit('setCurrent_user', data.data.current_user)
            LoginAlert.value = false
            currentUser.value = store.state.current_user

            requestFn({
                url: '/getPrivate',
                method: 'post',
                data: {
                    username: data.data.current_user
                }
            }).then(res => {
                store.commit('setUserInfo', res.data)
                imgURL.value = 'http://127.0.0.1:8000/' + store.state.userInfo[0][8]
                router.go(0)
            })

        } else {
            alert('登录失败，请重试!')
            LoginAlert.value = false
        }

    }).catch(error => {
        console.log(error)
    })

}

// 正则验证
const validatePass = (rule, value, callback) => {
    if (value === '') {
        callback(new Error('Please input the password'))
    } else {
        if (ruleForm.checkPass !== '') {
            if (!ruleFormRef2.value) return
            ruleFormRef2.value.validateField('checkPass', () => null)
        }
        callback()
    }
}
const rules = reactive({
    username: [{ validator: validatePass, trigger: 'blur' }],
    password: [{ validator: validatePass, trigger: 'blur' }],
    password2: [{ validator: validatePass, trigger: 'blur' }]
})

// 注册
const submitForm2 = (e) => {

    if (ruleForm2.password == ruleForm2.password2) {
        requestFn({
            url: '/Register',
            method: 'post',
            data: {
                username: ruleForm2.username,
                password: ruleForm2.password
            }
        }).then(data => {
            console.log(data.data)
            if(data.data.code==200){
                ElMessage({
    showClose: true,
    message: '注册成功，请登录.',
    type: 'success',
  })
            }
        }).catch(error => {
            console.log(error)
        })
    } else {
        ElMessage.error('两次密码不一致，请检查密码！')
    }
}

const resetForm = (formEl) => {
    if (!formEl) return
    formEl.resetFields()
}

let cur_time = new Date().getTime()
let fina_time = new Date('2023/12/24')
let diff = Math.abs(cur_time - fina_time.getTime())
// console.log(diff)
const time = ref(diff)


const chooseNav = (e) => {
    isActive.value = e.target.innerHTML
}
</script>

<style lang="less" scoped>
.avator {
    width: 40px;
    height: 40px;
    border-radius: 50%;
}

.active {
    color: #ff6602 !important;
    border-bottom: 2px solid #ff6602;
    //   border-bottom:1px solid #ff6602;
}

.el-dialog {
    border-radius: 20px;
}

.tab-item {
    div {
        margin-left: -10px;
    }
}

.tab-main {
    display: flex;
    justify-content: center;
    margin-bottom: 50px;

    // align-items:flex-start;
    li {
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
    margin: 50px auto;
    // background-color: red;
    // border-bottom: 1px solid #eee;

    .el-row {
        &:nth-of-type(1) {
            .el-col {
                &:nth-of-type(4) {
                    p {
                        display: flex;
                        align-items: center;

                        a {
                            display: flex;
                            align-items: center;

                            img {
                                margin: 0px 10px;
                            }
                        }

                    }
                }
            }
        }
    }

    .el-row {
        &:nth-of-type(2) {
            margin: 30px 0;
            // background-color: red;
            padding: 0px 80px;

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

.van-count-down {
    color: red;
    font-size: 16px;
    font-weight: 900;
}
</style>
