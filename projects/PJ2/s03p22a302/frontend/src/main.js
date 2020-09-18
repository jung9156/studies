import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
// Add vue router
import router from "./routes";
// Add vuex
import store from "./vuex/index";
// Add vue-cookies
import VueCookies from "vue-cookies";

Vue.use(VueCookies);

Vue.config.productionTip = false;

new Vue({
  store,
  vuetify,
  router,
  render: (h) => h(App),
}).$mount("#app");
