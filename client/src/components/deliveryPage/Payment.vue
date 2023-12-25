<template>
  <div class="payment-component">
    <div class="payment-max">
      <div class="payment-content">
        <div class="left-side">
          <h2>{{ payment_block.title }}</h2>
          <div class="contact">
            <a :href="payment_block.question_link" target="_blank">
              Задать вопрос по оплате
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="17" viewBox="0 0 16 17" fill="none">
                <path d="M6.66675 4.5L10.6667 8.5L6.66675 12.5" stroke="#289646" stroke-width="1.5"
                      stroke-linecap="round"
                      stroke-linejoin="round"/>
              </svg>
            </a>
          </div>
        </div>
        <div class="right-side">
          <div class="card-first">
            <div class="card-title">{{ payment_block.subtitle_first }}</div>
            <div class="card-description">{{ payment_block.text_first }}</div>
            <div class="card-additional">{{ payment_block.additional_first }}</div>
            <div class="image-container">
              <img :src="backendURL + payment_block.image_first" alt="Блок доставки. Изображение №1">
            </div>
          </div>

          <div class="card-second">
            <div class="card-title">{{ payment_block.subtitle_second }}</div>
            <div class="card-description">{{ payment_block.text_second }}</div>
            <div class="card-additional">{{ payment_block.additional_second }}</div>
            <div class="image-container">
              <img :src="backendURL + payment_block.image_second" alt="Блок доставки. Изображение №1">
            </div>
          </div>
        </div>
        <div class="bottom-container">
          <div class="contact">
            <a :href="payment_block.question_link" target="_blank">
              Задать вопрос по оплате
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="17" viewBox="0 0 16 17" fill="none">
                <path d="M6.66675 4.5L10.6667 8.5L6.66675 12.5" stroke="#289646" stroke-width="1.5"
                      stroke-linecap="round"
                      stroke-linejoin="round"/>
              </svg>
            </a>
          </div>
        </div>
      </div>
      <div class="payment-background"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Payment",
  inject: ['backendURL'],
  props: {
    payment_block: Object,
  },
  components: {},
  data() {
    return {}
  },
  mounted() {
  },
  methods: {},
}
</script>


<style scoped>
.payment-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 1rem;

  display: flex;
  justify-content: center;
  align-items: center;
}

.payment-max {
  max-width: 90rem;
  width: 100%;
  position: relative;
}

.payment-background {
  position: absolute;
  max-width: 90rem;
  width: 100%;
  height: calc(100%);
  border-radius: 1.5rem;
  background: #FFF;
  top: 0;
  z-index: 0;
}

.payment-content {
  padding: 5rem 6.8rem 5rem 6.8rem;
  position: relative;
  z-index: 2;

  display: flex;
  flex-direction: row;
  gap: 3rem;
}

.left-side {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex: 0;
  min-width: 22rem;
}

.contact {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.contact a {
  color: var(--green-light);
  text-decoration: none;
  transition: opacity 0.2s ease-in-out;
}

.contact a:hover {
  opacity: 0.5;
}

.contact a svg {
  bottom: -3px;
  position: relative;
}


.right-side {
  display: flex;
  gap: 1rem;
  flex: 1;
  justify-content: flex-end;
}

.card-first, .card-second {
  border-radius: 1rem;
  border: 2px solid #E5E2E1;
  background: #FFF;

  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 2rem;
  gap: 1rem;
  flex: 1;
  position: relative;
  overflow: hidden;

  min-height: 14.8rem;
  max-width: 20.8rem;
}

.card-title {
  margin-bottom: 0.5rem;

  display: flex;
  padding: 0.5rem 1rem;
  align-items: flex-start;
  gap: 0.625rem;

  border-radius: 0.5rem;
  border: 2px solid var(--green-light, #40AB5E);
  background: #FFF;
  color: var(--green-light, #40AB5E);
  font-weight: 500;
}

.card-description {
  width: 70%;
}

.card-additional {
  font-size: 1rem;
  color: var(--black-55);
}

.image-container {
  width: 14rem;
  height: 10rem;
  position: absolute;
}

.card-first .image-container {
  right: -8rem;
  bottom: 0.8rem;
  rotate: -9deg;
}

.card-second .image-container {
  right: 0;
  bottom: 0;
  width: 8rem;
  rotate: -9deg;
}

.image-container img {
  width: 100%;
  object-fit: cover;
}

.bottom-container {
  display: none;
}

@media screen and (max-width: 1280px) {
  .payment-content {
    padding: 3rem 2.25rem 3rem 2.25rem;
    gap: 3.75rem;
  }

  .card-additional {
    font-size: 0.875rem;
  }

  .image-container {
    width: 10rem;
    height: 10rem;
  }

  .left-side {
    min-width: 15.75rem;
  }

  .right-side {
    gap: 0.5rem;
  }

  .card-first, .card-second {
    padding: 1.5rem;
  }

  .card-first .image-container {
    right: -5rem;
    bottom: -1.6rem;
    width: 11rem;
  }

  .card-second .image-container {
    right: 0;
    bottom: -1rem;
  }
}

@media screen and (max-width: 1000px) {
  .payment-content {
    flex-direction: column;
    gap: 2rem;
  }

  h2 {
    width: 55%;
  }

  .contact {
    align-items: flex-start;
  }

  .left-side {
    flex-direction: row;
  }

  .card-first, .card-second {
    max-width: unset;
  }

  .card-title {
    font-size: 1rem;
  }

  .card-additional {
    font-size: 0.75rem;
  }

  .card-first .card-description {
    width: 82%;
  }

  .card-second .card-description {
    width: 69%;
  }

  .image-container {
    width: 9rem;
    height: 9rem;
  }

  .card-first .image-container {
    bottom: -0.3rem;
    right: -5.5rem;
  }

  .card-second .image-container {
    bottom: -0.5rem;
    width: 7rem;
  }
}

@media screen and (max-width: 640px) {
  .payment-content {
    padding: 2rem 1rem 2rem 1rem;
    gap: 1.5rem;
  }

  .left-side .contact {
    display: none;
  }

  h2 {
    width: 80%;
  }

  .right-side {
    flex-direction: column;
  }

  .card-first .card-description {
    width: 62%;
  }

  .card-second .card-description {
    width: 56%;
  }

  .card-first .image-container {
    bottom: -0.3rem;
    right: -2.5rem;
  }

  .card-second .image-container {
    width: 9rem;
    bottom: 1rem;
    right: 0.5rem;
  }

  .bottom-container {
    display: flex;
    justify-content: center;
  }

  .contact a svg {
    bottom: -5px;
  }
}
</style>