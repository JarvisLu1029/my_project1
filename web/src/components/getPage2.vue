<template>
    <div>
      <!-- 分页内容 -->
      <ul>
        <li v-for="item in paginatedData" :key="item.id">{{ item.name }}</li>
      </ul>
  
      <!-- 分页导航 -->
      <ul>
        <li v-for="pageNumber in totalPages" :key="pageNumber">
          <button @click="gotoPage(pageNumber)">{{ pageNumber }}</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        data: [], // 所有获取到的数据
        currentPage: 1, // 当前页码
        itemsPerPage: 3, // 每页显示的数据条数
      };
    },
    computed: {
      totalItems() {
        return this.data.length; // 总数据条数
      },
      totalPages() {
        return Math.ceil(this.totalItems / this.itemsPerPage); // 总页数
      },
      paginatedData() {
        const startIndex = (this.currentPage - 1) * this.itemsPerPage;
        const endIndex = startIndex + this.itemsPerPage;
        return this.data.slice(startIndex, endIndex); // 当前页的数据
      },
    },
    methods: {
      async fetchData() {
        // 通过异步请求获取 API 数据
        const response = await fetch('http://192.168.73.128:5000/data2/');
        this.data = await response.json();
        this.data = await [{name:'jack'}, {name:'jack'}, {name:'jack'}, {name:'Amy'}, {name:'jack'}, {name:'jack'}]
      },
      gotoPage(pageNumber) {
        this.currentPage = pageNumber; // 切换到指定页码
      },
    },
    mounted() {
      this.fetchData(); // 组件挂载后获取数据
    },
  };
  </script>
  