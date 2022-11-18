import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import VueAxios from 'vue-axios'
import App from './App.vue'
import router from './router'

//import './assets/main.css'
import "bootstrap/dist/css/bootstrap.min.css"

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(VueAxios, axios)

app.mount('#app')
import 'bootstrap/dist/js/bootstrap.min.js'
