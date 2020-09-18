<template>
  <div>
    <!-- 로그인 유무에 따라 보이기 (로그인 기능 구현시 수정예정) -->
    <MypageProfile />
    <MypageMark />
    <MypageReview />
    <button>개인 정보 수정</button>
    <button>탈퇴</button>
  </div>
</template>

<script>
import MypageProfile from "@/components/mypage/MypageProfile.vue";
import MypageMark from "@/components/mypage/MypageMark.vue";
import MypageReview from "@/components/mypage/MypageReview.vue";

export default {
  name: "Mypage",
  components: {
    MypageProfile,
    MypageMark,
    MypageReview,
  },
};
</script>

<style></style>
