import { createRouter, createWebHistory, useRoute, useRouter } from 'vue-router'
// import App from '@/App.vue'
import home from '@/views/home.vue'
import indexSchoolVue from '@/views/indexSchool.vue'
import major_list from '@/views/major_list.vue'
import searchResult from '@/views/searchResult.vue'
import schoolDetail from '@/views/schoolDetail.vue'
import schoolView from '@/components/schoolView.vue'
import reexamine from '@/components/reexamine.vue'
import zhaoshengxinxi from '@/components/zhaoshengxinxi.vue'
import community from '@/components/community.vue'
import majorDetail from '@/components/majorDetail.vue'
import AI from '@/views/AI.vue'
import personal from '@/views/Psersonal.vue'
import bigScreen from '@/views/bigScreen.vue'
import tools from '@/views/tools.vue'
import articleMain from '@/components/articleMain.vue'
import major_list_select from '@/views/major_list_select.vue'
import zuoti from '@/views/zuoti.vue'
const routes = [
  {
    path: '/home',
    name: 'home',
    component: home,
    meta: '{home:"首页"}'
  },
  {
    path: '/zuoti',
    name: 'zuoti',
    component: zuoti,
    meta: '{zuoti:"在线答题"}'
  },
  {
    path: '/bigScreen',
    name: 'bigScreen',
    component: bigScreen
  },
  {
    path: '/searchResult',
    name: 'searchResult',
    component: searchResult
  },
  {
    path: '/AI',
    name: 'AI',
    component: AI
  },
  {
    path: '/tools',
    name: 'tools',
    component: tools
  },
  {
    path: '/schoolDetail/:school_id',
    name: 'schoolDetail',
    // redirect:`/schoolDetail/:school_id/zhaoshengxinxi`,
    component: schoolDetail,
    children: [
      {
        path: 'schoolView',
        name: 'schoolView',
        component: schoolView,
        props: true
      },
      {
        path: 'reexamine',
        name: 'reexamine',
        component: reexamine,
        props: true
      },
      {
        path: 'zhaoshengxinxi',
        name: 'zhaoshengxinxi',
        component: zhaoshengxinxi,
      },
      {
        path: 'community',
        name: 'community',
        component: community,
      }, {
        path: 'majorDetail',
        // path:'majorDetail',
        name: 'majorDetail',
        component: majorDetail,
      }
    ]
  },
  {
    path: '/',
    name: 'indexSchoolVue',
    component: indexSchoolVue
  },
  {
    path:'/major_list_select',
    name:'major_list_select',
    component:major_list_select
  },
  {
    path: '/major_list',
    name: 'major_list',
    component: major_list,
    beforeEnter: (to, from, next) => {
      const isLogin = sessionStorage.getItem('vuex')
      if (!isLogin) {
        next({ path: '/' })
        alert('请您先登录，以浏览更多信息')
      } else {
        next()
      }
    }
  },
  {
    path: '/personal',
    name: 'personal',
    component: personal,
    beforeEnter: (to, from, next) => {
      let isLogin;
      try{
         isLogin =(JSON.parse(sessionStorage.getItem('vuex'))).isLogin
         console.log(isLogin,'当前登录状态')

      }catch(error){
        isLogin=false
      }
      console.log(isLogin)
      if (!isLogin) {
        next({ path: '/' })
      } else { next() }
    }
  },
  {
    path:'/articleDetail',
    name:'articleDetail',
    component:articleMain,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


export default router
