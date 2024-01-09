<template>
  <div class="header-container">
    <div class="header-component" id="header-component">
      <div class="flex-row">
        <div class="logo-container">
          <router-link class="logo" :to="{ name: 'main' }">
            <img :src="logo" alt="Логотип компании Cube"
                 width="64" height="64">
          </router-link>
        </div>


        <div class="navigate-links" :class="{ open: isBurgerMenuOpen }">
          <router-link :to="{ name: 'catalog' }" class="menu-item">Каталог</router-link>
          <router-link :to="{ name: 'delivery' }" class="menu-item">Доставка и оплата</router-link>
          <router-link :to="{ name: 'about' }" class="menu-item">О магазине</router-link>
          <router-link :to="{ name: 'contacts' }" class="menu-item">Контакты</router-link>
          <router-link :to="{ name: 'reviews' }" class="menu-item">Отзывы</router-link>
        </div>

        <div class="credentials">
          <a class="phone" :href="'tel:' + header_block.number">{{ number }}</a>
          <a class="address small-text-1" :href="header_block.yandex_map_link" target="_blank">{{ address }}</a>
        </div>

        <router-link class="cart-logo" :to="{ name: 'cart' }" title="Корзина">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path
                d="M1 1.00006L1.5 1V1C1.72586 1.00001 1.83878 1.00001 1.94018 1.00689C3.12785 1.08748 4.15552 1.86267 4.55926 2.98252C4.59373 3.07812 4.62476 3.1867 4.6868 3.40387L4.85714 4.00006M4.85714 4.00006L6.67378 10.3583C7.14917 12.0222 7.38687 12.8541 7.87213 13.4716C8.30044 14.0166 8.86305 14.441 9.50478 14.7031C10.2318 15.0001 11.0971 15.0001 12.8275 15.0001H15.1117C16.8624 15.0001 17.7377 15.0001 18.4706 14.6976C19.1174 14.4307 19.6829 13.9988 20.1106 13.445C20.5953 12.8175 20.8256 11.973 21.2862 10.284L21.3465 10.063C21.9086 8.00171 22.1897 6.97105 21.9513 6.15698C21.7425 5.44374 21.2763 4.8334 20.6432 4.44424C19.9205 4.00006 18.8522 4.00006 16.7156 4.00006H4.85714ZM12 20C12 21.1046 11.1046 22 10 22C8.89543 22 8 21.1046 8 20C8 18.8954 8.89543 18 10 18C11.1046 18 12 18.8954 12 20ZM20 20C20 21.1046 19.1046 22 18 22C16.8954 22 16 21.1046 16 20C16 18.8954 16.8954 18 18 18C19.1046 18 20 18.8954 20 20Z"
                stroke="#40AB5E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </router-link>

        <div class="side-container">
          <div class="burger-menu" @click="toggleBurgerMenu" :class="{ cross: isBurgerMenuOpen }">
            <span></span>
            <span></span>
            <span></span>
            <!--            <div class="background" :class="{ 'dark-background': isBurgerMenuOpen }"></div>-->
          </div>

          <div :class="isBurgerMenuOpen ? 'overlay' : 'overlay-hidden'" @click="toggleBurgerMenu"></div>

          <div class="burger-menu-items" :class="{ open: isBurgerMenuOpen }">
            <div class="side-menu">
              <div class="up-menu">
                <div class="logo-container">
                  <router-link class="logo" :to="{ name: 'main' }">
                    <img :src="backendURL + header_block.logo" alt="Логотип компании Cube"
                         width="64" height="64">
                  </router-link>
                </div>

                <div class="navigate-links">
                  <router-link :to="{ name: 'catalog' }" class="menu-item">Каталог</router-link>
                  <router-link :to="{ name: 'delivery' }" class="menu-item">Доставка и оплата</router-link>
                  <router-link :to="{ name: 'about' }" class="menu-item">О магазине</router-link>
                  <router-link :to="{ name: 'contacts' }" class="menu-item">Контакты</router-link>
                  <router-link :to="{ name: 'reviews' }" class="menu-item">Отзывы</router-link>
                </div>

              </div>

              <div class="down-menu">
                <div class="credentials">
                  <a class="phone" :href="'tel:' + header_block.number">{{ header_block.number }}</a>
                  <a class="mail" :href="'mailto:' + header_block.mail">{{ header_block.mail }}</a>
                  <a class="address" :href="header_block.yandex_map_link" target="_blank">{{ header_block.address }}</a>
                </div>
                <div class="out-links">
                  <a :href="header_block.tg_link" target="_blank" class="out-link">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
                      <path fill-rule="evenodd" clip-rule="evenodd"
                            d="M29.3333 15.9998C29.3333 23.3636 23.3637 29.3332 16 29.3332C8.63619 29.3332 2.66666 23.3636 2.66666 15.9998C2.66666 8.63604 8.63619 2.6665 16 2.6665C23.3637 2.6665 29.3333 8.63604 29.3333 15.9998ZM16.4777 12.5098C15.1809 13.0492 12.589 14.1656 8.70208 15.859C8.0709 16.1101 7.74026 16.3557 7.71016 16.5957C7.6593 17.0016 8.16744 17.1613 8.85939 17.3789C8.95352 17.4085 9.05104 17.4392 9.15102 17.4716C9.83179 17.6929 10.7476 17.9518 11.2236 17.9621C11.6555 17.9714 12.1375 17.7934 12.6696 17.428C16.3013 14.9765 18.176 13.7374 18.2936 13.7106C18.3767 13.6918 18.4917 13.6681 18.5697 13.7374C18.6477 13.8068 18.64 13.938 18.6317 13.9732C18.5815 14.1878 16.5868 16.0422 15.5545 17.0018C15.2328 17.301 15.0045 17.5132 14.9579 17.5617C14.8533 17.6702 14.7468 17.7729 14.6444 17.8716C14.012 18.4813 13.5376 18.9385 14.6707 19.6852C15.2152 20.044 15.6508 20.3406 16.0855 20.6366C16.5601 20.96 17.0336 21.2824 17.6463 21.684C17.8023 21.7862 17.9513 21.8925 18.0965 21.996C18.6489 22.3898 19.1452 22.7437 19.7584 22.6872C20.1147 22.6545 20.4827 22.3194 20.6696 21.3202C21.1113 18.9589 21.9796 13.8425 22.1803 11.7343C22.1979 11.5495 22.1757 11.3131 22.158 11.2094C22.1401 11.1056 22.1031 10.9577 21.9681 10.8483C21.8084 10.7186 21.5619 10.6913 21.4515 10.6932C20.95 10.7021 20.1805 10.9696 16.4777 12.5098Z"
                            fill="#40AB5E"/>
                    </svg>
                  </a>
                  <a :href="header_block.whatsapp_link" target="_blank" class="out-link">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
                      <g clip-path="url(#clip0_391_5858)">
                        <path
                            d="M2.67201 29.3332L4.47467 22.7092C3.28686 20.673 2.6628 18.3572 2.66667 15.9998C2.66667 8.63584 8.63601 2.6665 16 2.6665C23.364 2.6665 29.3333 8.63584 29.3333 15.9998C29.3333 23.3638 23.364 29.3332 16 29.3332C13.6437 29.337 11.3289 28.7134 9.29334 27.5265L2.67201 29.3332ZM11.188 9.74384C11.0158 9.75453 10.8476 9.79988 10.6933 9.87717C10.5487 9.95908 10.4167 10.0615 10.3013 10.1812C10.1413 10.3318 10.0507 10.4625 9.95334 10.5892C9.46056 11.2305 9.19549 12.0177 9.20001 12.8265C9.20267 13.4798 9.37334 14.1158 9.64001 14.7105C10.1853 15.9132 11.0827 17.1865 12.268 18.3665C12.5533 18.6505 12.832 18.9358 13.132 19.2012C14.6032 20.4965 16.3563 21.4306 18.252 21.9292L19.0107 22.0452C19.2573 22.0585 19.504 22.0398 19.752 22.0278C20.1403 22.0078 20.5195 21.9026 20.8627 21.7198C21.084 21.6025 21.188 21.5438 21.3733 21.4265C21.3733 21.4265 21.4307 21.3892 21.54 21.3065C21.72 21.1732 21.8307 21.0785 21.98 20.9225C22.0907 20.8078 22.1867 20.6732 22.26 20.5198C22.364 20.3025 22.468 19.8878 22.5107 19.5425C22.5427 19.2785 22.5333 19.1345 22.5293 19.0452C22.524 18.9025 22.4053 18.7545 22.276 18.6918L21.5 18.3438C21.5 18.3438 20.34 17.8385 19.632 17.5158C19.5574 17.4833 19.4774 17.4648 19.396 17.4612C19.3048 17.4518 19.2126 17.4621 19.1257 17.4913C19.0387 17.5205 18.9591 17.568 18.892 17.6305V17.6278C18.8853 17.6278 18.796 17.7038 17.832 18.8718C17.7767 18.9462 17.7005 19.0024 17.6131 19.0332C17.5257 19.0641 17.4311 19.0683 17.3413 19.0452C17.2545 19.0219 17.1694 18.9925 17.0867 18.9572C16.9213 18.8878 16.864 18.8612 16.7507 18.8118L16.744 18.8092C15.9812 18.4761 15.275 18.0263 14.6507 17.4758C14.4827 17.3292 14.3267 17.1692 14.1667 17.0145C13.6421 16.5122 13.185 15.9439 12.8067 15.3238L12.728 15.1972C12.6715 15.1121 12.6258 15.0202 12.592 14.9238C12.5413 14.7278 12.6733 14.5705 12.6733 14.5705C12.6733 14.5705 12.9973 14.2158 13.148 14.0238C13.2735 13.8643 13.3905 13.6983 13.4987 13.5265C13.656 13.2732 13.7053 13.0132 13.6227 12.8118C13.2493 11.8998 12.8627 10.9918 12.4653 10.0905C12.3867 9.91184 12.1533 9.78384 11.9413 9.7585C11.8693 9.7505 11.7973 9.7425 11.7253 9.73717C11.5463 9.72827 11.3669 9.73139 11.188 9.74384Z"
                            fill="#40AB5E"/>
                      </g>
                      <defs>
                        <clipPath id="clip0_391_5858">
                          <rect width="32" height="32" fill="white"/>
                        </clipPath>
                      </defs>
                    </svg>
                  </a>
                </div>
                <div class="copyright">
                  © {{ new Date().getFullYear() }} - cubekazan.ru
                </div>
              </div>

            </div>
          </div>
        </div>


      </div>
    </div>
  </div>
