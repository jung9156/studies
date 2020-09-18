import cookies from 'vue-cookies'
import router from '../routes';
export default {
  ADD_COUNT(state) {
    state.count++;
  },
  SET_TOKEN(state, token) {
    state.authToken = token
    cookies.set('auth-token', token)
  },
  SELECT_REVIEW(state, review) {
    state.review = review
    router.push({ name: "CommunityReviewItem", params: { id: review.view }})
  }
};
