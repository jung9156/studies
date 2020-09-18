<template>
  <div>
    <div>This is CommunityCarousel.vue</div>

    <div style="margin: 50px;">
      <VueSlickCarousel v-bind="settings">
        <div style="height:300px;">1</div>
        <div style="height:300px;">2</div>
        <div style="height:300px;">3</div>
        <div style="height:300px;">4</div>
        <div style="height:300px;">5</div>
        <div style="height:300px;">6</div>
        <div style="height:300px;">7</div>
        <div style="height:300px;">8</div>
        <div style="height:300px;">9</div>
        <div style="height:300px;">10</div>
      </VueSlickCarousel>
    </div>
  </div>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel"
import "vue-slick-carousel/dist/vue-slick-carousel.css"
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css"

export default {
  name: "CommunityCarousel",
  components: {
    VueSlickCarousel,
  },
  data() {
    return {
      settings: {
        arrows: true,
        dots: true,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        pauseOnDotsHover: true,
        pauseOnFocus: true,
        pauseOnHover: true,
      },
    }
  },
}
</script>

<style>
</style>