</template>

<script>
import debounce from 'lodash';

export default {
  name: "Header",
  props: {
    header_block: Object,
  },
  inject: ['backendURL', 'frontendURL'],
  components: {},
  data() {
    return {
      isHidden: false,
      isBurgerMenuOpen: false,
      logo: this.frontendURL + '/images/cube_logo_crop.png',
      number: '+7 995 007-16-54',
      address: 'г. Казань, Чистопольская, 7'
    }
  },
  mounted() {
    const debouncedScrollHandler = debounce.debounce(this.handleScroll, 50);

    window.addEventListener('scroll', debouncedScrollHandler);
    window.addEventListener('resize', this.updateWindowWidth);
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
    window.addEventListener('resize', this.updateWindowWidth);
  },

  watch: {
    header_block(newVal){
      // this.logo = this.backendURL + newVal.logo
      this.number = newVal.number
      this.address = newVal.address
    }
  },

  methods: {
    adjustBodyOverflow() {
      if (this.isBurgerMenuOpen) {
        document.body.style.overflow = "hidden";
      } else {
        document.body.style.overflow = "";
      }
    },

    updateWindowWidth() {
      if (window.innerWidth > 1000) {
        this.isBurgerMenuOpen = false
        document.body.style.overflow = "";
      }
    },

    toggleBurgerMenu() {
      this.isBurgerMenuOpen = !this.isBurgerMenuOpen;
      if (this.isBurgerMenuOpen) {
        document.body.style.overflow = "hidden";
      } else {
        document.body.style.overflow = "";
      }
    },

    handleScroll() {
      // Shadow on header-component on scroll
      let header_component = document.getElementById("header-component")
      if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        header_component.style.boxShadow = "0px 5px 10px 0px rgba(0, 0, 0, 0.25), 0px 1px 5px 0px rgba(0, 0, 0, 0.25)";
      } else {
        header_component.style.boxShadow = "unset";
      }
    },
  },
}
</script>


