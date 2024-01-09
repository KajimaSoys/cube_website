<template>
  <div class="teaser-component">
    <div class="teaser-max">
      <div class="teaser-head">
        <h2>{{ catalog_teaser_block.title }}</h2>
        <router-link :to="{ name: 'catalog' }" class="button">
          Каталог
        </router-link>
      </div>

      <div class="teaser-content">
        <router-link
            class="category"
            v-for="category in shown_category_list"
            :key="category.id"
            :to="{ name: 'catalog-category', params: { categorySlug: category.slug } }"
        >
          <div class="image-container">
            <img :src="backendURL + category.image_cat" :alt="'Категория ' + category.name" loading="lazy">
          </div>
          <div class="category-name">
            {{ category.name }}
          </div>
        </router-link>
      </div>

      <div
          class="button button-toggle"
          @click="toggleAllQuestions"
          v-if="category_list.length > 10"
      >
        <div class="button-text">
          {{ showAll ? 'Скрыть категории' : 'Показать все категории' }}
        </div>
        <div class="button-icon" :style="{ transform: showAll ? 'rotate(180deg)' : 'rotate(0deg)' }">
          <svg xmlns="http://www.w3.org/2000/svg" width="17" height="17" viewBox="0 0 17 17" fill="none">
            <path d="M4.5 6.5L8.5 10.5L12.5 6.5" stroke="#fff" stroke-width="1.5" stroke-linecap="round"
                  stroke-linejoin="round"/>
          </svg>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CatalogTeaser",
  inject: ['backendURL', 'frontendURL'],
  props: {
    catalog_teaser_block: Object,
    category_list: Array,
  },
  components: {},
  data() {
    return {
      showAll: false,
    }
  },
  computed: {
    shown_category_list() {
      return this.showAll ? this.category_list : this.category_list.slice(0, 10);
    },
  },
  mounted() {
  },
  methods: {
    toggleAllQuestions() {
      this.showAll = !this.showAll;
    },
  },
}
</script>


<style scoped>
.teaser-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 9rem;

  display: flex;
  justify-content: center;
  align-items: center;
}

.teaser-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
}

.teaser-head {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
}

.button {
  display: flex;
  align-items: center;
  justify-content: center;

  padding: 1.5rem 2rem;
  width: 6.3rem;

  color: white;
  border-radius: 0.5rem;
  background: var(--green-light, #40AB5E);
  text-decoration: none;
}

.teaser-content {
  margin-top: 4rem;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  gap: 1rem;
}

a {
  transition: opacity 0.2s ease-in-out;
}

a:hover {
  opacity: 0.5;
}

.category {
  flex: 1;
  display: flex;
  padding: 2rem 0rem;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  align-self: stretch;
  border-radius: 1rem;
  background: #FFF;
  text-decoration: none;
  justify-content: space-between;
}

.image-container {
  height: 7.5rem;
}

.image-container img {
  width: 100%;
  height: 7.5rem;
  object-fit: cover;
}

.category-name {
  width: 85%;
  text-align: center;

  color: var(--black);
  flex: 1;
}

.button-toggle {
  margin-top: 4rem;
  margin-left: auto;
  margin-right: auto;
  width: 16.3rem;
  display: flex;
  gap: 0.5rem;
  align-items: center;
  cursor: pointer;
  user-select: none;
}

.button-icon {
  display: flex;
}

@media screen and (max-width: 1280px) {
  .teaser-component {
    padding-top: 8rem;
  }

  .teaser-max {
    padding: 0 2.25rem;
  }

  .teaser-content {
    margin-top: 2.5rem;
    gap: 0.5rem;
  }

  .image-container, .image-container img {
    height: 6.25rem;
  }

  .category-name {
    font-size: 1rem;
  }

  .button-toggle {
    margin-top: 2rem;
  }
}

@media screen and (max-width: 1000px) {
  .teaser-component {
    padding-top: 5rem;
  }

  .button {
    padding: 0.75rem 1.5rem;
  }

  .teaser-content {
    grid-template-columns: 1fr 1fr 1fr 1fr;
  }

  .image-container, .image-container img {
    height: 5rem;
  }

  .category-name {
    font-size: 0.75rem;
  }
}

@media screen and (max-width: 640px) {
  .teaser-component {
    padding-top: 4.4rem;
  }

  .teaser-max {
    padding: 0 1rem;;
  }

  .teaser-content {
    margin-top: 1.5rem;
    grid-template-columns: 1fr 1fr;
  }

  .button {
    padding: 0.625rem 1rem 0.625rem 1rem;
  }

  .category {
    padding: 1.5rem 0rem;
  }

  .button-toggle {
    margin-top: 1.5rem;
  }
}
</style>