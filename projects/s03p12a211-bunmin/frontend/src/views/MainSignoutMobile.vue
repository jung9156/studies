<template>
  <div id="content" style="height:100%;margin-top:-64px">
    <div class="h-100 d-flex align-items-center">
      <div class="mx-auto text-center">
        <h4 id="greeting-text" class="text-white">원버튼 간편 교통 민원 DB 서비스</h4>
        <img id="greeting-logo" src="@/assets/logos/Logo_ico.png" alt="Logo-iconic-image" />
        <h5 id="first-text" class="text-white mb-5">
          서비스 이용을 위해
          <span style="color:#dac0a7;font-weight: bold" v-b-modal.modal-1>로그인</span>
        </h5>
        <h5 id="second-text" class="text-white mb-5">
          계정이 없다면
          <span style="color:#dac0a7;font-weight: bold" v-b-modal.modal-multi-3>회원 가입</span> 해주세요
        </h5>
        <p id="third-text" class="text-white mb-5">
          자세한 서비스 설명은
          <span>
            <br />
            <router-link
              to="/howtouse"
              class="text-decoration-none hover-none"
              style="color:#dac0a7;font-weight: bold"
            >이용방법</router-link>
          </span>&nbsp;페이지 확인
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainSignoutPC",
};
</script>

<style scoped>
#content {
  position: relative;
  background-color: rgba(0, 1, 41, 0.774);
  width: 100vw;
  height: 100vh;
}

#content:after {
  background-image: url("~@/assets/images/home-bg-mobile.jpg");

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

@keyframes popup-text {
  0% {
    opacity: 0;
    top: 150px;
  }
  25% {
    opacity: 1;
    top: 120px;
  }
  75% {
    opacity: 1;
    top: 120px;
  }
  100% {
    opacity: 0;
    top: 150px;
  }
}

@keyframes popup-logo {
  0% {
    opacity: 0;
    top: 160px;
  }
  25% {
    opacity: 1;
    top: 130px;
  }
  70% {
    opacity: 1;
    top: 130px;
  }
  100% {
    opacity: 0;
    top: 160px;
  }
}

@keyframes description-text {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

#greeting-text {
  opacity: 0;
  position: relative;
  animation-name: popup-text;
  animation-duration: 3.5s;
  animation-delay: 1s;
}

#greeting-logo {
  opacity: 0;
  position: relative;
  animation-name: popup-logo;
  animation-duration: 3s;
  animation-delay: 1.5s;
}

#first-text {
  opacity: 0;
  top: -90px;
  position: relative;
  animation: description-text 2s ease-in-out 3s;
  animation-fill-mode: forwards;
  animation-delay: 4.7s;
}

#second-text {
  opacity: 0;
  top: -120px;
  position: relative;
  animation: description-text 2s ease-in-out 3s;
  animation-fill-mode: forwards;
  animation-delay: 5.2s;
}

#third-text {
  opacity: 0;
  top: -130px;
  position: relative;
  animation: description-text 2s ease-in-out 3s;
  animation-fill-mode: forwards;
  animation-delay: 5.7s;
}
</style>