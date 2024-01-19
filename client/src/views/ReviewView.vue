<template>
  <Header
      :header_block="header_block"
  />

  <div v-if="show">

    <Breadcrumbs/>

    <Reviews
        :reviews="reviews"
    />

    <ProductSlider
        :product_list="recommended_product_block"
        title="Рекомендуем посмотреть"
    />

    <AddQuestion
        :add_question_block="add_question_block"
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
import Reviews from "../components/ReviewPage/Reviews.vue";
import ProductSlider from "../components/common/ProductSlider.vue";
import AddQuestion from "../components/common/AddQuestion.vue";
import Footer from "../components/common/Footer.vue";
import Breadcrumbs from "../components/common/Breadcrumbs.vue";
import axios from "axios";

export default {
  name: "ReviewView",
  inject: ['backendURL'],
  components: {
    Header,
    Reviews,
    ProductSlider,
    AddQuestion,
    Footer,
    Breadcrumbs,
  },
  data() {
    return {
      header_block: {},
      reviews: [],
      recommended_product_block: [],
      add_question_block: {},
      category_list: [],

      show: false
    }
  },
  created() {
    this.getPageData()
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero();

    document.title = 'Отзывы | Магазин упаковки КУБ в Казани';
    this.setMetaTag('description', 'Прочитайте отзывы клиентов о магазине упаковки КУБ. Узнайте, почему наши картонные коробки - выбор многих людей и предприятий в Казани.');
    this.setMetaTag('keywords', 'отзывы упаковка Казань, магазин картонных коробок, клиентские отзывы КУБ, качество упаковочных материалов');
  },
  methods: {
    async getPageData() {
      await axios
          .get(`${this.backendURL}/api/v1/reviews_page/`)
          .then(response => {
            let receivedData = response.data

            this.header_block = receivedData.header_block
            this.reviews = receivedData.reviews
            this.recommended_product_block = receivedData.recommended_product_block
            this.add_question_block = receivedData.add_question_block
            this.category_list = receivedData.category_list

            window.ym(96164548, 'hit', window.location.href);

            this.show = true
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


@media screen and (max-width: 1280px) {

}

@media screen and (max-width: 1000px) {

}

@media screen and (max-width: 640px) {

}
</style>