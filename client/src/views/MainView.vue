<template>

  <Header
      :header_block="header_block"
  />

  <div v-if="show">

    <Main
        :main_block="main_block"
    />

    <CatalogTeaser
        :catalog_teaser_block="catalog_teaser_block"
        :category_list="category_list"
    />

    <ServiceOptions
        :service_options_block="service_options_block"
    />

    <NewProduct
        :new_product_block="new_product_block"
    />

    <PopularProduct
        :popular_product_block="popular_product_block"
    />

    <Delivery
        :delivery_block="delivery_block"
    />

    <Advantages
        :advantages_block="advantages_block"
    />

    <CartonInfo
        :carton_info_block="carton_info_block"
    />

    <Request
        :request_block="request_block"
    />

    <Questions
        :questions_block="questions_block"
    />

    <Contacts
        :contacts_block="contacts_block"
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
import Main from "../components/mainPage/Main.vue"
import CatalogTeaser from "../components/mainPage/CatalogTeaser.vue"
import ServiceOptions from "../components/mainPage/ServiceOptions.vue"
import NewProduct from "../components/mainPage/NewProduct.vue"
import PopularProduct from "../components/mainPage/PopularProduct.vue"
import Delivery from "../components/mainPage/Delivery.vue"
import Advantages from "../components/mainPage/Advantages.vue"
import CartonInfo from "../components/mainPage/CartonInfo.vue"
import Request from "../components/mainPage/Request.vue"
import Questions from "../components/mainPage/Questions.vue"
import Contacts from "../components/mainPage/Contacts.vue"
import AddQuestion from "../components/common/AddQuestion.vue";
import Footer from "../components/common/Footer.vue";
import axios from "axios";

export default {
  name: "MainView",
  inject: ['backendURL'],
  components: {
    Header,
    Main,
    CatalogTeaser,
    ServiceOptions,
    NewProduct,
    PopularProduct,
    Delivery,
    Advantages,
    CartonInfo,
    Request,
    Questions,
    Contacts,
    AddQuestion,
    Footer
  },
  data() {
    return {
      header_block: {},
      main_block: {},
      catalog_teaser_block: {},
      category_list: [],
      service_options_block: {},
      new_product_block: [],
      popular_product_block: [],
      delivery_block: {},
      advantages_block: {},
      carton_info_block: {},
      request_block: {},
      questions_block: [],
      add_question_block: {},
      contacts_block: {},

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
          .get(`${this.backendURL}/api/v1/main_page/`)
          .then(response => {
            let receivedData = response.data

            this.header_block = receivedData.header_block
            this.main_block = receivedData.main_block
            this.catalog_teaser_block = receivedData.catalog_teaser_block
            this.service_options_block = receivedData.service_options_block
            this.category_list = receivedData.category_list
            this.new_product_block = receivedData.new_product_block
            this.popular_product_block = receivedData.popular_product_block
            this.delivery_block = receivedData.delivery_block
            this.advantages_block = receivedData.advantages_block
            this.carton_info_block = receivedData.carton_info_block
            this.request_block = receivedData.request_block
            this.questions_block = receivedData.questions_block
            this.contacts_block = receivedData.contacts_block
            this.add_question_block = receivedData.add_question_block

            // window.ym(95108306, 'hit', 'https://kamamebel.com/');

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