<template>
    <!-- 传送到id为back的位置 -->
    <teleport to='#back' >
    <div class="loader">
        <el-table v-loading="loading" element-loading-text="正在加载数据，请稍等" :element-loading-spinner="svg"
        element-loading-svg-view-box="-10, -10, 50, 50" element-loading-background="rgba(122, 122, 122, 0.8)"
        style="width: 100%;height: 1000px;">
    </el-table>
    </div>
    </teleport>
</template>

<script setup>
import { ref,onUnmounted } from 'vue'
const loading = ref(true)
const svg = `
        <path class="path" d="
          M 30 15
          L 28 17
          M 25.61 25.61
          A 15 15, 0, 0, 1, 15 30
          A 15 15, 0, 1, 1, 27.99 7.5
          L 15 15
        " style="stroke-width: 4px; fill: rgba(0, 0, 0, 0)"/>
      `

const node=document.createElement('div')
node.id='back'
document.body.appendChild(node)
onUnmounted(()=>{
    document.body.removeChild(node)
})
</script>
<style>
.loader{
    width: 100%;
    height: 100%;
    position: fixed;
    top: 0;left: 0;
    z-index: 999;
    text-align: center;
}
.el-loading-spinner{
    position: absolute;
    top: 20% !important;
}
</style>