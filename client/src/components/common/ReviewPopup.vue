<template>
  <div v-if="isVisible" class="popup-overlay" @click.self="close">
    <div class="popup">
      <button class="close-button" @click="close">×</button>
      <div class="image-container">
        <img :src="reviewOriginalLink" alt="" loading="lazy">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewPopup",
  props: {
    isVisible: Boolean,
    reviewOriginalLink: String
  },
  methods: {
    close() {

      this.$emit('close');
    }
  }
}
</script>

<style scoped>
.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.popup {
  background: white;
  padding: 4rem;
  border-radius: 24px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 26rem;
}

.close-button {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  border: none;
  background: none;
  font-size: 2.5rem;
  cursor: pointer;
  color: var(--green-light);
  border-radius: 50%;
  transition: all 0.3s ease-in-out;
  width: 3rem;
  height: 3rem;
}

.close-button:hover {
  opacity: 0.5;
}

.image-container {

}

.image-container img {
  width: 100%;
  object-fit: contain;
}

@media screen and (max-width: 1280px) {

}

@media screen and (max-width: 1000px) {

}

@media screen and (max-width: 640px) {
  .popup {
    max-width: 18rem;
    padding: 2rem;
  }
}

</style>
