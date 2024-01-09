<template>
  <Header
      :header_block="header_block"
  />

  <div v-if="show">

    <Breadcrumbs ref="breadcrumbs" v-if="category_list.length > 0"/>

    <Product
        :product="product"
        @add-to-cart="addToCart"
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
      cart: [],

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
    this.loadCart();
    Promise.all([
      this.getPageData(),
      this.getProduct()
    ])
        .then(() => {
          this.show = true
        })
        .catch(error => {
          console.log('An error occurred: ', error);
        });
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero();

    document.title = 'Качественные картонные коробки и упаковки | Магазин упаковки КУБ в Казани';
    this.setMetaTag('description', 'Высокое качество, надежность, доступная цена. Идеально подходят для маркетплейсов вроде OZON и Wildberries.');
    this.setMetaTag('keywords', 'картонные коробки, упаковка для продаж, магазин упаковки Казань, коробки на заказ');
  },
  methods: {
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
    clearCart() {
      this.cart = [];
      this.saveCart();
    },
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
      let productName = this.product.name;

      this.$route.meta.breadcrumb[2].name = this.product.category_info.name;
      this.$route.meta.breadcrumb[2].link = `/catalog/${this.product.category_info.slug}`
      this.$route.meta.breadcrumb[3].name = productName;

      document.title = `${productName} - Качественные картонные коробки и упаковки | Магазин упаковки КУБ в Казани`;
      this.setMetaTag('description', `Получите ${productName} в магазине упаковки КУБ. Высокое качество, надежность, доступная цена. Идеально подходят для маркетплейсов вроде OZON и Wildberries.`);
      this.setMetaTag('keywords', `${productName}, картонные коробки, упаковка для продаж, магазин упаковки Казань, коробки на заказ`);
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