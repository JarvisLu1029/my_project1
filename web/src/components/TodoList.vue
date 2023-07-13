<template>
    <div id="app">
      <h2>待辦事項清單</h2>
      <ul>
        <li v-for="item in todoList" :key="item.id">{{ item.title }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        todoList: [
          { id: 1, title: '完成專案報告' },
          { id: 2, title: '寫測試用例' },
          { id: 3, title: '修復Bug' }
        ]
      };
    }
  };
  </script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
