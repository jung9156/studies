<template>
  <div class="homeCalendar">
    <h1>문화재 월별 행사 정보</h1>
    <v-row class="fill-height">
      <v-col>
        <v-sheet height="64">
          <v-toolbar flat color="white">
            <v-btn outlined class="mr-4" color="grey darken-2" @click="setToday">Today</v-btn>
            <v-btn fab text small color="grey darken-2" @click="prev">
              <v-icon small>mdi-chevron-left</v-icon>
            </v-btn>
            <v-btn fab text small color="grey darken-2" @click="next">
              <v-icon small>mdi-chevron-right</v-icon>
            </v-btn>
            <v-toolbar-title v-if="$refs.calendar">
              {{
              $refs.calendar.title
              }}
            </v-toolbar-title>
            <!-- <v-spacer></v-spacer>
          <v-menu bottom right>
            <template v-slot:activator="{ on, attrs }">
              <v-btn outlined color="grey darken-2" v-bind="attrs" v-on="on">
                <span>{{ typeToLabel[type] }}</span>
                <v-icon right>mdi-menu-down</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item @click="type = 'day'">
                <v-list-item-title>Day</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = 'week'">
                <v-list-item-title>Week</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = 'month'">
                <v-list-item-title>Month</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = '4day'">
                <v-list-item-title>4 days</v-list-item-title>
              </v-list-item>
            </v-list>
            </v-menu>-->
          </v-toolbar>
        </v-sheet>
        <v-sheet height="600">
          <v-calendar
            ref="calendar"
            v-model="focus"
            color="primary"
            :events="events"
            :event-color="getEventColor"
            :type="type"
            @click:event="showEvent"
            @click:more="viewDay"
            @click:date="viewDay"
            @change="updateRange"
          ></v-calendar>
          <v-menu
            v-model="selectedOpen"
            :close-on-content-click="false"
            :activator="selectedElement"
            offset-x
          >
            <v-card color="grey lighten-4" min-width="350px" flat>
              <v-toolbar :color="selectedEvent.color" dark>
                <v-btn icon>
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
                <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
                <v-spacer></v-spacer>
                <v-btn icon>
                  <v-icon>mdi-heart</v-icon>
                </v-btn>
                <v-btn icon>
                  <v-icon>mdi-dots-vertical</v-icon>
                </v-btn>
              </v-toolbar>
              <v-card-text>
                <span v-html="selectedEvent.details"></span>
              </v-card-text>
              <v-card-actions>
                <v-btn text color="secondary" @click="selectedOpen = false">Cancel</v-btn>
              </v-card-actions>
            </v-card>
          </v-menu>
        </v-sheet>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "HomeCalendar",

  data: () => ({
    focus: "",
    type: "month",
    // typeToLabel: {
    //   month: "Month",
    //   week: "Week",
    //   day: "Day",
    //   "4day": "4 Days",
    // },
    selectedEvent: {},
    selectedElement: null,
    selectedOpen: false,
    events: [],
    colors: [
      "blue",
      "indigo",
      "deep-purple",
      "cyan",
      "green",
      "orange",
      "grey darken-1",
    ],
    names: [
      "Meeting",
      "Holiday",
      "PTO",
      "Travel",
      "Event",
      "Birthday",
      "Conference",
      "Party",
    ],
    dummyDatas: {
      8566: {
        seqNo: "8566",
        siteCode: "01",
        siteName: "문화재야행",
        subTitle:
          "2020강릉 문화재 야행(다시 깨어나는 천년의 관아, 강릉대도호부)",
        subContent:
          "가. (야경) 빛으로 만나는 천년의 관아\r\n   - 강릉 이야기로 태어난 등(燈)전시\r\n   (야경) 강릉문화재야행 선등거리 조성\r\n   - 강릉이 품고 있는 콘텐츠를 바탕으로 빛의터널 조성(강릉문화재야행 선등거리 조성)\r\n나. (야로) 신나는 서부마당 (가제)\r\n   - 서부시장에서 만나는 흥겨운 공연\r\n   (야로) 서부 Pop's(외국인 버스킹 공연)\r\n   - 전통시장에서 만나는 외국인 버스킹 공연\r\n   (야로) 달밤愛 버스킹\r\n   - 강릉지역 뮤지션의 테마가 있는 버스킹 공연(5개구역 이상 운영)\r\n다. (야사) 달빛 따라 걷는 강릉대도호부관아\r\n   - 강릉대도호부관아 역사 사료관 조성\r\n   (야사) 강릉문화재야행 해설사와 함께하는 역사투어)\r\n   - 관아아띠(역사해설사)와 함께 야행 역사투어\r\n   (야사) 강릉대도호부관아 수문장 교대식 및 퍼포먼스\r\n   - 강릉대도호부를 수호하는 수문장 퍼포먼스\r\n   (야사) 엄마아빠와 함께 강릉문화재 야행 벨을 울려라\r\n   - 온 가족이 참여하는 강릉문화재 관련 퀴즈대회\r\n   (야사) 칠사당락(칠사당을 즐기다)(칠사당 7가지 정무 체험)\r\n   - 문화재 기능 및 가치를 되살린 체험 프로그램\r\n라. (야화) 강릉문화재야행 설치미술전\r\n   - 강릉사투리 캘리그라피, 아트소품 제작/전시 등\r\n   (야화) 강릉 장인(匠人)학교\r\n   - 인간문화재, 무형문화재 등 장인과의 교류(지화, 방짜수저, 전각, 자수, 관노탈 등)\r\n   (야화) 강릉우체국(강릉우편문화연구회)과 함께하는 야행(夜行)우표 만들기\r\n   - 강릉야행 우표 만들기/우표전시 등\r\n   (야화) 한국은행과 함꼐하는 떠나는 화폐여행\r\n   - 강릉본부 화폐전시관 야간 최초 개방(~22시)\r\n   (야화) 당신의 강릉야행에 투표하세요\r\n   - 가장 흥미로운 강릉야행 프로그램에 투표\r\n   (야화) 예술인의 거리\r\n   - 강릉의 예술인들의 작품 전시 거리\r\n   (야화) 강릉 도화서(圖畵署)_밤을 그리는 화공\r\n   - 화공들의 작품 전시와 실시간 스케치\r\n   (야화) 밤에 하는 전통놀이\r\n   - 밤에 즐기는 전통놀이와 청사초롬 무료대여\r\n   (야화) 강릉문화재행 달빛초롱\r\n   - 야행초롱의 무료대여\r\n   (야화) 손톱도 얼굴도 달빛 물둘이기\r\n   - 강릉문화재야행 마스코트를 활용한 페이스페인팅/네일아트 등\r\n   (야화) 한복입고 달빛 출사\r\n   - 달밤의 정취와 함꼐 한복의 아름다움을 체험(한복무료대여)\r\n   (야화) 찍어야행\r\n   - 강릉문화재야행 현장스케치 및 홍보영상   \r\n   (야화) 강릉대도호부관아 역사 사진전\r\n   - 강릉대도호부관아의 역사를 한눈에 살펴보는 사진전\r\n마. (야설) 강릉대도호부관아 의복 패션쇼\r\n   - 과거 관아에 근무했던 인물(부사, 무관, 문관, 학자, 좌수, 관노 등)의 복식을 재현한 의복패션쇼 운영\r\n   (야설) 강릉대도호부사 부임 행차(거리퍼레이드)\r\n   - 강릉대도호부사의 부임행렬을 재현한 프로그램\r\n   (야설) 강릉풍류:강릉에서 만나는 풍류\r\n   - 강릉의 가락, 음율, 몸짓을 만나는 공연\r\n   (야설) 백년의 울림\r\n   - 100년의 역사를 지닌 임당동 성당 음악회\r\n   (야설) 인류무형문화유산 대향연\r\n   - 인류무형문화로 지정된 공연을 강릉에서 만나다(강릉아리랑, 관노가면극, 강릉농악, 학산오독떼기)\r\n   (야설) 강릉사투리 콘서트\r\n   - 강릉의 사투리로 꾸며진 이야기 콘서트\r\n   (야설) 거리에서 만나는 강릉인형극\r\n   - 거리에서 만나는 강릉인형극(관노가면극/무월량과 연화아가씨 이야기 등)\r\n바. (야식) 먹어야행:강릉문화재야행 푸드트럭\r\n   - 강릉마을(향토)음식을 활용한 푸드트럭(감자옹심이, 물회, 오징어탕수육 등)\r\n   (야식) 마셔야행:달빛아래 다도풍정\r\n   - 전통공간에서 들기는 달빛아래 다도체험\r\n   (야식) 쉬어야행:달빛충전소\r\n   - 야행방문객들의 쉼터가 되어줄 달빛쉼터\r\n   (야식) 받아야행: 스탬프 찍고 맛보는 강릉야행빵\r\n   - 스탬프투어 프로그램/강릉야행빵 제공\r\n   (야식) 반짝야행:반짝반짝 야행 쿠폰별   - 문화재 주변 상권과의 연계/할인 이벤트\r\n사. (야숙) 강룽문화재야행 달밤 스테이\r\n   - 문화재에서 하룻밤(오죽한옥마을, 선교장 등 연계)\r\n   (야숙) 코레일 강릉역과 함꼐하는 야행 내일로\r\n   - ktx강릉역과 연계한 내일로 체험단 운영\r\n   (야숙) 강릉문화재야행 특화여행상품\r\n   - 코레일 관광개발과 연계한 야행 특화 여행상품(버스이용 여행상품 포함)\r\n아. (야시) 저잣거리\r\n   - 시민 프리마켓 운영\r\n   (야시) 문화시전_예술가의 사생활\r\n   - 전문 예술인들의 전시 판매거리\r\n   (야시) 달달한 서부시장4色4味\r\n   - 강릉 서부시장을 연계한 프로그램 운영\r\n   1. 서부주막 2. 강릉수제맥주거리 조성 3. 강릉과자전 4. 예술가와",
        sDate: "20200910",
        eDate: "20200912",
        groupName: "강릉문화원",
        contact: "033-823-3212",
        subDesc: "강릉대도호부관아 ‧ 명주동 ‧ 서부시장 일원",
        subPath:
          "http://www.gncn.or.kr/web2018/main_1.php||https://www.facebook.com/culturtour/",
        subDesc_2: "전국민",
        subDesc_3: "일정 연기 및 개최 횟수 축소 (2회 → 1회)",
        mainImageTemp: " ",
        sido: "강원도",
        gugun: "강릉시",
        subDate: "9. 10.(목) ~ 9. 12(토)",
      },
      8561: {
        seqNo: "8561",
        siteCode: "01",
        siteName: "문화재야행",
        subTitle: "2020강화 문화재 야행(고려의 밤을 품다)",
        subContent:
          "가. (야경) 고려의 밤길\n   - 고려문양을 활용한 야행길 및 포토존 제작\n   - 청사초롱 저잣거리 연출\n   - 문화재 야간개방\n나. (야로) 문화재야행을 알리는 길거리 퍼레이드 공연\n   - 관내 학생 및 주민, 전문공연단의 참여로 만들어지는 퍼레이드 연출\n   (야로) 고려거리 예술단\n   - 고려의상을 입고 마임, 마술, 버블쇼 등 예술거리\n   (야로) 고려전통마차 이야기투어\n   - 친환경전기자전거를 전통꽃마차로 리폼하여 문화재야행 행사구간 투어\n   (야로) 고려의 밤에 빛나는 별을 찾아라!\n   - 8夜프로그램 종합적으로 즐길 수 있도록 스탬프 추진\n다. (야사) 스토리텔러와 함께한 보도투어\n   - 지역 스토리텔러와 함께 문화재를 보도 해설투어\n   (야사) 고려학당 및 전통놀이\n   - 고려의 6가지 문화를 배우고 직접 체험\n   (야사) 고려의 밤, 별저리 관측  \n   - 고려의 궁궐에서 바라보는 밤하늘의 별자리와 천문학 강연\n   (야사) 고려역사 골든벨\n   - 강화의 역사, 고려의 역사 골든벨 추진\n   (야사) 고려 다도체험\n   - 고려의 다도문화와 강화의 전통차를 마셔보는 다도체험\n   (야사) 고려이야기 극장\n   - 아날로그 인형극을 통해 강화의 역사와 설화를 재미있게 전달\n라. (야화) 강화문화재SNS 사진전시\n   - 강화문화재 및 과거여행 사진전시를 통해 문화재의 아름다운 모습을 공유 \n   (야화) 강화 과거이야기 사진전시\n   - 고려궁지가는 길을 활용한 사진전 추진\n마. (야설) 개막식 및 초청공연/고려궁지 버스킹/마당놀이\n   - 관광객들에게 볼거리 제공을 위한 다양한 문화공연(해당 장소에 따라 상이하게 구성)\n   - 퓨전국악공연, LED플래시몹, 전통한국무용, 마당놀이 등\n바. (야식) 강화지역 먹거리부스\n   - 강화지역 특색을 반영한 먹거리 부스운영 및 고려를 주제로 먹거리 이벤트\n사. (야숙) 강화에서 하룻밤\n   - 행사장 인근 숙박업소 및 한옥체험업과 연계한 홍보숙박 프로그램 운영\n아. (야시) 강화문화체험부스\n   - 강화소창, 고려문양, 화문석, 기념품 공모전을 활용한 문화체험 프로그램 운영\n   (야시) 강화로컬마켓부스\n   - 강화지역 특산품 마켓부스 운영",
        sDate: "20200911",
        eDate: "20200912",
        groupName: "강화군청(문화관광과)",
        contact: "032-930-3569",
        subDesc: "강화군 강화읍 용흥궁 공원 일원",
        subPath: "http://www.ganghwa.go.kr/open_content/main/",
        subDesc_2: "전국민",
        subDesc_3: " ",
        mainImageTemp: " ",
        sido: "인천광역시",
        gugun: "강화군",
        subDate: "9. 11(금) ~ 9. 12(토)",
      },
      8580: {
        seqNo: "8580",
        siteCode: "01",
        siteName: "문화재야행",
        subTitle: "순천 문화재 야행 (승평지로 바라본 순천문화재)",
        subContent:
          "가. (야경)\r\n   -순천문화재 탐방\r\n   -순천문화재 보물찾기(역사스탬프투어) \r\n 나. (야로)\r\n   -한여름의 문화재 거리\r\n   -영상으로 만나는 승평지\r\n   -순천문화재 거리도서관, 순천문화재 역사 거리\r\n   -순천 문화재 시간여행 포토\r\n 다. (야사)\r\n   -승평지 역사 아카이브, 순천문화재 역사체험 20종\r\n   -해설사와 함께하는 1,000년 역사이야기\r\n 라. (야화)\r\n   -그림과 사진으로 보는 순천 문화재, 순천과 가야사진전\r\n   -순천의 서원사진전\r\n   -순천야행 크로키전시회\r\n 마. (야설)\r\n   -순천야행풍류, 풍류달빛공연, 남도민요\r\n   -최석순천부사 거리순시\r\n   -퓨전국악을 울리다, 우리가락 우리마당, 변사극\r\n   -옥천서원 상상마당\r\n   -청수정 음악회, 청수정 한마당, 거리의 악사, 클래식의 밤 \r\n 마. (야식)\r\n   -순천야행 주전부리, 순천야행 달빛한모금 \r\n 바. (야시)\r\n   -순천문화재 장시, 순천문화재 공방체험 \r\n 사. (야숙)\r\n   -순천문화재 야행패키지(게스트 연계)",
        sDate: "20200911",
        eDate: "20200913",
        groupName: "순천시 문화예술과",
        contact: "061-749-6814",
        subDesc: "순천항교, 기독교역사박물관, 문화의거리 일원",
        subPath: "www.sc-heritage.com",
        subDesc_2: "전국민",
        subDesc_3: " ",
        mainImageTemp: " ",
        sido: "전라남도",
        gugun: "순천시",
        subDate: "9. 11(금) ~ 9. 13(일) 1·2차 통합개최",
      },
      10953: {
        seqNo: "10953",
        siteCode: "08",
        siteName: "한국문화재재단",
        subTitle: "국가무형문화재 제30호 가곡예능보유자 김영기 2020 공개행사",
        subContent:
          "&nbsp;<br>○ 일시 : 2020. 9. 12 (토) 오후5시<br>○ 장소 : 국가무형문화재전수교육관 민속극장 풍류<br>○ 관람 : 무관중공연 진행<br>○ 문의 : 02-3011-2178 / 010-6737-1902 / 010-8813-5345<br>○ 주최 : 국가무형문화재 제30호 가곡 예능보유자 김영기<br>​○ 후원 : 문화재청, 국립무형유산원, 한국문화재재단<br><br>○ 프로그램<br>&nbsp; 1. 여창가곡 우조 이수대엽 &lsquo;버들은&rsquo;<br>&nbsp; 2. 여창가곡 우조 두거 &lsquo;일각이&rsquo;<br>&nbsp; 3. 여창가곡 우조 우락 &lsquo;바람은&rsquo;<br>&nbsp; 4. 여창가곡 반우반계 반엽 &lsquo;남하여&rsquo;<br>&nbsp; 5. 여창가곡 계면조 중거 &lsquo;산촌에&rsquo;<br>&nbsp; 6. 여창가곡 계면조 평롱 &lsquo;북두칠성&rsquo;<br>&nbsp; 7. 여창가곡 반우반계 환계락 &lsquo;앞내나&rsquo;<br>&nbsp; 8. 여창가곡 계면조 계락 &lsquo;청산도&rsquo;<br>&nbsp; 9. 여창가곡 계면조 편수대엽 &lsquo;모란은&rsquo;<br><br>○ 출연진<br>&nbsp; - 예능보유자_김영기<br>&nbsp; - 이수자_이기쁨, 이아름, 백수영<br>&nbsp; - 전수자_김아련, 최여완, 김은비, 조예진, 신성은, 나일례, 류영애, 류정임<img src='http://www.chf.or.kr/cm_data/editorImage/202009/20200907173426.png' alt='국가무형문화재 제30호 가곡예능보유자 김영기 2020 공개행사'>",
        sDate: " ",
        eDate: " ",
        groupName: " ",
        contact: " ",
        subDesc: "국가무형문화재전수교육관",
        subPath: "https://www.chf.or.kr/c1/sub4_1_5.jsp?brdType=R&bbIdx=108063",
        subDesc_2: " ",
        subDesc_3: " ",
        mainImageTemp: " ",
        sido: "서울특별시",
        gugun: " ",
        subDate: "20200912 ~ 20200912",
      },
      8573: {
        seqNo: "8573",
        siteCode: "01",
        siteName: "문화재야행",
        subTitle: "전주 문화재 야행-문화재술사의 八야심작",
        subContent:
          "가. (야경) 빛의술사들\r\n1. 뜻밖의 시간여행\r\n2. 빛으로 문화재를 밝히다\r\n\r\n나.(야로) 문화재 술사들\r\n1. 전주문화재야행 VR 제작\r\n - 경기전, 전라감영, 풍남문, 조경단 등\r\n2. 왕과의 산책 \r\n3. 경기전 사람들\r\n4. 경기전 좀비 실록(분산진행)\r\n5. 야행 집콕 놀이터 영상공모전\r\n\r\n다. (야사) 이야기 술사들\r\n1. 이야기술사의 버스킹 “담화” \r\n2. 카카오톡 방탈출 챗봇을 활용한 문화재 OX 퀴즈\r\n\r\n라. (야화) 그림술사들\r\n1. 거리의 화공  \r\n2. 역사이야기를 활용한 인형만들기 \r\n   & 인형극 영상물제작 \r\n - 태조, 이방원/세종, 장영실/ 영조, 사도세자 정조, 정약용/철종, 최제우/고종, 명성황후 순종, 안중근\r\n\r\n마. (야설) 공연술사들\r\n1. 개(폐)막공연 \r\n2. 청년예술가무대1 \r\n3. 청년예술가무대2\r\n4. 문화재극장(마술, 서커스, 인형극)   \r\n\r\n바. (야식) 음식술사들\r\n1. 태조할아버지와 야행이가 간다\r\n  - 지역아동센터, 소외계층 대상으로\r\n    문화재야행 체험키트 배송\r\n2. 달빛 차회 (소규모분산진행)\r\n3. 한밤의“계”이득\r\n   (태조할아버지와 야행이가 간다)\r\n  - 사연공모 및 첼린지 통해 닭강정 배달\r\n\r\n사. (야숙) 여행술사들\r\n1. 전주문화재야행×아프리카BJ  \r\n - 왕과의산책, 경기전사람들, 좀비실록 탐방을 통한 영상콘텐츠 제작 \r\n2. 마인크래프트 공모전\r\n   (전주문화재)\r\n\r\n아. (야시) 흥정술사들\r\n1. 태조할아버지와 야행이가 간다",
        sDate: "20200926",
        eDate: "20200927",
        groupName: "문화예술공작소",
        contact: "063-232-9937",
        subDesc: "전주 경기전, 풍남문(구도심 전라감영길) 일원",
        subPath: "http://www.jeonjunight.com",
        subDesc_2: "전국민",
        subDesc_3: " ",
        mainImageTemp: " ",
        sido: "전라북도",
        gugun: "전주시",
        subDate:
          "온라인 - 9. 1 ~ 야행 종료시 까지/9. 12(토)∼9. 13(일) (1차)/9. 26(토)∼9. 27(일) (2차)",
      },
    },
  }),
  mounted() {
    this.$refs.calendar.checkChange();
  },
  methods: {
    viewDay({ date }) {
      this.focus = date;
      this.type = "day";
    },
    getEventColor(event) {
      return event.color;
    },
    setToday() {
      this.focus = "";
    },
    prev() {
      this.$refs.calendar.prev();
    },
    next() {
      this.$refs.calendar.next();
    },
    showEvent({ nativeEvent, event }) {
      const open = () => {
        this.selectedEvent = event;
        this.selectedElement = nativeEvent.target;
        setTimeout(() => (this.selectedOpen = true), 10);
      };

      if (this.selectedOpen) {
        this.selectedOpen = false;
        setTimeout(open, 10);
      } else {
        open();
      }

      nativeEvent.stopPropagation();
    },
    updateRange({ start, end }) {
      const events = [];

      const min = new Date(`${start.date}T00:00:00`);
      const max = new Date(`${end.date}T23:59:59`);
      const days = (max.getTime() - min.getTime()) / 86400000;
      const eventCount = this.rnd(days, days + 20);

      for (let i = 0; i < eventCount; i++) {
        const allDay = this.rnd(0, 3) === 0;
        const firstTimestamp = this.rnd(min.getTime(), max.getTime());
        const first = new Date(firstTimestamp - (firstTimestamp % 900000));
        const secondTimestamp = this.rnd(2, allDay ? 288 : 8) * 900000;
        const second = new Date(first.getTime() + secondTimestamp);

        events.push({
          name: this.names[this.rnd(0, this.names.length - 1)],
          start: first,
          end: second,
          color: this.colors[this.rnd(0, this.colors.length - 1)],
          timed: !allDay,
        });
      }

      this.events = events;
      // console.log(events);
    },
    rnd(a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a;
    },
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/home/homeCalendar.scss";
</style>
