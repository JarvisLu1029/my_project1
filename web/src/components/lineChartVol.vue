<template>
    <div style="position: relative; height: 100%; width: 100%">
        <Line v-if="loaded" :style="myStyles" :data="chartData" :options="chartOptions" />
    </div>
</template>
  
<script>
import {
    Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title,
    Tooltip,
    Legend
} from 'chart.js'
import { Line } from 'vue-chartjs'

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
)

export default {
    name: 'LineChart',
    components: { Line },
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
            plugins: {
                title: {
                    display: true,
                    text: '各職業交易成交量'
                }
            },
            stacked: false,
            responsive: true,
            // maintainAspectRatio: true,
            scales: {
                y: {
                    type: 'linear',
                    display: true,
                    position: 'left',
                },
            }
        }
    }),
    async mounted() { // 鉤子
        try {
            // const response = await fetch('http://192.168.73.128:5000/trading_vol');
            // const responseData = await response.json();
            // const date = responseData.date;
            const date = ['Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6', 'Day7'];
            // const data = responseData.vol;
            // this.chartData.labels = data.labels;
            // this.chartData.datasets = data.datasets;

            this.chartData = {
                labels: date,
                datasets: [
                    {
                        label: '野蠻人',
                        backgroundColor: '#f87979',
                        borderColor: '#f87979',
                        data: [21111, 16834, 13562, 24613, 23345, 15672, 23562]
                    },
                    {
                        label: '法師',
                        backgroundColor: '#7acbf9',
                        borderColor: '#7acbf9',
                        data: [13511, 11334, 18562, 16613, 13345, 11672, 20562]
                    },
                    {
                        label: '遊俠',
                        backgroundColor: '#f5f0e1',
                        borderColor: '#f5f0e1',
                        data: [27511, 21134, 10562, 11613, 13345, 19172, 13693]
                    },
                    {
                        label: '死靈',
                        backgroundColor: '#9f4e87',
                        borderColor: '#9f4e87',
                        data: [12511, 25334, 19562, 13613, 19345, 21672, 10562]
                    },
                    {
                        label: '德魯伊',
                        backgroundColor: '#8db73e',
                        borderColor: '#8db73e',
                        data: [11511, 15334, 18562, 13613, 21345, 11672, 10562]
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
  

  