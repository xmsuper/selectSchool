<template>
    
    <div class="majordetail" v-for="i of school_info.arr">
        <div class="pm" v-if="i.recruit_name=='全日制'" >
            <div class="majordetail-title">[{{ i.special_code }}]{{ i.special_name }}<span>{{ i.recruit_name }}</span>
            </div>
            <div class="majordetail-major">
                <p>专业信息</p>
                <div class="majordetail-major-list">
                    <el-row>
                        <el-col :span="10">
                            <div><span>所属院校：</span>{{i.school_name}}</div>
                            <div><span>学习方式：</span>{{i.recruit_type}}</div>
                            <div><span>所属一级学科：</span>[{{i.level2_code}}]{{i.level2}}</div>
                        </el-col>
                        <el-col :span="10">
                            <div><span>招生年份:</span>{{i.year}}</div>
                            <div><span>所属门类：</span>[{{i.level1_code}}]{{i.level1}}</div>
                            <div><span>统考计划招生人数：</span>{{i.recruit_number}}</div>
                        </el-col>
                    </el-row>
                </div>
            </div>

            <div class="majordetail-exam">
                <p>考试科目</p>
                <div class="majordetail-exam-list">
                    <el-row>
                        <el-col :span="4">研究方向</el-col>
                        <el-col :span="20">{{i.subject1}}</el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="4">初始科目</el-col>
                        <el-col :span="20">
                            <p v-for="j of i.subject2.split('<br/>')">{{ j }}</p>
                        </el-col>
                    </el-row>
                </div>
            </div>
        </div>
        <div class="am" v-if="i.recruit_name=='非全日制'" >
            <div class="majordetail-title">[{{ i.special_code }}]{{ i.special_name }}<span>{{ i.recruit_name }}</span>
            </div>
            <div class="majordetail-major">
                <p>专业信息</p>
                <div class="majordetail-major-list">
                    <el-row>
                        <el-col :span="10">
                            <div><span>所属院校：</span>{{i.school_name}}</div>
                            <div><span>学习方式：</span>{{i.recruit_type}}</div>
                            <div><span>所属一级学科：</span>[{{i.level2_code}}]{{i.level2}}</div>
                        </el-col>
                        <el-col :span="10">
                            <div><span>招生年份:</span>{{i.year}}</div>
                            <div><span>所属门类：</span>[{{i.level1_code}}]{{i.level1}}</div>
                            <div><span>统考计划招生人数：</span>{{i.recruit_number}}</div>
                        </el-col>
                    </el-row>
                </div>
            </div>

            <div class="majordetail-exam">
                <p>考试科目</p>
                <div class="majordetail-exam-list">
                    <el-row>
                        <el-col :span="4">研究方向</el-col>
                        <el-col :span="20">{{i.subject1}}</el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="4">初始科目</el-col>
                        <el-col :span="20">
                            <p v-for="j of i.subject2.split('<br/>')">{{ j }}</p>
                        </el-col>
                    </el-row>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive, nextTick, computed, watch, onMounted, onUpdated } from "vue"
import { useRoute, useRouter } from 'vue-router'
import requestFn from '@/api/requestFn.js'
const route = useRoute()
const school_info=reactive({arr:[]})
onMounted(()=>{
    requestFn({
        url:'/major_detail',
        method:'post',
        data:{
            depart_id:route.query.depart_id,
            special_id:route.query.special_id,
            school_id:route.params.school_id
        }
    }).then(data=>{
        school_info.arr=(eval("("+data.data+")"))
        // console.log()
    })
})

</script>

<style scoped lang="less">
.majordetail {
    width: 1200px;
    margin: 20px auto;
    .pm{
        border:1px solid #ff6600;
        padding: 20px;
        border-radius: 15px;
        .majordetail-title {
        width: 1200px;
        height: 40px;
        font-size: 20px;
        font-weight: 700;
        color: #000;

        span {
            float: right;
            color: #ff6600;
            margin-right: 900px;
            font-size: 25px;
        }
    }

    .majordetail-major {
        p {
            border-left: 5px solid #ff6600;
            font-size: 20px;
            font-weight: 700;
            color: #000;
        }

        .majordetail-major-list {
            margin-top: 10px;

            padding: 40px 40px;
            border: 1px solid #eee;
            border-radius: 15px;

            .el-row {
                .el-col {
                    font-size: 14px;

                    div {
                        span {
                            font-size: 14px;
                            font-weight: 700;
                            margin-right: 5px;
                        }
                    }
                }
            }
        }
    }

    .majordetail-exam {
        margin-top: 20px;

        p {
            font-size: 20px;
            font-weight: 700;
            color: #000;
            border-left: 5px solid #ff6600;
        }

        .majordetail-exam-list {
            margin-top: 10px;
            padding: 40px 40px;
            border: 1px solid #eee;
            border-radius: 15px;

            .el-row {
                margin-top:20px;
                p {
                    border: 0;
                    font-weight: 400;
                    font-size: 14px;
                }

                .el-col {
                    font-size: 14px;

                    &:nth-of-type(1) {
                        font-size: 14px;
                        font-weight: 700;
                    }
                }
            }
        }

    }
    }

    .am{
        border:1px solid #ff6600;
        padding: 20px;
        border-radius: 15px;
        margin-top:50px;
        .majordetail-title {
        width: 1200px;
        height: 40px;
        font-size: 20px;
        font-weight: 700;
        color: #000;

        span {
            float: right;
            color: #ff6600;
            margin-right: 900px;
            font-size: 25px;
        }
    }

    .majordetail-major {
        p {
            border-left: 5px solid #ff6600;
            font-size: 20px;
            font-weight: 700;
            color: #000;
        }

        .majordetail-major-list {
            margin-top: 10px;

            padding: 40px 40px;
            border: 1px solid #eee;
            border-radius: 15px;

            .el-row {
                .el-col {
                    font-size: 14px;

                    div {
                        span {
                            font-size: 14px;
                            font-weight: 700;
                            margin-right: 5px;
                        }
                    }
                }
            }
        }
    }

    .majordetail-exam {
        margin-top: 20px;

        p {
            font-size: 20px;
            font-weight: 700;
            color: #000;
            border-left: 5px solid #ff6600;
        }

        .majordetail-exam-list {
            margin-top: 10px;
            padding: 40px 40px;
            border: 1px solid #eee;
            border-radius: 15px;

            .el-row {

                p {
                    border: 0;
                    font-weight: 400;
                    font-size: 14px;
                }

                .el-col {
                    font-size: 14px;

                    &:nth-of-type(1) {
                        font-size: 14px;
                        font-weight: 700;
                    }
                }
            }
        }

    }
    }



}</style>