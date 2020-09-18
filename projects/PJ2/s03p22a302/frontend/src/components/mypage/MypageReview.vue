<template>
  <div>
    <div>MypageReview.vue | 문화재 리뷰 목록</div>
    <div v-if="isEmpty">
      아직 등록된 리뷰가 없습니다.
      <button>리뷰 작성하러가기</button>
    </div>
    <div v-else>
      <ul v-for="result in resultList" :key="result">
        <div @click="selectReview(result)">
          {{ result.title }}
          {{ result.created }}
        </div>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "MypageReview",
  created() {
    if (Object.keys(this.resultList).length === {}) {
      this.isEmpty = true;
    } else {
      this.isEmpty = false;
    }
  },
  methods: {
    selectReview(result) {
      this.$router.push({ name: "CommunityReviewItem", params: { result } });
    },
  },
  data() {
    return {
      resultList: [
        {
          thumbnail: "https://picsum.photos/510/300?random",
          title: "test1",
          user: "john",
          view: 1,
          created: "2020-09-23",
        },
        {
          thumbnail: "https://picsum.photos/510/300?random",
          title: "test2",
          user: "Harry",
          view: 22,
          created: "2020-09-23",
        },
        {
          thumbnail: "https://picsum.photos/510/300?random",
          title: "test3",
          user: "Taki",
          view: 33,
          created: "2020-09-23",
        },
        {
          thumbnail: "https://picsum.photos/510/300?random",
          title: "test4",
          user: "Cathy",
          view: 11,
          created: "2020-09-23",
        },
      ],
      isEmpty: true,
    };
  },
};
</script>

<style></style>
