<template>
  <div style="height: 100%">
    <!-- 전체 사용자 데이터 출력 -->
    <div v-if="this.$session.get('email') == null" style="height: 100%">
      <br />
      <div>
        <h1 class="text-center mb-3">전체 등록 현황</h1>
      </div>
      <div class="row align-items-center justify-content-center text-center mb-3 py-2">
        <div
          class="col-12 col-lg-4 shadow p-3 mb-5 mx-3 rounded"
          style="max-width: 20rem; height:100%"
        >
          <h2 class="text-center">전체 등록 건수</h2>
          <hr />
          <div>
            <p class="bolder" style="font-size:4rem;">{{ wholeCount }}건</p>
          </div>
        </div>
        <div
          class="col-12 col-lg-4 shadow p-3 mb-5 mx-3 bg-white rounded"
          style="max-width: 20rem;"
        >
          <h2 class="text-center">{{ year }}년 등록 건수</h2>
          <hr />
          <div>
            <p class="bolder" style="font-size:4rem">{{ yearCount }}건</p>
          </div>
        </div>
        <div
          class="col-12 col-lg-4 shadow p-3 mb-5 mx-3 bg-white rounded"
          style="max-width: 20rem;"
        >
          <h2 class="text-center">{{ month }}월 등록 건수</h2>
          <hr />
          <div>
            <p class="bolder" style="font-size:4rem">{{ monthCount }}건</p>
          </div>
        </div>
      </div>

      <!-- <div>
        <h1 class="text-center mb-3">접수 상황별 전체 현황</h1>
      </div>-->
      <div
        id="all-user-charts"
        class="row align-items-center justify-content-center text-center mb-3 py-2"
      >
        <div
          class="col-12 col-lg-4 shadow p-3 mb-5 mx-3 bg-white rounded"
          style="max-width: 20rem;"
        >
          <h2 class="text-center">신고 미접수 현황</h2>
          <hr />
          <Chart1 />
        </div>
        <div
          class="col-12 col-lg-4 shadow p-3 mb-5 mx-3 bg-white rounded"
          style="max-width: 20rem;"
        >
          <h2 class="text-center">접수완료 현황</h2>
          <hr />
          <Chart2 />
        </div>
        <div
          class="col-12 col-lg-4 shadow p-3 mb-5 mx-3 bg-white rounded"
          style="max-width: 20rem;"
        >
          <h2 class="text-center">처리완료 현황</h2>
          <hr />
          <Chart3 />
        </div>
      </div>
    </div>

    <!-- 개인 사용자 데이터 출력 -->
    <div v-if="this.$session.get('email') != null">
      <br />
      <div>
        <h1 class="text-center mb-3">나의 등록 현황</h1>
      </div>
      <div class="row align-items-center justify-content-center text-center mb-3 py-2">
        <div class="col-12 col-lg-4 shadow p-3 mb-5 mx-3 rounded" style="max-width: 20rem;">
          <h2 class="text-center">전체 등록 건수</h2>
          <hr />
          <div>
            <p class="bolder" style="font-size:4rem">{{ wholeCount }}건</p>
          </div>
        </div>
        <div
          class="col-12 col-lg-4 shadow p-3 mb-5 mx-3 bg-white rounded"
          style="max-width: 20rem;"
        >
          <h2 class="text-center">{{ year }}년 등록 건수</h2>
          <hr />
          <div>
            <p class="bolder" style="font-size:4rem">{{ yearCount }}건</p>
          </div>
        </div>
        <div
          class="col-12 col-lg-4 shadow p-3 mb-5 mx-3 bg-white rounded"
          style="max-width: 20rem;"
        >
          <h2 class="text-center">{{ month }}월 등록 건수</h2>
          <hr />
          <div>
            <p class="bolder" style="font-size:4rem">{{ monthCount }}건</p>
          </div>
        </div>
      </div>
      <hr class="pb-3" />
      <div>
        <h1 class="text-center mb-3">나의 상황별 현황</h1>
      </div>
      <div
        id="all-user-charts"
        class="row align-items-center justify-content-center text-center mb-3 py-2"
      >
        <div
          class="col-12 col-lg-4 shadow p-3 mb-5 mx-3 bg-white rounded"
          style="max-width: 20rem;"
        >
          <h2 class="text-center">신고 미접수 현황</h2>
          <hr />
          <ChartPersonal1 />
        </div>
        <div
          class="col-12 col-lg-4 shadow p-3 mb-5 mx-3 bg-white rounded"
          style="max-width: 20rem;"
        >
          <h2 class="text-center">접수완료 현황</h2>
          <hr />
          <ChartPersonal2 />
        </div>
        <div
          class="col-12 col-lg-4 shadow p-3 mb-5 mx-3 bg-white rounded"
          style="max-width: 20rem;"
        >
          <h2 class="text-center">처리완료 현황</h2>
          <hr />
          <ChartPersonal3 />
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import http from "@/util/http-common";

import Chart1 from "@/components/charts/chart1";
import Chart2 from "@/components/charts/chart2";
import Chart3 from "@/components/charts/chart3";
import ChartPersonal1 from "@/components/charts/chartpersonal1";
import ChartPersonal2 from "@/components/charts/chartpersonal2";
import ChartPersonal3 from "@/components/charts/chartpersonal3";

export default {
  name: "ReportInfo",
  components: {
    Chart1,
    Chart2,
    Chart3,
    ChartPersonal1,
    ChartPersonal2,
    ChartPersonal3,
  },
  data() {
    return {
      item: {},
      year: null,
      month: null,
      wholeCount: null,
      yearCount: null,
      monthCount: null,
    };
  },
  mounted() {
    var CurrentDate = new Date();
    this.year = CurrentDate.getFullYear();
    this.month = CurrentDate.getMonth() + 1;
    if (this.$session.get("email")) {
      http
        .get(`/situation/${this.$session.get("userNo")}`)
        .then(({ data }) => {
          if (data != null) {
            var yearCount = 0;
            var monthCount = 0;
            for (var i = 0; i < 3; i++) {
              for (var j = 0; j < 12; j++) {
                const currentCount = data[i][j].count;
                yearCount += currentCount;

                var now = new Date();
                if (j == now.getMonth()) {
                  monthCount += currentCount;
                }
              }
            }
            this.yearCount = yearCount;
            this.monthCount = monthCount;
            this.wholeCount = data[3][0];
          } else {
            console.log(" 실패했습니다.");
          }
        })
        .catch(() => {
          console.log("에러가 발생했습니다.");
        });
    } else {
      http
        .get(`/situation`)
        .then(({ data }) => {
          if (data != null) {
            var yearCount = 0;
            var monthCount = 0;
            for (var i = 0; i < 3; i++) {
              for (var j = 0; j < 12; j++) {
                const currentCount = data[i][j].count;
                yearCount += currentCount;

                var now = new Date();
                if (j == now.getMonth()) {
                  monthCount += currentCount;
                }
              }
            }
            this.yearCount = yearCount;
            this.monthCount = monthCount;
            this.wholeCount = data[3][0];
          } else {
            console.log(" 실패했습니다.");
          }
        })
        .catch((err) => {
          console.log(err + "에러가 발생했습니다.");
        });
    }
  },
};
</script>

<style></style>
