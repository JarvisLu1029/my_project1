import { createApp } from 'vue'
import App from './App.vue'
import fetchData from './components/fetchData.vue'
import chartVol from './components/barChartVol.vue'
import lineChartVol from './components/lineChartVol.vue'
import card from './components/fetchCard.vue'
import page from './components/getPage.vue'
import './assets/css/main.css';
// import './assets/css/card.css';

const app1 = createApp(App)
app1.mount('#app')

const app2 = createApp(fetchData)
app2.mount('#fetchData')

const app3 = createApp(chartVol)
app3.mount('#chartVol')

const app4 = createApp(card)
app4.mount('#fetchCard')

const app5 = createApp(page)
app5.mount('#page')

const app6 = createApp(lineChartVol)
app6.mount('#lineChart')