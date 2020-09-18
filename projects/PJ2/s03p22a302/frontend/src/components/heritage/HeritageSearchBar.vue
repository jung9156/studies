<template>
  <div>
    <div>
      This is CommunitySearchBar.vue
    </div>
    <div>
      <v-text-field
        class="mx-4"
        hide-details
        label="Search"
        solo-inverted
        prepend-inner-icon="search"
        style="width: 500px; margin: 10px auto;"
      ></v-text-field>
    </div>
  </div>
</template>

<script>
export default {
    name: 'CommunitySearchBar'
}
</script>

<style>

</style>