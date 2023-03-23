<template>
    <label>
        <svg t="1679202718226" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
            p-id="2802" width="200" height="200">
            <path
                d="M505.284 601.305c-103.659 0-187.992-84.333-187.992-187.992 0-103.659 84.333-187.992 187.992-187.992s187.992 84.333 187.992 187.992c0 103.659-84.333 187.992-187.992 187.992z m0-311.984c-68.37 0-123.992 55.623-123.992 123.992s55.623 123.992 123.992 123.992 123.992-55.623 123.992-123.992c0-68.37-55.623-123.992-123.992-123.992zM317.282 930.421l-82.075-142.858-143.301-21.24 131.835-197.712 53.248 35.506-75.816 113.702 74.084 10.98 44.231 76.989 60.713-97.515 54.33 33.827z"
                fill="" p-id="2803"></path>
            <path
                d="M505.284 752.984c-45.841 0-90.328-8.985-132.225-26.706-40.452-17.109-76.774-41.597-107.959-72.781s-55.671-67.507-72.781-107.959c-17.721-41.897-26.706-86.384-26.706-132.225s8.985-90.328 26.706-132.226c17.11-40.452 41.597-76.774 72.781-107.958s67.507-55.672 107.958-72.781c41.897-17.721 86.384-26.707 132.226-26.707s90.328 8.985 132.226 26.707c40.452 17.109 76.774 41.597 107.959 72.781s55.672 67.507 72.781 107.958c17.721 41.897 26.706 86.384 26.706 132.226s-8.985 90.328-26.706 132.225c-17.109 40.452-41.597 76.774-72.781 107.959s-67.508 55.672-107.959 72.781c-41.898 17.721-86.384 26.706-132.226 26.706z m0-615.343c-152.006 0-275.671 123.666-275.671 275.672 0 152.005 123.666 275.671 275.671 275.671s275.672-123.666 275.672-275.671c0-152.006-123.666-275.672-275.672-275.672z"
                fill="" p-id="2804"></path>
            <path
                d="M705.624 928.421L588.375 740.1l54.33-33.827 60.712 97.515 44.231-76.989 74.085-10.98-75.816-113.702 53.248-35.506 131.834 197.712-143.301 21.24z"
                fill="" p-id="2805"></path>
        </svg>
        <span>热搜院校推荐</span>
    </label>
    <div class="hotSearchItem">
        <ul>
            <li v-for="(i,index) of hotSearch.arr">
                <span>{{ index+1 }}</span>
                <img :src=i.school_name.school_img>
                <div>
                    <span>{{i.school_name.school_name}}</span>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
import { defineComponent, DefineComponent,onMounted,ref,reactive } from 'vue';
import requestFn from '@/api/requestFn.js'
export default defineComponent({
setup(){
    const hotSearch=reactive({arr:[]})
    requestFn({
        url:'hotSchool',
        method:'get'
    }).then(data=>{
        hotSearch.arr=data.data
    })

    return{
        hotSearch
    }
  }
})
</script>

<style lang="less" scoped>
label {
    margin-top: 10px;
    display: flex;
    justify-content: flex-start;
    align-items: center;

    span {
        font-size: 20px;
        font-weight: 700;
    }

    svg {
        width: 25px;
        height: 20px;
    }
}

.hotSearchItem {
    ul {
        li {
            margin-left: 20px;
            display: flex;
            overflow: hidden;
            padding: 30px 40px 0 0;

            span {
                margin-right: 20px;
                width: 20px;
                height: 20px;
                background-color: red;
                color: white;
                text-align: center;
                border-radius: 5px;
                line-height: 20px;
            }

            img {
                width: 21px;
                height: 21px;
                margin-right: 20px;
                transition-duration: 1s;

            }

            div {
                span {
                    font-size: 14px;
                    background-color: white;
                    color: #000000;
                }
            }
        }

        li:hover {
            cursor: pointer;
            padding: 50px 0;

            img {
                transform: scale(3);
            }

            span {
                margin-right: 40px;
            }

            div {
                margin-left: 20px;
            }
        }
    }
}</style>
