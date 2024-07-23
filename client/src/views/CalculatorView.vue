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
      :productList="productList"
      @calculate="handleCalculation"
    />

    <CalculationResult
      :calculationData="calculationData"
      :productList="productList"
      :additionalProductsDefault="additionalProducts"
      @add-to-cart="addToCart"
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
    Header, CalculatorDescription, BoxInfo, CalculationResult, Footer, Breadcrumbs,
  },
  data() {
    return {
      // received data from this.getPageData
      header_block: {},
      calculator_description_block: {},
      category_list: [],

      // received data from this.getProducts
      productList: [],

      // var for this.processAdditionalProducts
      additionalProducts: [],
      // var for this.handleCalculation (emitted from child)
      calculationData: null,

      cart: [],
      show: false,
    }
  },
  created() {
    this.loadCart();
    this.getPageData();
    this.getProducts();
  },
  mounted() {
    this.setupPage();
  },
  methods: {
    setupPage() {
      document.body.style.overflow = "";
      this.scrollToZero();

      document.title = 'Калькулятор | Магазин упаковки КУБ в Казани';
      this.setMetaTag('description', 'Используйте наш уникальный калькулятор для оптимизации упаковки в магазине коробок КУБ в Казани! Узнайте точное количество маленьких коробок, которое поместится в одну большую. Эффективные решения для вашего бизнеса с широким выбором картонных коробок на заказ.');
      this.setMetaTag('keywords', 'калькулятор коробок, оптимизация упаковки Казань, магазин упаковки Казань, упаковка для маркетплейсов, купить картонные коробки Казань, расчет коробок онлайн');
    },

    addToCart(productId, quantity) {
      const cartItem = this.cart.find(item => item.id === productId);

      if (cartItem) {
        cartItem.quantity += quantity;
      } else {
        this.cart.push({id: productId, quantity});
      }

      this.saveCart();
    },
    loadCart() {
      const cartData = localStorage.getItem('cart');
      if (cartData) {
        this.cart = JSON.parse(cartData);
      }
    },
    saveCart() {
      localStorage.setItem('cart', JSON.stringify(this.cart));
    },

    async getPageData() {
      await axios
        .get(`${this.backendURL}/api/v1/calculator_page/`)
        .then(response => {
          const receivedData = response.data
          const additionalProductsRaw = receivedData.additional_products_block

          this.header_block = receivedData.header_block
          this.calculator_description_block = receivedData.calculator_description_block
          this.category_list = receivedData.category_list
          this.additionalProducts = additionalProductsRaw ? additionalProductsRaw.map(product => this.calculateFinalPrice(product.product)) : [];

          window.ym(96164548, 'hit', window.location.href);

          this.show = true
        })
        .catch(error => {
          console.log('An error occurred: ', error);
        })
    },

    async getProducts() {
      const endpoints = [
        `${this.backendURL}/api/v1/category/samosbornye-korobki/`,
        `${this.backendURL}/api/v1/category/chetyrehklapannye-korobki/`
      ];

      try {
        const responses = await Promise.all(endpoints.map(url => axios.get(url)));
        const productList = responses.map(response => response.data).flat();
        this.productList = productList ? productList.map(this.calculateFinalPrice) : [];
      } catch (error) {
        console.error("Failed to fetch products:", error);
      }
    },

    // Общая функция для расчета цены продукта
    calculateFinalPrice(product) {
      const count = 1;
      const basePrice = product.prices.find(price => price.count === 1).price;
      let finalPrice = basePrice * count;
      product.prices.forEach(priceInfo => {
        if (count >= priceInfo.count) {
          finalPrice = priceInfo.price * count;
        }
      });
      const cleanSize = product.size.replace(/[^\d.,xXхХ*]/g, '');

      return {
        ...product,
        count: count,
        finalPrice: finalPrice,
        isScalingPlus: false,
        isScalingMinus: false,
        size: cleanSize
      };
    },

    scrollToZero() {
      document.documentElement.scrollTop = 0;
    },

    scrollToElement(elementId) {
      const requestElement = document.getElementById(elementId);
      const offset = 100;
      const elementPosition = requestElement.getBoundingClientRect().top + window.pageYOffset;
      const offsetPosition = elementPosition - offset;
      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth"
      });
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
      this.calculationData = JSON.parse(JSON.stringify(data));
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