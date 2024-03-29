<template>
  <Header
      :header_block="header_block"
  />

  <div v-if="show">


    <Breadcrumbs v-if="category_list.length > 0"/>

    <Catalog
        :category_list="category_list"
        :products="products"
    />

    <AddQuestion
        :add_question_block="add_question_block"
        button_text="Связаться в What’s App"
    />

  </div>
  <div v-else class="loading">
    <div class="spinner spinner-1"></div>
  </div>

  <Footer
      :header_block="header_block"
      :category_list="category_list"
  />
</template>

<script>
import Header from "../components/common/Header.vue";
import Catalog from "../components/catalogPage/Catalog.vue";
import AddQuestion from "../components/common/AddQuestion.vue";
import Footer from "../components/common/Footer.vue";
import Breadcrumbs from "../components/common/Breadcrumbs.vue";
import axios from "axios";

export default {
  name: "CatalogView",
  inject: ['backendURL'],
  components: {
    Header,
    Catalog,
    AddQuestion,
    Footer,
    Breadcrumbs
  },
  data() {
    return {
      header_block: {},
      add_question_block: {},
      category_list: [],

      products: [],

      show: false
    }
  },
  watch: {
    '$route.params.categorySlug': {
      immediate: true,
      handler(newSlug, oldSlug) {
        if (newSlug !== oldSlug) {
          this.updateBreadcrumb(newSlug);
        }
      }
    }
  },
  created() {
    Promise.all([
      this.getPageData(),
      this.getProducts()
    ])
        .then(() => {
          this.show = true
          const savedPosition = localStorage.getItem('catalogScrollPosition');
          if (savedPosition !== null) {
            this.$nextTick(() => {
              window.scrollTo(0, parseInt(savedPosition, 10));
              localStorage.removeItem('catalogScrollPosition');
            });
          }
        })
        .catch(error => {
          console.log('An error occurred: ', error);
        });

    window.addEventListener('beforeunload', this.saveScrollPosition);
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero();

    document.title = 'Каталог | Магазин упаковки КУБ в Казани';
    this.setMetaTag('description', 'Магазин упаковки КУБ предлагает широкий ассортимент картонных коробок и упаковки для любых нужд. Качественный материал, доступные цены.');
    this.setMetaTag('keywords', 'картонные коробки, упаковка Казань, коробки для бизнеса, оптовая упаковка, розничная упаковка');
  },
  destroyed() {
    window.removeEventListener('beforeunload', this.saveScrollPosition);
  },

  beforeRouteLeave(to, from, next) {
    this.saveScrollPosition()
    next();
  },
  methods: {
    async getPageData() {
      try {
        let response = await axios.get(`${this.backendURL}/api/v1/catalog_page/`);
        let receivedData = response.data;

        this.header_block = receivedData.header_block;
        this.add_question_block = receivedData.add_question_block;
        this.category_list = receivedData.category_list;

        window.ym(96164548, 'hit', window.location.href);

        let categorySlug = this.$route.params.categorySlug;
        let currentCategory = this.category_list.find(cat => cat.slug === categorySlug);
        if (currentCategory) {
          let category = currentCategory.name
          this.$route.meta.breadcrumb[2].name = category;
          document.title = `${category} | Магазин упаковки КУБ в Казани`;
          this.setMetaTag('description', `"Ищете ${category} в Казани? Магазин упаковки КУБ предлагает широкий ассортимент картонных коробок и упаковки для любых нужд. Качественный материал, доступные цены.`);
          this.setMetaTag('keywords', `${category}, картонные коробки, упаковка Казань, коробки для бизнеса, оптовая упаковка, розничная упаковка`);
        }
      } catch (error) {
        console.error('Ошибка в getPageData: ', error);
      }
    },
    async getProducts() {
      try {
        let response = await axios.get(`${this.backendURL}/api/v1/products/`);
        this.products = response.data;
      } catch (error) {
        console.error('Ошибка в getProducts: ', error);
      }
    },
    updateBreadcrumb(categorySlug) {
      let currentCategory = this.category_list.find(cat => cat.slug === categorySlug);
      if (currentCategory) {
        let category = currentCategory.name
        this.$route.meta.breadcrumb[2].name = category;
        document.title = `${category} | Магазин упаковки КУБ в Казани`;
        this.setMetaTag('description', `"Ищете ${category} в Казани? Магазин упаковки КУБ предлагает широкий ассортимент картонных коробок и упаковки для любых нужд. Качественный материал, доступные цены.`);
        this.setMetaTag('keywords', `${category}, картонные коробки, упаковка Казань, коробки для бизнеса, оптовая упаковка, розничная упаковка`);
      }
    },

    saveScrollPosition() {
      const scrollPosition = window.scrollY;
      localStorage.setItem('catalogScrollPosition', scrollPosition);
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
:deep(.description) {
  width: 75%;
}

@media screen and (max-width: 1280px) {

}

@media screen and (max-width: 1000px) {
  :deep(.description) {
    width: 95%;
  }
}

@media screen and (max-width: 640px) {

}
</style>