<template>
  <Header
      :header_block="header_block"
  />

  <div v-if="show">

    <Product/>

    <ProductSlider
        :product_list="recommended_product_block"
        title="Рекомендуем посмотреть"
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
import Product from "../components/productPage/Product.vue";
import ProductSlider from "../components/common/ProductSlider.vue";
import Footer from "../components/common/Footer.vue";
import axios from "axios";

export default {
  name: "ProductView",
  inject: ['backendURL'],
  components: {
    Header,
    Product,
    ProductSlider,
    Footer
  },
  data() {
    return {
      header_block: {},
      recommended_product_block: [],
      category_list: [],

      show: false
    }
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero();
  },
  created() {
    this.getPageData()
  },
  methods: {
    async getPageData() {
      await axios
          .get(`${this.backendURL}/api/v1/product_page/`)
          .then(response => {
            let receivedData = response.data

            this.header_block = receivedData.header_block
            this.recommended_product_block = receivedData.recommended_product_block
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