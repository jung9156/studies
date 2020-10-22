<template>
  <b-col class="col-12 col-sm-6 col-md-4">
    <div>
      <div
        v-b-modal="modalId(violationitem.violationNo)"
        variant="info"
        style="width: 100%;"
        class="shadow mb-4 bg-white rounded p-1"
      >
        <div class="mx-auto my-2" no-body style="max-width: 20rem;">
          <div style="pointer-events: none">
            <video style="width:100%">
              <source :src="violationitem.videoUrl" type="video/mp4" />
            </video>
          </div>
          <b-list-group flush>
            <b-list-group-item class="mt-1 p-0" @click="clickPrevent">
              <b-form-select
                v-model="selected1"
                :options="options1"
                :class="classes"
                value-field="item"
                text-field="name"
                disabled-field="notEnabled"
                :style="styles"
              ></b-form-select>
            </b-list-group-item>
            <div class="d-flex justify-content-left text-secondary my-2">
              <p class="mb-0">{{ date }}</p>
              <p class="ml-2 mb-0">{{ time }}</p>
            </div>
            <div>
              <p class="mb-0" style="font-size: 18px">{{ violationitem.address }}</p>
            </div>
          </b-list-group>
          <CaseModal :violationitem="violationitem" :date="date" :time="time" />
        </div>
      </div>
    </div>
  </b-col>
</template>

<script>
import { mapGetters } from "vuex";
import moment from "moment";
import http from "@/util/http-common";

import CaseModal from "@/components/case/CaseModal.vue";

export default {
  name: "Case",
  components: {
    CaseModal,
  },
  props: {
    violationitem: {
      type: Object,
    },
  },
  data() {
    return {
      selected1: "",
      options1: [
        { item: "0", name: "신고 미접수" },
        { item: "1", name: "접수 완료" },
        { item: "2", name: "처리 완료" },
      ],
      selectedNo: this.violationitem.reportStatus,
      classes: "",
      styles: "",
      date: "",
      time: "",
      statusChanged: 0,
    };
  },
  created() {},
  mounted: function () {
    this.transDateTime();
    this.mountStatus();
  },
  updated() {
    this.changeStatus();
  },
  watch: {
    selectedNo: function () {
      this.violationitem.reportStatus = this.selectedNo;
      http
        .put(
          `/violation/${this.violationitem.userNo}/${this.violationitem.violationNo}/${this.violationitem.reportStatus}`,
          {
            userNo: this.violationitem.userNo,
            violationNo: this.violationitem.violationNo,
            reportStatus: this.violationitem.reportStatus,
          },
          {
            headers: {
              token: this.$session.get("token"),
            },
          }
        )
        .then(({ data }) => {
          let msg = "저장에 실패하였습니다.";
          if (data === "success") {
            msg = "상태가 성공적으로 변경되었습니다.";
          }
          alert(msg);
          this.$router.go();
        })
        .catch(() => {
          alert("에러가 발생했습니다.");
        });
    },
  },
  methods: {
    modalId(i) {
      return "modal" + i;
    },
    indexPlus(i) {
      return (i = ++i);
    },
    getFormatDate(violationitem) {
      return moment(new Date(violationitem.date)).format("YYYY.MM.DD");
    },
    mountStatus() {
      var selected = this.violationitem.reportStatus;
      if (selected == 0) {
        this.selected1 = 0;
        this.classes = "border-0";
        this.styles = "width:100%; background-color: #F1EEE6; color:#616161";
      } else if (selected == 1) {
        this.selected1 = 1;
        this.classes = "text-white";
        this.styles = "width:100%; background-color: #B6CADA;";
      } else if (selected == 2) {
        this.selected1 = 2;
        this.classes = "text-white";
        this.styles = "width:100%; background-color: #0f4c81";
      }
    },
    changeStatus() {
      var selected = this.selected1;
      if (selected == 0) {
        this.classes = "border-0";
        this.styles = "width:100%; background-color: #F1EEE6; color:#616161";
      } else if (selected == 1) {
        this.classes = "text-white";
        this.styles = "width:100%; background-color: #B6CADA; ";
      } else if (selected == 2) {
        this.classes = "text-white";
        this.styles = "width:100%; background-color: #0f4c81";
      }
      this.selectedNo = this.selected1;
    },
    updateStatus() {
      if (
        this.selected1 === "접수 완료" &&
        this.violationitem.reportStatus != 0
      ) {
        http
          .put(
            `/violation`,
            {
              reportStatus: 0,
            },
            {
              headers: {
                token: this.$session.get("token"),
              },
            }
          )
          .then(({ data }) => {
            let msg = "저장에 실패하였습니다.";
            if (data === "success") {
              msg = "저장이 완료되었습니다.";
            }
            alert(msg);
          })
          .catch(() => {
            alert("에러가 발생했습니다.");
          });
      }
    },
    onClickCheck() {
      alert("check");
    },
    clickPrevent(event) {
      event.stopPropagation();
    },
    transDateTime() {
      var RawDate = this.violationitem.date.split("-");
      var newDate =
        RawDate[0] + "년" + " " + RawDate[1] + "월" + " " + RawDate[2] + "일";
      this.$store.state.violationitems;
      this.date = newDate;

      var RawTime = this.violationitem.time.split(":");
      if (RawTime[0] >= 12) {
        var ApTime = RawTime[0] - 12;
        if (ApTime === 0) {
          ApTime = 12;
        }
        var newTime = "오후" + " " + ApTime + "시" + " " + RawTime[1] + "분";
        this.time = newTime;
      } else {
        var AmTime = RawTime[0];
        if (AmTime == 0) {
          AmTime = 12;
        }
        newTime = "오전" + " " + AmTime + "시" + " " + RawTime[1] + "분";
        this.time = newTime;
      }
    },
  },
  computed: {
    ...mapGetters(["violationitems"]),
  },
};
</script>

<style scoped>
.bgblue {
  background-color: #0f4c81;
}

.bguviolet {
  background-color: #5f4b8b;
}
</style>