<style scoped>
.header-container {
  width: 100%;
  position: fixed;
  z-index: 101;
}

.header-component {
  max-width: calc(90rem - 6.875rem * 2);
  margin-left: auto;
  margin-right: auto;
  margin-top: 1rem;

  display: flex;
  padding: 1.5rem 6.875rem;
  justify-content: space-between;
  align-items: center;

  background: var(--white);
  border-radius: 1.5rem;
  transition: all 0.2s ease-in-out;
}

.flex-row {
  display: flex;
  align-items: center
}

.header-component .flex-row {
  justify-content: space-between;
  width: 100%;
}

.logo {
  display: flex;
  align-items: center;
  margin-right: 2rem;
}

.navigate-links {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 2rem;
  position: relative;
  flex: 1;
}

.menu-item {
  text-decoration: none;
  color: var(--black);
  font-weight: 400;
  cursor: pointer;
  position: relative;
  opacity: 1;
  transition: opacity 0.2s ease-in-out;
  user-select: none;
  z-index: 5;
}

.menu-item:hover {
  opacity: 0.5;
}

.credentials {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.25rem;
}

.phone, .address, .mail {
  color: var(--black-55);
}

.phone, .address, .mail {
  text-decoration: none;
  cursor: pointer;
  transition: opacity 0.2s ease-in-out;
}

