<template>
<div class="box-info-component">
    <div class="box-info-max">
      <h2>Введите размеры коробок</h2>

      <BoxInfoInput
        componentType="outer"
        defaultType="four-valve"
        :productList="productList"
        :isSubmitted="isSubmitted"
        @inputDataChange="processInput"
      />

      <BoxInfoInput
        componentType="inner"
        defaultType="self-assembled"
        :productList="productList"
        :isSubmitted="isSubmitted"
        @inputDataChange="processInput"
      />

      <a class="button" @click="submit">Рассчитать</a>
    </div>
  </div>
</template>

<script>
import BoxInfoInput from "./BoxInfoInput.vue";

export default {
  name: "BoxInfo",
  inject: ['backendURL'],
  props: {
    productList: Array
  },
  components: {
    BoxInfoInput,
  },
  data() {
    return {
      isSubmitted: false,
      boxData: { outer: {}, inner: {} },
    }
  },
  mounted() {
  },
  methods: {
    submit() {
      this.isSubmitted = true;
      if (!this.isEmpty(this.boxData.outer) && !this.isEmpty(this.boxData.inner)) {
        this.$emit('calculate', this.boxData);
      }
    },

    isEmpty(obj) {
      return Object.keys(obj).length === 0;
    },

    processInput(type, data) {
      this.boxData[type] = data;
    }
  },
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
  cursor: pointer;
  color: white;
  user-select: none;
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
  .box-info-component {
    padding-top: 5rem;
  }

  h2 {
    font-size: 1.5rem;
    margin-bottom: unset;
  }

  .button {
    width: -webkit-fill-available;
    width: -moz-fill-available;
    padding: 1rem;
    height: 1.5rem;
    flex-direction: column;
    justify-content: center;
    margin-top: unset;
  }
}

@media screen and (max-width: 640px) {
  .box-info-component {
    padding-top: 4.4rem;
  }

  .box-info-max {
    gap: 0.5rem;
    padding: 0 1rem;
  }

  h2 {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
  }

  .button {
    margin-top: 0.5rem;
    height: 1.25rem;
  }
}
</style>