<template>
  <div class="product-component">
    <div class="product-max">
      <div class="product-content">
        <div class="left-side">
          <h1 class="title tablet">
            {{ product.name }}
          </h1>

          <div class="image-slider" v-if="product.images.length > 1">
            <swiper
                :navigation="true"
                :modules="modules"
                :slides-per-view="1"
                :initial-slide="this.currentImageIndex"
                :space-between="32"
                :onSwiper="getSwiperInstance"
            >
              <swiper-slide
                  v-for="(image, index) in product.images"
                  :key="index"
              >
                <div class="slider-image-container">
                  <img :src="strippedSrc(image.image)" loading="lazy" alt=""/>
                </div>
              </swiper-slide>
            </swiper>
          </div>

          <div class="image-container" v-else>
            <img :src="strippedSrc(product.images[0].image)" loading="lazy" alt=""/>
          </div>

          <div class="images-navigation" v-if="product.images.length > 1">
            <div class="image-thumb"
                 :class="{'active': isActive(index)}"
                 v-for="(image, index) in product.images"
                 :key="index"
                 @click="switchImage(index)"
            >
              <img :src="strippedSrc(image.image)" loading="lazy" alt="">
            </div>
          </div>

        </div>
        <div class="right-side">
          <h1 class="title desktop">
            {{ product.name }}
          </h1>

          <div class="description-block">
            <div class="price-one">
              {{ product.prices[0].price }} ₽ / шт
            </div>
            <div class="description" v-html="product.description"></div>
            <div class="characteristics">

              <div class="characteristics-subtitle" v-if="product.size">
                Внутренний размер
              </div>
              <div class="characteristics-value" v-if="product.size">
                {{ product.size }}
              </div>

              <div class="characteristics-subtitle" v-if="product.material">
                Материал
              </div>
              <div class="characteristics-value" v-if="product.material">
                {{ product.material }}
              </div>

              <div class="characteristics-subtitle" v-if="product.color">
                Цвет
              </div>
              <div class="characteristics-value" v-if="product.color">
                {{ product.color }}
              </div>
            </div>
          </div>

          <div class="purchase-block">
            <div class="quantity-choice">
              <div
                  class="minus-button button"
                  :class="{
                'disabled': count===min_value,
                'scaling-svg': isScalingMinus,
                'out-of-stock-svg': !product.in_stock
              }"
                  @click="decreaseOnce"
                  @mousedown="startDecreasing"
                  @mouseup="stopDecreasing"
                  @mouseleave="stopDecreasing"
                  title="Удерживайте, чтобы быстрее уменьшить кол-во товара"
              >
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
                  <path fill-rule="evenodd" clip-rule="evenodd"
                        d="M5.77606 3.15396C7.05953 2.5 8.73969 2.5 12.1 2.5L35.9 2.5C39.2603 2.5 40.9405 2.5 42.2239 3.15396C43.3529 3.7292 44.2708 4.64709 44.846 5.77606C45.5 7.05953 45.5 8.73969 45.5 12.1V35.9C45.5 39.2603 45.5 40.9405 44.846 42.2239C44.2708 43.3529 43.3529 44.2708 42.2239 44.846C40.9405 45.5 39.2603 45.5 35.9 45.5H12.1C8.73969 45.5 7.05953 45.5 5.77606 44.846C4.64708 44.2708 3.7292 43.3529 3.15396 42.2239C2.5 40.9405 2.5 39.2603 2.5 35.9L2.5 12.1C2.5 8.73968 2.5 7.05953 3.15396 5.77606C3.7292 4.64708 4.64709 3.7292 5.77606 3.15396ZM16 23C15.4477 23 15 23.4477 15 24C15 24.5523 15.4477 25 16 25H32C32.5523 25 33 24.5523 33 24C33 23.4477 32.5523 23 32 23H16Z"
                        fill="#40AB5E"/>
                </svg>
              </div>

              <div class="price-container">
                <div class="quantity">
                  {{ count }} шт
                </div>
                <div class="price">
                  {{ calculatedPrice }} ₽
                </div>
              </div>

              <div class="plus-button button"
                   :class="{
                  'disabled': count===max_value,
                  'scaling-svg': isScalingPlus,
                  'out-of-stock-svg': !product.in_stock
               }"
                   @click="increaseOnce"
                   @mousedown="startIncreasing"
                   @mouseup="stopIncreasing"
                   @mouseleave="stopIncreasing"
                   title="Удерживайте, чтобы быстрее увеличить кол-во товара"
              >
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
                  <path fill-rule="evenodd" clip-rule="evenodd"
                        d="M5.77606 3.15396C7.05953 2.5 8.73969 2.5 12.1 2.5L35.9 2.5C39.2603 2.5 40.9405 2.5 42.2239 3.15396C43.3529 3.7292 44.2708 4.64709 44.846 5.77606C45.5 7.05953 45.5 8.73969 45.5 12.1V35.9C45.5 39.2603 45.5 40.9405 44.846 42.2239C44.2708 43.3529 43.3529 44.2708 42.2239 44.846C40.9405 45.5 39.2603 45.5 35.9 45.5H12.1C8.73969 45.5 7.05953 45.5 5.77606 44.846C4.64708 44.2708 3.7292 43.3529 3.15396 42.2239C2.5 40.9405 2.5 39.2603 2.5 35.9L2.5 12.1C2.5 8.73968 2.5 7.05953 3.15396 5.77606C3.7292 4.64708 4.64709 3.7292 5.77606 3.15396ZM25 16C25 15.4477 24.5523 15 24 15C23.4477 15 23 15.4477 23 16V23H16C15.4477 23 15 23.4477 15 24C15 24.5523 15.4477 25 16 25H23V32C23 32.5523 23.4477 33 24 33C24.5523 33 25 32.5523 25 32V25H32C32.5523 25 33 24.5523 33 24C33 23.4477 32.5523 23 32 23H25V16Z"
                        fill="#40AB5E"/>
                </svg>
              </div>
            </div>
            <div v-if="product.in_stock" @click="addToCart" class="purchase-button">
              В корзину
            </div>
            <div v-else class="purchase-button out-of-stock">
              Нет в наличии
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import CartPopup from "../common/CartPopup.vue";
import {ElNotification} from "element-plus";

