import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'
import store from './store/index.js'
import '../public/reset.css'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import locale from 'element-plus/es/locale/lang/zh-cn'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import {CountDown} from 'vant'
// import '@babel/polyfill'
const app=createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
  }
app.use(store).use(router)
app.use(CountDown)
app.use(ElementPlus,{locale})
// app.use(ElementPlus, { size: 'small', zIndex: 3000 })
app.mount('#app')
