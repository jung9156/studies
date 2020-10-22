import Vue from "vue";
import VueRouter from "vue-router";

import Home from "../views/Home.vue";
import CaseList from "../views/CaseList.vue";
import ReportInfo from "../views/ReportInfo.vue";
import MapMain from "../views/MapMain.vue";
import NoticeBoard from "../views/NoticeBoard.vue";
import NoticeWrite from "@/components/notice/NoticeWrite.vue";
import NoticeDetail from "@/components/notice/NoticeDetail.vue";
import NoticeModify from "@/components/notice/NoticeModify.vue";
import UserManagement from "../views/UserManagement.vue";
import HowToUse from "../views/HowToUse.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/caselist",
    name: "CaseList",
    component: CaseList,
  },
  {
    path: "/reportinfo",
    name: "ReportInfo",
    component: ReportInfo,
  },
  {
    path: "/mapmain",
    name: "MapMain",
    component: MapMain,
  },
  {
    path: "/noticeboard",
    name: "NoticeBoard",
    component: NoticeBoard,
  },
  {
    path: "/noticeWrite",
    name: "noticeWrite",
    component: NoticeWrite,
  },
  {
    path: "/noticeDetail",
    name: "noticeDetail",
    component: NoticeDetail,
  },
  {
    path: "/noticeModify",
    name: "noticeModify",
    component: NoticeModify,
  },
  {
    path: "/usermanagement",
    name: "usermanagement",
    component: UserManagement,
  },
  {
    path: "/howtouse",
    name: "howtouse",
    component: HowToUse,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
