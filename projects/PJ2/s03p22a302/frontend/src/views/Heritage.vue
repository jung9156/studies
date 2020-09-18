<template>
  <div class="heritage">
    <HeritageSearchBar />
    <HeritageCarousel />
    <HeritageCards />
  </div>
</template>

<script>
import HeritageSearchBar from "@/components/heritage/HeritageSearchBar";
import HeritageCarousel from "@/components/heritage/HeritageCarousel";
import HeritageCards from "@/components/heritage/HeritageCards";

export default {
  name: "Heritage",

  components: {
    HeritageSearchBar,
    HeritageCarousel,
    HeritageCards,
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/views/heritage.scss";
</style>