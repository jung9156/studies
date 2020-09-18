import Vue from "vue";
import App from "./App.vue";
import router from "./router";

// 로그인 복붙하면서 import
import store from "./store";
import VModal from "vue-js-modal";
import VueSession from "vue-session";

// bootstrap
import { BootstrapVue, BootstrapVueIcons } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);

// selectbox
import vSelect from "vselect-component";
Vue.use(vSelect);

// session
import VueSessionStorage from "vue-sessionstorage";
Vue.use(VueSessionStorage);

//로그인 복붙
Vue.use(VModal);
Vue.use(VueSession, sessionOptions);

// Global Font Css
import "@/assets/font.css";

Vue.config.productionTip = false;

var sessionOptions = {
  persist: true,
};

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
