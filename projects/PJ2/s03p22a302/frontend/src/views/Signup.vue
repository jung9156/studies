<template>
  <div>
    <h1>회원가입</h1>이름 :
    <input type="text" v-model="signupData.username" />
    닉네임 :
    <input type="text" v-model="signupData.nickname" />
    이메일 :
    <input type="email" v-model="signupData.email" />
    <button @click="checkEmail(signupData.email)">중복확인하기</button>
    비밀번호 :
    <input type="password" v-model="signupData.password" />
    <button @click="checkPassword(signupData.password)">중복확인하기</button>

    <div>
      <button @click="signup(signupData)">작성 완료</button>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Signup",
  methods: {
    ...mapActions(["signup"]),
    ...mapActions(["checkEmail"]),
    ...mapActions(["checkPassword"]),
  },
  data() {
    return {
      signupData: {
        username: "",
        nickname: "",
        email: "",
        password: "",
      },
    };
  },
};
</script>

<style>
</style>