import { createApp } from 'vue'
import './assets/style.css'
import App from './App.vue'
import router from './router'
import axios from "axios";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'


const app = createApp(App)
app.use(router, axios)
app.use(ElementPlus)

let hmac_key = import.meta.env.VITE_HMAC_SECRET_KEY;
let backendURL = import.meta.env.VITE_BACKEND_HOST;
let frontendURL = import.meta.env.VITE_FRONTEND_HOST;

axios.defaults.baseURL = backendURL
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

router.isReady().then(() => {
  app.mount('#app')

  window.ym = window.ym || function() {
    (window.ym.a = window.ym.a || []).push(arguments)
  }
  window.ym.l = 1 * new Date()
  ym(96164548, 'init', {
    clickmap: true,
    trackLinks: true,
    accurateTrackBounce: true,
    // webvisor: true,
  })

  let script = document.createElement('script')
  script.type = 'text/javascript'
  script.async = true
  script.src = 'https://mc.yandex.ru/metrika/tag.js'
  let firstScript = document.getElementsByTagName('script')[0]
  firstScript.parentNode.insertBefore(script, firstScript)
})

app.provide('hmac_key', hmac_key)
app.provide('backendURL', backendURL)
app.provide('frontendURL', frontendURL)
