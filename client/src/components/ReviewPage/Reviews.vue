<template>
  <div class="reviews-component">
    <div class="reviews-max">
      <h1>Отзывы</h1>
      <div class="reviews-content">
        <div
            class="review-card"
            v-for="review in reviews"
        >
          <div class="review-card-content">
            <div class="name">
              {{ review.name }}
            </div>
            <div class="review-text" v-html="review.review"></div>
          </div>
          <div class="review-link small-text-1" @click="showReviewPopup(review.image)">
            Оригинал отзыва
          </div>

        </div>
      </div>
    </div>
  </div>

  <review-popup
      :is-visible="isShowed"
      @close="isShowed = false"
      :reviewOriginalLink="reviewOriginalLink"
  />
</template>

<script>
import ReviewPopup from "../common/ReviewPopup.vue";

export default {
  name: "Reviews",
  inject: ['backendURL'],
  props: {
    reviews: Array
  },
  components: {
    ReviewPopup
  },
  data() {
    return {
      isShowed: false,
      reviewOriginalLink: ''
    }
  },
  mounted() {
  },
  methods: {
    showReviewPopup(link) {
      this.reviewOriginalLink = this.backendURL + '/media' + link.split('/media')[1]
      this.isShowed = true
    }
  },
}
</script>

r
<style scoped>
.reviews-component {
  margin-left: auto;
  margin-right: auto;

  display: flex;
  justify-content: center;
  align-items: center;
}

.reviews-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
}

.reviews-content {
  margin-top: 2rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.review-card {
  display: flex;
  padding: 2rem;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-between;
  gap: 2rem;

  border-radius: 1rem;
  background: #FFF;
}

.review-card-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.name {
  color: var(--black, #212121);
  font-family: 'Geologica', sans-serif;
  font-size: 1.5rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}

.review-link {
  color: var(--green-light, #289646);
  transition: opacity 0.2s ease-in-out;
  text-decoration: none;
  cursor: pointer;
}

.review-link:hover {
  opacity: 0.5;
}

@media screen and (max-width: 1280px) {
  .reviews-component {
  }

  .reviews-max {
    padding: 0 2.25rem;
  }

  .reviews-content {
    gap: 0.5rem;
  }

}

@media screen and (max-width: 1000px) {
  .reviews-component {
  }

  .reviews-max {
    padding: 0 2.25rem;
  }

  .reviews-content {
    margin-top: 1.5rem;
  }

  .review-card {
    padding: 1.5rem;
    border-radius: 0.75rem;
  }

  .name {
    font-size: 1.25rem;
  }
}

@media screen and (max-width: 640px) {
  .reviews-component {
  }

  .reviews-max {
    padding: 0 1rem;
  }

  .reviews-content {
    grid-template-columns: 1fr;
  }

  .review-card {
    padding: 1rem;
    gap: 1rem;
  }

  .review-card-content {
    gap: 0.5rem;
  }

  .name {
    font-size: 1.125rem;
  }
}
</style>