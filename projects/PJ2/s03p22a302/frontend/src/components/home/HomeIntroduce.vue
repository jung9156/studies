<template>
  <div class="homeIntroduce">
    <h1>문지기란?</h1>
    <div>
      <v-container class="pa-3 text-center">
        <v-row class="fill-height" align="center" justify="center">
          <template v-for="(item, i) in items">
            <v-col :key="i" cols="12" md="3">
              <v-hover v-slot:default="{ hover }">
                <v-card
                  @click="$router.push({ name: item.location })"
                  class="rounded-card"
                  :elevation="hover ? 12 : 2"
                >
                  <v-img :src="item.img" gradient="rgba(0,0,0,.5), rgba(0,0,0,.5)" height="225px">
                    <v-card-title class="title white--text">
                      <v-row class="fill-height flex-column" justify="space-between">
                        <h2 class="mt-4 subheading">{{ item.title }}</h2>
                        <h4 class="ma-3">{{ item.text }}</h4>
                      </v-row>
                    </v-card-title>
                  </v-img>
                </v-card>
              </v-hover>
            </v-col>
          </template>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeIntroduce",
  data: () => ({
    items: [
      {
        title: "문화재 추천",
        text: "사용자만을 위한 추천 서비스",
        img:
          "https://user-images.githubusercontent.com/60081201/93179267-66b8b400-f770-11ea-9227-8edb275c138d.png",
        location: "Heritage",
      },
      {
        title: "게시판",
        text: "문화재 방문 리뷰 공유",
        img:
          "https://user-images.githubusercontent.com/60081201/93179265-65878700-f770-11ea-923c-f7fed06a90a0.png",
        location: "Community",
      },
      {
        title: "지도",
        text: "문화재 주변 정보 제공",
        img:
          "https://user-images.githubusercontent.com/60081201/93179269-67514a80-f770-11ea-8975-1f6f3a2b0a18.png",
        location: "Map",
      },
    ],
    transparent: "rgba(255, 255, 255, 0)",
  }),
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/home/homeIntroduce.scss";
</style>

