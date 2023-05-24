<template>

    <div style="width:1200px; margin:20px auto;display: flex;align-items: center;" >
        <p style="font-size: 20px;">热议话题：</p>
        <span style="margin-right: 20px;font-size: 14px;" v-for="i of hotWord.item">{{ i }}</span>
    </div>
    <div  style="width:1200px; margin:20px auto;display: flex;align-items: center;">
        <img style="min-width:100%;" src="http://127.0.0.1:8000/media/wordcloud/wordcloud.png" alt="">
    </div>
    <el-backtop :right="100" :bottom="100" />
    <div class="muchText">
        <div class="wange" style="border: 1px solid #eee;">
            <Toolbar style="border-bottom: 1px solid #ccc" :editor="editorRef" :defaultConfig="toolbarConfig" />
            <Editor style="height:300px;overflow-y: hidden;" v-model="valueHtml" :defaultConfig="editorConfig"
                @onCreated="handleCreated" @onChange="handleChange" @onDestroyed="handleDestroyed" />
        </div>
        <el-button @click="insertText" color="#07AAFF" style="margin-top:20px;float:right;color: #fff;">发布</el-button>

    </div>
    <div class="community" v-for="i of article_list.item" >
        <!-- 顶部 -->
        <div class="community_top">
            <img :src=i.avator />
            <span>{{ i.username }}</span>
            <span>{{ i.cur_time }}</span>
        </div>
        <!-- 帖子主体 -->
        <div class="community_content" @click="toArticleDetail(i.id)">
            <p style="font-size: 20px;">
                {{ i.content }}
            </p>
            <ul>
                <li v-for="j of i.img_url">
                    <img :src=j alt="">
                </li>
            </ul>
        </div>


        <!-- 点赞数量，评论数量 -->
        <div class="community_bottom">
            <div class="dianzan" @click="dianzan(i.id)">
                <span>赞 {{ i.like }}</span>
                <svg v-if="isLikeIn(i.id)" t="1682426239288" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="2610" width="200" height="200">
                    <path
                        d="M508.765841 890.615107c-22.497387 0-239.805668-174.754093-322.129628-280.598746C130.011564 558.358841 84.231915 461.96442 84.231915 394.016889c0-144.30664 105.672738-261.651208 235.55997-261.651208 79.31851 0 146.614196 65.640999 188.169637 133.459594 41.529859-67.818595 108.825544-133.459594 188.16759-133.459594 129.888256 0 235.557924 117.344568 235.557924 261.651208 0 68.12354-46.020126 164.689876-102.881159 216.434377C745.698065 717.647707 532.525987 890.615107 508.765841 890.615107z"
                        fill="#fb2105" p-id="2611"></path>
                </svg>
                <svg v-else t="1682426786267" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="2909" width="200" height="200">
                    <path
                        d="M510.340709 900.892171c-23.173792 0-247.254314-180.180685-332.157006-289.301965-58.338686-53.264111-105.562221-152.650679-105.562221-222.732827 0-148.765185 108.952434-269.77626 242.874563-269.77626 81.781608 0 151.191444 67.679425 194.013739 137.605008 42.822294-69.925582 112.207571-137.605008 194.013739-137.605008 133.922129 0 242.874563 121.011074 242.874563 269.77626 0 70.239737-47.445592 169.805384-106.055454 223.182059C754.630505 722.553437 534.862195 900.892171 510.340709 900.892171zM315.497069 165.0685c-108.570741 0-196.887182 100.397594-196.887182 223.788879 0 58.382689 42.059931 145.353482 91.864244 189.903118 1.033539 0.943488 2.022053 1.977028 2.874467 3.098571 83.937714 109.042485 251.138784 234.421031 297.17119 267.923052 48.054459-34.715663 213.05542-161.193239 294.611901-267.451308 0.899486-1.12359 1.888-2.178619 2.964518-3.142573 50.03251-44.663222 92.312452-131.813095 92.312452-190.33086 0-123.391285-88.316441-223.788879-196.885136-223.788879-70.487378 0-137.808646 75.135234-173.241646 149.597133-7.634888 16.033162-33.908274 16.033162-41.543162 0C453.303668 240.203734 385.983423 165.0685 315.497069 165.0685z"
                        fill="#5D5D5D" p-id="2910"></path>
                </svg>
            </div>
            <div class="comment" @click="showComment">
                <span>评论 {{ i.comment_count }}</span>
                <svg t="1682159446703" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    p-id="2700" width="48" height="48">
                    <path
                        d="M519.110443 637.45734 339.641979 637.45734c-6.338359 0-11.477402-5.13802-11.477402-11.477402 0-6.337335 5.13802-11.478426 11.477402-11.478426l179.469488 0c6.337335 0 11.478426 5.13802 11.478426 11.478426C530.588869 632.318296 525.448802 637.45734 519.110443 637.45734z"
                        p-id="2701"></path>
                    <path
                        d="M670.981363 514.022053 339.641979 514.022053c-6.338359 0-11.477402-5.13802-11.477402-11.477402 0-6.338359 5.13802-11.477402 11.477402-11.477402l331.339384 0c6.338359 0 11.478426 5.13802 11.478426 11.477402C682.458765 508.885056 677.319721 514.022053 670.981363 514.022053z"
                        p-id="2702"></path>
                    <path
                        d="M574.334185 390.586766 339.641979 390.586766c-6.338359 0-11.477402-5.13802-11.477402-11.477402 0-6.339382 5.13802-11.477402 11.477402-11.477402l234.69323 0c6.337335 0 11.477402 5.13802 11.477402 11.477402C585.810564 385.448746 580.672544 390.586766 574.334185 390.586766z"
                        p-id="2703"></path>
                    <path
                        d="M919.060461 889.522216c-1.12973 0-2.270716-0.165776-3.38612-0.51063-0.62524-0.192382-63.340607-19.500123-123.917264-33.3035-6.179746-1.407046-10.048867-7.560186-8.639774-13.739932 1.407046-6.181793 7.563256-10.05296 13.740956-8.640798 37.45403 8.534374 75.674517 19.131733 99.956549 26.151613-7.981788-16.190751-18.782785-38.864146-28.837792-62.45954-35.845393-84.127026-32.279171-108.028389-25.168216-119.453602 33.617655-54.018288 51.387367-114.538663 51.387367-175.018106 0-190.297091-174.452217-345.115132-388.885008-345.115132-214.43893 0-388.897288 154.818041-388.897288 345.115132 0 194.506972 178.093141 358.831528 388.897288 358.831528 60.238966 0 118.250194-12.94073 172.424025-38.45994 5.732561-2.704598 12.573363-0.24457 15.274892 5.490038 2.701528 5.734608 0.2415 12.57234-5.492084 15.273868-57.255005 26.974351-118.557186 40.651862-182.205808 40.651862-55.288211 0-109.167329-10.429537-160.13821-31.000038-48.794309-19.690458-92.807732-47.75463-130.820488-83.408665-37.766139-35.422767-67.499323-76.343759-88.375793-121.627105-21.577434-46.806026-32.516578-95.842859-32.516578-145.750525 0-49.856501 10.958586-98.213859 32.573883-143.726425 20.827351-43.856857 50.615794-83.219353 88.537476-116.994598 77.726246-69.224618 180.978864-107.348913 290.740734-107.348913 109.75573 0 213.006302 38.124296 290.730501 107.348913 37.921681 33.775244 67.708078 73.138764 88.537476 116.994598 21.61325 45.51359 32.57286 93.869924 32.57286 143.726425 0 64.771189-18.968004 129.486096-54.853305 187.148377-0.916882 1.471514-7.952112 16.736173 26.748201 98.206696 18.646686 43.779086 39.96113 84.396155 40.173978 84.800361 2.159176 4.105504 1.636267 9.106402-1.327228 12.676717C925.673066 888.047632 922.415882 889.522216 919.060461 889.522216z"
                        p-id="2704"></path>
                </svg>
            </div>
        </div>

    </div>

