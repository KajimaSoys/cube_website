<template>
  <Header
    :header_block="header_block"
  />

  <Product/>

  <RecommendedProduct
    :recommended_product_block="recommended_product_block"
  />

  <Footer
    :header_block="header_block"
  />
</template>

<script>
import Header from "../components/common/Header.vue";
import Product from "../components/productPage/Product.vue";
import RecommendedProduct from "../components/common/RecommendedProduct.vue";
import Footer from "../components/common/Footer.vue";
import axios from "axios";

export default {
  name: "ProductView",
  inject: ['backendURL'],
  components: {
    Header,
    Product,
    RecommendedProduct,
    Footer
  },
  data() {
    return {
      header_block: {},
      recommended_product_block: [],
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