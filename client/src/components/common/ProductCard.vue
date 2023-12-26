<template>
  <div class="product-card">
    <div class="product-images">

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
          <div class="minus-button button"></div>
          <div class="quantity">
            {{ count }} шт
          </div>
          <div class="price">
            150.00 ₽
          </div>
          <div class="plus-button button"></div>
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

@media screen and (max-width: 1280px) {

}

@media screen and (max-width: 1000px) {

}

@media screen and (max-width: 640px) {

}
</style>