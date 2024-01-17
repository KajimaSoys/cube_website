<template>
  <Header
      :header_block="header_block"
  />

  <div v-if="show">

    <Breadcrumbs/>

    <Delivery
        :delivery_block="delivery_block"
        :separate="true"
    />

    <Payment
        :payment_block="payment_block"
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
import Delivery from "../components/mainPage/Delivery.vue";
import Payment from "../components/deliveryPage/Payment.vue";
import ProductSlider from "../components/common/ProductSlider.vue";
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
    ProductSlider,
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

      show: false
    }
  },
  created() {
    this.getPageData()
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero();

    document.title = 'Доставка и оплата | Магазин упаковки КУБ в Казани';
    this.setMetaTag('description', 'Узнайте о вариантах доставки и способах оплаты в магазине упаковки КУБ. Быстрая и надежная доставка картонных коробок по Казани и всей России.');
    this.setMetaTag('keywords', 'доставка упаковки, оплата картонных коробок, магазин упаковки Казань, упаковка для маркетплейсов, удобная доставка');


    window.ym(96164548, 'hit', window.location.href);
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