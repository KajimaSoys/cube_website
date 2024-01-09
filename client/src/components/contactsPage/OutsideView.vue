<template>
  <div class="outside-component">
    <div class="outside-max">
      <div class="outside-content">
        <div class="card">
          <div class="image-container">
            <img :src="backendURL + outside_view.image_first" alt="" loading="lazy">
          </div>
          <div class="title">
            {{ outside_view.text_first }}
          </div>
        </div>

        <div class="card">
          <div class="image-container">
            <img :src="backendURL + outside_view.image_second" alt="" loading="lazy">
          </div>
          <div class="title">
            {{ outside_view.text_second }}
          </div>
        </div>

        <div class="card">
          <div class="image-container">
            <img :src="backendURL + outside_view.image_third" alt="" loading="lazy">
          </div>
          <div class="title">
            {{ outside_view.text_third }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "OutsideView",
  inject: ['backendURL'],
  props: {
    outside_view: Object,
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

.outside-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 9rem;

  display: flex;
  justify-content: center;
  align-items: center;
}

.outside-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
}

.outside-content {
  display: flex;
  flex-direction: row;
  gap: 1rem;
}

.card {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.image-container {
  display: flex;
  border-radius: 1rem;
  overflow: hidden;
}

.image-container img {
  width: 100%;
  object-fit: cover;
}

.title {
  display: flex;
  padding: 1.5rem;
  justify-content: center;
  align-items: center;
  gap: 0.625rem;

  text-align: center;
  flex: 1;

  border-radius: 1rem;
  background: #FFF;
}


@media screen and (max-width: 1280px) {
  .outside-component {
    padding-top: 3rem;
  }

  .outside-max {
    padding: 0 2.25rem;
  }

  .outside-content, .card {
    gap: 0.5rem;
  }
}

@media screen and (max-width: 1000px) {
  .outside-component {
    padding-top: 2rem;
  }

  .outside-max {
    padding: 0 2.25rem;
  }

  .title {
    padding: 1.5rem 0.9rem;
  }
}

@media screen and (max-width: 640px) {
  .outside-component {
    padding-top: 4.4rem;
  }

  .outside-max {
    padding: 0 1rem;
  }

  .outside-content {
    flex-direction: column;
    gap: 1.5rem;
  }

  .title {
    font-size: 1rem;
    padding: 1rem 1.5rem;
  }
}
</style>