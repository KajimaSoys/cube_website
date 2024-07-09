<template>
  <Header
      :header_block="header_block"
  />

  <div v-if="show">

    <Breadcrumbs/>

    <CalculatorDescription
        :calculator_description_block="calculator_description_block"
    />

    <BoxInfo
      @calculate="handleCalculation"
    />

    <CalculationResult
      :calculationData="calculationData"
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

import CalculatorDescription from "../components/calculatorPage/CalculatorDescription.vue";
import BoxInfo from "../components/calculatorPage/BoxInfo.vue";
import CalculationResult from "../components/calculatorPage/CalculationResult.vue";

import Footer from "../components/common/Footer.vue";
import Breadcrumbs from "../components/common/Breadcrumbs.vue";
import axios from "axios";

export default {
  name: "CalculatorView",
  inject: ['backendURL'],
  components: {
    Header,

    CalculatorDescription,
    BoxInfo,
    CalculationResult,

    Footer,
    Breadcrumbs,
  },
  data() {
    return {
      header_block: {},
      calculator_description_block: {},
      additional_product_block: [],

      category_list: [],

      show: false,

      calculationData: null,
    }
  },
  created() {
    this.getPageData()
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero();

    // TODO change to new metadata
    document.title = 'Калькулятор | Магазин упаковки КУБ в Казани';
    // this.setMetaTag('description', 'Узнайте о вариантах доставки и способах оплаты в магазине упаковки КУБ. Быстрая и надежная доставка картонных коробок по Казани и всей России.');
    // this.setMetaTag('keywords', 'доставка упаковки, оплата картонных коробок, магазин упаковки Казань, упаковка для маркетплейсов, удобная доставка');
  },
  methods: {
    async getPageData() {
      await axios
          .get(`${this.backendURL}/api/v1/calculator_page/`)
          .then(response => {
            let receivedData = response.data

            this.header_block = receivedData.header_block
            this.calculator_description_block = receivedData.calculator_description_block
            this.additional_product_block = receivedData.additional_product_block
            this.category_list = receivedData.category_list

            // TODO uncomment on prod
            // window.ym(96164548, 'hit', window.location.href);

            this.show = true
          })
          .catch(error => {
            console.log('An error occurred: ', error);
          })
    },
    scrollToZero() {
      document.documentElement.scrollTop = 0;
    },

    scrollToElement(elementId) {
      const element = document.getElementById(elementId);
      element.scrollIntoView({behavior: "smooth"});
    },

    setMetaTag(name, content) {
      let tag = document.querySelector(`meta[name="${name}"]`);
      if (!tag) {
        tag = document.createElement('meta');
        tag.setAttribute('name', name);
        document.head.appendChild(tag);
      }
      tag.setAttribute('content', content);
    },

    handleCalculation(data) {
      this.calculationData = data;
      setTimeout(() => this.scrollToElement('calculation-result'), 500)

    }
  },
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