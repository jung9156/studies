<template>
  <div>
    <div>MypageProfile.vue | 문화재 사용자관련 부분</div>
    <div>{{ userData.nickname }}님의 마이페이지</div>
    <v-row>
      <v-col>
        <img src="" alt="사용자 프로필 이미지" />
        <div>
          <button>프로필 사진 설정</button>
        </div>
      </v-col>
      <v-col>
        이름 : {{ userData.username }} 성씨 본관 :{{ userData.ancestor }}
        <div>
          <button @click="searchAncestor(userData.ancestor)">
            조상과 관련된 문화재 보기
          </button>
        </div>
      </v-col>
      <v-col>
        {{ userData.grade }}
        <v-dialog v-model="gradeInfo" width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on">
              신분제알아보기
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">문지기의 신분제</span>
              리뷰수로 신분이 결정됩니다.
            </v-card-title>
            <v-card-text
              >왕 : 리뷰 50개 이상 / 영의정 : 리뷰 30개 이상 / 기미상궁 : 리뷰
              20개 이상 / 사또 : 리뷰 10개 이상 / 양반 : 리뷰 5개 이상 / 천민 :
              리뷰 0개 이상
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" text @click="gradeInfo = false"
                >닫기</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "MypageProfile",
  data() {
    return {
      userData: {
        nickname: "ssafy",
        ancestor: "평산 신",
        username: "신싸피",
        grade: "양반",
      },
      gradeInfo: false,
    };
  },
};
</script>

<style></style>
