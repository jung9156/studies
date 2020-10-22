<template>
  <b-modal id="modal-memberInfo" title="회원정보" hide-footer>
    <div class="form-group">
      <label for="email-info">이메일</label>
      <div id="email-info" class="ml-1 ft-nss light" v-text="this.$session.get('email')"></div>
    </div>
    <div class="form-group">
      <label for="pw">비밀번호</label>
      <input
        type="password"
        class="form-control ft-nss"
        id="pw"
        ref="pw"
        placeholder="비밀번호를 입력하세요"
        v-model="pw"
      />
    </div>
    <div class="form-group">
      <label for="pw_re">비밀번호 확인</label>
      <input
        type="password"
        class="form-control ft-nss light"
        id="pw_re"
        ref="pw_re"
        placeholder="비밀번호 한번 더 입력하세요"
        v-model="pw_re"
      />
    </div>
    <div class="form-group">
      <label for="name" class="d-flex">이름</label>
      <input
        type="text"
        class="form-control"
        id="name"
        ref="name"
        placeholder="이름을 입력하세요"
        v-model="name"
      />
    </div>
    <div class="form-group ft-nss light mb-1">
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
      <label for="birth" class="d-flex ft-nss light">생년월일</label>
      <input
        type="text"
        class="form-control ft-nss light"
        id="birth"
        ref="birth"
        placeholder="2020-01-01"
        v-model="birth"
        maxlength="10"
        @keyup="inputBirthDate"
      />
    </div>
    <div class="form-group">
      <label for="phone" class="d-flex ft-nss light">핸드폰 번호</label>
      <input
        type="text"
        class="form-control ft-nss light"
        id="phone"
        ref="phone"
        placeholder="핸드폰 번호를 입력하세요"
        v-model="phone"
        maxlength="13"
        @keyup="inputPhoneNumber"
      />
    </div>
    <div class="form-group d-flex justify-content-around">
      <button class="btn bg-cblue ft-nss text-light" @click="checkHandlerModify">회원정보수정</button>
      <button class="btn btn-danger ft-nss" @click="deleteHandler">
        <div class="ft-nss light" style="padding: 0px 12px; color: white;">회원탈퇴</div>
      </button>
    </div>
  </b-modal>
</template>

<script>
import http from "@/util/http-common";

export default {
  name: "MemberInfo",
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
    checkHandlerModify() {
      let err = true;
      let msg = "";
      !this.pw &&
        ((msg = "비밀번호를 입력해주세요"),
        (err = false),
        this.$refs.pw.focus());
      err &&
        !this.pw_re &&
        ((msg = "재입력 비밀번호를 입력해주세요"),
        (err = false),
        this.$refs.pw_re.focus());
      err &&
        !this.name &&
        ((msg = "이름을 입력해주세요"), (err = false), this.$refs.name.focus());
      err &&
        !this.email &&
        ((msg = "이메일을 입력해주세요"),
        (err = false),
        this.$refs.email.focus());
      err &&
        !this.gender &&
        ((msg = "성별을 입력해주세요"),
        (err = false),
        this.$refs.gender.focus());
      err &&
        !this.birth &&
        ((msg = "생년월일을 입력해주세요"),
        (err = false),
        this.$refs.birth.focus());
      err &&
        !this.phone &&
        ((msg = "핸드폰번호를 입력해주세요"),
        (err = false),
        this.$refs.phone.focus());
      err &&
        this.pw != this.pw_re &&
        ((msg = "비밀번호와 재입력 비밀번호가 다릅니다."),
        (err = false),
        this.$refs.pw_re.focus());

      if (!err) alert(msg);
      else this.modifyHandler();
    },
    deleteHandler() {
      http
        .post(
          `/user/del`,
          JSON.stringify({
            email: this.$session.get("email"),
          }),
          {
            headers: {
              token: this.$session.get("token"),
            },
          }
        )
        .then(({ data }) => {
          let msg = "회원삭제에 실패하였습니다..";
          if (data === "success") {
            msg = "회원삭제가 완료되었습니다.";
          }
          this.$root.$emit("bv::hide::modal", "modal-memberInfo");
          alert(msg);
          this.$session.destroy();
          this.$router.go();
        })
        .catch(() => {
          alert("에러가 발생했습니다.");
        });
    },
    modifyHandler() {
      http
        .put(
          `/user`,
          {
            email: this.$session.get("email"),
            password: this.pw,
            name: this.name,
            gender: this.gender,
            birth: this.birth,
            phone: this.phone,
          },
          {
            headers: {
              token: this.$session.get("token"),
            },
          }
        )
        .then(({ data }) => {
          // 여기서부터 코딩
          let msg = "회원수정에 실패하였습니다.";
          if (data.success === "success") {
            msg = "회원수정이 완료되었습니다.";
            this.$session.set("userNo", data.userinfo.userNo);
            this.$session.set("name", data.userinfo.name);
            this.$session.set("gender", data.userinfo.gender);
            this.$session.set("birth", data.userinfo.birth);
            this.$session.set("phone", data.userinfo.phone);
          }
          this.$root.$emit("bv::hide::modal", "modal-memberInfo");
          alert(msg);
          this.$router.go();
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