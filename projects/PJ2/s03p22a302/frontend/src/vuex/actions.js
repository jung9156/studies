import axios from "axios";
import cookies from 'vue-cookies'
import router from '@/routes'
import SERVER from '@/api/drf'

export default {
  postAuthData({ commit }, info) {
    axios.post(info.location, info.data)
      .then(res => {
        console.log(res)
        commit('SET_TOKEN', res.data.token)
        router.push({ name: 'Home' })
      })
      .catch((err) => { console.log(err.message) })
  },
  signup({ dispatch }, signupData) {
    const info = {
      location: SERVER.URL + SERVER.ROUTES.signup,
      data: signupData
    }
    dispatch('postAuthData', info)

  },
  login({ dispatch }, loginData) {
    const info = {
      location: SERVER.URL + SERVER.ROUTES.login,
      data: loginData
    }
    dispatch('postAuthData', info)
  },

  logout({ getters, commit }) {
    axios.post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config)
      .then(() => {
        commit('SET_TOKEN', null)
        cookies.remove('auth-token')
        router.push({ name: 'Home' })
      })
      .catch((err) => { console.log(err.message) })


  },

};
