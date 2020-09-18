<template>
  <div id="stop-main" style="height: 100%; margin-top:-128px">
    <div class="h-100 d-flex align-items-center">
      <div class="mx-auto text-center text-white">
        <p class="font-italic" style="font-size:15vh">앗...!</p>
        <h3>로그인이 되어있지 않아 제보 데이터를 불러올 수 없습니다.</h3>
        <h3>로그인 후 서비스를 다시 이용해주세요.</h3>
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
  background-color: rgba(59, 59, 59, 0.596);
  width: 100vw;
  height: 100vh;
}

#stop-main:after {
  background-image: url("~@/assets/images/stop-pc.jpg");

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