<template>
  <div class="container">
    <br />
    <!-- <h1 class="text-center mb-3">공지사항</h1> -->
    <div v-if="this.$session.get('email') == 'admin'" class="text-right">
      <router-link to="/noticeWrite" class="btn btn-warning m-3">글쓰기</router-link>
    </div>
    <div>
      <b-container class="bv-example-row">
        <b-row>
          <Notice
            v-for="noticeitem in this.$store.state.noticeitems"
            :key="noticeitem.noticeNo"
            :noticeitem="noticeitem"
          />
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

import Notice from "@/components/notice/Notice.vue";

export default {
  name: "NoticeBoard",
  components: {
    Notice,
  },

  computed: {
    ...mapGetters(["noticeitems"]),
  },

  created() {
    this.$store.dispatch("getNotices");
  },
};
</script>

<style>
</style>