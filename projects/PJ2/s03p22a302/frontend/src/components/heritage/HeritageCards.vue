<template>
  <div>
    <div>This is CommunityCards.vue</div>

    <div class="d-flex">
      <HeritageCardItem />
      <HeritageCardItem />
      <HeritageCardItem />
    </div>

  </div>
</template>

<script>
import HeritageCardItem from '@/components/heritage/HeritageCardItem'
export default {
  name: "CommunityCards",
  components: {
    HeritageCardItem
  }
};
</script>

<style>
</style>