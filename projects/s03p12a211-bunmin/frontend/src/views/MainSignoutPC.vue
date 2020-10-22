<template>
  <div class="content" style="height: 100%; margin-top:-128px">
    <div id="main-text" class="d-flex justify-content-center align-items-center h-100">
      <div class="my-auto px-3 py-3 text-center">
        <div id="meaningless-div" style="margin-top:148px"></div>
        <h1 id="greeting-text" class="text-white mb-3 bold">
          원버튼
          간편
          <span class="bolder" style="color:#C10016">교통</span> 민원 DB 서비스
        </h1>
        <img id="greeting-logo" src="@/assets/logos/Logo_solid.png" />
        <h1 id="first-text" class="text-white mb-5 bold">
          서비스 이용을 위해
          <span class="btn btn-danger" v-b-modal.modal-1>
            <b-icon icon="power"></b-icon>&nbsp;로그인
          </span>
        </h1>
        <h1 id="second-text" class="text-white mb-5 bold">
          계정이 없다면
          <span class="bolder" style="color:#C10016;" v-b-modal.modal-multi-3>회원 가입</span> 해주세요
        </h1>
        <h3 id="third-text" class="text-white mb-5 bold">
          자세한 서비스 설명은
          <span class="bolder">
            <router-link
              to="/howtouse"
              class="text-decoration-none hover-none bolder"
              style="color:#C10016"
            >이용방법</router-link>
          </span>&nbsp;페이지 확인
        </h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainSignout",
};
</script>

<style scoped>
.content {
  position: relative;
  background-color: rgba(24, 12, 12, 0.712);
  width: 100vw;
  height: 100vh;
}

.content:after {
  background-image: url("~@/assets/images/home-bg.jpg");
  background-attachment: fixed;
  background-position: left;
  background-repeat: no-repeat;
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
    top: 90px;
  }
  25% {
    opacity: 1;
    top: 60px;
  }
  75% {
    opacity: 1;
    top: 60px;
  }
  100% {
    opacity: 0;
    top: 90px;
  }
}

@keyframes popup-logo {
  0% {
    opacity: 0;
    top: 100px;
  }
  25% {
    opacity: 1;
    top: 70px;
  }
  70% {
    opacity: 1;
    top: 70px;
  }
  100% {
    opacity: 0;
    top: 100px;
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
  top: -120px;
  position: relative;
  animation: description-text 2s ease-in-out 3s;
  animation-fill-mode: forwards;
  animation-delay: 4.7s;
}

#second-text {
  opacity: 0;
  top: -150px;
  position: relative;
  animation: description-text 2s ease-in-out 3s;
  animation-fill-mode: forwards;
  animation-delay: 5.2s;
}

#third-text {
  opacity: 0;
  top: -160px;
  position: relative;
  animation: description-text 2s ease-in-out 3s;
  animation-fill-mode: forwards;
  animation-delay: 5.7s;
}
</style>