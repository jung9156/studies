<template>
  <div>
    <h1>문화재 인기순</h1>
    <div class="d-flex">
      <HeritageCardItem />
      <HeritageCardItem />
      <HeritageCardItem />
    </div>
  </div>
</template>

<script>
import HeritageCardItem from "@/components/heritage/HeritageCardItem";

export default {
  name: "HomeHeritage",
  components: {
    HeritageCardItem,
  },
};
</script>

<style></style>
