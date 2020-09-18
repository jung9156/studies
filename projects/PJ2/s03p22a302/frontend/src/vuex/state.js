import cookies from 'vue-cookies'

export default {
  count: 0,
  authToken: cookies.get('auth-token'),
  review: {
    type: Object
  },
  
}
