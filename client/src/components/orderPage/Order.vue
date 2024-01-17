<template>
  <div class="order-component">
    <div class="order-max">
      <router-link class="breadcrumb-native" :to="{name: 'catalog'}">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path d="M9.33301 4L5.33301 8L9.33301 12" stroke="#737373" stroke-width="1.5" stroke-linecap="round"
                stroke-linejoin="round"/>
        </svg>
        <span>Вернуться к товарам</span>
      </router-link>

      <h1><span>Оформление</span> заказа</h1>

      <div class="order-content" v-if="!successfulSend && !errorSend && products.length > 0">
        <div class="products-block">
          <h2>Выбранные товары</h2>
          <div class="product-list">
            <div
                class="product-card"
                v-for="product in products"
                :key="product.id"
            >
              <div class="card-left-side">
                <router-link
                    class="image-container"
                    :to="{ name: 'product', params: { categorySlug: product.category_info.slug, productId: product.id } }"
                >
                  <img
                      :src="computedSrc(product)"
                      loading="lazy"
                      alt="">
                </router-link>

                <div class="base-info">
                  <router-link
                      class="title"
                      :to="{ name: 'product', params: { categorySlug: product.category_info.slug, productId: product.id }}"
                  >
                    {{ product.name }}
                  </router-link>
                  <div class="quantity-choice" v-if="product.in_stock">
                    <div
                        class="minus-button button"
                        :class="{
                            'disabled': product.count===min_value,
                            'scaling-svg': product.isScalingMinus,
                            'out-of-stock-svg': !product.in_stock
                          }"
                        @click="decreaseOnce(product)"
                        @mousedown="startDecreasing(product)"
                        @mouseup="stopDecreasing(product)"
                        @mouseleave="stopDecreasing(product)"
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
                      <!--                        <div class="price">-->
                      <!--                          {{ calculatedPrice }} ₽-->
                      <!--                        </div>-->
                    </div>

                    <div class="plus-button button"
                         :class="{
                              'disabled': product.count===max_value,
                              'scaling-svg': product.isScalingPlus,
                              'out-of-stock-svg': !product.in_stock
                           }"
                         @click="increaseOnce(product)"
                         @mousedown="startIncreasing(product)"
                         @mouseup="stopIncreasing(product)"
                         @mouseleave="stopIncreasing(product)"
                         title="Удерживайте, чтобы быстрее увеличить кол-во товара"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
                        <path fill-rule="evenodd" clip-rule="evenodd"
                              d="M5.77606 3.15396C7.05953 2.5 8.73969 2.5 12.1 2.5L35.9 2.5C39.2603 2.5 40.9405 2.5 42.2239 3.15396C43.3529 3.7292 44.2708 4.64709 44.846 5.77606C45.5 7.05953 45.5 8.73969 45.5 12.1V35.9C45.5 39.2603 45.5 40.9405 44.846 42.2239C44.2708 43.3529 43.3529 44.2708 42.2239 44.846C40.9405 45.5 39.2603 45.5 35.9 45.5H12.1C8.73969 45.5 7.05953 45.5 5.77606 44.846C4.64708 44.2708 3.7292 43.3529 3.15396 42.2239C2.5 40.9405 2.5 39.2603 2.5 35.9L2.5 12.1C2.5 8.73968 2.5 7.05953 3.15396 5.77606C3.7292 4.64708 4.64709 3.7292 5.77606 3.15396ZM25 16C25 15.4477 24.5523 15 24 15C23.4477 15 23 15.4477 23 16V23H16C15.4477 23 15 23.4477 15 24C15 24.5523 15.4477 25 16 25H23V32C23 32.5523 23.4477 33 24 33C24.5523 33 25 32.5523 25 32V25H32C32.5523 25 33 24.5523 33 24C33 23.4477 32.5523 23 32 23H25V16Z"
                              fill="#40AB5E"/>
                      </svg>
                    </div>
                  </div>
                  <div class="current-price small-text-1" v-if="product.in_stock">
                    {{ currentPriceOne(product) }} ₽ / шт
                  </div>
                </div>

              </div>
              <div class="card-right-side">
                <div class="product-price" v-if="product.in_stock">
                  {{ product.finalPrice.toFixed(2) }} ₽
                </div>
                <div class="product-price" v-else>
                  Нет в наличии
                </div>
                <div class="delete-button" @click="deleteProduct(product.id)">
                  Удалить
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="form-block" id="form-block">
          <h2>Укажите ваши контактные данные</h2>
          <form @submit.prevent="onSubmit" ref="sendForm" class="request-form">
            <div class="form-field-wrapper">
              <input
                  type="text"
                  v-model="name"
                  class="form_input"
                  :class="{'error-border': !name && isSubmitted}"
                  maxlength="256"
                  name="request-name"
                  @input="validateName"
                  placeholder="Ваше имя"
                  id="request-name"/>
            </div>

            <div class="form-field-wrapper">
              <input
                  type="text"
                  v-model="phone"
                  class="form_input"
                  :class="{'error-border': phoneError && isSubmitted}"
                  @input="validatePhone"
                  name="request-phone"
                  placeholder="+7 (___) ___-__-__"
                  v-mask="'+7 (###) ###-##-##'"
              >
            </div>
          </form>
          <div
              class="submit-button button tablet"
              :class="{'out-of-stock': calculatedTotalPrice === 0 }"
              @click="checkForm"
          >
            {{ sendButton }}
          </div>
          <div class="privacy-info small-text-2">
            Нажимая кнопку «Оформить заказ» вы даете согласие на обработку персональных данных и принимаете условия
            <router-link :to="{name: 'policy'}" class="privacy-link">политики конфиденциальности</router-link>
          </div>
        </div>
        <div class="order-block">
          <h2>Ваш заказ</h2>
          <div class="order-info">
            <div class="product-count">
              {{ getProductSummary() }}
            </div>
            <div class="total-price">
              {{ calculatedTotalPrice.toFixed(2) }} ₽
            </div>
            <div class="manager-info">
              Наш менеджер вам перезвонит и уточнит детали по вашему заказу
            </div>
          </div>

          <div
              class="submit-button button desktop"
              :class="{'out-of-stock': calculatedTotalPrice === 0 }"
              @click="checkForm"
          >
            {{ sendButton }}
          </div>
        </div>
      </div>
      <div class="order-content" v-if="!successfulSend && !errorSend && products.length === 0">
        <div class="response empty-cart">
          <h2>Ваша корзина пока пуста!</h2>
          <span>
            Перейдите в наш каталог, чтобы открыть для себя множество качественных картонных коробок и упаковок, способных удовлетворить любые ваши потребности.
          </span>
          <router-link :to="{ name: 'catalog' }" class="catalog-button">
            Перейти в каталог
          </router-link>
        </div>
      </div>
      <div class="order-content" v-if="successfulSend">
        <div class="response">
          <h2>Заказ №{{ orderId }} успешно создан</h2>
          <span>Наш менеджер вам перезвонит и уточнит детали по вашему заказу.</span>
        </div>
      </div>
      <div class="order-content" v-if="errorSend">
        <div class="response">
          <h2>Произошла ошибка</h2>
          <span>
            К сожалению, при отправке заявки произошла ошибка. Попробуйте еще раз позже или
            <a href="https://wa.me/79950071654" target="_blank">свяжитесь с нами</a>
            напрямую.
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mask} from "vue-the-mask";
import axios from "axios";
import crypto from 'crypto-js';