.phone:hover, .address:hover, .mail:hover {
  opacity: 0.5;
}

.cart-logo {
  width: 3.25rem;
  height: 3.25rem;
  margin-left: 1.5rem;
  background-color: #D9E9DE;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: opacity 0.2s ease-in-out;
}

.cart-logo svg {
  margin-left: -0.1rem;
  margin-bottom: -0.1rem;
}

.cart-logo:hover {
  opacity: 0.5;
}

.side-container {
  display: none;
  flex-direction: row;
  align-items: center;
  gap: 2.5rem;
  height: 3.25rem;
  width: 3.25rem;
  margin-left: 1rem;

}

.tablet-size {
  display: none;
}

.burger-menu {
  display: none;
  flex-direction: column;
  justify-content: space-around;
  width: 20px;
  height: 20px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  background-color: #D9E9DE;
  border-radius: 50%;
  padding: 1rem;
}

.burger-menu:hover {
  opacity: 0.5;
}

.burger-menu span {
  width: 100%;
  height: 2px;
  background-color: var(--green-light);
  transition: 0.3s;
  z-index: 1;
}

.burger-menu.cross {
  z-index: 1001;
  position: absolute;
  right: 1rem;
}

.burger-menu.cross:hover span {
  background-color: #DD1D1D;
}

.burger-menu.cross span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.burger-menu.cross span:nth-child(2) {
  opacity: 0;
}

.burger-menu.cross span:nth-child(3) {
  transform: translateY(-5px) rotate(-45deg);
}

.background {
  z-index: 0;
  width: 2.25rem;
  height: 2.25rem;
  background: white;
  position: absolute;
  top: 50%;
  transform: translate(-23%, -50%);
}

.overlay-hidden {
  display: none;
}

