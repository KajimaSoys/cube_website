<template>
  <Header
      :header_block="header_block"
  />

  <div v-if="show">

    <Order
        :products="products"
        @update-cart="updateCart"
        @remove-from-cart="removeFromCart"
        @clear-cart="clearCart"
        @scroll-to-zero="scrollToZero"
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
import Order from "../components/orderPage/Order.vue";
import Footer from "../components/common/Footer.vue";
import axios from "axios";

export default {
  name: "OrderView",
  inject: ['backendURL'],
  components: {
    Header,
    Order,
    Footer
  },
  data() {
    return {
      header_block: {},
      category_list: [],

      cart: [],
      products: [],

      show: false
    }
  },
  created() {
    this.loadCart();

    Promise.all([
      this.getPageData(),
      this.getProducts()
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
  },
  methods: {
    loadCart() {
      const cartData = localStorage.getItem('cart');
      if (cartData) {
        this.cart = JSON.parse(cartData);
      }
    },
    saveCart() {
      localStorage.setItem('cart', JSON.stringify(this.cart));
    },
    updateCart(productId, count) {
      const cartItem = this.cart.find(item => item.id === productId);
      cartItem.quantity = count;

      this.saveCart();
    },
    removeFromCart(productId) {
      this.cart = this.cart.filter(item => item.id !== productId);
      this.saveCart();

      this.products = this.products.filter(item => item.id !== productId);
    },
    clearCart() {
      this.cart = [];
      this.saveCart();

      this.products = []
    },

    async getPageData() {
      try {
        let response = await axios.get(`${this.backendURL}/api/v1/header_data/`);
        let receivedData = response.data;

        this.header_block = receivedData.header_block
        this.category_list = receivedData.category_list
      } catch (error) {
        console.error('Ошибка в getPageData: ', error);
      }
    },
    async getProducts() {
      try {
        let response = await axios.post(`${this.backendURL}/api/v1/products/`, this.cart);
        let fetchedProducts = response.data;

        this.products = fetchedProducts.map(product => {
          // count calculation
          let cartItem = this.cart.find(item => item.id === product.id);
          let count = cartItem ? cartItem.quantity : 0;

          // price calculation
          const basePrice = product.prices.find(price => price.count === 1).price;
          let finalPrice = basePrice * count;
          product.prices.forEach(priceInfo => {
            if (count >= priceInfo.count) {
              finalPrice = priceInfo.price * count;
            }
          });

          return {
            ...product,
            count: count,
            finalPrice: finalPrice,
            isScalingPlus: false,
            isScalingMinus: false,
          };
        });
      } catch (error) {
        console.error('Ошибка в getProducts: ', error);
      }
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