<template>
    <div  style="position: relative; height: 100%; width: 100%">
        <Bar v-if="loaded" :style="myStyles" :data="chartData" :options="chartOptions" />
    </div>
</template>
  
<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
    name: 'BarChart',
    components: { Bar },
    data: () => ({
        loaded: false,
        chartData: null,
        myStyles: {
            // display: auto
            display: 'initial !important', // 取消預設的 display: block 才可以隨著畫面縮放
            // width: '100%',
            // position: 'relative',
        },
        chartOptions: {
            responsive: true,
            // maintainAspectRatio: true,
            scales: {
                x: {
                    stacked: true,
                },
                y: {
                    stacked: true,
                }
            }
        }
    }),
    async mounted() { // 鉤子
        try {
            const response = await fetch('http://192.168.73.128:5000/trading_vol');
            const responseData = await response.json();
            const date = responseData.date;
            // const data = responseData.vol;
            // this.chartData.labels = data.labels;
            // this.chartData.datasets = data.datasets;

            this.chartData = {
                labels: date,
                datasets: [
                    {
                        label: '野蠻人',
                        backgroundColor: '#f87979',
                        data: [12345, 12345]
                    },
                    {
                        label: '法師',
                        backgroundColor: '#7acbf9',
                        data: [12345, 12345]
                    },
                    {
                        label: '遊俠',
                        backgroundColor: '#f5f0e1',
                        data: [12345, 12345]
                    },
                    {
                        label: '死靈',
                        backgroundColor: '#f5f5f5',
                        data: [12345, 12345]
                    },
                    {
                        label: '德魯伊',
                        backgroundColor: '#f2e9e4',
                        data: [12345, 12345]
                    }
                ]
            }

            this.loaded = true;
        } catch (error) {
            console.error(error);
        }
    }
};
</script>
  

  