</template>

<script setup>
import { ref, onBeforeUnmount, shallowRef, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"
import '@wangeditor/editor/dist/css/style.css' // 引入 css
import { Editor, Toolbar } from '@wangeditor/editor-for-vue'
import { DomEditor } from '@wangeditor/editor'
import requestFn from "@/api/requestFn.js"
import store from "@/store/index.js"
import router from "@/router/index.js"
import { ElMessage } from 'element-plus'
const centerDialogVisible = ref(false)
const isShowComment = ref(false)
const showComment = () => {
    isShowComment.value = !isShowComment.value
}


const article_content = reactive({ item: [] })
const article_list = reactive({ item: [] })
const editorRef = shallowRef();
const usercomment = ref('');
const isLogin = store.state.isLogin

const toArticleDetail=(e)=>{
    router.push({
        path:'/articleDetail',
        query:{
            article_id:e
        }
    })
}

const allComment = reactive({ item: [] })
const isLike = reactive({ item: [] })
// 内容 HTML
const valueHtml = ref()
const isLikeIn = (e) => {
    return isLike.item.includes(String(e))

}

const hotWord=reactive({item:[]})
onMounted(() => {
    requestFn({
        url: '/getPrivate',
        method: 'post',
        data: {
            username: store.state.current_user
        }
    }).then(res => {
        isLike.item = (((res.data[0][9]).split(',')).slice(0, ((res.data[0][9]).split(',')).length - 1))
    })

    requestFn({
        url:'/TF',
        method:'get'
    }).then(res=>{
        console.log(res.data)
        hotWord.item=res.data.final_word
    })

    request_post()
})


const request_post = () => {
    requestFn({
        url: '/article_list',
        method: 'get'
    }).then(res => {
        article_content.item = res.data
        article_content.item.forEach(val => {
            article_list.item.push({
                'username': val.username,
                'avator': `http://127.0.0.1:8000` + val.avator,
                'content': val.content,
                'img_url': val.img_url.map(value => 'http://127.0.0.1:8000/media/wangeditor/' + val.username + '/' + value),
                'like': val.like,
                'id': val.id,
                'cur_time': val.cur_time,
                'comment_count':val.comment_count
            })
        })
    })
    article_list.item.length = 0
    requestFn({
        url: '/getAllComment',
        method: 'get'
    }).then(res => {
        res.data.map((val) => {
            val.avator = 'http://127.0.0.1:8000' + val.avator
        })
        allComment.item = res.data
    })
}

const editorConfig = {
    MENU_CONF: {}
}
editorConfig.MENU_CONF['uploadImage'] = {
    // 上传图片的地址API
    server: 'http://127.0.0.1:8000/article_img',
    maxFileSize: '10*1024*1024',
    filedName: 'file',
    uploadImgMaxLength: 5,
    meta: {
        username: store.state.current_user
    }
}
editorConfig.placeholder = '请输入内容'

// 组件销毁时，也及时销毁编辑器
onBeforeUnmount(() => {
    const editor = editorRef.value
    if (editor == null) return
    editor.destroy()
})


const handleCreated = (editor) => {
    editorRef.value = editor
    // console.log('created', editor)
}
const handleChange = (editor) => {
    // console.log(editor.children[0].children[0].text)
    valueHtml.value = editor.children[0].children[0].text;
}
const handleDestroyed = (editor) => {
    // console.log('destroyed', editor) 
}


const insertText = () => {
    const editor = editorRef.value // 获取 editor ，必须等待它渲染完之后
    // if (editor == null) return
    // editor.insertText('hello world') // 执行 editor API
    if (isLogin) {
        requestFn({
            url: '/acticle_content',
            method: 'post',
            data: {
                article: valueHtml.value,
                username: store.state.current_user
            }
        }).then(data => {
            console.log(data.data)

        })

        valueHtml.value = ''
        request_post()

    } else {
        ElMessage.error('您还没有登录，请先登录！')
    }

}



const toolbarConfig = {

}


const dianzan = (e) => {

    requestFn({
        url: '/dianzan',
        method: 'post',
        data: {
            username: store.state.current_user,
            article_id: e
        }
    }).then(res => {
        requestFn({
            url: '/getPrivate',
            method: 'post',
            data: {
                username: store.state.current_user
            }
        }).then(res => {
            isLike.item = (((res.data[0][9]).split(',')).slice(0, ((res.data[0][9]).split(',')).length - 1))
            request_post()
        })

    }).catch(error=>{
        console.log(error)
        if(error.code==500){
            ElMessage.error('您还没有登录请先登录！')
        }
    })
}


</script>

<style scoped lang="less">
.muchText {
    width: 1200px;
    height: 500px;
    margin: 0 auto;
}

.community {

    width: 1200px;
    // height: 800px;
    margin: 50px auto;
    border: 1px solid #eee;
    padding: 20px;
    border-radius: 15px;

    .community_top {
        width: 100%;
        display: flex;
        align-items: center;

        img {
            width: 50px;
            height: 50px;
            border-radius: 50%;
        }

        span {
            &:nth-of-type(1) {
                margin-left: 30px;
                font-size: 20px;
                font-weight: bold;
            }

            &:nth-of-type(2) {
                margin-left: 900px;
            }

        }
    }

    .community_content {
        margin: 20px 0;
        border: 1px solid #eee;
        border-radius: 15px;
        padding: 20px;

        p {
            font-size: 16 px;
            margin: 20px;
        }

        ul {
            display: flex;
            justify-content: space-between;

            // background-color: yellow;
            li {
                margin: 0px auto;
                width: 400px;
                height: 400px;
                text-align: center;

                img {
                    vertical-align: middle;
                    // transform: scale(0.5);
                    max-width: 100%;
                    max-height: 100%;
                }
            }

        }

    }

    .comment_list {
        margin: 20px auto;

        li {
            border: 1px solid #eee;
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 20px;

            .userInfo {
                display: flex;
                align-items: center;


                img {
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    margin-right: 40px;
                }

                p {
                    font-size: 20px;
                    font-weight: bold;
                }
            }

            .comment_text {
                margin-top: 10px;
                font-size: 16px;
            }
        }
    }

    .community_bottom {
        display: flex;
        justify-content: space-around;
        margin-bottom: 20px;

        .dianzan {
            font-size: 16px;
            display: flex;
            align-items: center;

            span {
                margin-right: 20px;
            }

            svg {
                width: 30px !important;
                height: 30px !important;
            }
        }

        .comment {
            font-size: 16px;
            display: flex;
            align-items: center;

            span {
                margin-right: 20px;
            }

            svg {
                width: 30px !important;
                height: 30px !important;
            }
        }
    }
}
</style>