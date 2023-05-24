<template>
  <div class="formSubmit">
    <h2>基础信息</h2>
    <el-button color="#07AAFF" style="float: right;color: #fff;" @click="edit">编辑</el-button>
    <el-form :model="form">
      <el-form-item v-if="!isShow" label="头像上传">
        <el-upload v-model="form.avatar" class="avatar-uploader" :auto-upload="false" :on-change="handleChange"
          :headers=headers :show-file-list="false" with-credentials>
          <!-- <img v-if="!imageUrl" :src="imageUrl" class="avatar" /> -->
          <img v-if="isShowImage" src="../assets/头像.svg" class="avatar" />
          <img v-else :src="imageUrl" class="avatar" />
          <!-- <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon> -->
        </el-upload>
      </el-form-item>
      <el-form-item>
        <p>昵称:</p><span v-if="isShow">{{ personalInfo?.item[0]}}</span>
        <el-input v-else v-model="form.modifyName" class="w-20" placeholder="请输入昵称" />
      </el-form-item>
      <el-form-item>
        <p>性别:</p><span v-if="isShow">{{ personalInfo?.item[1] }}</span>
        <el-radio-group v-else v-model="form.gender">
          <el-radio label="男" />
          <el-radio label="女" />
        </el-radio-group>
      </el-form-item>
      <el-form-item>
        <p>报考年份:</p><span v-if="isShow">{{ personalInfo?.item[2] }}</span>
        <!-- <el-date-picker @change="gotyear" v-else v-model="form.year" type="year" placeholder="选择年份" /> -->
        <el-date-picker v-else  v-model="form.year" type="year" placeholder="Pick a year" />
      </el-form-item>
      <el-form-item>
        <p>所学专业：</p><span v-if="isShow">{{ personalInfo?.item[6] }}</span>
        <el-input v-else v-model="form.currentMajor" placeholder="请输入所学专业" />
      </el-form-item>
      <el-form-item>
        <p>报考类型：</p><span v-if="isShow">{{ personalInfo?.item[5] }}</span>
        <el-radio-group v-else v-model="form.learnType">
          <el-radio label="学术型硕士" />
          <el-radio label="专业型硕士" />
        </el-radio-group>
      </el-form-item>
      <el-form-item>
        <p>所在院校：</p><span v-if="isShow">{{ personalInfo?.item[7]}}</span>
        <el-input v-else v-model="form.currentSchool" placeholder="" />
      </el-form-item>
      <el-form-item>
        <p>报考院校: </p><span v-if="isShow">{{ personalInfo?.item[3] }}</span>
        <el-cascader v-else v-model="form.joinSchool" :options="school_name_choose" @change="handleChangeJilian" />
      </el-form-item>
      <el-form-item>
        <p>报考专业: </p><span v-if="isShow">{{ personalInfo?.item[4]}}</span>
        <el-cascader v-else v-model="form.joinMajor" :options="major_name_choose" @change="handleMajorChangeJilian" />
      </el-form-item>
      <el-form-item>
        <el-button v-if="!isShow" type="primary" @click="onSubmit">提交</el-button>
      </el-form-item>
    </el-form>
  </div>

</template>

<script setup>
import { ref, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"
import { Plus } from '@element-plus/icons-vue'
import requestFn from "@/api/requestFn";
import axios from "axios";
import store from "@/store";
import { useRouter, useRoute } from "vue-router";
import { ElMessage } from 'element-plus'


const isShowImage=ref(true)
const router = useRouter()
const isShow = ref(true)
const edit = () => {
  isShow.value = !isShow.value
  // imageUrl.value=false
}
const imageUrl = ref('')
const headers = reactive({
  'Content-Type': 'multipart/form-data'
})


const form = reactive({
  avatar: [],
  currentMajor: store.state.userInfo[0][6],
  currentSchool: store.state.userInfo[0][7],
  year: store.state.userInfo[0][2],
  gender: store.state.userInfo[0][1],
  joinMajor: store.state.userInfo[0][4],
  joinSchool: store.state.userInfo[0][3],
  learnType: store.state.userInfo[0][5],
  modifyName: ''
})


const currentUserName = ref(store.state.current_user)
form.modifyName = currentUserName
const handleChange = (file, fileList) => {
  // 上传文件推入到图库中
  form.avatar.length = 0
  form.avatar = fileList



  const formdata=new FormData();
  fileList.forEach((val,index)=>{
    formdata.append('file',val.raw)
  })

  axios({
    url: 'http://127.0.0.1:8000/upload_review',
    method: "post",
    data: formdata,
  }).then(data => {
    isShowImage.value=false
    imageUrl.value = 'http://127.0.0.1:8000/' + data.data.url_upload_file
  })

}

const fd = new FormData();

const onSubmit = () => {
  if(String(form.year).split(" ").length>2){
    form.year=form.year.getFullYear()
    fd.append('year', form.year)
  }else{
    fd.append('year', form.year)
  }
  fd.append('username', store.state.current_user)
  form.avatar.forEach((val, index) => {
    fd.append('file', val.raw)
  })
  fd.append('modifyName', form.modifyName)
  fd.append('learnType', form.learnType)
  fd.append('currentMajor', form.currentMajor)
  fd.append('currentSchool', form.currentSchool)

  fd.append('gender', form.gender)
  fd.append('joinMajor', form.joinMajor)
  fd.append('joinSchool', form.joinSchool)

  const token=localStorage.getItem('token')
  axios({
    url: 'http://127.0.0.1:8000/upload_avator',

    method: "post",
    headers: { 'Content-Type': 'multipart/form-data' , 'token': token},
    data: fd,
  }).then(data => {
    isShowImage.value=false
    imageUrl.value = 'http://127.0.0.1:8000/' + data.data.upload_url
    store.commit('setCurrent_user', data.data.username)
    personInfo()
    router.go(0)
  })
  fd.delete('username')
  fd.delete('file')
  fd.delete('learnType')
  fd.delete('currentMajor')
  fd.delete('currentSchool')
  fd.delete('year')
  fd.delete('gender')
  fd.delete('joinMajor')
  fd.delete('joinSchool')

}

let school_name_choose = []
let major_name_choose = []
onMounted(() => {

  requestFn({
    url: '/provinceSchool',
    method: 'get'
  }).then(res => {
    school_name_choose = res.data
  })
  requestFn({
    url: '/majorChoose',
    method: 'get'
  }).then(res => {
    major_name_choose = res.data
  })
  personInfo()
})


const personalInfo = reactive({ item: [] })

const personInfo = () => {
  requestFn({
    url: '/getPrivate',
    method: 'post',
    data: {
      username: store.state.current_user
    }
  }).then(res => {
    personalInfo.item = res.data[0]
    if(res.data[0][8]==''|null){
      isShowImage.value=true
    }
    else{
      isShowImage.value=false
      imageUrl.value = 'http://127.0.0.1:8000/'+ res.data[0][8]

    }
    
  }).catch(error=>{
    console.log(error)
    if(error.code==500){
      ElMessage.error('无效，非法的token，请退出重新登录')
    }
  })
}

const handleChangeJilian = (e) => {
  form.joinSchool = e['1']
}
const handleMajorChangeJilian = (e) => {
  form.joinMajor = e['2']
}
</script>

<style scoped lang="less">
.avatar-uploader .el-upload {
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
  border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  text-align: center;
}

.el-form-item {
  display: flex;

  p {
    margin-right: 20px;
  }
}

.formSubmit {
  width: 95%;
  margin: 0px auto;
}
.avatar{
  width: 100px;
  height: 100px;
  border-radius: 50%;
}
</style>