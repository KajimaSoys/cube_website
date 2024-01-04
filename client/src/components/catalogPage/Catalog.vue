<template>
  <div class="catalog-component">
    <div class="catalog-max">
      <h1>Каталог</h1>
      <div class="catalog-content">
        <div class="category-grid top">
          <router-link class="category-item"
                       v-for="category in category_list"
                       :key="category.id"
                       :to="getRoute(category)"
                       :class="{'active': isActive(category.slug)}"
          >
            {{ category.name }}
          </router-link>
        </div>

        <div class="products-grid">
          <ProductCard
              v-for="product in productsSorted"
              :key="product.id"
              :product="product"
              @add-to-cart="addToCart"
          />
        </div>

        <div class="category-grid top">
          <router-link class="category-item"
                       v-for="category in category_list"
                       :key="category.id"
                       :to="{ name: 'catalog-category', params: { categorySlug: category.slug } }"
                       :class="{'active': isActive(category.slug)}"
          >
            {{ category.name }}
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProductCard from "../common/ProductCard.vue";

export default {
  name: "Catalog",
  props: {
    products: {
      type: Array
    },
    category_list: {
      type: Object
    },
  },
  components: {
    ProductCard
  },
  data() {
    return {
      cart: []
    }
  },
  computed: {
    currentCategoryId() {
      const categorySlug = this.$route.params.categorySlug;
      const currentCategory = this.category_list.find(category => category.slug === categorySlug);
      return currentCategory ? currentCategory.id : null;
    },

    productsSorted() {
      if (!this.currentCategoryId) {
        return this.products;
      }

      return this.products.filter(product => product.category === this.currentCategoryId);
    }
  },
  created() {
    this.loadCart();
  },
  mounted() {
  },
  methods: {
    handleClick(category) {
      if (this.isActive(category.slug)) {
        this.$router.push({name: 'catalog'});
      }
    },
    getRoute(category) {
      return this.isActive(category.slug) ? {name: 'catalog'} : {
        name: 'catalog-category',
        params: {categorySlug: category.slug}
      };
    },
    isActive(slug) {
      if (slug === this.$route.params.categorySlug) {
        return true
      }
    },
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
}
</script>


<style scoped>
.catalog-component {
  margin-left: auto;
  margin-right: auto;

  display: flex;
  justify-content: center;
  align-items: center;
}

.catalog-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
}

.catalog-content {
  margin-top: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.category-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  gap: 0.5rem;
}

.category-item {
  display: flex;
  padding: 1rem 1.5rem;
  justify-content: center;
  align-items: center;
  gap: 0.625rem;
  flex: 1;
  white-space: nowrap;

  border-radius: 0.5rem;
  background: #FFF;

  text-decoration: none;
  color: var(--black);

  transition: all 0.2s ease-in-out;
}

.category-item:hover {
  color: white;
  background: var(--green-light);
}

.category-item.active {
  color: white;
  background: var(--green-light);
}

.products-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 1rem;
}

@media screen and (max-width: 1280px) {
  .catalog-component {
  }

  .catalog-max {
    padding: 0 2.25rem;
  }

  .catalog-content {
    gap: 4rem;
  }

  .products-grid {
    gap: 0.5rem;
  }
}

@media screen and (max-width: 1000px) {
  .catalog-component {
  }

  .catalog-max {
    padding: 0 2.25rem;
  }

  .catalog-content {
    margin-top: 1.5rem;
    gap: 2rem;
  }

  .products-grid {
    grid-template-columns: 1fr 1fr 1fr;
  }
}

@media screen and (max-width: 640px) {
  .catalog-component {
  }

  .catalog-max {
    padding: 0 1rem;
  }

  .catalog-content {
    margin-top: 1rem;
  }

  .products-grid {
    grid-template-columns: 1fr 1fr;
  }
}
</style>