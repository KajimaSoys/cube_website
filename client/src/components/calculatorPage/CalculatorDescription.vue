<template>
<div class="calculator-description-component zero-top-padding">
    <div class="calculator-description-max">
      <div class="calculator-description-content">
        <h1 v-html="calculator_description_block.title"></h1>
        <div class="description">{{ calculator_description_block.description }}</div>
      </div>
      <div class="calculator-description-background"></div>
      <div class="image-container">
        <img :src="backendURL + calculator_description_block.image" alt="" loading="lazy">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CalculatorDescription",
  inject: ['backendURL'],
  props: {
    calculator_description_block: Object,
  },
  components: {},
  data() {
    return {
    }
  },
  mounted() {
  },
  methods: {},
}
</script>


<style scoped>
.calculator-description-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 9rem;

  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.zero-top-padding {
  padding-top: 0!important;
}

.calculator-description-max {
  max-width: 90rem;
  width: 100%;
  position: relative;
  overflow: hidden;
  border-radius: 1.5rem;
}

.calculator-description-background {
  position: absolute;
  max-width: 90rem;
  width: 100%;
  height: calc(100%);
  border-radius: 1.5rem;
  background: #FFF;
  top: 0;
  z-index: 0;
}

.calculator-description-content {
  padding: 5rem 0 5rem 6.8rem;
  position: relative;
  z-index: 2;

  display: flex;
  flex-direction: column;
  align-items: flex-start;

  width: 55%;
  gap: 1rem;
}

h1 {
  font-size: 2.75rem;
}

.description {
  width: 68%;
}

.image-container {
  position: absolute;
  z-index: 1;
  bottom: -14rem;
  right: 2rem;
}

.image-container img {
  width: 100%;
  max-width: 40rem;
  object-fit: cover;
}

@media screen and (max-width: 1280px) {
  .calculator-description-component {
    padding-top: 8rem;
  }

  .calculator-description-content {
    padding: 4rem 0 4rem 2.25rem;
    width: 45%;
  }

  h1 {
    width: 80%;
    font-size: 2rem;
  }

  .description {
    width: 80%;
  }

  .image-container {
    bottom: -14rem;
    right: -1rem;
  }

  .image-container img {
    max-width: 38rem;
  }
}

@media screen and (max-width: 1000px) {
  .calculator-description-component {
    padding-top: 5rem;
  }

  .calculator-description-content {
    padding: 3rem 0 3rem 2.25rem;
    gap: 0.5rem;
    width: 70%;
  }

  h1 {
    width: 90%;
    font-size: 2.125rem;
  }

  .description {
    width: 75%;
  }

  .image-container {
    bottom: -7rem;
    right: -7rem;
  }

  .image-container img {
    max-width: 24rem;
  }
}

@media screen and (max-width: 640px) {
  .calculator-description-component {
    padding-top: 4.4rem;
  }

  .calculator-description-background {
    height: calc(100%);
  }

  .calculator-description-content {
    padding: 2rem 1rem 0 1rem;
    align-items: center;
    width: unset;
  }

  h1 {
    width: 43vw;
    text-align: center;
    font-size: 1.875rem;
  }

  .description {
    text-align: center;
    width: 85%;
  }

  .image-container {
    position: relative;
    bottom: -1rem;
    right: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 14rem;
  }

  .image-container img {
    width: 22rem;
  }
}

@media screen and (max-width: 400px) {
  h1 {
    width: 50vw;
  }
}
</style>