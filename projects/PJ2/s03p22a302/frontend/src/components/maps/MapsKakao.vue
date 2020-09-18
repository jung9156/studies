<template>
  <div>
    <div>
      <span>This is KakaoMaps.vue</span>
    </div>
    
    <div id="map" style="width: 500px; height: 400px; position: inline-block; margin: 10px auto;"></div>
  </div>
</template>

<script >
export default {
  name: "MapsKakao",
  mounted() {
    window.kakao && window.kakao.maps ? this.initMap() : this.addScript()
  },
  methods: {
    initMap() {
      var container = document.getElementById("map")
      var options = {
        center: new kakao.maps.LatLng(37.501276, 127.039642),
        level: 3,
      }
      var map = new kakao.maps.Map(container, options)

      var marker = new kakao.maps.Marker({ position: map.getCenter() })
      marker.setMap(map)
    },

    addScript() {
      const script = document.createElement("script")
      /* global kakao */ script.onload = () => kakao.maps.load(this.initMap)
      const API_KEY = process.env.VUE_APP_KAKAO_MAP_KEY
      script.src =
        `http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${API_KEY}`
      document.head.appendChild(script)
    },
    
  },
  data() {
    return {
    }
  },
}
</script>

<style>
</style>