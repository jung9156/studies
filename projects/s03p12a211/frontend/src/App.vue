<template >
  <div class="wrapper1" style="height:100%">
    <NavBar id="navbar" class="fixed-top ft-nns" />
    <div class="wrapper2" style="height:100%">
      <div id="main-content" style="height:100%">
        <div class="d-none d-md-block" style="padding-top:128px;"></div>
        <div class="d-md-none" style="padding-top:64px"></div>
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/layout/NavBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
  },
  data() {
    return {};
  },
};
</script>

<style>
p a {
  color: black;
  font-size: 120%;
}

#navbar {
  background-color: #333; /* Black background color */
  position: fixed; /* Make it stick/fixed */
  top: 0; /* Stay on top */
  width: 100%; /* Full width */
  transition: top 0.3s; /* Transition effect when sliding down (and up) */
}
</style>