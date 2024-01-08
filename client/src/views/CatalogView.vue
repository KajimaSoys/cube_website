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
        })
        .catch(error => {
          console.log('An error occurred: ', error);
        });
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero();
  },
  methods: {
    async getPageData() {
      try {
        let response = await axios.get(`${this.backendURL}/api/v1/catalog_page/`);
        let receivedData = response.data;

        this.header_block = receivedData.header_block;
        this.add_question_block = receivedData.add_question_block;
        this.category_list = receivedData.category_list;

        let categorySlug = this.$route.params.categorySlug;
        let currentCategory = this.category_list.find(cat => cat.slug === categorySlug);
        if (currentCategory) {
          this.$route.meta.breadcrumb[2].name = currentCategory.name;
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
        this.$route.meta.breadcrumb[2].name = currentCategory.name;
      }
    },
    scrollToZero() {
      document.documentElement.scrollTop = 0;
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