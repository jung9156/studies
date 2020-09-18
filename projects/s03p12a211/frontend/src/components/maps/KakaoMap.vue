<template>
  <div id="app" style="height:100%">
    <div id="map-body" style="height:100%">
      <!-- Map Division -->
      <div id="map"></div>
    </div>
    <!-- Modal Division -->
    <div v-for="( violationitem, index ) in items" :key="violationitem.violationNo">
      <b-button
        hidden
        :id="'modalButton' + violationitem.violationNo"
        v-b-modal="'modal'+ violationitem.violationNo"
      ></b-button>
      <b-modal
        :ref="'modalref' + violationitem.violationNo"
        :id="'modal' + violationitem.violationNo"
        title="제보 상세보기"
        hide-footer
      >
        <div class="text-center justify-content-center p-0">
          <video id="video1" style="width:100%" controls>
            <source :src="violationitem.videoUrl" type="video/mp4" />
          </video>
          <a
            :href="violationitem.videoUrl"
            download
            class="btn"
            style="width:100%; background-color: #0f4c81; color: white;"
          >영상 다운로드</a>
        </div>
        <hr />
        <!-- 세부사항 -->
        <div>
          <p>
            위반항목
            <b-form-select
              v-model="violationitem.item"
              :options="options2"
              class="mb-0"
              value-field="item"
              text-field="name"
              disabled-field="notEnabled"
            ></b-form-select>
          </p>
          <p>
            <label for="date">위반일자</label>
            <input
              type="text"
              class="form-control"
              id="date"
              readonly
              ref="date"
              v-model="date[index]"
            />
          </p>

          <p>
            <label for="time">위반시간</label>
            <input
              type="text"
              class="form-control"
              id="time"
              readonly
              ref="time"
              v-model="time[index]"
            />
          </p>
          <p>
            <label for="item">위반차량번호</label>
            <input
              type="text"
              class="form-control"
              id="item"
              ref="item"
              v-model="violationitem.carNum"
            />
          </p>
          <p>
            <label for="address">위반장소</label>
            <input
              type="text"
              class="form-control"
              id="address"
              readonly
              ref="address"
              v-model="violationitem.address"
            />
          </p>
          <p>
            <label for="spot">위반위치</label>
            <input
              type="text"
              class="form-control"
              id="spot"
              ref="spot"
              v-model="violationitem.spot"
            />
          </p>
          <p>
            <label for="contents">신고내용</label>
            <input
              type="text"
              class="form-control"
              id="contents"
              ref="contents"
              v-model="violationitem.contents"
            />
          </p>
          <hr />
          <b-button
            style="width: 100%; background-color: #0f4c81; color: white;"
            href="http://onetouch.police.go.kr/"
            onclick="window.open(this.href);return false;"
            target="_blank"
          >스마트 국민제보로 신고하러 가기</b-button>
        </div>
      </b-modal>
    </div>
  </div>
</template>

<script>
var KakaoApi = process.env.VUE_APP_KAKAO_API_KEY;

import MapPin from "@/assets/pngs/map-pin.png";

export default {
  name: "Map",
  props: {
    items: {
      type: Array,
    },
  },
  data() {
    return {
      options2: [
        { item: "신호위반", name: "신호위반" },
        { item: "끼어들기 금지 위반", name: "끼어들기 금지 위반" },
        { item: "통행의 금지 및 제한 위반", name: "통행의 금지 및 제한 위반" },
        {
          item: "교차로 통행방법위반(꼬리물기)",
          name: "교차로 통행방법위반(꼬리물기)",
        },
        {
          item: "제차 신호 조작 불이행(방향지시등)",
          name: "제차 신호 조작 불이행(방향지시등)",
        },
        { item: "중앙선침범", name: "중앙선침범" },
        { item: "적재물 추락방지 조치위반", name: "적재물 추락방지 조치위반" },
        { item: "적재중량, 적재용량초과", name: "적재중량, 적재용량초과" },
        { item: "지정차로 위반", name: "지정차로 위반" },
        { item: "진로변경 위반", name: "진로변경 위반" },
        { item: "교차로 통행방법 위반", name: "교차로 통행방법 위반" },
        { item: "고속도로 갓길통행 위반", name: "고속도로 갓길통행 위반" },
        { item: "기타", name: "기타" },
      ],
      date: [],
      time: [],
      startLat: 37.5013391,
      startLng: 127.0391208,
    };
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.initMap();
    } else {
      const script = document.createElement("script");
      /* global kakao */
      script.onload = () => kakao.maps.load(this.initMap);
      script.src = `http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${KakaoApi}`;
      document.head.appendChild(script);
    }
  },
  methods: {
    initMap() {
      var container = document.getElementById("map");
      var MapOptionLevel = 1;

      if (this.items.length != 0) {
        this.startLat = this.items[this.items.length - 1].lat;
        this.startLng = this.items[this.items.length - 1].lng;
        MapOptionLevel = 2;
      }

      var options = {
        center: new kakao.maps.LatLng(this.startLat, this.startLng),
        level: MapOptionLevel,
      };
      var map = new kakao.maps.Map(container, options);

      for (var i = 0; i < this.items.length; i++) {
        const violationitem = this.items[i];

        // Date And Time Divison
        this.transDateTime(violationitem.date, violationitem.time);

        var markerPosition = new kakao.maps.LatLng(
          violationitem.lat,
          violationitem.lng
        );

        if (i == this.items.length - 1) {
          this.startLat = violationitem.lat;
          this.startLng = violationitem.lng;
        }

        var imageSrc = MapPin,
          imageSize = new kakao.maps.Size(30, 50);

        var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

        var marker = new kakao.maps.Marker({
          map: map,
          position: markerPosition,
          clickable: true,
          image: markerImage,
        });

        var content =
          "<div class='ml-auto text-center' style='width:180px'>" +
          "<div class='mx-auto' style='width:100%'>" +
          "<p class='m-0' style='width:100%'>" +
          this.date[i] +
          "</p>" +
          "<p class='m-0' style='width:100%'>" +
          violationitem.item +
          "</p>" +
          "</div>" +
          "</div>";

        var infowindow = new kakao.maps.InfoWindow({
          content: content,
        });

        (function (marker, infowindow) {
          kakao.maps.event.addListener(marker, "click", function () {
            document
              .getElementById("modalButton" + violationitem.violationNo)
              .click();
          });
          kakao.maps.event.addListener(marker, "mouseover", function () {
            infowindow.open(map, marker);
          });
          kakao.maps.event.addListener(marker, "mouseout", function () {
            infowindow.close();
          });
        })(marker, infowindow);
      }
    },
    transDateTime(inputDate, inputTime) {
      var RawDate = inputDate.split("-");
      const newDate =
        RawDate[0] + "년" + " " + RawDate[1] + "월" + " " + RawDate[2] + "일";
      this.date.push(newDate);

      var RawTime = inputTime.split(":");
      if (RawTime[0] >= 12) {
        var ApTime = RawTime[0] - 12;
        if (ApTime === 0) {
          ApTime = 12;
        }
        const newTime = "오후" + " " + ApTime + "시" + " " + RawTime[1] + "분";
        this.time.push(newTime);
      } else {
        var AmTime = RawTime[0].slice(0, 1);
        if (AmTime == 0) {
          AmTime = 12;
        }
        const newTime = "오전" + " " + AmTime + "시" + " " + RawTime[1] + "분";
        this.time.push(newTime);
      }
    },
  },
  created() {},
};
</script>

<style>
#map {
  min-width: 100%;
  height: 100%;
}
</style>
