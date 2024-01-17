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
                :modules="modules"
                :slides-per-view="1"
                :initial-slide="this.currentImageIndex"
                :space-between="32"
                :navigation="{ nextEl: `.swiper-button-next`, prevEl: `.swiper-button-prev` }"
                :onSwiper="getSwiperInstance"
                @slideChange="onSlideChange"
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
            <div class="swiper-controls">
              <div class="swiper-button-prev">
                <div class="swiper-button">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
                    <path fill-rule="evenodd" clip-rule="evenodd"
                          d="M2.5 24C2.5 12.1259 12.1259 2.5 24 2.5C35.8741 2.5 45.5 12.1259 45.5 24C45.5 35.8741 35.8741 45.5 24 45.5C12.1259 45.5 2.5 35.8741 2.5 24ZM22.5303 18.5303C22.8232 18.2374 22.8232 17.7626 22.5303 17.4697C22.2374 17.1768 21.7626 17.1768 21.4697 17.4697L15.4697 23.4696C15.329 23.6103 15.25 23.801 15.25 23.9999C15.25 24.1988 15.329 24.3896 15.4697 24.5303L21.4697 30.5303C21.7626 30.8232 22.2374 30.8232 22.5303 30.5303C22.8232 30.2374 22.8232 29.7625 22.5303 29.4696L17.8107 24.7499H32C32.4142 24.7499 32.75 24.4141 32.75 23.9999C32.75 23.5857 32.4142 23.2499 32 23.2499H17.8107L22.5303 18.5303Z"
                          fill="#40AB5E"/>
                  </svg>
                </div>
              </div>
              <div class="swiper-button-next">
                <div class="swiper-button">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
                    <path fill-rule="evenodd" clip-rule="evenodd"
                          d="M2.5 24C2.5 12.1259 12.1259 2.5 24 2.5C35.8741 2.5 45.5 12.1259 45.5 24C45.5 35.8741 35.8741 45.5 24 45.5C12.1259 45.5 2.5 35.8741 2.5 24ZM26.5303 17.4697C26.2374 17.1768 25.7626 17.1768 25.4697 17.4697C25.1768 17.7626 25.1768 18.2374 25.4697 18.5303L30.1893 23.25H16C15.5858 23.25 15.25 23.5858 15.25 24C15.25 24.4142 15.5858 24.75 16 24.75H30.1893L25.4697 29.4697C25.1768 29.7626 25.1768 30.2374 25.4697 30.5303C25.7626 30.8232 26.2374 30.8232 26.5303 30.5303L32.5303 24.5303C32.8232 24.2374 32.8232 23.7626 32.5303 23.4697L26.5303 17.4697Z"
                          fill="#40AB5E"/>
                  </svg>
                </div>
              </div>
            </div>
          </div>

          <div class="image-container" v-else>
            <img :src="strippedSrc(product.images[0].image)" loading="lazy" alt=""/>
          </div>

          <div class="images-navigation" v-if="product.images.length > 1">
            <div class="image-thumb"
                 :class="{'active': isActive(index)}"
                 v-for="(image, index) in product.images.slice(0, slice_count)"
                 :key="index"
                 @click="switchImage(index)"
            >
              <img :src="strippedSrc(image.image)" loading="lazy" alt="">
            </div>
          </div>

          <div class="characteristics tablet">

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
        <div class="right-side">
          <h1 class="title desktop">
            {{ product.name }}
          </h1>

          <div class="description-block">
            <div class="price-one">
              {{ product.prices[0].price }} ₽ / шт
            </div>
            <div class="description" v-html="product.description"></div>
            <div class="characteristics desktop">

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

import {Navigation} from 'swiper/modules';
import {Swiper, SwiperSlide} from 'swiper/vue';

