<template>

  <div class="not-found-container">
    <Header
        :header_block="header_block"
    />

    <div class="not-found-view">
      <div class="not-found-max">
        <h1>Страница не найдена</h1>
      </div>
    </div>

    <Footer
        :header_block="header_block"
        :category_list="category_list"
    />
  </div>
</template>

<script>
import Header from "../components/common/Header.vue";

import Footer from "../components/common/Footer.vue";
import axios from "axios";

export default {
  name: "NotFoundView",
  inject: ['backendURL'],
  components: {
    Header,
    Footer
  },
  data() {
    return {
      header_block: {},
      category_list: [],
    }
  },
  created() {
    this.getPageData()
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero();

    document.title = 'Страница не найдена | Магазин упаковки КУБ в Казани';
    this.setMetaTag('description', 'Страница не найдена. Вернитесь на главную страницу магазина упаковки КУБ для поиска картонных коробок и упаковок в Казани.');
    this.setMetaTag('keywords', 'страница не найдена, ошибка 404, магазин упаковки Казань, навигация по сайту');
  },
  methods: {
    async getPageData() {
      await axios
          .get(`${this.backendURL}/api/v1/header_data/`)
          .then(response => {
            let receivedData = response.data

            this.header_block = receivedData.header_block
            this.category_list = receivedData.category_list

            window.ym(96164548, 'hit', window.location.href);
          })
          .catch(error => {
            console.log('An error occurred: ', error);
          })
    },
    scrollToZero() {
      document.documentElement.scrollTop = 0;
    },
    setMetaTag(name, content) {
      let tag = document.querySelector(`meta[name="${name}"]`);
      if (!tag) {
        tag = document.createElement('meta');
        tag.setAttribute('name', name);
        document.head.appendChild(tag);
      }
      tag.setAttribute('content', content);
    }
  },
  setup() {
    const title = 'Title';
    const description = 'Description';
  }
}
</script>


<style scoped>
.not-found-container {
  height: 100vh;

}

.not-found-view {
  text-align: center;
  margin-left: auto;
  margin-right: auto;
  padding-top: 15.375rem;
  padding-left: 2rem;
  padding-right: 2rem;
  margin-bottom: 12.5rem;
  flex: 1;
}

.not-found-max {
  width: 100%;
}


@media screen and (max-width: 1280px) {

}

@media screen and (max-width: 1000px) {

}

@media screen and (max-width: 640px) {

}
</style>