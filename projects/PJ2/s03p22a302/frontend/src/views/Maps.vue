<template>
  <div>
      This is Maps.vue
      <MapsKakao />
      <MapsInfoList />
  </div>
</template>

<script>
import MapsKakao from '@/components/maps/MapsKakao'
import MapsInfoList from '@/components/maps/MapsInfoList'

export default {
  name: 'Maps',
  components: {
    MapsKakao,
    MapsInfoList
  },
  data() {
    return {

    }
  }
}
</script>

<style>

</style>