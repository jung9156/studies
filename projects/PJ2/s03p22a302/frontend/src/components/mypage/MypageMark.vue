<template>
  <div>
    <div>MypageMark.vue | 찜한 문화재 목록</div>
    <div v-if="isEmpty">
      아직 등록된 문화재가 없습니다.
      <button @click="goHeritage">추천 문화재 보러가기</button>
    </div>
    <div v-else>
      <ul v-for="markData in markDatas" :key="markData">
        {{
          markData.k_name
        }}
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "MypageMark",
  created() {
    if (Object.keys(this.markDatas).length === {}) {
      this.isEmpty = true;
    } else {
      this.isEmpty = false;
    }
  },
  methods: {
    goHeritage() {
      this.$router.push({ name: "Heritage" });
    },
  },
  data() {
    return {
      markDatas: {
        "14860000": {
          selnum: "14860000",
          k_name: "이광사 초상",
          h_name: "李匡師 肖像",
          clsfc_code: "12",
          clsfc_name: "보물",
          longitude: "126.980350241652",
          latitude: "37.5240413763397",
          content:
            "李匡師(1705-1777)는 원교체를 완성하고 동국진체를 이룩한 조선시대 대표적 서예가 중 한 사람이다. <이광사 초상> 화면 우상단에 ‘朝鮮國光山李公諱匡師字道甫圓嶠先生遺像 … 此本卽 先生七十歲甲午冬畵師申漢枰所寫……’라고 쓰여 있어 이 작품의 주인공과 제작시기, 화가 등 내력을 알 수 있다. 기록을 토대로 1775년에 이광사 말년의 모습을 신윤복의 아버지로 유명한 화원화가 신한평이 그린 것임이 확인된다.\n   전체적으로 섬세하고 우아한 필묘와 은근한 요철감을 표현하는 수법으로 강렬하지는 않지만 품격 있고 깊은 傳神을 성취하였다는 점에서 수준이 높은 역작이다. 또한 신한평이 초상으로 유명하였지만 전해지는 작품이 없다는 점에서도 이 작품은 희귀한 가치를 지니고 있다. \n  ㅇ 규격(세로x가로) : 66.8 x 53.7cm",
          imageURL:
            "http://www.cha.go.kr/unisearch/images/treasure/1614874.jpg",
          era: "1775년",
          address: "서울특별시 용산구 서빙고로 137 (용산동6가, 국립중앙박물관)",
        },
        "14870000": {
          selnum: "14870000",
          k_name: "서직수 초상",
          h_name: "徐直修 肖像",
          clsfc_code: "12",
          clsfc_name: "보물",
          longitude: "126.980350241652",
          latitude: "37.5240413763397",
          content:
            "서직수(1735-?)는 본관은 達城이며, 자는 敬之, 호는 十友軒이다. 영의정 서명균의 조카로서, 진사로 관직에 있지 않고 일생을 시서화를 하면서 보냈다한다. <서직수초상> 화면의 오른 편 상단에는 서직수의 自贊이 있어 서직수 62세인 1796년 당대 최고의 초상화가인 이명기가 얼굴을 그리고 김홍도가 몸체를 그린 합작품임을 알 수 있다.   \n   <서직수초상>은 동파관에 도포를 입고 흑색 광다회를 두르고, 버선발로 서 있는 좌안8분면의 전신입상이다. 조선시대 초상화의 대부분이 좌상인데 반해 입상(그 것도 실내장면)일 뿐더러, 당대 최고화가들의 합작이라는 점 등에서 중요성을 지닌다. 그리고 매우 뛰어난 형태 묘사와 투시법, 명암법을 구사하면서도 높은 품격을 보여주어 정조대 초상화의 백미로 꼽히는 걸작이다.\n  ㅇ 규격(세로x가로) : 148.8x72cm",
          imageURL:
            "http://www.cha.go.kr/unisearch/images/treasure/1614875.jpg",
          era: "1796년",
          address: "서울특별시 용산구 서빙고로 137 (용산동6가, 국립중앙박물관)",
        },
      },
      isEmpty: true,
    };
  },
};
</script>

<style></style>
