<template>
    <div>
    </div>
    <div class="personal">
        <el-tabs :tab-position="tabPosition" style="height: 200px" class="demo-tabs">
            <el-tab-pane label="个人信息">
                <avator></avator>
            </el-tab-pane>
            <el-tab-pane label="收藏院校" class="loveSchool">
                <h1>关注院校</h1>
                <div v-for="i of collect_school_list.arr">
                    <el-row>
                        <el-col :span="2">
                            <div>
                                <img style="width: 60px;height: 60px;" :src=i.school_img>
                            </div>
                        </el-col>
                        <el-col :span="14" @click="gotoDetail(i.school_id)">
                            <div>
                                <div class="school_list_item_content">
                                    <span>{{ i.school_name }}</span>
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
                                        {{ i.province }}
                                    </span>
                                </div>
                                <el-breadcrumb separator="|">
                                    <el-breadcrumb-item>{{ i.type }}</el-breadcrumb-item>
                                    <el-breadcrumb-item>{{ i.school_type }}</el-breadcrumb-item>
                                    <el-breadcrumb-item>{{ i.area }}</el-breadcrumb-item>
                                </el-breadcrumb>
                            </div>
                        </el-col>
                        <el-col :span="8">
                            <!-- 右侧=开始 -->
                            <div class="schoolListBtn">
                                <el-button @click="cancelSubcribe(i.school_id)" type="warning">取消关注</el-button>
                            </div>
                            <!-- 右侧--结束 -->
                        </el-col>
                    </el-row>
                </div>

            </el-tab-pane>
            <el-tab-pane label="账户问题">
                <ul class="account">
                    <li>
                        <p>修改密码</p>
                        <el-input class="w-50 m-2" v-model="password1" placeholder="请输入密码" :prefix-icon="Unlock" />
                        <el-input class="w-50 m-2" v-model="password2" placeholder="请再次输入密码" :prefix-icon="Unlock" />
                    </li>
                    <li><el-button type='primary' @click="modifySecret">确认修改</el-button><el-button @click="exitAccount"
                            type="success">退出登录</el-button><el-button @click="cancelAccount" type='danger'>注销账户</el-button>
                    </li>
                </ul>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<script setup>

import avator from '@/components/avator.vue'
import { useRoute, useRouter } from 'vue-router'
import { Unlock } from "@element-plus/icons-vue"
import { ref, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"
import requestFn from '@/api/requestFn';
import { ElMessage } from 'element-plus'
import store from '@/store';
const tabPosition = ref('left')
const router = useRouter()
const collect_school_list = reactive({ arr: [] })
const current_user = store.state.current_user
const userInfo = reactive({ item: [] })
const year = ref('2023')
const currentUserAvator = reactive({ item: [] })


onMounted(() => {
    requestFn({
        url: '/getCollectSchool',
        method: 'post',
        data: {
            username: store.state.current_user
        }
    }).then(data => {
        collect_school_list.arr = (eval("(" + data.data + ")"))
    })

    requestFn({
        url: 'select_userInfo',
        method: 'post',
        data: {
            user: current_user
        }
    }).then(data => {
        userInfo.item = data.data[0]
    })
})
const exitAccount = () => {
    sessionStorage.removeItem('vuex')
    localStorage.removeItem('token')
    localStorage.removeItem('username')
    store.state.isLogin = false
    store.state.current_user = ''
    store.state.userInfo.length = 0
    router.push('/')

}
// 路由带参跳转
const gotoDetail = (e) => {
    router.push({
        // path:'/schoolDetail/'+e,
        name: 'schoolDetail',
        params: {
            school_id: e,
        }
    })
}

const cancelSubcribe = (e) => {
    requestFn({
        url: '/collectSchool',
        method: 'post',
        data: {
            school_id: e,
            user: store.state.current_user
        }
    }).then(data => {
        console.log(data.data)
    })
}

const password1 = ref('')
const password2 = ref('')
const modifySecret = () => {
    if ((password1.value == password2.value)&&((password1.value!=''|null)&(password2.value!=''|null))) {
        requestFn({
            url: '/modify_secret',
            method: 'post',
            data: {
                password: password1.value,
                username: store.state.current_user
            }
        }).then(res => {
            console.log(res.data)
            if (res.data.msg == '成功') {
                sessionStorage.removeItem('vuex')
    localStorage.removeItem('token')
    localStorage.removeItem('username')
    store.state.isLogin = false
    store.state.current_user = ''
    store.state.userInfo.length = 0
    router.push('/')
            } else {
                alert('修改失败，请重试！')

            }
        })
    } else {
        ElMessage.error('密码不能为空，并且两次密码必须一致!');
    }
}

const cancelAccount = () => {
    if ((password1.value !='' || null) && (password2.value != '' || null)) {
        if (password1.value == password2.value) {
            requestFn({
                url: '/cancelAccount',
                method: 'post',
                data: {
                    username: store.state.current_user,
                    password: password1.value
                }
            }).then(res => {
                if (res.data.code == 200) {
                    ElMessage({
                        showClose: true,
                        message: '注销成功,欢迎下次再来！',
                        type: 'success',
                    })
                    sessionStorage.removeItem('vuex')
    localStorage.removeItem('token')
    localStorage.removeItem('username')
    store.state.isLogin = false
    store.state.current_user = ''
    store.state.userInfo.length = 0
    router.push('/')
                } else {
                    ElMessage.error(`${res.data.error},请重试!`)

                }
            }).catch(error => {
                console.log(error)
            })
        } else {
            ElMessage.error('两次密码不一致！')
        }
    } else {
        ElMessage.error('密码不能为空！')
    }
}



</script>

<style scoped lang="less">
.account {
    p {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 30px;
    }

    .el-input {
        margin-bottom: 30px;
    }

    padding:50px 50px;
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

.school_list_item_content span:nth-of-type(2) {
    font-size: 14px;
    color: #888888;
}

.school_list_item_label span {
    float: left;
    margin-right: 10px;
}

.schoolListBtn {
    padding-top: 15px;
}

.personal {
    width: 1200px;
    height: 500px;
    margin: 0 auto;

    // background-color: red;
    ::v-deep(.el-tabs) {
        height: 600px !important;
        // background-color: pink;

        .el-tabs__header {
            height: 600px;
            font-size: 16px !important;
        }

        .el-tabs__content {
            height: 600px;
            overflow: hidden;
            overflow-y: scroll;

            .baseInfo {
                p {
                    margin: 20px;
                }

                font-size: 16px;

                ul {
                    padding: 20px 100px;

                    li {
                        margin-bottom: 20px;
                    }
                }
            }

            .stuInfo {
                p {
                    margin: 20px;
                }

                font-size: 16px;

                ul {
                    padding: 20px 100px;
                    font-size: 16px;

                    li {
                        margin-bottom: 20px;
                        display: flex;
                        align-items: center;
                    }
                }
            }
        }
    }
}
</style>