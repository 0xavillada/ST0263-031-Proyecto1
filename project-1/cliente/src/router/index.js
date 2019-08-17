import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login'
import registro from '@/components/registro'
import mainpage from '@/components/mainpage'
import editaruser from '@/components/editaruser'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/register',
      name: 'registro',
      component: registro
    },
    {
      path: '/mainpage',
      name: 'mainpage',
      component: mainpage,
      props: true
    },
    {
      path: '/edituser',
      name: 'editaruser',
      component: editaruser,
      props: true
    },
    {
      path: '/login',
      name: 'login',
      component: login
    }
  ],
  mode: 'history'
})
