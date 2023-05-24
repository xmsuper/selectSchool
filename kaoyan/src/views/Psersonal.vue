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
            <el-tab-pane label="我的帖子">
                <div class="MyArticle">
                    <h1 style="padding: 30px;">我的帖子</h1>
                    <svg style="display: block;margin: 50px auto;" v-if="isNUll" t="1682666854435" class="icon"
                        viewBox="0 0 1567 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5191" width="200"
                        height="200">
                        <path
                            d="M156.662278 699.758173h21.097186A10.444152 10.444152 0 0 1 187.994733 710.202325c0 5.765172-4.490985 10.444152-10.235269 10.444152H156.662278v21.097186A10.444152 10.444152 0 0 1 146.218126 751.978932a10.277045 10.277045 0 0 1-10.444152-10.235269V720.646477H114.676787A10.444152 10.444152 0 0 1 104.441518 710.202325c0-5.765172 4.490985-10.444152 10.235269-10.444152H135.773974v-21.097187A10.444152 10.444152 0 0 1 146.218126 668.425717c5.765172 0 10.444152 4.490985 10.444152 10.235269v21.097187z m1378.628042-83.553215v-21.097186A10.277045 10.277045 0 0 0 1524.846168 584.872503a10.444152 10.444152 0 0 0-10.444152 10.235269v21.097186h-21.097186a10.277045 10.277045 0 0 0-10.235269 10.444152c0 5.598065 4.595427 10.444152 10.235269 10.444152h21.097186v21.097187c0 5.744284 4.67898 10.235269 10.444152 10.235268a10.444152 10.444152 0 0 0 10.444152-10.235268V637.093262h21.097187c5.744284 0 10.235269-4.67898 10.235268-10.444152a10.444152 10.444152 0 0 0-10.235268-10.444152H1535.29032zM776.460024 960.861969H250.596979A20.80475 20.80475 0 0 1 229.77134 939.973665c0-11.530344 9.462402-20.888304 20.825639-20.888303h94.728457A83.010119 83.010119 0 0 1 334.212859 877.413196v-605.96969A83.49055 83.49055 0 0 1 417.849627 187.994733H480.430984V167.001988A83.49055 83.49055 0 0 1 564.067752 83.553215h501.152182A83.448773 83.448773 0 0 1 1148.856702 167.001988v605.969689c0 15.185797-4.052331 29.410732-11.133466 41.672166h115.554096c11.551232 0 20.909192 9.274407 20.909192 20.888304 0 11.530344-9.295295 20.888304-20.888304 20.888304H1002.638576v20.992745c0 15.185797-4.052331 29.410732-11.133466 41.672166h11.196131c11.488567 0 20.825639 9.274407 20.825639 20.888303 0 11.530344-9.462402 20.888304-20.825639 20.888304h-109.893365c9.545955 16.000441 7.478013 36.972297-6.41271 50.863019a41.672166 41.672166 0 0 1-59.072122 0L776.460024 960.861969z m76.367638-41.776607h66.424806c22.977134 0 41.609501-18.59059 41.609501-41.881049V270.461756c0-22.559368-18.047494-40.690416-40.314426-40.690416H416.303892c-22.266932 0-40.314426 18.214601-40.314426 40.690416v606.742557c0 23.123352 18.799473 41.881049 41.588613 41.881049h317.084449l-10.736588-10.757477a41.693054 41.693054 0 0 1-10.861918-40.377091l-19.718558-19.739447A146.259902 146.259902 0 0 1 502.363703 627.693525a146.218126 146.218126 0 0 1 220.517822 190.981761l19.739447 19.739447a41.630389 41.630389 0 0 1 40.377091 10.841029L852.827662 919.085362zM1002.638576 814.643843h62.852906A41.797496 41.797496 0 0 0 1107.080095 772.867236V167.106429c0-23.14424-18.632367-41.776607-41.588613-41.776607H563.775316A41.797496 41.797496 0 0 0 522.207592 167.106429v20.888304h396.794216A83.448773 83.448773 0 0 1 1002.638576 271.443506V814.643843zM266.325872 46.998683h31.123572c8.773088 0 15.875111 6.955805 15.875111 15.666228 0 8.647758-7.102023 15.666228-15.875111 15.666228h-31.123572v31.123572c0 8.773088-6.955805 15.875111-15.666228 15.875111a15.770669 15.770669 0 0 1-15.666228-15.875111V78.331139H203.869844A15.728893 15.728893 0 0 1 187.994733 62.664911c0-8.647758 7.102023-15.666228 15.875111-15.666228h31.123572V15.875111c0-8.773088 6.955805-15.875111 15.666228-15.875111 8.647758 0 15.666228 7.102023 15.666228 15.875111v31.123572zM20.888304 939.973665c0-11.530344 9.462402-20.888304 20.825638-20.888303h125.455152c11.488567 0 20.825639 9.274407 20.825639 20.888303 0 11.530344-9.462402 20.888304-20.825639 20.888304H41.713942A20.80475 20.80475 0 0 1 20.888304 939.973665z m658.733544-135.021995a104.441518 104.441518 0 1 0-147.722083-147.722083 104.441518 104.441518 0 0 0 147.722083 147.722083zM459.542681 313.324555a20.888304 20.888304 0 0 1 20.867415-20.888304H710.202325a20.888304 20.888304 0 1 1 0 41.776608H480.430984A20.825639 20.825639 0 0 1 459.542681 313.324555z m0 104.441518c0-11.530344 9.295295-20.888304 20.742085-20.888303h334.505295c11.44679 0 20.742086 9.274407 20.742086 20.888303 0 11.530344-9.295295 20.888304-20.742086 20.888304H480.284766A20.762974 20.762974 0 0 1 459.542681 417.766073z m0 104.441519c0-11.530344 9.316183-20.888304 20.846527-20.888304h146.301679c11.509455 0 20.846527 9.274407 20.846527 20.888304 0 11.530344-9.316183 20.888304-20.846527 20.888303h-146.301679A20.80475 20.80475 0 0 1 459.542681 522.207592zM62.664911 396.87777a62.664911 62.664911 0 1 1 0-125.329822 62.664911 62.664911 0 0 1 0 125.329822z m0-31.332456a31.332456 31.332456 0 1 0 0-62.664911 31.332456 31.332456 0 0 0 0 62.664911zM1357.739739 271.547948a62.664911 62.664911 0 1 1 0-125.329822 62.664911 62.664911 0 0 1 0 125.329822z m0-31.332456a31.332456 31.332456 0 1 0 0-62.664911 31.332456 31.332456 0 0 0 0 62.664911z"
                            fill="#8A96A3" p-id="5192"></path>
                    </svg>
                    <ul v-else style="padding: 30px;">

                        <li v-for="i of article_list.item"
                            style="padding: 50px;border-radius: 15px;border: 1px solid #eee;margin-bottom: 30px;">
                            <div style="display: flex;align-items: center;justify-content: space-between;">
                                <p style="width: 400px;text-overflow: ellipsis;">{{ i.content }}</p>
                                <p><el-button @click="deleteArticle(i.id)" color="#f56c6c"
                                        style="color: #fff;">点击删除</el-button></p>
                            </div>
                        </li>

                    </ul>
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

