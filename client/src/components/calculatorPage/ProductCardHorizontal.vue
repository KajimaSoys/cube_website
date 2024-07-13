<template>
  <div class="product-card">
    <div class="card-left-side">
      <router-link
          class="image-container"
          :to="{ name: 'product', params: { categorySlug: product.category_info.slug, productId: product.id } }"
      >
        <img
            v-if="product.images.length > 0"
            :src="computedSrc(product)"
            loading="lazy"
            alt=""
        >
        <img
            v-else
            :src="frontendURL + '/images/no-image.png'"
            loading="lazy"
            alt=""
        >
      </router-link>

      <div class="base-info">
        <router-link
            class="title"
            :to="{ name: 'product', params: { categorySlug: product.category_info.slug, productId: product.id }}"
        >
          {{ product.name }}
        </router-link>
        <div class="quantity-choice" v-if="product.status === 'in_stock'">
          <div
              class="minus-button button"
              :class="{
                  'disabled': product.count===min_value,
                  'scaling-svg': product.isScalingMinus,
                  'out-of-stock-svg': product.status !== 'in_stock'
                }"
              @click="handleClick(product, 'decreaseOnce')"
              @mousedown="startDecreasing(product)"
              @mouseup="stopAutoChange(product)"
              @mouseleave="stopAutoChange(product)"
              @touchstart.prevent="handleTouchStart(product, 'startDecreasing')"
              @touchend="handleTouchEnd(product, 'decreaseOnce')"
              @touchcancel="handleTouchCancel(product)"
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
              {{ product.count }} шт
            </div>
          </div>

          <div class="plus-button button"
               :class="{
                    'disabled': product.count===max_value,
                    'scaling-svg': product.isScalingPlus,
                    'out-of-stock-svg': product.status !== 'in_stock'
                 }"
               @click="handleClick(product, 'increaseOnce')"
               @mousedown="startIncreasing(product)"
               @mouseup="stopAutoChange(product)"
               @mouseleave="stopAutoChange(product)"
               @touchstart.prevent="handleTouchStart(product, 'startIncreasing')"
               @touchend="handleTouchEnd(product, 'increaseOnce')"
               @touchcancel="handleTouchCancel(product)"
               title="Удерживайте, чтобы быстрее увеличить кол-во товара"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
              <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M5.77606 3.15396C7.05953 2.5 8.73969 2.5 12.1 2.5L35.9 2.5C39.2603 2.5 40.9405 2.5 42.2239 3.15396C43.3529 3.7292 44.2708 4.64709 44.846 5.77606C45.5 7.05953 45.5 8.73969 45.5 12.1V35.9C45.5 39.2603 45.5 40.9405 44.846 42.2239C44.2708 43.3529 43.3529 44.2708 42.2239 44.846C40.9405 45.5 39.2603 45.5 35.9 45.5H12.1C8.73969 45.5 7.05953 45.5 5.77606 44.846C4.64708 44.2708 3.7292 43.3529 3.15396 42.2239C2.5 40.9405 2.5 39.2603 2.5 35.9L2.5 12.1C2.5 8.73968 2.5 7.05953 3.15396 5.77606C3.7292 4.64708 4.64709 3.7292 5.77606 3.15396ZM25 16C25 15.4477 24.5523 15 24 15C23.4477 15 23 15.4477 23 16V23H16C15.4477 23 15 23.4477 15 24C15 24.5523 15.4477 25 16 25H23V32C23 32.5523 23.4477 33 24 33C24.5523 33 25 32.5523 25 32V25H32C32.5523 25 33 24.5523 33 24C33 23.4477 32.5523 23 32 23H25V16Z"
                    fill="#40AB5E"/>
            </svg>
          </div>
        </div>
        <div class="current-price small-text-1" v-if="product.status === 'in_stock'">
          {{ currentPriceOne(product) }} ₽ / шт
        </div>
      </div>

    </div>
    <div class="card-right-side">
      <div class="product-price" v-if="product.status === 'in_stock'">
        {{ product.finalPrice.toFixed(2) }} ₽
      </div>
      <div class="product-price" v-else>
        Нет в наличии
      </div>
      <div v-if="removable" class="delete-button" @click="deleteProduct(product.id)">
        Удалить
      </div>
      <div v-else class="dummy"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductCardHorizontal",
  inject: ['backendURL', 'frontendURL'],
  props: {
    product: {
      type: Object
    },
    quantity: {
      type: Number,
      default: 1
    },
    removable: {
      type: Boolean,
      default: false
    }
  },
  emits: [
    'remove-from-add-list'
  ],
  components: {},
  data() {
    return {
      max_value: 9999,
      min_value: 1,

      interval: null,
      increaseAmount: 1,
    }
  },
  computed: {

  },
  mounted() {
  },
  methods: {
    computedSrc(product) {
      return this.backendURL + '/media' + product.images[0].image.split('/media')[1]
    },

    currentPriceOne(product) {
      let finalPrice = product.prices.find(price => price.count === 1).price;

      product.prices.forEach(priceInfo => {
        if (product.count >= priceInfo.count) {
          finalPrice = priceInfo.price;
        }
      });

      return finalPrice;
    },

    calculatePrice(product) {
      const basePrice = product.prices.find(price => price.count === 1).price;
      let finalPrice = basePrice * product.count;

      product.prices.forEach(priceInfo => {
        if (product.count >= priceInfo.count) {
          finalPrice = priceInfo.price * product.count;
        }
      });

      product.finalPrice = finalPrice
      // this.updateCart(product)
    },

    handleClick(product, action) {
      if (!this.touchEventTriggered) {
        this[action](product);
      }
    },
    handleTouchStart(product, action) {
      this.touchEventTriggered = true;
      this[action](product);
      setTimeout(() => {
        this.touchEventTriggered = false;
      }, 500);
    },
    handleTouchEnd(product, action) {
      this[action](product);
      this.stopAutoChange(product);
    },
    handleTouchCancel(product) {
      this.stopAutoChange(product);
    },

    increaseOnce(product) {
      product.count++;
      if (product.count > this.max_value) {
        product.count = this.max_value
      }
      this.calculatePrice(product)
    },
    decreaseOnce(product) {
      product.count--;
      if (product.count < this.min_value) {
        product.count = this.min_value
      }
      this.calculatePrice(product)
    },
    startIncreasing(product) {
      if (this.interval) return;
      this.interval = setInterval(() => {
        if (product.count < this.max_value) {
          product.count += this.increaseAmount;
          if (product.count > this.max_value) {
            product.count = this.max_value;
          }
          this.increaseAmount++;
          this.calculatePrice(product);
        }
      }, 200);
      product.isScalingPlus = true;
    },
    startDecreasing(product) {
      if (this.interval) return;
      this.interval = setInterval(() => {
        if (product.count > this.min_value) {
          product.count -= this.increaseAmount;
          if (product.count < this.min_value) {
            product.count = this.min_value;
          }
          this.increaseAmount++;
          this.calculatePrice(product);
        }
      }, 200);
      product.isScalingMinus = true;
    },
    stopAutoChange(product) {
      clearInterval(this.interval);
      product.isScalingPlus = false;
      product.isScalingMinus = false;
      this.interval = null;
      this.increaseAmount = 1;
    },

    // Todo убедиться в необходимости этого метода
   /* updateCart(product) {
      this.$emit('update-cart', product.id, product.count);
    },*/
    deleteProduct(productId) {
      this.$emit('remove-from-add-list', productId);
    },
  },
  watch: {
    quantity: {
      handler(newQuantity) {
        if (this.product) {
          this.product.count = newQuantity;
        }
      },
      immediate: true
    }
  }
}
</script>


