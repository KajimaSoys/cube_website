import { createApp } from 'vue'
import './assets/style.css'
import App from './App.vue'
import router from './router'
import axios from "axios";
// import { createMetaManager } from 'vue-meta'


const app = createApp(App)
app.use(router, axios)
// app.use(createMetaManager() )

let backendURL = import.meta.env.VITE_BACKEND_HOST;

axios.defaults.baseURL = backendURL
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

app.mount('#app')

app.provide('backendURL', backendURL)
