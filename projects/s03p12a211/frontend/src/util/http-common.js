import axios from "axios";

// axios 객체 생성
export default axios.create({
  baseURL: "http://localhost:8399/ssafy/api",
  headers: {
    "Content-type": "application/json",
  },
});
