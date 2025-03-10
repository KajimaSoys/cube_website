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

    document.title = 'Корзина | Магазин упаковки КУБ в Казани';
    this.setMetaTag('description', 'Оформите заказ на индивидуальные картонные коробки в магазине упаковки КУБ. Простой процесс, быстрая обработка и доставка в Казани и по России.');
    this.setMetaTag('keywords', 'оформление заказа, индивидуальные коробки, магазин упаковки Казань, заказ коробок онлайн');
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
      this.products = this.products.filter(product => product.status !== 'in_stock');

      this.cart = this.cart.filter(cartItem =>
          this.products.some(product => product.id === cartItem.id)
      );

      this.saveCart();
    },

    async getPageData() {
      try {
        let response = await axios.get(`${this.backendURL}/api/v1/header_data/`);
        let receivedData = response.data;

        this.header_block = receivedData.header_block
        this.category_list = receivedData.category_list

        window.ym(96164548, 'hit', window.location.href);

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