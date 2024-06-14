import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import elementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import "@icon-park/vue-next/styles/index.css";
import ECharts from 'echarts'
const app = createApp(App)
// 将 ECharts 挂载到全局属性 $echarts 上
app.config.globalProperties.$echarts = ECharts;
app.use(router).use(elementPlus).mount('#app')
