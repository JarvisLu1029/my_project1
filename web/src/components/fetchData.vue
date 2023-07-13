<template>
  <div id="fetchData">
    <div>
    <button @click="fetchData">點擊請求API</button>
    </div>
    <div class="card" v-for="item in data" :key="item.id">
      <div class="header">
        <img :src="item.img_url" alt="图片描述">
      </div>
      <div class="info">
        <p class="title">{{ item.title }}</p>
        <p>$ {{ item.price }}</p>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      data: []
    };
  },
  methods: {
    fetchData() {
      axios.get('http://192.168.73.128:5000/data2/')
        .then(response => {
          this.data = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
  
  
<style scoped src="@/assets/css/plus.css">
/* @import '../assets/css/plus.css'; */

</style>
  