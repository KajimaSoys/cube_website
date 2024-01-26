<template>
  <div class="product-card">
    <div class="product-images">
      <router-link
          class="image-container"
          :to="{ name: 'product', params: { categorySlug: product.category_info.slug, productId: product.id } }"
          @mouseenter="hover = true"
          @mouseleave="hover = false">
        <img
            v-if="product.images.length > 0"
            :src="computedSrc"
            loading="lazy"
            alt="">
      </router-link>
    </div>
    <div class="product-content">
      <div class="base-info">
        <router-link
            class="title"
            :to="{ name: 'product', params: { categorySlug: product.category_info.slug, productId: product.id }}"
        >
          {{ product.name }}
        </router-link>
        <!--        <div class="material" v-if="product.material">-->
        <!--          {{ product.material }}-->
        <!--        </div>-->
      </div>

      <div class="prices">
        <div class="price-one">
          {{ product.prices[0].price }} ₽
        </div>
        <div class="price-wholesale" v-if="product.prices[1]">
          {{ product.prices[1].price }} ₽ от {{ product.prices[1].count }} шт
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
              @click="handleClick('decreaseOnce')"
              @mousedown="startDecreasing"
              @mouseup="stopAutoChange"
              @mouseleave="stopAutoChange"
              @touchstart.prevent="handleTouchStart('startDecreasing')"
              @touchend="handleTouchEnd('decreaseOnce')"
              @touchcancel="handleTouchCancel"
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
               @click="handleClick('increaseOnce')"
               @mousedown="startIncreasing"
               @mouseup="stopAutoChange"
               @mouseleave="stopAutoChange"
               @touchstart.prevent="handleTouchStart('startIncreasing')"
               @touchend="handleTouchEnd('increaseOnce')"
               @touchcancel="handleTouchCancel"
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

  <cart-popup
      :is-visible="showCartPopup"
      @close="showCartPopup = false"
      :product="product"
  />
</template>

<script>
import CartPopup from "./CartPopup.vue";
import {ElNotification} from 'element-plus'

export default {
  name: "ProductCard",
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
    CartPopup
  },
  data() {
    return {
      hover: false,

      count: 1,
      min_value: 1,
      max_value: 9999,

      touchEventTriggered: false,
      interval: null,
      increaseAmount: 1,

      isScalingPlus: false,
      isScalingMinus: false,

      showCartPopup: false,
    }
  },
  // watch: {
  //   product: {
  //     handler(newProduct) {
  //       newProduct.count = 15
  //       // this.$set(newProduct, 'count', 15); // Добавляем count к продукту
  //     },
  //     deep: true // Включаем глубокое наблюдение
  //   }
  // },
  mounted() {
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
    computedSrc() {
      let src = this.hover && this.product.images[1] ? this.product.images[1].image : this.product.images[0].image
      return this.backendURL + '/media' + src.split('/media')[1]
    }
  },
  methods: {
    handleClick(action) {
      if (!this.touchEventTriggered) {
        this[action]();
      }
    },
    handleTouchStart(action) {
      this.touchEventTriggered = true;
      this[action]();
      setTimeout(() => {
        this.touchEventTriggered = false;
      }, 500);
    },
    handleTouchEnd(action) {
      this[action]();
      this.stopAutoChange();
    },
    handleTouchCancel() {
      this.stopAutoChange();
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
      this.stopAutoChange();
      this.increaseAmount = 1;
      this.isScalingPlus = true;
      this.interval = setInterval(() => {
        if (this.count < this.max_value) {
          this.count += this.increaseAmount;
          if (this.count > this.max_value) {
            this.count = this.max_value;
          }
          this.increaseAmount++;
        } else {
          this.stopAutoChange();
        }
      }, 200);
    },
    startDecreasing() {
      if (this.interval) return;
      this.stopAutoChange();
      this.increaseAmount = 1;
      this.isScalingMinus = true;
      this.interval = setInterval(() => {
        if (this.count > this.min_value) {
          this.count -= this.increaseAmount;
          if (this.count < this.min_value) {
            this.count = this.min_value;
          }
          this.increaseAmount++;
        } else {
          this.stopAutoChange();
        }
      }, 200);
    },
    stopAutoChange() {
      clearInterval(this.interval);
      this.isScalingPlus = false;
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
    }

  },
}
</script>


<style scoped>
.product-card {
  display: flex;
  padding: 2rem 1rem 1rem 1rem;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  flex: 1 0 0;

  border-radius: 1rem;
  background: #FFF;
}

.product-images {
  display: flex;
  align-items: flex-start;
  height: 9.375rem;
  overflow: hidden;
}

/*.image-container {
  display: flex;
  align-items: center;
  height: 8.375rem;
}*/

.image-container img {
  width: 100%;
  object-fit: contain;
  height: 9.375rem;
}

.product-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  width: 100%;
  flex: 1;
}

.base-info {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  align-items: center;
  flex: 1;
}

.title {
  text-align: center;
  width: 90%;
  text-decoration: none;
  color: var(--black);
  font-size: 1.25rem;
  transition: opacity 0.2s ease-in-out;
}

.title:hover {
  opacity: 0.5;
}

.material {
  text-align: center;
  color: var(--black-55, #737373);
  font-size: 0.875rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
}

.prices {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  align-items: center;
}

.price-one {
  font-size: 1.125rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}

.price-wholesale {
  color: var(--black-55);
  font-size: 0.875rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
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
}

.button {
  display: flex;
  align-items: center;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease-in-out;
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
  font-size: 0.875rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
}


.purchase-button {
  display: flex;
  padding: 1rem 1.5rem;
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
  .product-images {
    height: 7.5rem;
  }

  .image-container img {
    height: 7.5rem;
  }
}

@media screen and (max-width: 1000px) {
  .product-images {
    height: 5rem;
  }

  .image-container img {
    height: 5rem;
  }

  .title, .price-one, .quantity {
    font-size: 1rem;
  }

  .material, .price-wholesale, .price {
    font-size: 0.75rem;
  }

  .button svg {
    height: 2rem;
    width: 2rem;
  }

  .purchase-button {
    padding: 1rem 0.5rem;
  }
}

@media screen and (max-width: 640px) {
  .product-card {
    padding: 1.5rem 0.5rem 0.5rem 0.5rem;
  }

  .product-content {
    gap: 1rem;
  }

  .quantity {
    font-size: 0.875rem;
  }

  .purchase-button {
    padding: 0.75rem 0.5rem;
  }
}
</style>