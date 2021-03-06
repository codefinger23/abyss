import Vue from 'vue'
import Router from 'vue-router'
import Index from "@/views/home/Index.vue"
import Signin from "@/views/home/Signin.vue"
import Signup from "@/views/home/Signup.vue"

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', redirect: '/index'},
    { path: '/index', component: Index},
    { path: '/signin', component: Signin},
    { path: '/signup', component: Signup}
  ]
})
