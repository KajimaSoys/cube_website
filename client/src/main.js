import { createApp } from 'vue'
import './assets/style.css'
import App from './App.vue'
import router from './router'
import axios from "axios";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
// import { createMetaManager } from 'vue-meta'


const app = createApp(App)
app.use(router, axios)
app.use(ElementPlus)
// app.use(createMetaManager() )

let hmac_key = import.meta.env.VITE_HMAC_SECRET_KEY;
let backendURL = import.meta.env.VITE_BACKEND_HOST;
let frontendURL = import.meta.env.VITE_FRONTEND_HOST;

axios.defaults.baseURL = backendURL
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

app.mount('#app')

app.provide('hmac_key', hmac_key)
app.provide('backendURL', backendURL)
app.provide('frontendURL', frontendURL)
