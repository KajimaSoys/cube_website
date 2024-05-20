<template>
<div class="calculator-description-component zero-padding">
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

.zero-padding {
  padding-top: 0!important;
}

.calculator-description-max {
  max-width: 76.3rem;
  width: 100%;

  position: relative;
  overflow: hidden;
  border-radius: 1.5rem;

  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.calculator-description-background {
  position: absolute;
  max-width: 76.3rem;
  width: 100%;
  height: calc(100%);
  border-radius: 1.5rem;
  background: #FFF;
  top: 0;
  z-index: 0;
}

.calculator-description-content {
  padding: 2rem 0 4rem 2rem;
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
  width: 70%;
}

.image-container {
  position: absolute;
  z-index: 1;
  bottom: -1rem;
  right: -12rem;
}

.image-container img {
  width: 100%;
  object-fit: cover;
}

@media screen and (max-width: 1280px) {
  .calculator-description-component {
    padding-top: 8rem;
  }

  .calculator-description-max {
    padding: 0 2.25rem;
  }

  .calculator-description-content {
    padding: 3rem 7rem 4rem 3rem;
    justify-content: space-between;
  }

  h1 {
    width: 80%;
    font-size: 2rem;
  }
}

@media screen and (max-width: 1000px) {
  .calculator-description-max {
    padding: 0;
  }

  .calculator-description-component {
    padding-top: 5rem;
  }

  .calculator-description-content {
    padding: 3rem 4.5rem 4rem 2.25rem;
  }

  h1 {
    width: 70%;
    font-size: 1.5rem;
  }
}

@media screen and (max-width: 640px) {
  .calculator-description-component {
    padding-top: 4.4rem;
  }

  .calculator-description-max {
    gap: 0.5rem;
  }

  .calculator-description-content {
    padding: 2rem 4.5rem 3rem 4.5rem;
    flex-direction: column;
    gap: 1.5rem;
  }

  h1 {
    width: 43vw;
    text-align: center;
    font-size: 1.25rem;
  }
}

@media screen and (max-width: 400px) {
  h1 {
    width: 50vw;
  }
}
</style>