<template>
  <div>
    This is CommunityReviewList.vue
    <div v-for="(review, idx) in reviewList" :key="idx">
      <v-card class="review-list" outlined @click="SELECT_REVIEW(review)">
        <v-list-item class="d-flex justify-space-around review-list-item">
          <v-img class="review-list-image" :src="review.thumbnail"></v-img>

          <div class="review-list-text">
            <div class="overline mb-4">{{ review.title }}</div>
            <v-list-item-subtitle>{{ review.user }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ review.view }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ review.created }}</v-list-item-subtitle>
          </div>
        </v-list-item>
      </v-card>
    </div>
  </div>
</template>

<script>
import { mapMutations } from "vuex";
export default {
  name: "CommunityReviewList",
  methods: {
    ...mapMutations(["SELECT_REVIEW"]),
  },
  data() {
    return {
      reviewList: [
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
    };
  },
};
</script>

<style>
</style>