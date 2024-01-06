<template>
  <Header
      :header_block="header_block"
  />

  <div v-if="show">

    <Breadcrumbs ref="breadcrumbs" v-if="category_list.length > 0"/>

    <Product
        :product="product"
    />

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
import Breadcrumbs from "../components/common/Breadcrumbs.vue";
import axios from "axios";

export default {
  name: "ProductView",
  inject: ['backendURL'],
  components: {
    Header,
    Product,
    ProductSlider,
    Breadcrumbs,
    Footer
  },
  data() {
    return {
      header_block: {},
      recommended_product_block: [],
      category_list: [],

      product: {},

      show: false
    }
  },
  watch: {
    '$route': {
      immediate: true,
      handler() {
        this.getProduct();
      }
    }
  },
  created() {
    Promise.all([
      this.getPageData(),
      this.getProduct()
    ])
        .then(() => {
          console.log("Оба запроса завершены");
          this.show = true
        })
        .catch(error => {
          console.log('Произошла ошибка при выполнении запросов: ', error);
        });
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero();
  },
  methods: {
    async getPageData() {
      try {
        let response = await axios.get(`${this.backendURL}/api/v1/product_page/`);
        let receivedData = response.data;

        this.header_block = receivedData.header_block;
        this.recommended_product_block = receivedData.recommended_product_block
        this.category_list = receivedData.category_list;
      } catch (error) {
        console.error('Ошибка в getPageData: ', error);
      }
    },
    async getProduct() {
      this.show = false
      try {
        let productId = this.$route.params.productId;
        let response = await axios.get(`${this.backendURL}/api/v1/products/${productId}/`);
        this.product = response.data[0];
        console.log(this.product)

        this.updateBreadcrumb()
        if (this.$refs.breadcrumbs) {
          this.$refs.breadcrumbs.updateList();
        }

        this.show = true
      } catch (error) {
        console.error('Ошибка в getProduct: ', error);
        this.show = true
      }
    },
    updateBreadcrumb() {
      this.$route.meta.breadcrumb[2].name = this.product.category_info.name;
      this.$route.meta.breadcrumb[2].link = `/catalog/${this.product.category_info.slug}`
      this.$route.meta.breadcrumb[3].name = this.product.name;
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