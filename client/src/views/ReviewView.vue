<template>
  <Header
      :header_block="header_block"
  />

  <div v-if="show">

    <Breadcrumbs/>

    <Reviews/>

    <RecommendedProduct
        :recommended_product_block="recommended_product_block"
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
import RecommendedProduct from "../components/common/RecommendedProduct.vue";
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
    RecommendedProduct,
    AddQuestion,
    Footer,
    Breadcrumbs,
  },
  data() {
    return {
      header_block: {},
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
  },
  methods: {
    async getPageData() {
      await axios
          .get(`${this.backendURL}/api/v1/reviews_page/`)
          .then(response => {
            let receivedData = response.data

            this.header_block = receivedData.header_block
            this.recommended_product_block = receivedData.recommended_product_block
            this.add_question_block = receivedData.add_question_block
            this.category_list = receivedData.category_list

            this.show = true

            console.log(response.data)
          })
          .catch(error => {
            console.log('An error occurred: ', error)
          })
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


@media screen and (max-width: 1280px) {

}

@media screen and (max-width: 1000px) {

}

@media screen and (max-width: 640px) {

}
</style>