<style scoped>

.product-card {
  display: flex;
  padding: 1.5rem;
  justify-content: space-between;
  gap: 1rem;

  border-radius: 1rem;
  background-color: var(--background);
  width: 60%;
}

.card-left-side {
  display: flex;
  flex-direction: row;
  gap: 2rem;
}

.image-container {
  width: 8.125rem;
  height: 7.125rem;
  border-radius: 0.5rem;
  background: #F5F2F1;
  display: flex;
  align-items: center;
  transition: opacity 0.2s ease-in-out;
}

.image-container:hover {
  opacity: 0.5;
}

.image-container img {
  object-fit: contain;
  width: 8.125rem;
  height: 7.125rem;
}

.base-info {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.title {
  text-decoration: none;
  transition: opacity 0.2s ease-in-out;
  color: var(--black)
}

.title:hover {
  opacity: 0.5;
}

.quantity-choice {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  align-items: center;
}

.minus-button, .plus-button {
  display: flex;
  align-items: center;
  width: 2.25rem;
  height: 2.25rem;
  transition: all 0.2s ease-in-out;
  user-select: none;
  cursor: pointer;
}

.minus-button:hover, .plus-button:hover {
  opacity: 0.5;
}

.disabled {
  opacity: 0.5;
  pointer-events: none;
}

.scaling-svg {
  transform: scale(1.2);
}

.price-container {
  min-width: 4.5rem;
  text-align: center;
}

.card-right-side {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-end;
}

.product-price {
  font-size: 1.25rem;
  font-style: normal;
  font-weight: 400;
  line-height: 130%;
  text-align: end;
}

.delete-button {
  border-radius: 0.375rem;
  border: 1px solid var(--green-light, #40AB5E);

  color: var(--green-light);
  display: flex;
  padding: 0.5rem 1rem;
  align-items: flex-start;
  gap: 0.625rem;
  width: 4.375rem;
  justify-content: center;

  cursor: pointer;
  user-select: none;

  transition: all 0.2s ease-in-out;
}

.delete-button:hover {
  color: white;
  background-color: var(--green-light);
}

.out-of-stock {
  pointer-events: none;
  background-color: var(--black-35) !important;
}

.out-of-stock-svg {
  pointer-events: none;
}

.out-of-stock-svg svg path {
  fill: var(--black-35);
}

.current-price {
  color: var(--black-35)
}

@media screen and (max-width: 1280px) {
  .product-card {
    width: -webkit-fill-available;
    width: -moz-fill-available;
  }
}

@media screen and (max-width: 1000px) {
  .product-card {
    padding: 1rem;
    border-radius: 0.75rem;
  }

  .image-container {
    width: 7.1875rem;
    height: 6.25rem;
  }

  .image-container img {
    width: 7.1875rem;
    height: 6.25rem;
  }

  .product-price {
    font-size: 1rem;
  }

  .delete-button {
    width: 3rem;
    font-size: 0.75rem;
  }

  .card-left-side {
    gap: 1.5rem;
  }
}

@media screen and (max-width: 640px) {
  .card-left-side {
    flex-direction: column;
    gap: 1rem;
  }

  .image-container {
    width: 3.875rem;
    height: 3.375rem;
  }

  .image-container img {
    width: 3.875rem;
    height: 3.375rem;
  }

  .card-right-side {
    justify-content: flex-end;
    gap: 2.1rem;
  }

  .base-info {
    gap: 0.5rem;
  }

  .price-container {
    min-width: 3.5rem;
  }

  .product-price {
    font-size: 0.875rem;
  }
}
</style>