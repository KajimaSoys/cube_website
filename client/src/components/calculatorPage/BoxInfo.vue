<template>
<div class="box-info-component">
    <div class="box-info-max">
      <h2>Введите размеры коробок</h2>

      <BoxInfoInput
        title="Внешняя коробка"
      />

      <BoxInfoInput
        title="Внутренняя коробка или товар"
      />

      <a class="button">Рассчитать</a>

    </div>
  </div>
</template>

<script>
import BoxInfoInput from "./BoxInfoInput.vue";

export default {
  name: "BoxInfo",
  inject: ['backendURL'],
  components: {
    BoxInfoInput,
  },
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
.box-info-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 5rem;

  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.box-info-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: flex-start;

  gap: 1rem;
}

h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.button {
  margin-top: 1rem;
  padding: 1rem 6rem;
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

@media screen and (max-width: 1280px) {
  .box-info-component {
    padding-top: 8rem;
  }

  .box-info-max {
    padding: 0 2.25rem;
  }
}

@media screen and (max-width: 1000px) {
  .box-info-max {
    padding: 0;
  }

  .box-info-component {
    padding-top: 5rem;
  }
}

@media screen and (max-width: 640px) {
  .box-info-component {
    padding-top: 4.4rem;
  }

  .box-info-max {
    gap: 0.5rem;
  }
}
</style>