<template>
  <div class="schoolLocation">
    <!-- 院校位置--开始 -->
    <div class="yxlocation">
      <el-row :gutter="24">
        <el-col :span="3">
          <div>
            <span>院校位置</span>
            <el-icon>
              <ArrowRight />
            </el-icon>
          </div>
        </el-col>
        <el-col :span="2">
          <div>
            全部
          </div>
        </el-col>
        <el-col :span="18">
          <!-- A区 -->
          <el-row :gutter="24">
            <el-col :span="4">A区</el-col>
            <el-col :span="20">
              <span @click="Abtn(v.name,k)" class="final_span" v-for="(v,k) of province_a.arr">{{ v.name }}</span>
            </el-col>
          </el-row>
          <!-- B区 -->
          <el-row :gutter="24">
            <el-col :span="4">B区</el-col>
            <el-col :span="20">
              <span @click="Bbtn(v.name,k)" class="final_span" v-for="(v,k) of province_b.arr">{{ v.name }}</span>
            </el-col>
          </el-row>
          <!-- 其他 -->
          <el-row :gutter="24">
            <el-col :span="4">其他</el-col>
            <el-col :span="20">
              <span @click="otherBtn(v.name,k)" class="final_span"  v-for="(v,k) of province_other.arr">{{ v.name }}</span>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
    </div>
    <!-- 院校位置--结束 -->


    <!-- 院校类型--开始 -->
    <div class="yxtype">
      <el-row :gutter="24">
        <el-col :span="3">
          <div>
            <span>院校类型</span>
            <el-icon>
              <ArrowRight />
            </el-icon>
          </div>
        </el-col>
        <el-col :span="2">
          <div>
            全部
          </div>
        </el-col>
        <el-col :span="18">
          <span @click="typeBtn(v.name,k)" class="final_span" v-for="(v,k) of allSchoolType.arr" :key="v.code">{{ v.name }}</span>
        </el-col>
      </el-row>
    </div>
    <!-- 院校类型--结束 -->



    <!-- 院校特色--开始 -->
    <div class="yxts">
      <el-row :gutter="24">
        <el-col :span="3">
          <div>
            <span>院校特色</span>
            <el-icon>
              <ArrowRight />
            </el-icon>
          </div>
        </el-col>
        <el-col :span="2">
          <div>
            全部
          </div>
        </el-col>
        <el-col :span="18">
          <span class="final_span" @click="tsBtn(v.name,k)" v-for="(v,k) of feature.arr">{{ v.name }}</span>
        </el-col>
      </el-row>
    </div>
    <!-- 院校特色--结束 -->
  </div>
</template>

<script setup>
import { ref, onMounted, reactive, watch,onUpdated } from "vue"
import requestFn from '@/api/requestFn.js'
      const allSchoolType=reactive({arr:[]})
      const province_a=reactive({arr:[]})
      const province_b=reactive({arr:[]})
      const province_other=reactive({arr:[]})
      const feature=reactive({arr:[]})

      const school_addition=reactive({
        Location:'',
        SchoolType:'',
        SchoolTs:'',
      })
      watch(school_addition,(newVal,oldVal)=>{
        console.log(newVal.Location,newVal.SchoolTs,newVal.SchoolType)
      })
      onMounted(()=>{
        requestFn({
          url:'allSchoolType',
          method:'get'
        }).then(data=>{
          // console.log(data.data)
          allSchoolType.arr=data.data
        })
        requestFn({
          url:'province_a',
          method:'get'
        }).then(data=>{
          // console.log(data.data)
          province_a.arr=data.data
        })
        requestFn({
          url:'province_b',
          method:'get'
        }).then(data=>{
          // console.log(data.data)
          province_b.arr=data.data
        })
        requestFn({
          url:'province_other',
          method:'get'
        }).then(data=>{
          // console.log(data.data)
          province_other.arr=data.data
        })

        requestFn({
          url:'allFeature',
          method:'get'
        }).then(data=>{
          feature.arr=data.data
        })


      })
      const Abtn=(v,k)=>{
        console.log(v,k)
        school_addition.Location=v
      }
      const Bbtn=(v,k)=>{
        console.log(v,k)
        school_addition.Location=v

      }
      const otherBtn=(v,k)=>{
        console.log(v,k)
        school_addition.Location=v
      }
      const typeBtn=(v,k)=>{
        console.log(v,k)
      }
      const tsBtn=(v,k)=>{
        console.log(v,k)
      }

</script>

<style lang="less" scoped>
.schoolLocation{
  border:1px solid #eee;
  border-radius: 15px;
  margin-bottom: 20px;
  margin-left: 80px;
}
.final_span{
  margin-right: 20px;
}
.final_span:hover{
  cursor: pointer;
}
.commonCss() {
  padding: 10px 10px;
  width: 100%;
  // height: 200px;

  .el-row {
    .el-col {
      &:nth-of-type(1) {
        div {
          display: flex;
          // 中轴
          align-items: center;
          // 主轴
          justify-content: center;
          // background-color: blue;

          span {
            font-size: 14px;
            margin-right: 20px;
          }

          .el-icon {
            color: gray;
          }
        }
      }

      &:nth-of-type(2) {}
      font-size: 14px;
        div:hover{
          cursor: pointer;
        }
      &:nth-of-type(3) {
        .el-row {
          margin-bottom: 30px;
          font-size: 14px;

          .el-col {
            &:nth-of-type(2) {
              span {
                font-size: 14px;
                margin-right: 15px;

              }
            }
          }
        }
      }
    }
  }
}

.yxlocation {

  .commonCss

}

.yxtype {
  .el-row{
    .el-col{
      font-size: 14px;
    }
  }
  .commonCss
  
}

.yxts {
  margin-top: 50px;
  .el-row{
    .el-col{
      font-size: 14px;
    }
  }
  .commonCss
}
</style>