import {Navigation, Pagination, Scrollbar, A11y} from 'swiper/modules';
import {Swiper, SwiperSlide, useSwiper} from 'swiper/vue';

import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import 'swiper/css/keyboard'

export default {
  name: "Product",
  inject: ['backendURL'],
  props: {
    product: {
      type: Object
    }
  },
  emits: [
    'add-to-cart'
  ],
  components: {
    CartPopup,
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      currentImageIndex: 0,
      swiperInstance: null,

      count: 1,
      interval: null,
      increaseAmount: 1,

      isScalingPlus: false,
      isScalingMinus: false,

      max_value: 9999,
      min_value: 1,

      showCartPopup: false,
    }
  },
  mounted() {
  },
  watch: {
    currentImageIndex: {
      immediate: true,
      handler(newVal) {
        console.log(newVal)
      }
    }
  },
  computed: {
    calculatedPrice() {
      const basePrice = this.product.prices.find(price => price.count === 1).price;
      let finalPrice = basePrice * this.count;

      this.product.prices.forEach(priceInfo => {
        if (this.count >= priceInfo.count) {
          finalPrice = priceInfo.price * this.count;
        }
      });

      return finalPrice.toFixed(2);
    },
  },
  methods: {

    getSwiperInstance(swiper) {
      this.swiperInstance = swiper;
    },

    switchImage(index) {
      if (this.swiperInstance) {
        this.swiperInstance.slideTo(index);
      }
      this.currentImageIndex = index
    },

    isActive(index) {
      return index === this.currentImageIndex
    },

    increaseOnce() {
      this.count++;
      if (this.count > this.max_value) {
        this.count = this.max_value
      }
    },
    decreaseOnce() {
      this.count--
      if (this.count < this.min_value) {
        this.count = this.min_value
      }
    },
    startIncreasing() {
      if (this.interval) return;

      this.interval = setInterval(() => {
        this.count += this.increaseAmount;
        if (this.count > this.max_value) {
          this.count = this.max_value
          this.increaseAmount = 1
        }
        this.isScalingPlus = true;
        this.increaseAmount++;
      }, 200);
    },
    stopIncreasing() {
      clearInterval(this.interval);
      this.isScalingPlus = false;

      this.interval = null;
      this.increaseAmount = 1;
    },
    startDecreasing() {
      if (this.interval) return;

      this.interval = setInterval(() => {
        this.count -= this.increaseAmount;
        if (this.count < this.min_value) {
          this.count = this.min_value
          this.increaseAmount = 1
        }
        this.isScalingMinus = true;
        this.increaseAmount++;
      }, 200);
    },
    stopDecreasing() {
      clearInterval(this.interval);
      this.isScalingMinus = false;

      this.interval = null;
      this.increaseAmount = 1;
    },

    addToCart() {
      this.$emit('add-to-cart', this.product.id, this.count);
      // this.showCartPopup = true;
      ElNotification({
        title: 'Товар добавлен в корзину!',
        type: 'success',
        duration: 2500,
        position: 'bottom-right',
        dangerouslyUseHTMLString: true,
        message: '<a class="button notification" href="/cart">Перейти в корзину</a>',
      })
    },

    strippedSrc(image) {
      return this.backendURL + '/media' + image.split('/media')[1]
    }
  },
  setup() {
    // const swiper = useSwiper();

    return {
      // swiper,
      modules: [Navigation],
    };
  },
}
</script>


