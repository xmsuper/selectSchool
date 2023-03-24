import { createRouter, createWebHistory } from 'vue-router'
import App from '@/App.vue'
import home from '@/views/home.vue'
import indexSchoolVue from '@/views/indexSchool.vue'
import major_list from '@/views/major_list'
const routes = [
  // {
  //   path:'/index',
  //   name:index,
  //   component:indexSchoolVue
  // },
  {
    path:'/home',
    name:home,
    component:home
  },
  {
    path:'/',
    name:indexSchoolVue,
    component:indexSchoolVue
  },
  {
    path:'/major_list',
    name:major_list,
    component:major_list
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
