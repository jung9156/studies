<template>
  <div style="height:100%">
    <div v-if="this.$session.get('email') != null" class="pt-3 px-0 container">
      <!-- filter division -->
      <div
        id="filter-division"
        class="row align-items-center text-center mb-4 mx-0 py-2 text-light"
        style="width:100%; border-radius:5px"
      >
        <!-- Report Condition Check Boxes -->
        <div class="col-12 text-left mt-2 mb-3">
          <b-form-checkbox-group
            v-model="selected"
            :options="options"
            class="mx-0"
            value-field="item"
            text-field="name"
            disabled-field="notEnabled"
            @input="optionController"
            style="width:100%"
          ></b-form-checkbox-group>
        </div>
        <!-- items dropdown -->
        <div class="col-12 col-md-5 col-lg-4 mb-2">
          <b-form-select
            v-model="selected2"
            :options="options2"
            class="my-0"
            value-field="item"
            text-field="name"
            disabled-field="notEnabled"
            @input="optionController"
          ></b-form-select>
        </div>
        <!-- find term calendar -->
        <div class="col-12 col-md-7 col-lg-5 mb-2 d-flex">
          <b-form-group id="input-group-3" class="pl-0 pr-1 my-auto col-6">
            <b-form-datepicker
              id="example-datepicker1"
              v-model="startdate"
              class
              @input="optionController"
              label-help
              label-no-date-selected="시작일"
              :max="maxdate"
              today-button
              reset-button
              close-button
              :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
            ></b-form-datepicker>
          </b-form-group>
          <b-form-group id="input-group-3" class="pl-1 pr-0 my-auto col-6">
            <b-form-datepicker
              id="example-datepicker2"
              v-model="enddate"
              right
              class
              @input="optionController"
              label-help
              label-no-date-selected="종료일"
              :min="startdate"
              :max="today"
              today-button
              reset-button
              close-button
              :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
            ></b-form-datepicker>
          </b-form-group>
        </div>
        <!-- search bar -->
        <div class="col-12 col-md-12 col-lg-3 mb-2">
          <b-input-group id="searchBar">
            <b-input-group-prepend is-text @click="optionController" style="cursor: pointer">
              <b-icon icon="search"></b-icon>
            </b-input-group-prepend>
            <b-form-input class type="text" v-model="searchText" @keydown.enter="optionController"></b-form-input>
          </b-input-group>
        </div>
      </div>
      <!-- cards divison -->
      <div
        v-if="searchviolationitems.length == 0 && selected2 == '전체' && searchWord.length == 0 && selected.length == 0 && startdate.length == 0 && enddate.length == 0"
      >
        <b-container class="bv-example-row">
          <b-row>
            <Case
              v-for="violationitem in this.$store.state.violationitems.slice().reverse()"
              :key="violationitem.violationNo"
              :violationitem="violationitem"
            />
          </b-row>
        </b-container>
      </div>
      <div v-else>
        <b-container class="bv-example-row">
          <b-row>
            <Case
              v-for="violationitem in searchviolationitems.slice().reverse()"
              :key="violationitem.violationNo"
              :violationitem="violationitem"
            />
          </b-row>
        </b-container>
      </div>
    </div>
    <div v-else style="height:100%">
      <StopPC class="d-none d-md-block" />
      <StopMobile class="d-md-none" />
    </div>
  </div>
</template>

<script>
import http from "@/util/http-common";
import Case from "@/components/case/CaseTube.vue";
import StopPC from "@/views/StopPC.vue";
import StopMobile from "@/views/StopMobile.vue";

export default {
  name: "CaseList",
  components: {
    Case,
    StopPC,
    StopMobile,
  },
  props: {},
  data() {
    return {
      local_violationitems: [],
      searchText: "",
      searchWord: "",
      searchviolationitems: [],
      selected: [],
      options: [
        { item: 0, name: "신고 미접수" },
        { item: 1, name: "접수 완료" },
        { item: 2, name: "처리 완료" },
      ],
      startdate: "",
      enddate: "",
      templist_click: [],
      templist_select: [],
      templist_find: [],
      selected2: "전체",
      options2: [
        { item: "전체", name: "전체" },
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
      maxdate: "",
      today: "",
    };
  },
  mounted() {
    this.getToday();
  },
  created() {
    if (this.$session.get("email")) {
      http
        .get(`/violation/${this.$session.get("userNo")}`, {
          headers: {
            token: this.$session.get("token"),
          },
        })
        .then(({ data }) => {
          if (data != null) {
            this.local_violationitems = data;
            this.$store.state.violationitems = data;
          } else {
            alert(" 실패했습니다.");
          }
        });
    }
  },
  methods: {
    clickFilter() {
      const emptyItems = new Array();
      this.templist_click = emptyItems;
      if (this.selected.length != 0) {
        for (var i in this.local_violationitems) {
          if (
            this.selected.includes(this.local_violationitems[i].reportStatus)
          ) {
            this.templist_click.push(this.local_violationitems[i]);
          }
        }
      } else {
        this.templist_click = this.local_violationitems;
      }
    },
    selectItem() {
      const emptyItems = new Array();
      this.templist_select = emptyItems;
      if (this.selected2 != "전체") {
        for (var i in this.templist_click) {
          if (this.selected2 == this.templist_click[i].item) {
            this.templist_select.push(this.templist_click[i]);
          }
        }
      } else {
        this.templist_select = this.templist_click;
      }
    },
    findTerm() {
      const emptyItems = new Array();
      this.templist_find = emptyItems;

      if (this.enddate) {
        this.maxdate = this.enddate;
      }

      if (this.startdate.length != 0 && this.enddate.length != 0) {
        for (var i in this.templist_select) {
          // input Date Transformation
          var tempDate = this.templist_select[i].date.split("-");

          if (tempDate[1] < 10) {
            tempDate[1] = "0" + tempDate[1];
          }

          if (tempDate[2] < 10) {
            tempDate[2] = "0" + tempDate[2];
          }

          const newDate = tempDate[0] + "-" + tempDate[1] + "-" + tempDate[2];
          if (this.startdate <= newDate && newDate <= this.enddate) {
            this.templist_find.push(this.templist_select[i]);
          }
        }
      } else {
        this.templist_find = this.templist_select;
      }
    },
    searchOnlist() {
      const emptyItems = new Array();
      this.searchviolationitems = emptyItems;

      const searchWord = this.searchText;
      this.searchWord = searchWord;
      for (var i in this.templist_find) {
        if (
          (this.templist_find[i].contents != null &&
            this.templist_find[i].contents.includes(searchWord)) ||
          (this.templist_find[i].spot != null &&
            this.templist_find[i].spot.includes(searchWord)) ||
          (this.templist_find[i].carNum != null &&
            this.templist_find[i].carNum.includes(searchWord)) ||
          (this.templist_find[i].address != null &&
            this.templist_find[i].address.includes(searchWord))
        ) {
          this.searchviolationitems.push(this.templist_find[i]);
        }
      }
    },
    optionController() {
      this.clickFilter();
      this.selectItem();
      this.findTerm();
      this.searchOnlist();
    },
    getToday() {
      var today = new Date();
      var dd = today.getDate();
      var mm = today.getMonth() + 1;
      var yyyy = today.getFullYear();

      if (dd < 10) {
        dd = "0" + dd;
      }

      if (mm < 10) {
        mm = "0" + mm;
      }

      today = yyyy + "-" + mm + "-" + dd;
      this.today = today;
      this.maxdate = today;
    },
  },
  computed: {},
};
</script>

<style>
#filter-division {
  background-color: rgb(15, 76, 129);
}
</style>