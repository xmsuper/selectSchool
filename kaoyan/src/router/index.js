import { createRouter, createWebHistory,useRoute,useRouter } from 'vue-router'
import App from '@/App.vue'
import home from '@/views/home.vue'
import indexSchoolVue from '@/views/indexSchool.vue'
import major_list from '@/views/major_list'
import searchResult from '@/views/searchResult.vue'
import schoolDetail from '@/views/schoolDetail.vue'
import schoolView from '@/components/schoolView.vue'
import reexamine from '@/components/reexamine.vue'
import zhaoshengxinxi from '@/components/zhaoshengxinxi.vue'
import community from '@/components/community.vue'
const routes = [
  {
    path:'/home',
    name:'home',
    component:home
  },
  {
    path:'/searchResult',
    name:'searchResult',
    component:searchResult
  },
  {
    path:'/schoolDetail/:school_id',
    name:'schoolDetail',
    // redirect:'schoolView',
    component:schoolDetail,
    children:[
      {
        path:'schoolView',
        name:'schoolView',
        component:schoolView,
        props:true
      },
      {
        path:'reexamine',
        name:'reexamine',
        component:reexamine,
        props:true
      },
      {
        path:'zhaoshengxinxi',
        name:'zhaoshengxinxi',
        component:zhaoshengxinxi,
      },
      {
        path:'community',
        name:'community',
        component:community,
      }
    ]
  },
  {
    path:'/',
    name:'indexSchoolVue',
    component:indexSchoolVue
  },
  {
    path:'/major_list',
    name:'major_list',
    component:major_list
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
