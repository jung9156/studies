<template>
  <b-modal id="modal-1" title="로그인" style="padding: 16px 32px;" hide-footer>
    <div class="modal-body">
      <form @submit.prevent>
        <div class="form-group">
          <input
            type="text"
            class="form-control ft-nss light"
            id="email"
            ref="email"
            placeholder="이메일을 입력하세요"
            v-model="email"
          />
        </div>
        <div class="form-group">
          <input
            @keypress.enter="checkHandlerLogin"
            type="password"
            class="form-control ft-nss light"
            id="pw"
            ref="pw"
            placeholder="비밀번호를 입력하세요"
            v-model="pw"
          />
        </div>
        <div class="form-group">
          <!-- 로그인 버튼 -->
          <a
            class="btn text-decoration-none m-auto"
            @click="checkHandlerLogin"
            style="width: 100%; height: 50px; background-color:#0f4c81"
          >
            <p style="color: white; font-size: 20px; margin-top: 4px;">로그인</p>
          </a>
          <br />
          <hr />
          <!-- 네이버 로그인 버튼 -->
          <div class="text-center font-italic text-muted">
            <p>혹은</p>
          </div>
          <div class="text-center">
            <img
              @click="naverLogin"
              width="50%"
              style="cursor: pointer;"
              src="https://developers.naver.com/doc/review_201802/CK_bEFnWMeEBjXpQ5o8N_20180202_7aot50.png"
            />
          </div>
        </div>
      </form>
    </div>

    <div class="d-flex justify-content-around">
      <p class v-b-modal.modal-multi-1>이메일 찾기</p>
      <p class v-b-modal.modal-multi-2>비밀번호 찾기</p>
      <p class v-b-modal.modal-multi-3 style="margin: 0px 10px;">회원가입</p>
    </div>
  </b-modal>
</template>

<script>
import http from "@/util/http-common";

var CLIENT_ID = process.env.VUE_APP_NAVER_CLIENT_ID;

export default {
  name: "LoginModal",

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
  created() {},
  methods: {
    checkHandlerLogin() {
      let err = true;
      let msg = "";
      !this.email && ((msg = "아이디를 입력해주세요"), (err = false)),
        this.$refs.email.focus();
      err && !this.pw && ((msg = "비밀번호를 입력해주세요"), (err = false)),
        this.$refs.pw.focus();

      if (!err) alert(msg);
      else this.loginHandler();
    },
    loginHandler() {
      http
        .post(`/user/login`, {
          email: this.email,
          password: this.pw,
        })
        .then(({ data }) => {
          // JSON 형태
          let msg = "아이디 혹은 비밀번호를 다시 확인해주세요.";

          if (data.success === "success") {
            this.$session.set("email", this.email);
            this.$session.set("userNo", data.userinfo.userNo);
            this.$session.set("name", data.userinfo.name);
            this.$session.set("gender", data.userinfo.gender);
            this.$session.set("birth", data.userinfo.birth);
            this.$session.set("phone", data.userinfo.phone);
            this.$session.set("token", data.token);
            this.$router.push("/");
            this.$router.go();
          } else {
            alert(msg);
          }
        })
        .catch((err) => {
          alert(err + "에러가 발생했습니다");
        });
    },
    naverLogin() {
      this.naverLoginURL += "&client_id=" + CLIENT_ID;
      this.naverLoginURL += "&redirect_uri=" + this.redirectURI;
      this.naverLoginURL += "&state=" + this.state;

      location.href = this.naverLoginURL;
    },
  },
};
</script>

<style>
</style>