import { Bar } from "vue-chartjs";
import http from "@/util/http-common";

export default {
  extends: Bar,
  data() {
    return {
      items: [],
      maxNum: -1,
    };
  },

  mounted() {
    // Overwriting base render method with actual data.
    http
      .get(`/situation`)
      .then(({ data }) => {
        if (data != null) {
          this.$store.state.situations = data;
          this.items = data;

          for (let index = 0; index < this.items[1].length; index++) {
            if (this.maxNum < this.items[1][index].count) {
              this.maxNum = this.items[1][index].count;
            }
          }

          this.makegraph();
        } else {
          alert(" 실패했습니다.");
        }
      })
      .catch(() => {
        alert("에러가 발생했습니다.");
      });
  },
  methods: {
    makegraph() {
      this.renderChart(
        {
          labels: [
            "1월",
            "2월",
            "3월",
            "4월",
            "5월",
            "6월",
            "7월",
            "8월",
            "9월",
            "10월",
            "11월",
            "12월",
          ],
          datasets: [
            {
              label: "교통 사고 현황",
              borderColor: "rgba(100, 100, 100, 1)",
              backgroundColor: "rgba(15, 76, 129, 0.6)",
              data: [
                this.items[1][0].count,
                this.items[1][1].count,
                this.items[1][2].count,
                this.items[1][3].count,
                this.items[1][4].count,
                this.items[1][5].count,
                this.items[1][6].count,
                this.items[1][7].count,
                this.items[1][8].count,
                this.items[1][9].count,
                this.items[1][10].count,
                this.items[1][11].count,
              ],
            },
          ],
        },
        {
          legend: {
            //hides the legend
            display: false,
          },
          scales: {
            yAxes: [
              {
                ticks: {
                  max: this.maxNum * 1.2,
                  beginAtZero: true,
                },
              },
            ],
          },
        }
      );
    },
  },
};
