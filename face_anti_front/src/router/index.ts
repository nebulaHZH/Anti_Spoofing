import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: ()=>import('../views/Nav.vue'),
    children:[
      {
        path:'/login',
        name:'login',
        component:()=>import('../components/userLogin.vue')
      },
      {
        path:'/datasetPicture',
        name:'datasetPicture',
        component:()=>import('../components/datasetPicture.vue')
      },
      {
        path:'/datasetVedio',
        name:'datasetVedio',
        component:()=>import('../components/datasetVedio.vue')
      },
      {
        path:'/load',
        name:'load',
        component:()=>import('../components/load.vue')
      },
      {
        path:'/onlineAlaysis',
        name:'onlineAlaysis',
        component:()=>import('../components/onlineAlaysis.vue')
      },
      {
        path:'/setting',
        name:'setting',
        component:()=>import('../components/setting.vue')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
