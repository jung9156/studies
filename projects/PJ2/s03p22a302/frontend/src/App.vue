<template>
  <v-app>
    <div id="nav" class="d-flex justify-space-between">
      <div class="nav-logo">
        <router-link :to="{ name: 'Home' }">
          <img src="@/assets/logo.png" />
        </router-link>
      </div>

      <div class="nav-lists">
        <router-link class="header" :to="{ name: 'Heritage' }">문화재</router-link>
        <router-link class="header" :to="{ name: 'Community' }">게시판</router-link>
        <router-link class="header" :to="{ name: 'Maps' }">지도</router-link>
        <router-link v-show="!isLogin" class="header-user" :to="{ name: 'Login' }">로그인</router-link>
        <router-link v-show="isLogin" class="header-user" :to="{ name: 'Mypage' }">마이페이지</router-link>
        <a v-show="isLogin" class="header-user" @click="logout">로그아웃</a>
      </div>
    </div>
    <router-view class="router-view-margin" />
  </v-app>
</template>

<script>
import { mapGetters } from "vuex"
import { mapActions } from "vuex"

export default {
  name: "App",
  computed: {
    ...mapGetters(["isLogin"]),
  },
  methods: {
    ...mapActions(["logout"])
  }
};
</script>
<style type="text/css" lang="scss">
@import "@/assets/css/app.scss";
</style>
