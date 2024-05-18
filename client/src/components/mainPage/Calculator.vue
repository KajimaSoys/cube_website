<template>
  <div class="calculator-component">
    <div class="calculator-max">
      <div class="calculator-content">

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
}

.calculator-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
}

.calculator-content {
  display: flex;
  flex-direction: row;
  gap: 2.6rem;
}

@media screen and (max-width: 1280px) {
  .calculator-component {
    padding-top: 8rem;
  }

  .calculator-max {
    padding: 0 2.25rem;
  }

  .calculator-content {
    gap: 1.6rem;
  }
}

@media screen and (max-width: 1000px) {
   .calculator-component {
    padding-top: 5rem;
  }

  .calculator-max {
    padding: 0 2.25rem;
  }

  .calculator-content {
    flex-direction: column;
    gap: 0.5rem;
  }
}

@media screen and (max-width: 640px) {
   .calculator-component {
    padding-top: 4.4rem;
  }

  .calculator-max {
    padding: 0 1rem;
  }
}

</style>