import 'swiper/css';
import 'swiper/css/navigation';

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

      slice_count: 5,

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
  created() {
    this.updateWindowWidth()
  },
  mounted() {
    window.addEventListener('resize', this.updateWindowWidth);
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.updateWindowWidth);
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

    onSlideChange(swiper) {
      this.currentImageIndex = swiper.activeIndex
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

    updateWindowWidth() {
      if (window.innerWidth > 425) {
        this.slice_count = 5
      } else {
        this.slice_count = 4
      }
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
    return {
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

:deep(.description ul) {
  padding-inline-start: 1.125rem;
}

.characteristics {
  display: grid;
  grid-template-columns: 2fr 2fr;
  gap: 0.5rem 4rem;
}

.characteristics.tablet {
  display: none;
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

.image-slider {
  position: relative;
}

.swiper-controls {
  display: flex;
  justify-content: space-between;
  gap: 30px;
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  user-select: none;
}

.swiper-button-next,
.swiper-button-prev {
  height: 2.85rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

.swiper-button-prev {
  left: -0.85rem;
}

.swiper-button-next {
  right: -0.85rem;
}


.swiper-button {
  display: flex;
  align-items: center;
  justify-content: center;
}

.swiper-button svg {
  height: 2.85rem;
  width: 2.85rem;

  background: radial-gradient(circle, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 1) 45%, rgba(64, 171, 94, 1) 50%, rgba(64, 171, 94) 100%);
  border-radius: 50%;
}

.swiper-button-prev svg, .swiper-button-next svg {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Chrome, Safari, Opera */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Нестандартное свойство */
}

svg path {
  transition: fill 0.2s ease-in-out;
}

.swiper-button-next:after, .swiper-button-prev:after {
  content: none;
}

.swiper-button-next:after, .swiper-button-prev:after {
  font-family: none;
  font-size: none;
  text-transform: none !important;
  letter-spacing: 0;
  font-variant: initial;
  line-height: 1;
}

@media screen and (max-width: 1400px) {
  .product-content {
    gap: 5.4rem;
  }

  .image-container {
    width: 32.625rem;
    height: 24.375rem;
  }

  .image-container img {
    width: 32.625rem;
    height: 24.375rem;
  }

  :deep(.swiper-wrapper) {
    width: 32.625rem !important;
  }

  .slider-image-container {
    width: 32.625rem;
    height: 26.375rem;
  }

  .slider-image-container img {
    width: 32.625rem;
    height: 24.375rem;
    scale: 0.9;
  }
}

@media screen and (max-width: 1280px) {
  .product-component {
  }

  .product-max {
    padding: unset;
  }

  .product-content {
    padding: 0 2.25rem;
  }

  .left-side {
    flex: 1;
    width: 45%;
  }

  .image-container {
    width: unset;
    height: 20.875rem;
  }

  .image-container img {
    width: 100%;
    height: 20.875rem;
  }

  :deep(.swiper-wrapper) {
    width: unset !important;
  }

  .slider-image-container {
    width: unset;
    height: 22.875rem;
  }

  .slider-image-container img {
    width: unset;
    height: 22.875rem;
    scale: 0.9;
  }

  .swiper-button-prev {
    left: 1.2rem;
  }

  .swiper-button-next {
    right: 1.2rem;
  }

  .images-navigation {
    gap: 0.5rem;
  }

  .characteristics.tablet {
    display: grid;
    margin-top: 3rem;
  }

  .characteristics.desktop {
    display: none;
  }

  .title {
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }

  .description-block {
    gap: 1rem;
    margin-bottom: 2rem;
  }
}

@media screen and (max-width: 1000px) {
  .product-component {
  }

  .product-max {
  }

  .product-content {
    gap: 2rem;
    flex-direction: column;
  }

  .left-side {
    width: unset;
    gap: 0.5rem;
  }

  .image-container, .image-slider {
    max-width: 34.5rem;
  }

  .swiper-button svg {
    width: 2rem;
    height: 2rem;
  }

  .swiper-button-prev {
    height: 2.5rem;
    left: 0.65rem;
  }

  .swiper-button-next {
    height: 2.5rem;
    right: 0.65rem;
  }

  /*  .image-thumb {
      width: 4rem;
      height: 3.5rem;
    }

    .image-thumb img {
      width: 4rem;
      height: 3.5rem;
    }*/
  .right-side {

  }

  .title.tablet {
    display: block;
    margin-bottom: 1.5rem;
  }

  .title.desktop, .characteristics.tablet {
    display: none;
  }

  .characteristics.desktop {
    display: grid;
    margin-top: 1rem;
    grid-template-columns: 1fr 2fr;
    gap: 0.5rem 1rem;
  }

  .description-block {
    order: 2;
    margin-bottom: unset;
    margin-top: 3rem;
  }

  .purchase-block {
    order: 1;
    flex-direction: row;
    gap: 0.5rem;
  }

  .quantity-choice {
    flex: 1;
    -webkit-border-radius: 0.5rem;
    -moz-border-radius: 0.5rem;
    border-radius: 0.5rem;
    padding: unset;
  }

  .purchase-button {
    flex: 1;
    padding: unset;
  }

  .price {
    font-size: 1rem;
  }

  .button svg {
    width: 3rem;
    height: 3rem;
    padding: 0.5rem;
  }
}

@media screen and (max-width: 640px) {
  .product-component {
  }

  .product-max {

  }

  .product-content {
    padding: 0 1rem;
  }

  .title.tablet {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
  }

  .image-slider {
    max-width: unset;
  }

  .slider-image-container {
    height: 18.25rem;
    overflow: hidden;

  }

  .slider-image-container img {
    height: 18.25rem;
    scale: 0.85;
  }

  .image-container {
    max-width: unset;
    height: 16.25rem;
  }

  .image-container img {
    height: 16.25rem;
  }

  .image-thumb {
    width: 3.75rem;
    height: 3rem;
    padding: 0.25rem;
  }

  .image-thumb img {
    width: 3.75rem;
    height: 3rem;
  }

  .purchase-block {
    flex-direction: column;
  }

  .purchase-button {
    padding: 1rem 2rem;
  }

  .price {
    font-size: 0.75rem;
  }

  .description-block {
    margin-top: 2rem;
  }

  .characteristics.desktop {
    gap: 0.5rem 1rem;
    grid-template-columns: 2fr 2fr;
  }
}
</style>