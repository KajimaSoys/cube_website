<template>
<div class="calculation-result-component" id="calculation-result">
    <div class="calculation-result-max">

      <h2>Расчет</h2>
      <div class="calculation-result-content">
        Какой-то результат
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "CalculationResult",
  inject: ['backendURL'],
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
.calculation-result-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 5rem;

  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.calculation-result-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
  display: flex;
  flex-direction: column;

  gap: 1rem;
}

.calculation-result-content {
  border-radius: 1.5rem;
  background: #FFF;

  padding: 2rem;
  display: flex;
  flex-direction: row;
}

h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

@media screen and (max-width: 1280px) {
  .calculation-result-component {
    padding-top: 8rem;
  }

  .calculation-result-max {
    padding: 0 2.25rem;
  }

  .calculation-result-content {
    padding: 3rem 7rem 4rem 3rem;
    justify-content: space-between;
  }
}

@media screen and (max-width: 1000px) {
  .calculation-result-max {
    padding: 0;
  }

  .calculation-result-component {
    padding-top: 5rem;
  }

  .calculation-result-content {
    padding: 3rem 4.5rem 4rem 2.25rem;
  }
}

@media screen and (max-width: 640px) {
  .calculation-result-component {
    padding-top: 4.4rem;
  }

  .calculation-result-max {
    gap: 0.5rem;
  }

  .calculation-result-content {
    padding: 2rem 4.5rem 3rem 4.5rem;
    flex-direction: column;
    gap: 1.5rem;
  }
}
</style>