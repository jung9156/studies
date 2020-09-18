<template>
  <div id="nav-bar">
    <div
      id="main-logo"
      class="d-none d-md-block text-center bg-white border-bottom"
      style="height:75px"
    >
      <a href="/" style="text-decoration: none;">
        <img
          src="@/assets/logos/Logo_1.png"
          class="my-2"
          alt="logo-image"
          style="height:75%; width:auto;"
        />
      </a>
    </div>
    <div>
      <b-navbar toggleable="md" class="py-1 shadow-sm" type="light" variant="white">
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <!-- 분민 로고 -->
        <div class="ml-auto d-md-none" style="height:56px">
          <a href="/">
            <img
              src="@/assets/logos/Logo_ico.png"
              alt="mini-logo-image"
              style="height:100%; rgba:(0,0,0,0)"
            />
          </a>
        </div>

        <!-- 그리드 축소 상태 사용자 버튼 -->
        <b-navbar-nav id="sm-user" class="ml-auto mr-2 my-0 py-0">
          <b-nav-item class="d-md-none ft-nns light">
            <b-nav-item
              id="nav-user-item"
              v-if="this.$session.get('email') == null"
              v-b-modal.modal-1
            >
              <b-icon icon="power"></b-icon>
              <a>&nbsp;로그인</a>
            </b-nav-item>

            <a
              v-if="this.$session.get('email') != null"
              v-b-toggle
              href="#user-collapse"
              @click.prevent
              class="text-decoration-none py-0"
            >
              <b-nav-item id="nav-user-item">
                <b-icon icon="person-circle"></b-icon>
                <span v-if="this.$session.get('email') == 'admin'">&nbsp;관리자</span>
                <span v-else>&nbsp;{{ name }}</span>
              </b-nav-item>
            </a>
          </b-nav-item>
        </b-navbar-nav>

        <b-collapse id="nav-collapse" class="justify-content-center" is-nav>
          <b-navbar-nav class="w-100 justify-content-between" style="max-width:1080px">
            <b-nav-item to="/caselist">
              <b-icon icon="list"></b-icon>
              <span class>&nbsp;제보목록</span>
            </b-nav-item>
            <b-nav-item to="/reportinfo">
              <b-icon icon="bar-chart"></b-icon>
              <span>&nbsp;제보현황</span>
            </b-nav-item>
            <b-nav-item to="/mapmain">
              <b-icon icon="map"></b-icon>
              <span>&nbsp;지도보기</span>
            </b-nav-item>
            <b-nav-item to="/noticeboard">
              <b-icon icon="info-circle"></b-icon>
              <span>&nbsp;공지사항</span>
            </b-nav-item>
            <b-nav-item to="/howtouse">
              <b-icon icon="question-circle"></b-icon>
              <span>&nbsp;이용방법</span>
            </b-nav-item>

            <!-- 사용자 버튼 -->
            <li class="d-none d-md-block">
              <!-- 비로그인 상태 -->
              <b-nav-item v-if="this.$session.get('email') == null" v-b-modal.modal-1>
                <b-icon icon="power"></b-icon>
                <a>&nbsp;로그인</a>
              </b-nav-item>

              <!-- 로그인 상태 -->
              <b-nav-item-dropdown v-if="this.$session.get('email') != null" right no-caret>
                <template v-slot:button-content>
                  <b-icon icon="person-circle"></b-icon>
                  <span>&nbsp;{{ name }}</span>
                </template>

                <div v-if="this.$session.get('email') == 'admin'">
                  <b-dropdown-item class="p-0 m-0" to="usermanagement/">
                    <b-icon icon="people"></b-icon>
                    <span>&nbsp;회원관리</span>
                  </b-dropdown-item>
                  <hr class="mx-0 px-0" />
                </div>

                <b-dropdown-item v-if="!this.$session.get('isSNS')" v-b-modal.modal-memberInfo>
                  <b-icon icon="person-lines-fill"></b-icon>
                  <span>&nbsp;회원정보 수정</span>
                </b-dropdown-item>
                <hr />

                <b-dropdown-item v-on:click="sessionDistroy">
                  <i class="fas fa-running fa-lg"></i>
                  <span>&nbsp;로그아웃</span>
                </b-dropdown-item>
              </b-nav-item-dropdown>
            </li>
          </b-navbar-nav>
        </b-collapse>

        <!-- 모달 -->
        <div>
          <!-- 로그인 -->
          <LoginModal />
          <!-- 이메일 찾기 -->
          <SearchEmail />
          <!-- 비밀번호 찾기 -->
          <SearchPassword />
          <!-- 회원가입 -->
          <SignUp />
          <!-- 회원정보 -->
          <MemberInfo />
        </div>
      </b-navbar>

      <!-- 토글시 사용자 드랍다운 구역 -->
      <b-collapse class="bg-white border boder-bottom d-md-none" id="user-collapse">
        <div class="p-3" style="list-style: none; height:75%">
          <b-dropdown-item
            v-if="this.$session.get('email') == 'admin'"
            class="p-0 m-0"
            to="usermanagement/"
          >
            <b-icon icon="people"></b-icon>
            <span>&nbsp;회원관리</span>
            <hr />
          </b-dropdown-item>

          <b-dropdown-item v-if="!this.$session.get('isSNS')" v-b-modal.modal-memberInfo>
            <b-icon icon="person-lines-fill"></b-icon>
            <span>&nbsp;회원정보 수정</span>
          </b-dropdown-item>
          <hr />

          <b-dropdown-item v-on:click="sessionDistroy">
            <i class="fas fa-running fa-lg"></i>
            <span>&nbsp;로그아웃</span>
          </b-dropdown-item>
        </div>
      </b-collapse>
    </div>
  </div>
