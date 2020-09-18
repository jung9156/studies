<template>
  <div id="stop-main" style="height: 100%; margin-top:-64px">
    <div class="h-100 d-flex align-items-center">
      <div class="mx-auto text-center text-white">
        <p class="font-italic" style="font-size:10vh">어라...?</p>
        <h5>로그인이 되어있지 않아</h5>
        <h5>데이터를 불러올 수 없습니다.</h5>
        <h5 class="mt-3">로그인 후 다시 이용해주세요.</h5>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StopPC",
};
</script>

<style scoped>
#stop-main {
  position: relative;
  background-color: rgba(0, 3, 51, 0.596);
  width: 100vw;
  height: 100vh;
}

#stop-main:after {
  background-image: url("~@/assets/images/stop-mobile.jpg");

  background-attachment: fixed;
  background-position: center;
  background-size: cover;

  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: -1;
}
</style>