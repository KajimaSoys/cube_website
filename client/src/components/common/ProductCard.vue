<template>
  <div class="product-card">
    <div class="product-images">
      <div class="image-container">
        <img :src="product.images[0].image" loading="lazy" alt="">
      </div>
    </div>
    <div class="product-content">
      <div class="base-info">
        <div class="title">
          {{ product.name }}
        </div>
        <div class="material" v-if="product.material">
          {{ product.material }}
        </div>
      </div>

      <div class="prices">
        <div class="price-one">
          {{ product.prices[0].price }} ₽
        </div>
        <div class="price-wholesale" v-if="product.prices[1]">
          {{ product.prices[0].price }} ₽ от {{ product.prices[1].count }} шт
        </div>
      </div>

      <div class="purchase-block">
        <div class="quantity-choice">
          <div class="minus-button button">
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
              150.00 ₽
            </div>
          </div>

          <div class="plus-button button">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
              <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M5.77606 3.15396C7.05953 2.5 8.73969 2.5 12.1 2.5L35.9 2.5C39.2603 2.5 40.9405 2.5 42.2239 3.15396C43.3529 3.7292 44.2708 4.64709 44.846 5.77606C45.5 7.05953 45.5 8.73969 45.5 12.1V35.9C45.5 39.2603 45.5 40.9405 44.846 42.2239C44.2708 43.3529 43.3529 44.2708 42.2239 44.846C40.9405 45.5 39.2603 45.5 35.9 45.5H12.1C8.73969 45.5 7.05953 45.5 5.77606 44.846C4.64708 44.2708 3.7292 43.3529 3.15396 42.2239C2.5 40.9405 2.5 39.2603 2.5 35.9L2.5 12.1C2.5 8.73968 2.5 7.05953 3.15396 5.77606C3.7292 4.64708 4.64709 3.7292 5.77606 3.15396ZM25 16C25 15.4477 24.5523 15 24 15C23.4477 15 23 15.4477 23 16V23H16C15.4477 23 15 23.4477 15 24C15 24.5523 15.4477 25 16 25H23V32C23 32.5523 23.4477 33 24 33C24.5523 33 25 32.5523 25 32V25H32C32.5523 25 33 24.5523 33 24C33 23.4477 32.5523 23 32 23H25V16Z"
                    fill="#40AB5E"/>
            </svg>
          </div>
        </div>
        <div class="purchase-button">
          В корзину
        </div>
      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: "ProductCard",
  inject: ['backendURL'],
  props: {
    product: {
      type: Object
    }
  },
  components: {},
  data() {
    return {
      count: 15,
    }
  },
  mounted() {
  },
  methods: {},
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
  height: 12.5rem;
  overflow: hidden;
}

/*.image-container {
  display: flex;
  align-items: center;
  height: 8.375rem;
}*/

.image-container img {
  width: 100%;
  object-fit: cover;
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
  transition: opacity 0.2s ease-in-out;
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


@media screen and (max-width: 1280px) {

}

@media screen and (max-width: 1000px) {

}

@media screen and (max-width: 640px) {

}
</style>