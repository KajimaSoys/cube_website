<template>
<div class="box-info-input-content">
  <h3>{{ title }}</h3>
</div>
</template>

<script>
export default {
  name: "BoxInfoInput",
  inject: ['backendURL'],
  props: {
    // calculator_description_block: Object,
    title: String
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
.box-info-input-content {
  border-radius: 1.5rem;
  background: #FFF;

  padding: 2rem;
  display: flex;
  flex-direction: row;
  width: -webkit-fill-available;
  width: -moz-fill-available;
}

h3 {
  font-size: 1.5rem;
}

@media screen and (max-width: 1280px) {
  .box-info-input-content {
    padding: 3rem 7rem 4rem 3rem;
    justify-content: space-between;
  }
}

@media screen and (max-width: 1000px) {
  .box-info-input-content {
    padding: 3rem 4.5rem 4rem 2.25rem;
  }
}

@media screen and (max-width: 640px) {
  .box-info-input-content {
    padding: 2rem 4.5rem 3rem 4.5rem;
    flex-direction: column;
    gap: 1.5rem;
  }
}
</style>