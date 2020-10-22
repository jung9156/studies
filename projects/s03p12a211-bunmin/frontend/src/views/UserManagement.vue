<template>
  <div class="container">
    <br />
    <h1 class="text-center mb-3">회원관리</h1>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">회원번호</th>
          <th scope="col">이메일</th>
          <th scope="col">이름</th>
          <th scope="col">전화번호</th>
          <th scope="col">관리</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="userdata in userdatas" v-bind:key="userdata.userNo">
          <th scope="row" class="bg-white">{{ userdata.userNo }}</th>
          <td>{{ userdata.email }}</td>
          <td>{{ userdata.name }}</td>
          <td>{{ userdata.phone }}</td>
          <td>
            <b-button
              @click="userDel(userdata.email)"
              class="bg-warning border-warning"
              style="padding: 4px 8px;"
            >삭제</b-button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import http from "@/util/http-common";
export default {
  name: "UserManagement",
  data() {
    return {
      userdatas: [],
    };
  },
  methods: {
    userDel(userEmail) {
      http
        .post(
          `/user/del`,
          JSON.stringify({
            email: userEmail,
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
          alert(msg);
          this.$router.go();
        })
        .catch((err) => {
          alert("에러가 발생했습니다." + err);
        });
    },
  },
  computed: {
    rows() {
      return this.userdata.length;
    },
  },

  created() {
    http
      .get(`/user/all`, {
        headers: {
          token: this.$session.get("token"),
        },
      })
      .then(({ data }) => {
        if (data != null) {
          this.userdatas = data;
        } else {
          alert(" 실패했습니다.");
        }
      })
      .catch(() => {
        alert("에러가 발생했습니다.");
      });
  },
};
</script>

<style>
</style>