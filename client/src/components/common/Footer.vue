<template>
  <div class="footer-component">
    <div class="footer-max">
      <div class="footer-content">
        <div class="top-content">
          <div class="left-side">
            <div class="logo-container">
              <router-link class="logo" :to="{ name: 'main' }">
                <img :src="logo" alt="Логотип компании Cube"
                     width="64" height="64">
              </router-link>
            </div>
            <div class="title">
              Магазин упаковки <span style="color: #289646;">КУБ</span>
            </div>
            <div class="copyright top">
              © {{ new Date().getFullYear() }} - cubekazan.ru
            </div>
          </div>
          <div class="right-side">
            <div class="catalog-block">
              <router-link class="subtitle"
                 :to="{ name: 'catalog' }"
                 @click="scrollToZero()"
              >
                Каталог
              </router-link>
              <div class="catalog-items">
                <router-link class="catalog-item"
                   v-for="category in category_list"
                   :key="category.id"
                   :to="{ name: 'catalog-category', params: { categorySlug: category.slug } }"
                   @click="scrollToZero()"
                >
                  {{ category.name }}
                </router-link>
              </div>
            </div>
            <div class="info-block">
              <div class="subtitle">
                Информация
              </div>
              <div class="info-items">
                <router-link :to="{ name: 'delivery' }" class="info-item">Доставка и оплата</router-link>
                <router-link :to="{ name: 'about' }" class="info-item">О магазине</router-link>
                <router-link :to="{ name: 'contacts' }" class="info-item">Контакты</router-link>
                <router-link :to="{ name: 'reviews' }" class="info-item">Отзывы</router-link>
              </div>
            </div>
            <div class="contacts-block">
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
              <div class="developers top">
                <a href="https://vk.com/shemyakin_er" target="_blank">Дизайн - Максим Шемякин</a>
                <a href="https://t.me/OneDudeAdam" target="_blank">Разработка - Вадим Гришин</a>
              </div>
            </div>
          </div>
        </div>
        <div class="bottom-content">
          <div class="barcode">
            <div class="copyright bottom first">
              © {{ new Date().getFullYear() }} - cubekazan.ru
            </div>
            <svg xmlns="http://www.w3.org/2000/svg" width="193" height="34" viewBox="0 0 193 34" fill="none">
              <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M0 1C0 0.447715 0.447716 0 1 0H6.81864C7.37092 0 7.81864 0.447714 7.81864 0.999999V2.86033C7.81864 3.41262 7.37092 3.86033 6.81864 3.86033H4.85266C4.30038 3.86033 3.85266 4.30805 3.85266 4.86033V14.2637C3.85266 14.8159 4.30038 15.2637 4.85266 15.2637H6.81864C7.37092 15.2637 7.81864 15.7114 7.81864 16.2637V17.6879C7.81864 18.2402 7.37092 18.6879 6.81864 18.6879H4.85266C4.30038 18.6879 3.85266 19.1356 3.85266 19.6879V29.1235C3.85266 29.6758 4.30038 30.1235 4.85266 30.1235H6.81864C7.37092 30.1235 7.81864 30.5712 7.81864 31.1235V33C7.81864 33.5523 7.37092 34 6.81864 34H1C0.447715 34 0 33.5523 0 33V1ZM22.7922 1C22.7922 0.447715 22.3445 0 21.7922 0H12.2342C11.6819 0 11.2342 0.447716 11.2342 1V33C11.2342 33.5523 11.6819 34 12.2342 34H13.6498C14.2021 34 14.6498 33.5523 14.6498 33V19.6879C14.6498 19.1356 15.0975 18.6879 15.6498 18.6879H18.3928C18.9451 18.6879 19.3928 19.1356 19.3928 19.6879V33C19.3928 33.5523 19.8405 34 20.3928 34H21.7922C22.3445 34 22.7922 33.5523 22.7922 33V1ZM26.3373 1C26.3373 0.447715 26.785 0 27.3373 0H33.0588C33.6111 0 34.0588 0.447714 34.0588 0.999999V2.86033C34.0588 3.41262 33.6111 3.86033 33.0588 3.86033H31.2062C30.6539 3.86033 30.2062 4.30805 30.2062 4.86033V29.1235C30.2062 29.6758 30.6539 30.1235 31.2062 30.1235H33.0588C33.6111 30.1235 34.0588 30.5712 34.0588 31.1235V33C34.0588 33.5523 33.6111 34 33.0588 34H27.3373C26.785 34 26.3373 33.5523 26.3373 33V1ZM15.6498 3.35962C15.0975 3.35962 14.6498 3.80733 14.6498 4.35962V14.2637C14.6498 14.8159 15.0975 15.2637 15.6498 15.2637H18.3928C18.9451 15.2637 19.3928 14.8159 19.3928 14.2637V4.35962C19.3928 3.80734 18.9451 3.35962 18.3928 3.35962H15.6498Z"
                    fill="#40AB5E"/>
              <path
                  d="M53.9947 1V17V33C53.9947 33.5523 53.547 34 52.9947 34H52.5266H52.0586C51.5063 34 51.0586 33.5523 51.0586 33V17V1C51.0586 0.447715 51.5063 0 52.0586 0H52.5266H52.9947C53.547 0 53.9947 0.447715 53.9947 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M55.4628 17V0.975229C55.4628 0.434707 55.9009 0 56.4415 0C56.982 0 57.4202 0.434262 57.4202 0.974783V17V33.0213C57.4202 33.5618 56.982 34 56.4415 34C55.9009 34 55.4628 33.5618 55.4628 33.0213V17Z"
                  fill="#40AB5E"/>
              <path
                  d="M60.3563 17V0.732784C60.3563 0.327393 60.6849 0 61.0903 0C61.4957 0 61.8243 0.326615 61.8243 0.732006V17V33.266C61.8243 33.6714 61.4957 34 61.0903 34C60.6849 34 60.3563 33.6714 60.3563 33.266V17Z"
                  fill="#40AB5E"/>
              <path
                  d="M68.1859 17V0.732784C68.1859 0.327393 68.5145 0 68.9199 0C69.3253 0 69.6539 0.326615 69.6539 0.732006V17V33.266C69.6539 33.6714 69.3253 34 68.9199 34C68.5145 34 68.1859 33.6714 68.1859 33.266V17Z"
                  fill="#40AB5E"/>
              <path
                  d="M79.4409 1V17V33C79.4409 33.5523 78.9932 34 78.4409 34H76.9942H75.5474C74.9951 34 74.5474 33.5523 74.5474 33V17V1C74.5474 0.447715 74.9951 0 75.5474 0H76.9942H78.4409C78.9932 0 79.4409 0.447715 79.4409 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M83.8451 1V17V33C83.8451 33.5523 83.3974 34 82.8451 34H82.377H81.909C81.3567 34 80.909 33.5523 80.909 33V17V1C80.909 0.447715 81.3567 0 81.909 0H82.377H82.8451C83.3974 0 83.8451 0.447715 83.8451 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M90.2067 1V17V33C90.2067 33.5523 89.7589 34 89.2067 34H88.0046H86.8025C86.2502 34 85.8025 33.5523 85.8025 33V17V1C85.8025 0.447715 86.2502 0 86.8025 0H88.0046H89.2067C89.7589 0 90.2067 0.447715 90.2067 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M95.1002 1V17V33C95.1002 33.5523 94.6525 34 94.1002 34H93.6321H93.1641C92.6118 34 92.1641 33.5523 92.1641 33V17V1C92.1641 0.447715 92.6118 0 93.1641 0H93.6321H94.1002C94.6525 0 95.1002 0.447715 95.1002 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M99.9937 17V0.732784C99.9937 0.327393 100.322 0 100.728 0C101.133 0 101.462 0.328478 101.462 0.73387V17V33.266C101.462 33.6714 101.133 34 100.728 34C100.322 34 99.9937 33.6714 99.9937 33.266V17Z"
                  fill="#40AB5E"/>
              <path
                  d="M102.93 17V0.732783C102.93 0.327392 103.258 0 103.664 0C104.069 0 104.398 0.328477 104.398 0.733868V17V33.266C104.398 33.6714 104.069 34 103.664 34C103.258 34 102.93 33.6714 102.93 33.266V17Z"
                  fill="#40AB5E"/>
              <path
                  d="M110.759 1V17V33C110.759 33.5523 110.312 34 109.759 34H108.557H107.355C106.803 34 106.355 33.5523 106.355 33V17V1C106.355 0.447715 106.803 0 107.355 0H108.557H109.759C110.312 0 110.759 0.447715 110.759 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M118.589 1V17V33C118.589 33.5523 118.141 34 117.589 34H117.121H116.653C116.101 34 115.653 33.5523 115.653 33V17V1C115.653 0.447715 116.101 0 116.653 0H117.121H117.589C118.141 0 118.589 0.447715 118.589 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M120.546 17V0.732788C120.546 0.327395 120.875 0 121.28 0C121.686 0 122.014 0.326616 122.014 0.73201V17V33.266C122.014 33.6714 121.686 34 121.28 34C120.875 34 120.546 33.6714 120.546 33.266V17Z"
                  fill="#40AB5E"/>
              <path
                  d="M129.844 1V17V33C129.844 33.5523 129.396 34 128.844 34H127.397H125.951C125.398 34 124.951 33.5523 124.951 33V17V1C124.951 0.447715 125.398 0 125.951 0H127.397H128.844C129.396 0 129.844 0.447715 129.844 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M136.206 1V17V33C136.206 33.5523 135.758 34 135.206 34H134.493H133.78C133.228 34 132.78 33.5523 132.78 33V17V1C132.78 0.447715 133.228 0 133.78 0H134.493H135.206C135.758 0 136.206 0.447715 136.206 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M137.674 17V0.732781C137.674 0.327392 138.002 0 138.408 0C138.813 0 139.142 0.326613 139.142 0.732003V17V33.266C139.142 33.6714 138.813 34 138.408 34C138.002 34 137.674 33.6714 137.674 33.266V17Z"
                  fill="#40AB5E"/>
              <path
                  d="M146.971 1V17V33C146.971 33.5523 146.524 34 145.971 34H144.769H143.567C143.015 34 142.567 33.5523 142.567 33V17V1C142.567 0.447715 143.015 0 143.567 0H144.769H145.971C146.524 0 146.971 0.447715 146.971 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M153.333 1V17V33C153.333 33.5523 152.885 34 152.333 34H151.865H151.397C150.845 34 150.397 33.5523 150.397 33V17V1C150.397 0.447715 150.845 0 151.397 0H151.865H152.333C152.885 0 153.333 0.447715 153.333 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M158.226 1V17V33C158.226 33.5523 157.779 34 157.226 34H156.514H155.801C155.249 34 154.801 33.5523 154.801 33V17V1C154.801 0.447715 155.249 0 155.801 0H156.514H157.226C157.779 0 158.226 0.447715 158.226 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M166.056 1V17V33C166.056 33.5523 165.608 34 165.056 34H163.609H162.163C161.61 34 161.163 33.5523 161.163 33V17V1C161.163 0.447715 161.61 0 162.163 0H163.609H165.056C165.608 0 166.056 0.447715 166.056 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M169.481 17V0.732788C169.481 0.327395 169.81 0 170.216 0C170.621 0 170.95 0.324684 170.95 0.730077V17V33.266C170.95 33.6714 170.621 34 170.216 34C169.81 34 169.481 33.6714 169.481 33.266V17Z"
                  fill="#40AB5E"/>
              <path
                  d="M177.311 1V17V33C177.311 33.5523 176.863 34 176.311 34H174.864H173.418C172.865 34 172.418 33.5523 172.418 33V17V1C172.418 0.447715 172.865 0 173.418 0H174.864H176.311C176.863 0 177.311 0.447715 177.311 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M181.715 1V17V33C181.715 33.5523 181.268 34 180.715 34H180.247H179.779C179.227 34 178.779 33.5523 178.779 33V17V1C178.779 0.447715 179.227 0 179.779 0H180.247H180.715C181.268 0 181.715 0.447715 181.715 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M188.077 1V17V33C188.077 33.5523 187.629 34 187.077 34H185.875H184.673C184.12 34 183.673 33.5523 183.673 33V17V1C183.673 0.447715 184.12 0 184.673 0H185.875H187.077C187.629 0 188.077 0.447715 188.077 1Z"
                  fill="#40AB5E"/>
              <path
                  d="M192.97 1V17V33C192.97 33.5523 192.523 34 191.97 34H191.258H190.545C189.993 34 189.545 33.5523 189.545 33V17V1C189.545 0.447715 189.993 0 190.545 0H191.258H191.97C192.523 0 192.97 0.447715 192.97 1Z"
                  fill="#40AB5E"/>
            </svg>
          </div>
          <div class="service-block">
            <div class="copyright bottom second">
              © {{ new Date().getFullYear() }} - cubekazan.ru
            </div>
            <router-link class="service-item" :to="{ name: 'policy' }">
              Политика конфиденциальности
            </router-link>
            <router-link class="service-item" :to="{ name: 'terms' }">
              Положения и условия
            </router-link>
          </div>
          <div class="developers bottom">
            <a href="https://vk.com/shemyakin_er" target="_blank">Дизайн - Максим Шемякин</a>
            <a href="https://t.me/OneDudeAdam" target="_blank">Разработка - Вадим Гришин</a>
          </div>
        </div>
      </div>

      <div class="footer-background"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
  inject: ['backendURL', 'frontendURL'],
  props: {
    header_block: Object,
    category_list: Array,
  },
  components: {},
  data() {
    return {
      logo: this.frontendURL + '/images/cube_logo_crop.png'
    }
  },
  mounted() {
  },
  methods: {
    scrollToZero(){
      document.documentElement.scrollTop = 0;
    }
  },
}
</script>