export default {
  name: "Order",
  components: {},
  inject: ['backendURL', 'hmac_key'],
  directives: {mask},
  props: {
    products: Array,
  },
  emits: [
    'update-cart',
    'remove-from-cart',
    'clear-cart',
    'scroll-to-zero'
  ],
  data() {
    return {
      max_value: 9999,
      min_value: 1,

      interval: null,
      increaseAmount: 1,

      name: '',
      phone: '',
      phoneError: false,
      isSubmitted: false,

      sendButton: 'Оформить заказ',
      sending: false,

      successfulSend: false,
      errorSend: false,
      orderId: '',
    }
  },
  created() {

  },
  mounted() {
  },
  watch: {},
  computed: {
    calculatedTotalPrice() {
      let totalPrice = 0
      const inStockProducts = this.products.filter(product => product.in_stock === true);

      return inStockProducts.reduce(
          (accumulator, currentValue) => {
            return accumulator + currentValue.finalPrice
          },
          totalPrice,
      );
    }
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
      this.updateCart(product)
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
        product.count += this.increaseAmount;
        if (product.count > this.max_value) {
          product.count = this.max_value
          this.increaseAmount = 1
        }
        this.calculatePrice(product)
        product.isScalingPlus = true;
        this.increaseAmount++;
      }, 200);
    },
    stopIncreasing(product) {
      clearInterval(this.interval);
      product.isScalingPlus = false;

      this.interval = null;
      this.increaseAmount = 1;
    },
    startDecreasing(product) {
      if (this.interval) return;

      this.interval = setInterval(() => {
        product.count -= this.increaseAmount;
        if (product.count < this.min_value) {
          product.count = this.min_value
          this.increaseAmount = 1
        }
        this.calculatePrice(product)
        product.isScalingMinus = true;
        this.increaseAmount++;
      }, 200);
    },
    stopDecreasing(product) {
      clearInterval(this.interval);
      product.isScalingMinus = false;

      this.interval = null;
      this.increaseAmount = 1;
    },

    updateCart(product) {
      this.$emit('update-cart', product.id, product.count);
    },
    deleteProduct(productId) {
      this.$emit('remove-from-cart', productId);
    },

    getProductSummary() {
      const inStockProducts = this.products.filter(product => product.in_stock === true);
      const totalQuantity = inStockProducts.length

      const wordForm = this.getWordForm(totalQuantity);
      return `${totalQuantity} ${wordForm} на сумму`;
    },
    getWordForm(number) {
      const cases = [2, 0, 1, 1, 1, 2];
      return ['товар', 'товара', 'товаров'][(number % 100 > 4 && number % 100 < 20) ? 2 : cases[(number % 10 < 5) ? number % 10 : 5]];
    },

    validateName(event) {
      this.name = event.target.value.replace(/[^а-яА-ЯёЁ]/g, '');
    },

    validatePhone() {
      this.phoneError = this.phone.length !== 18;
    },

    scrollToElement(elementId) {
      const requestElement = document.getElementById(elementId);
      const offset = 200;
      const elementPosition = requestElement.getBoundingClientRect().top + window.pageYOffset;
      const offsetPosition = elementPosition - offset;
      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth"
      });
    },

    checkForm() {
      this.isSubmitted = true;
      this.phoneError = this.phone.length !== 18;

      if (this.name && this.phone && !this.phoneError) {
        this.sending = true
        this.sendRequest()
      } else {
        console.log('Form error!');
        if (window.innerWidth > 1280) {
          this.scrollToElement('form-block')
        }
      }
    },

    async sendRequest() {
      this.sendButton = 'Пожалуйста, подождите..'
      this.sending = true

      let body = {
        request: {
          name: this.name,
          phone_number: this.phone,
          total: this.calculatedTotalPrice,
          products: this.products
              .filter(product => product.in_stock === true)
              .map(product => ({
                product_id: product.id,
                count: product.count,
                price: product.finalPrice
              })),
        }
      }
      const payloadString = JSON.stringify(body);
      const signature = crypto.HmacSHA256(payloadString, this.hmac_key).toString();
      await axios
          .post('api/v1/create_order/', body, {
            headers: {
              'X-Signature': signature
            }
          })
          .then(response => {
            this.sending = false
            // window.ym(95108306, 'reachGoal', 'request_calculate_success')
            this.$emit('clear-cart');

            this.successfulSend = true
            this.orderId = response.data.order_number
            this.$emit('scroll-to-zero');
          })
          .catch(error => {
            console.log('An error occurred: ', error);
            // window.ym(95108306, 'reachGoal', 'request_calculate_error')

            this.errorSend = true
            this.$emit('scroll-to-zero');
          })
    }
  },
}
</script>


