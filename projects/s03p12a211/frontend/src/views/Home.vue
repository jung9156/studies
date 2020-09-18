<template>
  <div style="height:100%">
    <div class="container px-1" v-if="this.$session.get('email') != null">
      <CaseList />
    </div>
    <div v-else style="min-width:100%; height:100%">
      <MainSignoutPC class="d-none d-md-block" />
      <MainSignoutMobile class="d-md-none" />
    </div>
  </div>
</template>

<script>
import CaseList from "@/views/CaseList.vue";
// import ReportInfo from "@/views/ReportInfo.vue";
import MainSignoutPC from "@/views/MainSignoutPC.vue";
import MainSignoutMobile from "@/views/MainSignoutMobile.vue";

export default {
  name: "Home",
  components: {
    CaseList,
    // ReportInfo,
    MainSignoutPC,
    MainSignoutMobile,
  },
};
</script>

<style>
#signout-main {
  background-image: url("~@/assets/images/home-bg.jpg");
  background-size: 100%;
}
</style>
