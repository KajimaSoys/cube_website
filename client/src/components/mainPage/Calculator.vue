<template>
  <div class="calculator-component">
    <div class="calculator-max">
      <div class="calculator-content">
        <h2 v-html="calculator_block.title"></h2>
        <div class="description">{{ calculator_block.description }}</div>
        <router-link :to="{ name: 'calculator' }" class="button">{{ button_text}}</router-link>
      </div>
      <div class="calculator-background"></div>
      <div class="image-container">
        <img :src="backendURL + calculator_block.image" alt="" loading="lazy">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Calculator",
  inject: ['backendURL'],
  props: {
    calculator_block: Object,
    button_text: {
      type: String,
      default: 'Рассчитать'
    }
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
.calculator-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 9rem;

  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.calculator-max {
  max-width: 90rem;
  width: 100%;
  position: relative;
  overflow: hidden;
  border-radius: 1.5rem;
}

.calculator-background {
  position: absolute;
  max-width: 90rem;
  width: 100%;
  height: calc(100%);
  border-radius: 1.5rem;
  background: #FFF;
  top: 0;
  z-index: 0;
}

.calculator-content {
  padding: 5rem 0 5rem 6.8rem;
  position: relative;
  z-index: 2;

  display: flex;
  flex-direction: column;
  align-items: flex-start;

  width: 55%;
  gap: 1rem;
}

.description {
  width: 68%;
}

.button {
  margin-top: 2rem;
  padding: 1rem 2.5rem;
  height: 2.5rem;

  display: flex;
  justify-content: space-between;
  align-items: center;

  border-radius: 0.5rem;
  background: var(--green-light, #40AB5E);
  text-decoration: none;
  color: white;
}

a {
  transition: opacity 0.2s ease-in-out;
}

a:hover {
  opacity: 0.5;
}

.image-container {
  position: absolute;
  z-index: 1;
  bottom: -11rem;
  right: -4rem;
}

.image-container img {
  width: 100%;
  max-width: 40rem;
  object-fit: cover;
}

@media screen and (max-width: 1280px) {
  .calculator-component {
    padding-top: 8rem;
  }

  .calculator-content {
    padding: 4rem 0 4rem 2.25rem;
    width: 45%;
  }

  .description {
    width: 80%;
  }

  .button {
    height: 1.5rem;
    margin-top: 1rem;
    padding: 1rem 2rem;
  }

  .image-container {
    bottom: -10rem;
    right: -4rem;
  }

  .image-container img {
    max-width: 38rem;
  }
}

@media screen and (max-width: 1000px) {
  .calculator-component {
    padding-top: 5rem;
  }

  .calculator-content {
    padding: 3rem 0 3rem 2.25rem;
    gap: 0.5rem;
  }

  .description {
    width: 90%;
  }

  .button {
    margin-top: 1.5rem;
    padding: 0.75rem 1.5rem;
  }

  .image-container {
    bottom: -3rem;
    right: -3rem;
  }

  .image-container img {
    max-width: 24rem;
  }

}

@media screen and (max-width: 640px) {
  .calculator-component {
    padding-top: 4.4rem;
  }

  .calculator-background {
    height: calc(100%);
  }

  .calculator-content {
    padding: 2rem 1rem 0 1rem;
    align-items: center;
    width: unset;
  }

  h2 {
    text-align: center;
  }

  .description {
    text-align: center;
    width: 85%;
  }

  .button {
    justify-content: center;
    margin-top: 1rem;
  }

  .image-container {
    position: relative;
    bottom: -1rem;
    right: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 16rem;
  }

  .image-container img {
    width: 22rem;
  }

}
</style>