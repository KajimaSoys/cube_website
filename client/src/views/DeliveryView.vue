<template>
  <Header
      :header_block="header_block"
  />

  <Breadcrumbs />

  <Delivery
      :delivery_block="delivery_block"
      :separate="true"
  />

  <Payment
      :payment_block="payment_block"
  />

  <RecommendedProduct
      :recommended_product_block="recommended_product_block"
  />

  <AddQuestion
      :add_question_block="add_question_block"
  />

  <Footer
      :header_block="header_block"
      :category_list="category_list"
  />
</template>

<script>
import Header from "../components/common/Header.vue";
import Delivery from "../components/mainPage/Delivery.vue";
import Payment from "../components/deliveryPage/Payment.vue";
import RecommendedProduct from "../components/common/RecommendedProduct.vue";
import AddQuestion from "../components/common/AddQuestion.vue";
import Footer from "../components/common/Footer.vue";
import Breadcrumbs from "../components/common/Breadcrumbs.vue";
import axios from "axios";

export default {
  name: "DeliveryView",
  inject: ['backendURL'],
  components: {
    Header,
    Delivery,
    Payment,
    RecommendedProduct,
    AddQuestion,
    Footer,
    Breadcrumbs,
  },
  data() {
    return {
      header_block: {},
      delivery_block: {},
      payment_block: {},
      recommended_product_block: [],
      add_question_block: {},
      category_list: [],
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
          .get(`${this.backendURL}/api/v1/delivery_page/`)
          .then(response => {
            let receivedData = response.data

            this.header_block = receivedData.header_block
            this.delivery_block = receivedData.delivery_block
            this.payment_block = receivedData.payment_block
            this.recommended_product_block = receivedData.recommended_product_block
            this.add_question_block = receivedData.add_question_block
            this.category_list = receivedData.category_list

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