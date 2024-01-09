<template>
  <div class="main-component">

    <div class="main-max">
      <div class="main-content">
        <div class="small-text-1">{{ main_block.company_name }}</div>
        <h1 v-html="main_block.title" class="title"></h1>
        <div v-html="main_block.description" class="description"></div>

        <router-link :to="{ name: 'catalog' }" class="button">
          Перейти в каталог
        </router-link>

        <div class="cards">
          <div class="card">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
              <path
                  d="M20.7703 4.50913L23.437 5.90853C26.3059 7.41405 27.7403 8.16681 28.5369 9.51949C29.3334 10.8722 29.3334 12.5554 29.3334 15.9218V16.0778C29.3334 19.4442 29.3334 21.1276 28.5369 22.4802C27.7403 23.8329 26.3059 24.5856 23.437 26.0912L20.7703 27.4905C18.4295 28.7189 17.2591 29.3332 16.0001 29.3332C14.741 29.3332 13.5706 28.7189 11.2298 27.4905L8.56313 26.0912C5.69425 24.5856 4.2598 23.8329 3.46328 22.4802C2.66675 21.1276 2.66675 19.4442 2.66675 16.0778V15.9218C2.66675 12.5554 2.66675 10.8722 3.46328 9.51949C4.2598 8.16681 5.69425 7.41405 8.56313 5.90853L11.2298 4.50913C13.5706 3.28072 14.741 2.6665 16.0001 2.6665C17.2591 2.6665 18.4295 3.28072 20.7703 4.50913Z"
                  stroke="#40AB5E" stroke-width="2" stroke-linecap="round"/>
              <path
                  d="M28 10L22.6667 12.6667M22.6667 12.6667C22.6667 12.6667 22.2604 12.8698 22 13C19.6568 14.1716 16 16 16 16M22.6667 12.6667V17.3333M22.6667 12.6667L10 6M16 16L4 10M16 16V28.6667"
                  stroke="#40AB5E" stroke-width="2" stroke-linecap="round"/>
            </svg>
            {{ main_block.bar_first }}
          </div>

          <div class="card">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
              <path d="M2.50391 5.94531V26.2281" stroke="#289646" stroke-width="2" stroke-linecap="round"
                    stroke-linejoin="round"/>
              <path d="M9.55664 14.7222L9.55664 26.1286" stroke="#289646" stroke-width="2" stroke-linecap="round"
                    stroke-linejoin="round"/>
              <path d="M9.55664 5.85059L9.55664 9.65273" stroke="#289646" stroke-width="2" stroke-linecap="round"
                    stroke-linejoin="round"/>
              <path d="M22.4966 5.94531V26.2281" stroke="#289646" stroke-width="2" stroke-linecap="round"
                    stroke-linejoin="round"/>
              <path d="M16.043 24.2275V26.2284" stroke="#289646" stroke-width="2" stroke-linecap="round"
                    stroke-linejoin="round"/>
              <path d="M16.0334 5.85059L16.0334 18.5244" stroke="#289646" stroke-width="2" stroke-linecap="round"
                    stroke-linejoin="round"/>
              <path d="M28.9751 18.6216V26.2276" stroke="#289646" stroke-width="2" stroke-linecap="round"
                    stroke-linejoin="round"/>
              <path d="M28.9873 5.85059L28.9873 13.4549" stroke="#289646" stroke-width="2" stroke-linecap="round"
                    stroke-linejoin="round"/>
            </svg>
            {{ main_block.bar_second }}
          </div>

          <div class="card">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
              <path
                  d="M5 27V19.6667M5 27H12.3333M5 27L10.1944 21.8056L12.0278 19.9722M27 5V12.3333M27 5H19.6667M27 5L21.8056 10.1944L19.9722 12.0278"
                  stroke="#289646" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            {{ main_block.bar_third }}
          </div>

          <div class="card">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
              <path
                  d="M5.2 23.2L10.1704 18.2296C10.952 17.448 11.3427 17.0573 11.7943 16.9083C12.1916 16.7773 12.6199 16.7741 13.0191 16.8993C13.4728 17.0415 13.8693 17.4265 14.6623 18.1964L18.9833 22.3917M27.4 22.825L25.2377 20.6627C24.4457 19.8707 24.0497 19.4747 23.593 19.3263C23.1914 19.1958 22.7587 19.1958 22.357 19.3263C21.9003 19.4747 21.5042 19.8708 20.7119 20.6631C19.7757 21.5993 18.9833 22.3917 18.9833 22.3917M23.8 27.2083L18.9833 22.3917M23.2 11.2C23.2 12.5255 22.1255 13.6 20.8 13.6C19.4745 13.6 18.4 12.5255 18.4 11.2C18.4 9.87452 19.4745 8.8 20.8 8.8C22.1255 8.8 23.2 9.87452 23.2 11.2ZM13.6 28H18.4C21.7603 28 23.4405 28 24.7239 27.346C25.8529 26.7708 26.7708 25.8529 27.346 24.7239C28 23.4405 28 21.7603 28 18.4V13.6C28 10.2397 28 8.55953 27.346 7.27606C26.7708 6.14708 25.8529 5.2292 24.7239 4.65396C23.4405 4 21.7603 4 18.4 4H13.6C10.2397 4 8.55953 4 7.27606 4.65396C6.14708 5.2292 5.2292 6.14708 4.65396 7.27606C4 8.55953 4 10.2397 4 13.6V18.4C4 21.7603 4 23.4405 4.65396 24.7239C5.2292 25.8529 6.14708 26.7708 7.27606 27.346C8.55953 28 10.2397 28 13.6 28Z"
                  stroke="#289646" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            {{ main_block.bar_fourth }}
          </div>
        </div>
      </div>
      <div class="image-container">
        <img :src="backendURL + main_block.image" alt="Изображение главного блока компании Cube" loading="lazy">
      </div>
      <div class="main-background"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Main",
  inject: ['backendURL'],
  props: {
    main_block: Object,
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
.main-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 9rem;
  /*  padding-left: 1rem;
    padding-right: 1rem;*/

  display: flex;
  justify-content: center;
  align-items: center;
}

