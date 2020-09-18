<template>
  <div>
    This is CommunityReviewItem.vue
    <div>
      <span>{{ review.title }}</span> <br>
      <span>{{ review.user }}</span> <br>
      <span>{{ review.thumbnail }}</span> <br>
      <span>{{ review.created }}</span> <br>
      <span>{{ review.view }}</span> <br>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex"

export default {
  name: "CommunityReviewItem",
  computed: { 
    ...mapState({review: "review"})
    
  }
}

</script>

<style>

</style>