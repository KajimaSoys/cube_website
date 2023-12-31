<template>
  <div class="catalog-component">
    <div class="catalog-max">
      <h1>Каталог</h1>
      <div class="catalog-content">
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

        <div class="products-grid">
          <ProductCard
              v-for="(product, idx) in productsSorted"
              :key="idx"
              :product="product"
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
    return {}
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
  mounted() {
  },
  methods: {
    isActive(slug) {
      if (slug === this.$route.params.categorySlug) {
        return true
      }
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
}

@media screen and (max-width: 1000px) {
  .catalog-component {
  }

  .catalog-max {
    padding: 0 2.25rem;
  }
}

@media screen and (max-width: 640px) {
  .catalog-component {
  }

  .catalog-max {
    padding: 0 1rem;
  }
}
</style>