.main-max {
  max-width: 90rem;
  width: 100%;
  position: relative;
}

.main-background {
  position: absolute;
  max-width: 90rem;
  width: 100%;
  height: calc(100% - 5.125rem);
  border-radius: 1.5rem;
  background: #FFF;
  top: 0;
  z-index: 0;
}

.main-content {
  padding: 5rem 6.8rem 0 6.8rem;
  position: relative;
  z-index: 2;
}

.title {
  width: 66%;
  text-align: unset;
  margin-top: 1rem;
}

.description {
  margin-top: 2rem;
  width: 40%;
  text-align: unset;
}

.button {
  display: flex;
  align-items: center;
  justify-content: center;

  margin-top: 3rem;
  padding: 1.5rem 2rem;
  width: 17%;

  color: white;
  border-radius: 0.5rem;
  background: var(--green-light, #40AB5E);
  text-decoration: none;
}

a {
  transition: opacity 0.2s ease-in-out;
}

a:hover {
  opacity: 0.5;
}

.cards {
  display: flex;
  flex-direction: row;
  gap: 1rem;

  border-radius: 1rem;
  margin-top: 6.25rem;
  position: relative;
}

.card {
  border-radius: 1rem;
  background: #FFF;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 1rem;
  bottom: -3.125rem;
  box-shadow: 0px 4px 77px 0px rgba(24, 12, 4, 0.06);
  flex: 1;
}

.image-container {
  position: absolute;
  top: 5.6rem;
  right: 4.25rem;
  z-index: 1;
}

.image-container img {
  width: 100%;
  object-fit: cover;
}

@media screen and (max-width: 1280px) {
  .main-content {
    padding: 4rem 2.25rem 0 2.25rem;
  }

  .small-text-1 {
    font-size: 1rem;
  }

  .description {
    margin-top: 1.5rem;
  }

  .button {
    margin-top: 4rem;
    width: 20%;
  }

  .cards {
    margin-top: 8rem;
    gap: 0.5rem;
  }

  .card {
    padding: 1.5rem;
  }

  .image-container {
    right: -3.75rem;
    top: 4rem;
  }

  .image-container img {
    /*width: 87%;*/
  }
}

@media screen and (max-width: 1000px) {
  .main-component {
    padding-top: 7.75rem;
  }

  .main-content {
    padding: 3rem 2.25rem 0 2.25rem;
  }

  .main-background {
    height: calc(100% - 13.125rem);
  }

  .small-text-1 {
    font-size: 0.75rem;
  }

  .title {
    width: 100%;
  }

  .description {
    margin-top: 1.5rem;
    width: 50%;
  }


  .button {
    margin-top: 2rem;
    width: 30%;
  }

  .cards {
    margin-top: 14.4rem;
    display: grid;
    grid-template-columns: 2fr 2fr;

  }

  .image-container {
    right: -11.75rem;
    top: 14rem;
  }

  .image-container img {
    width: 80%;
  }
}

@media screen and (max-width: 640px) {
  .main-component {
    padding-top: 6.5rem;
  }

  .main-content {
    padding: 2rem 1rem 0 1rem;
  }

  .main-background {
    height: calc(100% - 18.125rem);
  }

  .small-text-1 {
    text-align: center;
  }

  .title {
    text-align: center;
    margin-top: 0.5rem;
  }

  .description {
    text-align: center;
    margin-top: 1rem;
    width: 100%;
  }

  .button {
    width: -moz-available;
    width: -webkit-fill-available;
  }

  .cards {
    margin-top: 20rem;
    grid-template-columns: unset;
  }

  .card {
    flex-direction: row;
    align-items: center;
  }

  .image-container {
    right: -16.75rem;
    top: unset;
    bottom: 18rem;
  }

  .image-container img {
    width: 65%;
  }
}
</style>