</template>

<script>
import http from "@/util/http-common";
import { mapGetters } from "vuex";

import LoginModal from "@/components/layout/navs/LoginModal.vue";
import SearchEmail from "@/components/layout/navs/SearchEmail.vue";
import SearchPassword from "@/components/layout/navs/SearchPassword.vue";
import SignUp from "@/components/layout/navs/SignUp.vue";
import MemberInfo from "@/components/layout/navs/MemberInfo.vue";

export default {
  name: "NavBar",
  props: {
    type: { type: String },
  },
  components: {
    LoginModal,
    SearchEmail,
    SearchPassword,
    SignUp,
    MemberInfo,
  },
  data: function () {
    return {
      // 백엔드에서 필요로 하는 데이터
      email: this.$session.get("email"),
      pw: "", // 백엔드로 보낼 때 password 변수에 담아서 ex) password: this.pw
      pw_re: "",
      name: this.$session.get("name"),
      gender: this.$session.get("gender"),
      birth: this.$session.get("birth"),
      phone: this.$session.get("phone"),

      // 토큰 관리
      jwt: module.require("jsonwebtoken"),
      access_token: this.$route.query.token,
      redirectURI: "http://localhost:8399/ssafy/api/sns/login",
      state: 123,
      naverLoginURL:
        "https://nid.naver.com/oauth2.0/authorize?response_type=code",
    };
  },
  computed: {
    ...mapGetters(["violationitems"]),
  },
  methods: {
    sessionDistroy() {
      if (this.access_token != null) {
        http.post(`/sns/logout`).then(({ data }) => {
          if (data == "success") {
            alert("로그아웃 " + data);
          }
        });
      }
      this.$session.destroy();
      this.jwt = "";
      this.access_token = "";
      this.email = "";
      this.pw = "";
      this.name = "";
      this.birth = "";
      this.phone = "";
      this.joindate = "";
      this.$router.push("/");
      this.$router.go();
    },
  },
  created() {
    // 네이버 로그인
    if (this.access_token != null) {
      this.$session.set("userNo", this.jwt.decode(this.access_token).userNo);
      this.$session.set("email", this.jwt.decode(this.access_token).email);
      this.$session.set("isSNS", this.jwt.decode(this.access_token).isSNS);
      this.$session.set("name", this.jwt.decode(this.access_token).name);
      this.$session.set("token", this.access_token);
      this.name = this.jwt.decode(this.access_token).name;
    }
  },
};
</script>

<style scoped>
#nav-user-item > .nav-link {
  padding: 0;
}
</style>
