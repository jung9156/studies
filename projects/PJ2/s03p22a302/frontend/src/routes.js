import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from "@/views/Home.vue"
import Login from "@/views/Login"
import Community from "@/views/Community"
import CommunityReviewItem from "@/components/community/CommunityReviewItem"
import Heritage from "@/views/Heritage"
import Maps from "@/views/Maps"
import Signup from "@/views/Signup"
import Mypage from "@/views/Mypage"

Vue.use(VueRouter)

const routes =  [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/heritage",
    name: "Heritage",
    component: Heritage,
  },
  {
    path: "/community",
    name: "Community",
    component: Community,
  },
  {
    path: "/community/:id",
    name: "CommunityReviewItem",
    component: CommunityReviewItem
  },
  {
    path: "/maps",
    name: "Maps",
    component: Maps,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/mypage",
    name: "Mypage",
    component: Mypage,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router