<style scoped>
.footer-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 9rem;

  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.footer-max {
  max-width: 90rem;
  width: 100%;
  position: relative;
  overflow: hidden;
  border-radius: 1.5rem;
  margin-bottom: 1.5rem;
}

.footer-background {
  position: absolute;
  max-width: 90rem;
  width: 100%;
  height: calc(100%);
  border-radius: 1.5rem;
  background: #FFF;
  top: 0;
  z-index: 0;
}

.footer-content {
  padding: 3rem 6.6rem 4.3rem 6.8rem;
  position: relative;
  z-index: 2;

  display: flex;
  flex-direction: column;
  gap: 3rem;
}

.top-content {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.left-side {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  width: 0%;
}

.logo {
  width: 5.4375rem;
  height: 5.4375rem;
  display: flex;
}

.logo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.title {
  font-family: 'Geologica', sans-serif;
  font-size: 1.5rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}

.copyright.top, .copyright.bottom.first {
  display: none;
}

.right-side {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 4rem;
}

.catalog-block, .info-block, .contacts-block {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.subtitle {
  font-size: 1.125rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
  color: #212121;
  text-decoration: none;
}

.catalog-items, .info-items {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.catalog-item, .info-item {
  font-size: 1rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  color: var(--black-55);
  text-decoration: none;
}

.contacts-block {
  gap: 2rem;
  align-items: flex-end;
  margin-left: 6.7rem;
}

.credentials {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.5rem;
}

.credentials a {
  text-decoration: none;
  color: var(--black);
  font-size: 1rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  text-align: right;
}

.out-links {
  display: flex;
  gap: 0.5rem;
}

.bottom-content {
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: space-between;
  gap: 1.5rem;
}

.barcode {
  width: 10.56063rem;
  height: 2.125rem;
  display: flex;
}

.barcode svg {
  width: 100%;
}

.copyright {
  font-size: 1rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  color: var(--black-35);
  white-space: nowrap;
}

.service-block {
  display: flex;
  flex-direction: row;
  gap: 1.5rem;
}

.service-item {
  font-size: 1rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  color: var(--black-35);
  text-decoration: none;
}

.developers {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.5rem;
  white-space: nowrap;
}

.developers a {
  text-decoration: none;
  color: var(--black-35);
  font-size: 0.875rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
}

.developers.top {
  display: none;
}

a {
  transition: opacity 0.2s ease-in-out;
}

a:hover:not(.logo) {
  opacity: 0.5;
}

@media screen and (max-width: 1280px) {
  .footer-component {
    padding-top: 8rem;
  }

  .footer-content {
    padding: 3rem 2.25rem 4rem 2.25rem;
  }

  .top-content {
    gap: 6rem;
  }

  .left-side {
    gap: 1rem;
    width: 13%;
  }

  .logo {
    width: 4.375rem;
    height: 4.375rem;
  }

  .copyright.top {
    margin-top: 0.5rem;
    display: flex;
    font-size: 0.875rem;
  }

  .right-side {
    flex: 1;
  }

  .barcode {
    height: 1.625rem;
    width: 13%;
  }

  .catalog-block {
    width: 33%;
  }

  .contacts-block {
    margin-left: 1rem;
    width: 25%;
  }

  .bottom-content {
    gap: 6rem;
  }

  .copyright.bottom {
    display: none;
  }

  .service-item {
    font-size: 0.875rem;
  }

  .developers {
    flex: 1;
  }

}

@media screen and (max-width: 1000px) {
  .footer-component {
    padding-top: 5rem;
  }

  .footer-max {
    margin-bottom: 1rem;
  }

  .footer-content {
    padding: 2rem 2.25rem 3rem 2.25rem;
    gap: 4rem;
  }

  .top-content {
    flex-direction: column;
    gap: 2rem;
  }

  .left-side {
    width: 100%;
    flex-direction: row;
    align-items: center;
  }

  .logo {
    width: 3rem;
    height: 3rem;
  }

  .title {
    font-size: 1.25rem;
  }

  .copyright.top {
    display: none;
  }

  .right-side {
    gap: 2rem;
  }

  .catalog-block {
    width: unset;
  }

  .contacts-block {
    gap: 1rem;
  }

  .subtitle {
    font-size: 1rem;
  }

  .catalog-item, .info-item, .credentials a, .developers a {
    font-size: 0.75rem;
  }

  .developers.top {
    display: flex;
    margin-top: 1rem;
  }

  .developers.bottom {
    display: none;
  }

  .bottom-content {
    gap: unset;
  }

  .barcode {
    width: unset;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    height: unset ;
  }

  .barcode svg {
    width: 8.5rem;
    height: 1.5rem;
  }

  .copyright.bottom.first {
    display: flex;
    font-size: 0.75rem;
  }

  .service-item {
    font-size: 0.75rem;
  }
}

@media screen and (max-width: 640px) {
  .footer-component {
    padding-top: 4.4rem;
  }

  .footer-content {
    padding: 2rem 2.25rem 4rem 2.25rem;
    gap: 2rem;
  }

  .left-side {
    flex-direction: column;
    gap: 0.5rem;
  }

  .title {
    font-size: 1.1225rem;
  }

  .right-side {
    flex-direction: column;
    gap: 1.5rem;
  }

  .catalog-block, .catalog-items, .info-block, .info-items, .contacts-block, .credentials, .bottom-content,
  .service-block, .developers.bottom {
    align-items: center;
  }

  .contacts-block {
    width: unset;
    margin-left: unset;
  }

  .developers.top {
    display: none;
  }

  .developers.bottom {
    display: flex;
    order: 2;
  }

  .bottom-content {
    flex-direction: column;
    gap: 2rem;
  }

  .barcode {
    order: 3;
    gap: 0.5rem;
  }

  .service-block {
    flex-direction: column;
    order: 1;
    gap: 0.5rem;
  }
}
</style>