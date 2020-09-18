<template>
  <b-modal id="modal-multi-1" title="이메일 찾기" hide-footer>
    <div class="modal-body">
      <div class="form-group">
        <label for="name">이름</label>
        <input
          type="text"
          class="form-control"
          id="name"
          ref="name"
          placeholder="이름을 입력하세요"
          v-model="name"
        />
      </div>
      <div class="form-group light mb-1">
        <label for="gender">성별</label>
        <div id="gender" class="d-flex">
          <div class="mr-2">
            <input type="radio" id="one" value="남" v-model="gender" class="mr-1" />
            <label for="one">남</label>
          </div>
          <div>
            <input type="radio" id="two" value="여" v-model="gender" class="mr-1" />
            <label for="two">여</label>
          </div>
          <input
            hidden
            type="text"
            class="form-control"
            id="gender"
            ref="gender"
            placeholder="남 또는 여"
            v-model="gender"
          />
        </div>
      </div>
      <div class="form-group">
        <label for="birth">생년월일</label>
        <input
          type="text"
          class="form-control"
          id="birth"
          ref="birth"
          placeholder="예) 2020-01-01"
          v-model="birth"
          maxlength="10"
          @keyup="inputBirthDate"
        />
      </div>
      <div class="form-group">
        <label for="phone">핸드폰 번호</label>
        <input
          type="text"
          class="form-control"
          id="phone"
          ref="phone"
          placeholder="핸드폰 번호를 입력하세요"
          v-model="phone"
          maxlength="13"
          @keyup="inputPhoneNumber"
        />
      </div>
      <div class="form-group">
        <button class="btn bg-cblue text-light btn-lg btn-block login-btn" @click="findEmail">이메일 찾기</button>
      </div>
    </div>
  </b-modal>
</template>

<script>
import http from "@/util/http-common";

export default {
  name: "SearchEmail",
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
  methods: {
    findEmail() {
      http
        .post(`/user/findEmail`, {
          name: this.name,
          gender: this.gender,
          birth: this.birth,
          phone: this.phone,
        })
        .then(({ data }) => {
          if (data == "fail") {
            alert("없는 회원입니다.");
          }
          if (data != "fail") {
            alert(data);
            this.$root.$emit("bv::hide::modal", "modal-multi-1");
          }
        })
        .catch(() => {
          alert("에러가 발생했습니다.");
        });
    },
    inputBirthDate() {
      var number = this.birth.replace(/[^0-9]/g, "");
      var birthDate = "";

      if (number.length < 5) {
        return number;
      } else if (number.length < 7) {
        birthDate += number.substr(0, 4);
        birthDate += "-";
        birthDate += number.substr(4);
      } else {
        birthDate += number.substr(0, 4);
        birthDate += "-";
        birthDate += number.substr(4, 2);
        birthDate += "-";
        birthDate += number.substr(6);
      }
      this.birth = birthDate;
    },
    inputPhoneNumber() {
      var number = this.phone.replace(/[^0-9]/g, "");
      var phone = "";

      if (number.length < 4) {
        return number;
      } else if (number.length < 7) {
        phone += number.substr(0, 3);
        phone += "-";
        phone += number.substr(3);
      } else if (number.length < 11) {
        phone += number.substr(0, 3);
        phone += "-";
        phone += number.substr(3, 3);
        phone += "-";
        phone += number.substr(6);
      } else {
        phone += number.substr(0, 3);
        phone += "-";
        phone += number.substr(3, 4);
        phone += "-";
        phone += number.substr(7);
      }
      this.phone = phone;
    },
  },
};
</script>

<style>
</style>