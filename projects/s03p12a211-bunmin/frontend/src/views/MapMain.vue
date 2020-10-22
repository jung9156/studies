<template >
  <div class="p-0" style="height: 100%; margin-top:-108px">
    <div class="d-md-none" style="padding-top:84px;"></div>
    <div style="height: 100%;">
      <Map :items="this.$store.state.violationitems" />
    </div>
  </div>
</template>

<script>
import http from "@/util/http-common";

import Map from "@/components/maps/KakaoMap.vue";

export default {
  name: "MapMain",
  components: {
    Map,
  },
  created() {
    if (this.$session.get("email")) {
      http
        .get(`/violation/${this.$session.get("userNo")}`, {
          headers: {
            token: this.$session.get("token"),
          },
        })
        .then(({ data }) => {
          if (data) {
            this.$store.state.violationitems = data;
          } else {
            alert(" 실패했습니다.");
          }
        })
        .catch((err) => {
          alert("에러가 발생했습니다." + " " + err);
        });
    }
  },
};
</script>

<style></style>
