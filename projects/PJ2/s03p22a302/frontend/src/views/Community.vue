<template>
  <div>
      This is community.vue
      <CommunityReviewList />
  </div>
</template>

<script>
import CommunityReviewList from '@/components/community/CommunityReviewList'

export default {
  name: "Community",
  components: {
    CommunityReviewList,
  }
  
}
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/views/community.scss";
</style>