<template>
  <div class="product-list-component">
    <div class="product-list-max">
      <h2>{{ title }}</h2>
      <div class="product-list-content">
        <swiper
            :slides-per-view="slidesPerView"
            :space-between="spaceBetween"
            :modules="modules"
            :loop="slidesPerView < 4"
            :autoplay="{
              delay: 2500,
              disableOnInteraction: true,
            }"
            :grabCursor="true"
        >
          <swiper-slide
              v-for="product in product_list"
              :key="product.product.id"
          >
            <ProductCard
                :product="product.product"
                @add-to-cart="addToCart"
            />
          </swiper-slide>
        </swiper>


      </div>
    </div>
  </div>
</template>

<script>
import ProductCard from "../common/ProductCard.vue";
import {computed, onBeforeUnmount, onMounted, ref} from "vue";
import {Swiper, SwiperSlide} from 'swiper/vue';
import {Autoplay} from 'swiper/modules';

import 'swiper/css';

export default {
  name: "NewProduct",
  props: {
    product_list: Array,
    title: String
  },
  components: {
    ProductCard,
    Swiper,
    SwiperSlide
  },
  data() {
    return {
      cart: [],
    }
  },
  created() {
    this.loadCart();
  },
  mounted() {
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
    }
  },
  setup() {
    const windowWidth = ref(window.innerWidth);
    const slidesPerView = computed(() =>
        windowWidth.value > 1000 ? 4 :
            windowWidth.value > 640 ? 3 : 2
    );

    const spaceBetween = computed(() => windowWidth.value >= 1280 ? 16 : 8);

    const updateWindowWidth = () => {
      windowWidth.value = window.innerWidth;
    };

    onMounted(() => {
      window.addEventListener('resize', updateWindowWidth);
    });

    onBeforeUnmount(() => {
      window.removeEventListener('resize', updateWindowWidth);
    });
    return {
      onSwiper,
      onSlideChange,
      slidesPerView,
      spaceBetween,
      modules: [Autoplay]
    };
  },
}
</script>


<style scoped>
.product-list-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 9rem;

  display: flex;
  justify-content: center;
  align-items: center;
}

.product-list-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
}

.product-list-content {
  margin-top: 4rem;
  display: flex;
  flex-direction: row;
  gap: 1rem;
}

:deep(.product-card) {
  height: 28.5rem;
}

@media screen and (max-width: 1280px) {
  .product-list-component {
    padding-top: 8rem;
  }

  .product-list-max, h2, .product-list-content {
    padding: 0 2.25rem;
  }

  .product-list-content {
    margin-top: 2.5rem;
    gap: 0.5rem;
  }

  :deep(.product-card) {
    height: 26.6rem;
  }
}

@media screen and (max-width: 1000px) {
  .product-list-component {
    padding-top: 5rem;
  }

  :deep(.product-card) {
    height: 21.9rem;
  }
}

@media screen and (max-width: 640px) {
  .product-list-component {
    padding-top: 4.4rem;
  }

  .product-list-max, h2, .product-list-content {
    padding: 0 1rem;
  }

  .product-list-content {
    margin-top: 1.5rem;
  }

  :deep(.product-card) {
    height: 20.1rem;
  }
}
</style>