const isNUll = ref(true)
const tabPosition = ref('left')
const router = useRouter()
const collect_school_list = reactive({ arr: [] })
const current_user = store.state.current_user
const userInfo = reactive({ item: [] })
const year = ref('2023')
const currentUserAvator = reactive({ item: [] })

const article_list = reactive({ item: [] })
const deleteArticle = (id) => {
    requestFn({
        url: '/DeleteArticle',
        method: 'post',
        data: {
            username: store.state.current_user,
            article_id: id
        }
    }).then(res => {
        console.log(res.data)
        ElMessage({
            showClose: true,
            message: res.data.msg,
            type: 'success',
        })
        requestFn({
            url: '/getUserArticle',
            method: 'post',
            data: {
                username: store.state.current_user
            }
        }).then(res => {
            console.log(res.data)
            article_list.item = res.data

        })
    })
}
onMounted(() => {
    requestFn({
        url: '/getCollectSchool',
        method: 'post',
        data: {
            username: store.state.current_user
        }
    }).then(data => {
        collect_school_list.arr = (eval("(" + data.data + ")"))
        if (collect_school_list.arr.length == 0) {
            isNUll.value = true
        } else {
            isNUll.value = false
        }
    })

    requestFn({
        url: '/select_userInfo',
        method: 'post',
        data: {
            user: current_user
        }
    }).then(data => {
        userInfo.item = data.data[0]
    })

    requestFn({
        url: '/getUserArticle',
        method: 'post',
        data: {
            username: store.state.current_user
        }
    }).then(res => {
        console.log(res.data)
        if (res.data.length > 0) {
            isNUll.value = false
            article_list.item = res.data

        } else {
            isNUll.value = true
        }

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

        requestFn({
        url: '/getCollectSchool',
        method: 'post',
        data: {
            username: store.state.current_user
        }
    }).then(data => {
        collect_school_list.arr = (eval("(" + data.data + ")"))
        if (collect_school_list.arr.length == 0) {
            isNUll.value = true
        } else {
            isNUll.value = false
        }
    })
    })
}

const password1 = ref('')
const password2 = ref('')
const modifySecret = () => {
    if ((password1.value == password2.value) && ((password1.value != '' | null) & (password2.value != '' | null))) {
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
    if ((password1.value != '' || null) && (password2.value != '' || null)) {
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
}</style>