<template>
  <div v-if="isVisible" class="popup-overlay" @click.self="close">
    <div class="popup">
      <button class="close-button" @click="close">×</button>
      <div class="popup-icon">
        <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="100" height="100" viewBox="0,0,256,256">
          <g fill="#ffffff" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt"
             stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none"
             font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal">
            <g transform="scale(3.55556,3.55556)">
              <path
                  d="M57.658,12.643c1.854,1.201 2.384,3.678 1.183,5.532l-25.915,40c-0.682,1.051 -1.815,1.723 -3.064,1.814c-0.098,0.008 -0.197,0.011 -0.294,0.011c-1.146,0 -2.241,-0.491 -3.003,-1.358l-13.051,-14.835c-1.459,-1.659 -1.298,-4.186 0.36,-5.646c1.662,-1.46 4.188,-1.296 5.646,0.361l9.563,10.87l23.043,-35.567c1.203,-1.854 3.68,-2.383 5.532,-1.182z"></path>
            </g>
          </g>
        </svg>
      </div>
      <h2>Товар успешно добавлен в корзину!</h2>
      <div class="buttons">
        <div class="button secondary" @click="close">Продолжить выбор</div>
        <router-link class="button primary" :to="{ name: 'cart' }">Перейти в корзину</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SuccessPopUp",
  props: {
    isVisible: Boolean,
    product: {
      type: Object
    }
  },
  methods: {
    close() {
      // let html = document.getElementsByTagName('html')[0]
      // html.style.overflow = ""
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
  max-width: 35rem;
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

.popup-icon {
  display: flex;
  border-radius: 50%;
  border: white 8px solid;
  background-color: var(--green-light);
  justify-content: center;
  box-shadow: 0 1px 2px 0 rgba(16, 24, 40, 0.05), 0 0 32px 16px #4edb66;;
}

.popup-icon svg {
  width: 50%;
  height: 70px;
}

h2 {
  margin-top: 4rem;
  font-weight: 600;
  font-size: 2rem;
}

h2, p {
  text-align: center;
}

.buttons {
  margin-top: 3rem;
  display: flex;
  flex-direction: row;
  gap: 1rem;
}

.button {
  display: flex;
  padding: 1rem 1.5rem;
  justify-content: center;
  align-items: center;
  align-self: stretch;
  border-radius: 0.5rem;

  user-select: none;
  text-decoration: none;
  cursor: pointer;
  transition: opacity 0.2s ease-in-out;
}

.button:hover {
  opacity: 0.5;
}

.button.primary {
  background: var(--green-light, #40AB5E);
  color: white;
}

.button.secondary {
  border: 3px var(--green-light, #40AB5E) solid;
  color: var(--green-light);
}


@media screen and (max-width: 1280px) {

}

@media screen and (max-width: 1000px) {
  .popup {
    max-width: 26rem;
  }
}

@media screen and (max-width: 640px) {
  .popup {
    max-width: 18rem;
    padding: 4rem 3rem;
  }

  h2 {
    font-size: 1.5rem;
    margin-top: 3rem;
  }

  .buttons {
    flex-direction: column;
    margin-top: 1.5rem;
    gap: 0.5rem;
    width: 100%;
  }

  .button {
    align-items: center;
  }
}

</style>