<style scoped>
.product-component {
  margin-left: auto;
  margin-right: auto;

  display: flex;
  justify-content: center;
  align-items: center;
}

.product-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
}

.product-content {
  display: flex;
  flex-direction: row;
  gap: 7.5rem;
}

.left-side {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.title.tablet {
  display: none;
}

:deep(.swiper-wrapper) {
  width: 35.625rem !important;
}

.slider-image-container {
  width: 35.625rem;
  height: 31.375rem;
  border-radius: 1rem;
  background: #FFF;
  display: flex;
  /* padding: 1rem; */
  align-items: center;
  justify-content: center;
}

.slider-image-container img {
  object-fit: contain;
  width: 35.625rem;
  height: 29.375rem;
  scale: 0.9;
}

.image-container {
  width: 35.625rem;
  height: 29.375rem;
  border-radius: 1rem;
  background: #FFF;
  padding: 1rem;
  cursor: pointer;
}

.image-container img {
  object-fit: contain;
  width: 35.625rem;
  height: 29.375rem;
}

.images-navigation {
  display: flex;
  flex-direction: row;
  gap: 1rem;
}

.image-thumb {
  width: 4.4375rem;
  height: 3.5625rem;
  border-radius: 0.5rem;
  background: #FFF;
  padding: 0.5rem;
  cursor: pointer;
  transition: opacity 0.2s ease-in-out;
}

.image-thumb.active {
  border: 1px solid var(--green-light, #40AB5E);
}

.image-thumb:hover {
  opacity: 0.5;
}

.image-thumb img {
  object-fit: contain;
  width: 4.4375rem;
  height: 3.5625rem;
}

.right-side {
  display: flex;
  flex-direction: column;
  flex: 1;
}

.title {
  font-size: 2rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;

  margin-bottom: 2rem;
}

.description-block {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin-bottom: 4rem;
}

.characteristics {
  display: grid;
  grid-template-columns: 2fr 2fr;
  gap: 0.5rem 4rem;
}

.characteristics-subtitle {
  color: var(--black-55);
}

.purchase-block {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.quantity-choice {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;

  border-radius: 1rem;
  background: #FFF;
  padding: 0.5rem;
}

.button {
  display: flex;
  align-items: center;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease-in-out;
}

.button svg {
  width: 3.5rem;
  height: 3.5rem;
}

.button:hover {
  opacity: 0.5;
}

.price-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.quantity {

}

.price {
  color: var(--black-55);
  font-size: 1.125rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
}

.purchase-button {
  display: flex;
  padding: 1.5rem 1.5rem;
  justify-content: center;
  align-items: center;
  align-self: stretch;
  text-align: center;

  border-radius: 0.5rem;
  background: var(--green-light, #40AB5E);
  color: white;
  user-select: none;
  cursor: pointer;

  transition: opacity 0.2s ease-in-out;
}

.purchase-button:hover {
  opacity: 0.5;
}

.disabled {
  opacity: 0.5;
  pointer-events: none;
}

.scaling-svg {
  transform: scale(1.2);
}

.out-of-stock {
  pointer-events: none;
  background-color: var(--black-35);
}

.out-of-stock-svg {
  pointer-events: none;
}

.out-of-stock-svg svg path {
  fill: var(--black-35);
}

@media screen and (max-width: 1280px) {
  .product-component {
  }

  .product-max {
    padding: 0 2.25rem;
  }

  .product-content {
    gap: 4rem;
  }

  .title {
    font-size: 1.5rem;
  }
}

@media screen and (max-width: 1000px) {
  .product-component {
  }

  .product-max {
    padding: 0 2.25rem;
  }

  .product-content {
    gap: 2rem;
  }
}

@media screen and (max-width: 640px) {
  .product-component {
  }

  .product-max {
    padding: 0 1rem;
  }

  .product-content {
  }

  .title {
    font-size: 1.25rem;
  }

}
</style>