.overlay {
  display: block;
  position: fixed;
  height: 100vh;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 999;
}

.burger-menu-items {
  display: flex;
  position: fixed;
  top: 0;
  right: 0;
  width: 70%;
  max-width: 300px;
  height: 100vh;
  background-color: white;
  border-radius: 1.5rem 0rem 0rem 1.5rem;
  flex-direction: column;
  gap: 10%;
  padding: 2rem 2.25rem 4rem 3rem;
  z-index: 1000;
  overflow-y: auto;
  transform: translateX(100%);
  transition: transform 0.3s ease;
}

.burger-menu-items.open {
  transform: translateX(0);
}

.side-menu {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

@media screen and (max-width: 1460px) {
  .header-component {
    margin-top: 0 !important;
    border-radius: unset;
  }
}

@media screen and (max-width: 1280px) {
  .header-component {
    padding: 1.5rem 2.5rem;
  }

  .menu-item {
    font-size: 1rem;
  }

  .phone {
    font-size: 1rem;
  }

  .navigate-links {
    gap: 1.5rem;
  }

}

@media screen and (max-width: 1000px) {
  .header-component {
    margin-top: 0.5rem;
  }

  .logo-container {
    flex: 1;
    display: flex;
  }

  .logo img {
    width: 3.25rem;
    height: 3.25rem;
  }

  .navigate-links {
    display: none;
  }

  .side-container {
    display: flex;
  }

  .burger-menu {
    display: flex;
  }

  .burger-menu-items {
    height: calc(100% - 2rem - 4rem);
  }

  .side-menu {
    justify-content: space-between;
    height: 100%;
  }

  .side-menu .logo-container {
    margin-bottom: 3rem;
  }

  .side-container .navigate-links {
    display: flex;
    flex-direction: column;
    align-items: start;
    gap: 1rem;
    font-family: 'Geologica', sans-serif;

    font-style: normal;
    font-weight: 500;
    line-height: normal;
  }

  .menu-item {
    font-size: 1.25rem;
  }

  .side-menu .credentials {
    align-items: flex-start;
    gap: 0.5rem;
  }

  .down-menu {
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  .side-menu .phone, .side-menu .address, .side-menu .mail {
    color: var(--black);
  }

  .out-links {
    display: flex;
    flex-direction: row;
    gap: 0.5rem;
  }

  .out-link {
    transition: opacity 0.2s ease-in-out;
  }

  .out-link:hover {
    opacity: 0.5;
  }

  .copyright {
    color: var(--black-35, #B3B3B3);
    font-family: 'Onest', sans-serif;
    font-size: 1rem;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    margin-top: 1rem;
  }

  .burger-menu.cross span:nth-child(3) {
    transform: translateY(-7px) rotate(-45deg);
  }

}

@media screen and (max-width: 640px) {
  .credentials {
    display: none;
  }

  .side-menu .credentials {
    display: flex;
  }

  .header-component {
    padding: 1rem 1.25rem;
  }

  .side-menu .logo-container {
    margin-bottom: 2rem;
  }

  .logo img, .cart-logo, .side-container {
    width: 3rem;
    height: 3rem;
  }

  .burger-menu {
    height: 16px;
  }

  .burger-menu-items {
    padding: 1.5rem 1.25rem 3rem 2rem;
    height: calc(100% - 1.5rem - 3rem);
  }

  .side-container {
    margin-left: 0.5rem;
  }

  .menu-item {
    font-size: 1.125rem;
  }

  .down-menu {
    gap: 1rem;
  }

  .side-menu .phone, .side-menu .address, .side-menu .mail {
    font-size: 0.75rem;
  }

  .copyright {
    font-size: 0.75rem;
  }

  .burger-menu.cross span:nth-child(1) {
    transform: translateY(5px) rotate(45deg);
  }

  .burger-menu.cross span:nth-child(3) {
    transform: translateY(-5px) rotate(-45deg);
  }

  .cross {
    width: 1rem;
  }

}
</style>