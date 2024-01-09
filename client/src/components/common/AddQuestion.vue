<template>
  <div class="question-component">
    <div class="question-max">
      <div class="question-content">
        <h2 v-html="add_question_block.title"></h2>
        <div class="description">{{ add_question_block.description }}</div>
        <a class="button" :href="add_question_block.whatsapp_link" target="_blank">{{ button_text}}</a>
      </div>
      <div class="question-background"></div>
      <div class="image-container">
        <img :src="backendURL + add_question_block.image" alt="" loading="lazy">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddQuestion",
  inject: ['backendURL'],
  props: {
    add_question_block: Object,
    button_text: {
      type: String,
      default: 'Связаться'
    }
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
.question-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 9rem;

  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.question-max {
  max-width: 90rem;
  width: 100%;
  position: relative;
  overflow: hidden;
  border-radius: 1.5rem;
}

.question-background {
  position: absolute;
  max-width: 90rem;
  width: 100%;
  height: calc(100%);
  border-radius: 1.5rem;
  background: #FFF;
  top: 0;
  z-index: 0;
}

.question-content {
  padding: 5rem 0 7.4rem 6.8rem;
  position: relative;
  z-index: 2;

  display: flex;
  flex-direction: column;
  align-items: flex-start;

  width: 50%;
  gap: 1rem;
}

.description {
  width: 50%;
}

.button {
  margin-top: 2rem;
  padding: 1rem 2rem;
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
  bottom: -19rem;
  right: -20rem;
}

.image-container img {
  width: 100%;
  object-fit: cover;
}

@media screen and (max-width: 1280px) {
  .question-component {
    padding-top: 8rem;
  }

  .question-content {
    padding: 4rem 0 5rem 2.25rem;
  }

  .description {
    width: 60%;
  }

  .button {
    height: 1.5rem;
    margin-top: 1.5rem;
  }

  .image-container {
    bottom: -15.5rem;
    right: -28rem;
  }

  .image-container img {
    width: 80%;
  }
}

@media screen and (max-width: 1000px) {
  .question-component {
    padding-top: 5rem;
  }

  .question-content {
    padding: 3rem 0 4rem 2.25rem;
    gap: 0.5rem;
  }

  .description {
    width: 84%;
  }

  .button {
    margin-top: 1.5rem;
    padding: 0.75rem 1.5rem;
  }

  .image-container {
    bottom: -4.5rem;
    right: -46rem;
  }

  .image-container img {
    width: 43%;
  }

}

@media screen and (max-width: 640px) {
  .question-component {
    padding-top: 4.4rem;
  }

  .question-max {

  }

  .question-background {
    height: calc(100%);
  }

  .question-content {
    padding: 2rem 1rem 0 1rem;
    align-items: center;
    width: unset;
  }

  h2 {
    text-align: center;
  }

  .description {
    text-align: center;
    width: 53%;
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
    height: 10rem;
  }

  .image-container img {
    width: 21rem;
    rotate: 26deg;
  }

}
</style>