<style scoped>
.order-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 12rem;

  display: flex;
  justify-content: center;
  align-items: center;
}

.order-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
}

.breadcrumb-native {
  display: flex;
  flex-direction: row;
  gap: 0.25rem;
  align-items: center;
  text-decoration: none;
  transition: opacity 0.2s ease-in-out;
}

.breadcrumb-native:hover {
  opacity: 0.5;
}

.breadcrumb-native span {
  font-size: 1rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  color: var(--black-55);
}

h1 {
  margin-top: 2rem;
}

h1 span {
  color: var(--green-primary);
}

h2 {
  font-size: 2rem;
}

.order-content {
  margin-top: 2rem;
  display: grid;
  gap: 4rem 7.5rem;
  grid-template-columns: 2fr 1fr;
  justify-content: space-between;
}

.products-block {
  grid-area: 1 / 1 / 1 / 1;
}

.product-list {
  margin-top: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.product-card {
  display: flex;
  padding: 1.5rem;
  justify-content: space-between;
  gap: 1rem;

  border-radius: 1rem;
  background: #FFF;
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

.form-block {
  grid-area: 2 / 1 / 2 / 1;
}

.request-form {
  display: -ms-grid;
  display: grid;
  grid-auto-columns: 1fr;
  grid-column-gap: 1rem;
  grid-row-gap: 1rem;
  -ms-grid-columns: 1fr;
  grid-template-columns: 1fr;
  -ms-grid-rows: auto auto;
  grid-template-rows: auto auto;
  margin-top: 2rem;
  width: 60%;
}

.form-field-wrapper {
  position: relative;
}

.form_input {
  width: 100%;
  height: auto;
  min-height: 1.25rem;
  box-sizing: border-box;
  padding: 0.75rem 1rem;

  border-style: solid;
  border-width: 1px;
  border-color: #d0d5dd;
  border-radius: 0.5rem;
  background-color: #fff;

  -webkit-transition: all 200ms ease;
  transition: all 200ms ease;

  color: var(--black);
  font-size: 1rem;
  line-height: 1.5;
}

.form_input:focus {
  border-color: var(--green-light);
  box-shadow: 0 1px 2px 0 rgba(16, 24, 40, 0.05), 0 0 0 4px #60c93461;
  color: var(--black);
}

.form_input::-webkit-input-placeholder {
  color: var(--black-20);
}

.form_input:-ms-input-placeholder {
  color: var(--black-20);
}

.form_input::-ms-input-placeholder {
  color: var(--black-20);
}

.form_input::placeholder {
  color: var(--black-20);
}

.form_input:focus-visible {
  outline: none;
}

.error-border {
  border-color: #ff5c7e !important;
  box-shadow: 0 1px 2px 0 rgba(16, 24, 40, 0.05), 0 0 0 4px #fdbecb !important;
}

.error-border:focus {
  border-color: #ff5c7e;
  box-shadow: 0 1px 2px 0 rgba(16, 24, 40, 0.05), 0 0 0 4px #fdbecb;
}

.privacy-info {
  margin-top: 1rem;
  color: var(--black-35);
  width: 85%;
}

.privacy-link {
  text-decoration: none;
  color: var(--black-55);
  transition: color 0.2s ease-in-out;
}

.privacy-link:hover {
  color: var(--black)
}

.order-block {
  grid-area: 1 / 2 / 1 / 2;
}

.order-info {
  margin-top: 2rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.product-count {
  color: var(--black-55, #737373);
}

.total-price {
  font-family: 'Geologica', sans-serif;
  font-size: 2rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
  margin-bottom: 0.5rem;
}

.manager-info {
  width: 95%;
}

.submit-button {
  margin-top: 4rem;
  display: flex;
  width: 14.3125rem;
  height: 2.375rem;
  padding: 1rem 2rem;
  justify-content: center;
  align-items: center;

  border-radius: 0.5rem;
  background: var(--green-light, #40AB5E);
  color: white;
  cursor: pointer;
  user-select: none;

  transition: opacity 0.2s ease-in-out;
}

.submit-button:hover {
  opacity: 0.5;
}

.submit-button.tablet {
  display: none;
}

.response {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin-top: 2rem;
}

.response:not(.empty-cart) span {
  margin-bottom: 10rem;
}

.response a {
  text-decoration: none;
  color: var(--green-primary);
  transition: opacity 0.2s ease-in-out;
}

.response a:hover {
  opacity: 0.5;
}

.catalog-button {
  display: flex;
  align-items: center;
  justify-content: center;

  /*  margin-top: 3rem;*/
  padding: 1.5rem 2rem;
  width: 50%;

  color: white !important;
  border-radius: 0.5rem;
  background: var(--green-light, #40AB5E);
  text-decoration: none;
}


@media screen and (max-width: 1280px) {
  .order-component {
    padding-top: 10rem;
  }

  .order-max {
    padding: 0 2.25rem;
  }

  .order-content {
    grid-template-columns: 3fr 2fr;
  }

  .products-block {
    grid-area: 1 / 1 / 1 / 3;
  }

  .form-block {
    grid-area: 2 / 1 / 3 / 2;
  }

  .order-block {
    grid-area: 2 / 2 / 3 / 3;
  }

  .product-list {
    gap: 0.5rem;
  }

  .form-block h2, .order-block h2, .total-price {
    font-size: 1.5rem;
  }

  .request-form {
    margin-top: 1.5rem;
    width: 24.75rem;
  }

  .order-info {
    margin-top: 1.5rem;
  }

  .submit-button {
    width: unset;
    margin-top: 2rem;
  }
}

@media screen and (max-width: 1000px) {
  .order-component {
    padding-top: 8.75rem;
  }

  .order-max {
    padding: 0 2.25rem;
  }

  h2 {
    font-size: 1.5rem;
  }

  .submit-button.desktop {
    display: none;
  }

  .submit-button.tablet {
    display: flex;
    margin-top: 1rem;
    padding: 1rem 2rem;
    width: 20.75rem;
    height: 1.25rem;
  }

  .order-content {
    grid-template-columns: 1fr;
    gap: 3rem;
  }

  .products-block {
    grid-area: 1 / 1 / 1 / 2;
  }

  .order-block {
    grid-area: 2 / 1 / 2 / 2;
  }

  .form-block {
    grid-area: 3 / 1 / 3 / 2;
  }

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

  .manager-info {
    width: 50%;
  }

  .privacy-info {
    width: 24.75rem;
  }

  .breadcrumb-native span {
    font-size: 0.75rem;
  }

  .response {
    margin-top: unset;
    gap: 1rem;
  }

  .response:not(.empty-cart) span {
    margin-bottom: 7rem;
  }

  .catalog-button {
    margin-top: 1rem;
    margin-bottom: 3rem;
    padding: 1rem 2rem;
    width: 20.75rem;
    height: 1.25rem;
  }
}

@media screen and (max-width: 640px) {
  .order-component {
    padding-top: 7.5rem;
  }

  .order-max {
    padding: 0 1rem;
  }

  h2 {
    font-size: 1.25rem !important;
  }

  .order-content {
    gap: 2rem;
  }

  .product-list {
    margin-top: 1rem;
  }

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

  .order-info {
    margin-top: 1rem;
  }

  .total-price {
    font-size: 1.25rem;
  }

  .manager-info {
    width: 80%;
  }

  .request-form, .privacy-info {
    width: 100%;
  }

  .submit-button.tablet {
    width: -webkit-fill-available;
  }

  .form-block h2 {
    width: 70%;
  }

  .catalog-button {
    margin-top: 1rem;
    margin-bottom: 3rem;
    width: -webkit-fill-available;
  }
}
</style>