<template>
  <div class="contacts-component" :class="separate ? 'zero-top-padding': ''">
    <div class="contacts-max">
      <div class="map">
        <iframe
            src="https://yandex.ru/map-widget/v1/?um=constructor%3Ae40b59d86c82e85e8070761d3edbc55814dd9837ec655d232d40988fddf26e04&amp;source=constructor"
            width="1220" height="480" frameborder="0"></iframe>
      </div>
      <div class="contacts-content">
        <div class="left-side">
          <h2 v-html="contacts_block.title"></h2>
          <div class="social-links top">
            <a class="telegram-link" :href="contacts_block.tg_link" target="_blank">
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
                <path fill-rule="evenodd" clip-rule="evenodd"
                      d="M29.3334 15.9998C29.3334 23.3636 23.3638 29.3332 16.0001 29.3332C8.63628 29.3332 2.66675 23.3636 2.66675 15.9998C2.66675 8.63604 8.63628 2.6665 16.0001 2.6665C23.3638 2.6665 29.3334 8.63604 29.3334 15.9998ZM16.4778 12.5098C15.181 13.0492 12.5891 14.1656 8.70217 15.859C8.07099 16.1101 7.74035 16.3557 7.71025 16.5957C7.65939 17.0016 8.16753 17.1613 8.85948 17.3789C8.95361 17.4085 9.05113 17.4392 9.15111 17.4716C9.83188 17.6929 10.7477 17.9518 11.2237 17.9621C11.6556 17.9714 12.1375 17.7934 12.6697 17.428C16.3014 14.9765 18.1761 13.7374 18.2937 13.7106C18.3767 13.6918 18.4918 13.6681 18.5698 13.7374C18.6478 13.8068 18.6401 13.938 18.6318 13.9732C18.5815 14.1878 16.5869 16.0422 15.5546 17.0018C15.2329 17.301 15.0046 17.5132 14.9579 17.5617C14.8534 17.6702 14.7469 17.7729 14.6445 17.8716C14.0121 18.4813 13.5377 18.9385 14.6707 19.6852C15.2153 20.044 15.6509 20.3406 16.0855 20.6366C16.5602 20.96 17.0337 21.2824 17.6463 21.684C17.8023 21.7862 17.9514 21.8925 18.0966 21.996C18.649 22.3898 19.1453 22.7437 19.7585 22.6872C20.1147 22.6545 20.4827 22.3194 20.6697 21.3202C21.1114 18.9589 21.9797 13.8425 22.1803 11.7343C22.1979 11.5495 22.1758 11.3131 22.1581 11.2094C22.1402 11.1056 22.1031 10.9577 21.9682 10.8483C21.8085 10.7186 21.5619 10.6913 21.4515 10.6932C20.9501 10.7021 20.1806 10.9696 16.4778 12.5098Z"
                      fill="#40AB5E"/>
              </svg>
              Telegram
            </a>
            <a class="vk-link" :href="contacts_block.vk_link" target="_blank">
              <div id="vk-link">
                <svg viewBox="4 7.6 13.84 8.84" xmlns="http://www.w3.org/2000/svg">
                  <path d="M4 7.6C4.12 13.12 6.88 16.44 11.72 16.44V13.28C13.48 13.46 14.8 14.72 15.34 16.44H17.84C17.15 13.93 15.34 12.55 14.21 12.02C15.34 11.37 16.93 9.78 17.31 7.6H15.04C14.54 9.38 13.06 10.97 11.72 11.12V7.6H9.45V13.77C8.09 13.43 6.37 11.72 6.29 7.6H4Z" fill="white"/>
                </svg>
              </div>
              ВКонтакте
            </a>
            <a class="whatsapp-link" :href="contacts_block.whatsapp_link" target="_blank">
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
                <g clip-path="url(#clip0_210_806)">
                  <path
                      d="M2.6721 29.3332L4.47477 22.7092C3.28695 20.673 2.66289 18.3572 2.66677 15.9998C2.66677 8.63584 8.6361 2.6665 16.0001 2.6665C23.3641 2.6665 29.3334 8.63584 29.3334 15.9998C29.3334 23.3638 23.3641 29.3332 16.0001 29.3332C13.6438 29.337 11.329 28.7134 9.29343 27.5265L2.6721 29.3332ZM11.1881 9.74384C11.0159 9.75453 10.8477 9.79988 10.6934 9.87717C10.5488 9.95908 10.4168 10.0615 10.3014 10.1812C10.1414 10.3318 10.0508 10.4625 9.95343 10.5892C9.46065 11.2305 9.19558 12.0177 9.2001 12.8265C9.20277 13.4798 9.37343 14.1158 9.6401 14.7105C10.1854 15.9132 11.0828 17.1865 12.2681 18.3665C12.5534 18.6505 12.8321 18.9358 13.1321 19.2012C14.6033 20.4965 16.3564 21.4306 18.2521 21.9292L19.0108 22.0452C19.2574 22.0585 19.5041 22.0398 19.7521 22.0278C20.1404 22.0078 20.5196 21.9026 20.8628 21.7198C21.0841 21.6025 21.1881 21.5438 21.3734 21.4265C21.3734 21.4265 21.4308 21.3892 21.5401 21.3065C21.7201 21.1732 21.8308 21.0785 21.9801 20.9225C22.0908 20.8078 22.1868 20.6732 22.2601 20.5198C22.3641 20.3025 22.4681 19.8878 22.5108 19.5425C22.5428 19.2785 22.5334 19.1345 22.5294 19.0452C22.5241 18.9025 22.4054 18.7545 22.2761 18.6918L21.5001 18.3438C21.5001 18.3438 20.3401 17.8385 19.6321 17.5158C19.5575 17.4833 19.4775 17.4648 19.3961 17.4612C19.3049 17.4518 19.2127 17.4621 19.1258 17.4913C19.0388 17.5205 18.9592 17.568 18.8921 17.6305V17.6278C18.8854 17.6278 18.7961 17.7038 17.8321 18.8718C17.7768 18.9462 17.7006 19.0024 17.6132 19.0332C17.5258 19.0641 17.4312 19.0683 17.3414 19.0452C17.2546 19.0219 17.1695 18.9925 17.0868 18.9572C16.9214 18.8878 16.8641 18.8612 16.7508 18.8118L16.7441 18.8092C15.9813 18.4761 15.2751 18.0263 14.6508 17.4758C14.4828 17.3292 14.3268 17.1692 14.1668 17.0145C13.6422 16.5122 13.1851 15.9439 12.8068 15.3238L12.7281 15.1972C12.6716 15.1121 12.6259 15.0202 12.5921 14.9238C12.5414 14.7278 12.6734 14.5705 12.6734 14.5705C12.6734 14.5705 12.9974 14.2158 13.1481 14.0238C13.2736 13.8643 13.3906 13.6983 13.4988 13.5265C13.6561 13.2732 13.7054 13.0132 13.6228 12.8118C13.2494 11.8998 12.8628 10.9918 12.4654 10.0905C12.3868 9.91184 12.1534 9.78384 11.9414 9.7585C11.8694 9.7505 11.7974 9.7425 11.7254 9.73717C11.5464 9.72827 11.3669 9.73139 11.1881 9.74384Z"
                      fill="#40AB5E"/>
                </g>
                <defs>
                  <clipPath id="clip0_210_806">
                    <rect width="32" height="32" fill="white"/>
                  </clipPath>
                </defs>
              </svg>
              What'sApp
            </a>
            <a class="max-link" :href="contacts_block.max_link" target="_blank">
              <div id="max-link">
                <svg viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg">
                  <path fill="white" fill-rule="evenodd" clip-rule="evenodd"
                    d="M508.211 878.328c-75.007 0-109.864-10.95-170.453-54.75-38.325 49.275-159.686 87.783-164.979 21.9 0-49.456-10.95-91.248-23.36-136.873-14.782-56.21-31.572-118.807-31.572-209.508 0-216.626 177.754-379.597 388.357-379.597 210.785 0 375.947 171.001 375.947 381.604.707 207.346-166.595 376.118-373.94 377.224m3.103-571.585c-102.564-5.292-182.499 65.7-200.201 177.024-14.6 92.162 11.315 204.398 33.397 210.238 10.585 2.555 37.23-18.98 53.837-35.587a189.8 189.8 0 0 0 92.71 33.032c106.273 5.112 197.08-75.794 204.215-181.95 4.154-106.382-77.67-196.486-183.958-202.574Z"/>
                </svg>
              </div>
              MAX
            </a>
          </div>
        </div>
        <div class="right-side">
          <div class="schedule">
            <div class="title">
              График работы
            </div>
            <div class="schedule-content">
              <div class="subtitle">ПН-ПТ</div>
              <div class="schedule-item">{{ contacts_block.monday_friday_schedule }}</div>
              <div class="subtitle">СБ</div>
              <div class="schedule-item">{{ contacts_block.sunday_schedule }}</div>
              <div class="subtitle">ВС</div>
              <div class="schedule-item">{{ contacts_block.dinner_schedule }}</div>
            </div>
          </div>
          <div class="contacts">
            <div class="title">
              Контакты
            </div>
            <div class="contacts-items">
              <a :href="'tel:' + contacts_block.number" class="phone">{{ contacts_block.number }}</a>
              <a :href="'mailto:' + contacts_block.mail" class="mail">{{ contacts_block.mail }}</a>
            </div>
          </div>
        </div>
        <div class="social-links bottom">
          <a class="telegram-link" :href="contacts_block.tg_link" target="_blank">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
              <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M29.3334 15.9998C29.3334 23.3636 23.3638 29.3332 16.0001 29.3332C8.63628 29.3332 2.66675 23.3636 2.66675 15.9998C2.66675 8.63604 8.63628 2.6665 16.0001 2.6665C23.3638 2.6665 29.3334 8.63604 29.3334 15.9998ZM16.4778 12.5098C15.181 13.0492 12.5891 14.1656 8.70217 15.859C8.07099 16.1101 7.74035 16.3557 7.71025 16.5957C7.65939 17.0016 8.16753 17.1613 8.85948 17.3789C8.95361 17.4085 9.05113 17.4392 9.15111 17.4716C9.83188 17.6929 10.7477 17.9518 11.2237 17.9621C11.6556 17.9714 12.1375 17.7934 12.6697 17.428C16.3014 14.9765 18.1761 13.7374 18.2937 13.7106C18.3767 13.6918 18.4918 13.6681 18.5698 13.7374C18.6478 13.8068 18.6401 13.938 18.6318 13.9732C18.5815 14.1878 16.5869 16.0422 15.5546 17.0018C15.2329 17.301 15.0046 17.5132 14.9579 17.5617C14.8534 17.6702 14.7469 17.7729 14.6445 17.8716C14.0121 18.4813 13.5377 18.9385 14.6707 19.6852C15.2153 20.044 15.6509 20.3406 16.0855 20.6366C16.5602 20.96 17.0337 21.2824 17.6463 21.684C17.8023 21.7862 17.9514 21.8925 18.0966 21.996C18.649 22.3898 19.1453 22.7437 19.7585 22.6872C20.1147 22.6545 20.4827 22.3194 20.6697 21.3202C21.1114 18.9589 21.9797 13.8425 22.1803 11.7343C22.1979 11.5495 22.1758 11.3131 22.1581 11.2094C22.1402 11.1056 22.1031 10.9577 21.9682 10.8483C21.8085 10.7186 21.5619 10.6913 21.4515 10.6932C20.9501 10.7021 20.1806 10.9696 16.4778 12.5098Z"
                    fill="#40AB5E"/>
            </svg>
            Telegram
          </a>
          <a class="vk-link" :href="contacts_block.vk_link" target="_blank">
            <div id="vk-link">
              <svg viewBox="4 7.6 13.84 8.84" xmlns="http://www.w3.org/2000/svg">
                <path d="M4 7.6C4.12 13.12 6.88 16.44 11.72 16.44V13.28C13.48 13.46 14.8 14.72 15.34 16.44H17.84C17.15 13.93 15.34 12.55 14.21 12.02C15.34 11.37 16.93 9.78 17.31 7.6H15.04C14.54 9.38 13.06 10.97 11.72 11.12V7.6H9.45V13.77C8.09 13.43 6.37 11.72 6.29 7.6H4Z" fill="white"/>
              </svg>
            </div>
            ВКонтакте
          </a>
          <a class="whatsapp-link" :href="contacts_block.whatsapp_link" target="_blank">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
              <g clip-path="url(#clip0_210_806)">
                <path
                    d="M2.6721 29.3332L4.47477 22.7092C3.28695 20.673 2.66289 18.3572 2.66677 15.9998C2.66677 8.63584 8.6361 2.6665 16.0001 2.6665C23.3641 2.6665 29.3334 8.63584 29.3334 15.9998C29.3334 23.3638 23.3641 29.3332 16.0001 29.3332C13.6438 29.337 11.329 28.7134 9.29343 27.5265L2.6721 29.3332ZM11.1881 9.74384C11.0159 9.75453 10.8477 9.79988 10.6934 9.87717C10.5488 9.95908 10.4168 10.0615 10.3014 10.1812C10.1414 10.3318 10.0508 10.4625 9.95343 10.5892C9.46065 11.2305 9.19558 12.0177 9.2001 12.8265C9.20277 13.4798 9.37343 14.1158 9.6401 14.7105C10.1854 15.9132 11.0828 17.1865 12.2681 18.3665C12.5534 18.6505 12.8321 18.9358 13.1321 19.2012C14.6033 20.4965 16.3564 21.4306 18.2521 21.9292L19.0108 22.0452C19.2574 22.0585 19.5041 22.0398 19.7521 22.0278C20.1404 22.0078 20.5196 21.9026 20.8628 21.7198C21.0841 21.6025 21.1881 21.5438 21.3734 21.4265C21.3734 21.4265 21.4308 21.3892 21.5401 21.3065C21.7201 21.1732 21.8308 21.0785 21.9801 20.9225C22.0908 20.8078 22.1868 20.6732 22.2601 20.5198C22.3641 20.3025 22.4681 19.8878 22.5108 19.5425C22.5428 19.2785 22.5334 19.1345 22.5294 19.0452C22.5241 18.9025 22.4054 18.7545 22.2761 18.6918L21.5001 18.3438C21.5001 18.3438 20.3401 17.8385 19.6321 17.5158C19.5575 17.4833 19.4775 17.4648 19.3961 17.4612C19.3049 17.4518 19.2127 17.4621 19.1258 17.4913C19.0388 17.5205 18.9592 17.568 18.8921 17.6305V17.6278C18.8854 17.6278 18.7961 17.7038 17.8321 18.8718C17.7768 18.9462 17.7006 19.0024 17.6132 19.0332C17.5258 19.0641 17.4312 19.0683 17.3414 19.0452C17.2546 19.0219 17.1695 18.9925 17.0868 18.9572C16.9214 18.8878 16.8641 18.8612 16.7508 18.8118L16.7441 18.8092C15.9813 18.4761 15.2751 18.0263 14.6508 17.4758C14.4828 17.3292 14.3268 17.1692 14.1668 17.0145C13.6422 16.5122 13.1851 15.9439 12.8068 15.3238L12.7281 15.1972C12.6716 15.1121 12.6259 15.0202 12.5921 14.9238C12.5414 14.7278 12.6734 14.5705 12.6734 14.5705C12.6734 14.5705 12.9974 14.2158 13.1481 14.0238C13.2736 13.8643 13.3906 13.6983 13.4988 13.5265C13.6561 13.2732 13.7054 13.0132 13.6228 12.8118C13.2494 11.8998 12.8628 10.9918 12.4654 10.0905C12.3868 9.91184 12.1534 9.78384 11.9414 9.7585C11.8694 9.7505 11.7974 9.7425 11.7254 9.73717C11.5464 9.72827 11.3669 9.73139 11.1881 9.74384Z"
                    fill="#40AB5E"/>
              </g>
              <defs>
                <clipPath id="clip0_210_806">
                  <rect width="32" height="32" fill="white"/>
                </clipPath>
              </defs>
            </svg>
            What'sApp
          </a>
          <a class="max-link" :href="contacts_block.max_link" target="_blank">
            <div id="max-link">
              <svg viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg">
                <path fill="white" fill-rule="evenodd" clip-rule="evenodd"
                  d="M508.211 878.328c-75.007 0-109.864-10.95-170.453-54.75-38.325 49.275-159.686 87.783-164.979 21.9 0-49.456-10.95-91.248-23.36-136.873-14.782-56.21-31.572-118.807-31.572-209.508 0-216.626 177.754-379.597 388.357-379.597 210.785 0 375.947 171.001 375.947 381.604.707 207.346-166.595 376.118-373.94 377.224m3.103-571.585c-102.564-5.292-182.499 65.7-200.201 177.024-14.6 92.162 11.315 204.398 33.397 210.238 10.585 2.555 37.23-18.98 53.837-35.587a189.8 189.8 0 0 0 92.71 33.032c106.273 5.112 197.08-75.794 204.215-181.95 4.154-106.382-77.67-196.486-183.958-202.574Z"/>
              </svg>
            </div>
            MAX
          </a>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "Contacts",
  props: {
    contacts_block: Object,
    separate: {
      type: Boolean,
      default: false
    }
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
.contacts-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 9rem;

  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.zero-top-padding {
  padding-top: 0!important;
}

.contacts-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.map iframe {
  border-radius: 1rem;

  width: 100%;
  height: 29.9375rem;
}

.contacts-content {
  border-radius: 1.5rem;
  background: #FFF;

  padding: 4rem 4rem 5rem 4rem;
  display: flex;
  flex-direction: row;
  gap: 1.5rem;
}

.social-links.bottom {
  display: none;
}

.left-side {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  flex-basis: 50%;
}

.social-links {
  display: flex;
  flex-direction: row;
  gap: 1rem;
}

.telegram-link, .vk-link, .whatsapp-link, .max-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
  color: var(--black-55);
}

#vk-link, #max-link {
  background: #40AB5E;
  border-radius: 50%;
  height: 26.67px;
  width: 26.67px;
  display: grid;
  place-items: center;
  margin: 3px 2px 2px 2px;
}

#vk-link svg{
  width: 15px;
  height: 10px;
  display: block;
}


#max-link svg {
  width: 70%;
  height: 70%;
  display: block;
}

.right-side {
  display: flex;
  flex-basis: 50%;
}

.title {
  font-size: 1.5rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}

.schedule {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.schedule-content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 0.5rem 0;
}

.subtitle {
  font-size: 1.125rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  color: var(--black-55);
}

.contacts {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.contacts-items {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.phone, .mail {
  text-decoration: none;
  color: var(--black);
}

a {
  transition: opacity 0.2s ease-in-out;
}

a:hover {
  opacity: 0.5;
}

@media screen and (max-width: 1280px) {
  .contacts-component {
    padding-top: 8rem;
  }

  .contacts-max {
    padding: 0 2.25rem;
  }

  .contacts-content {
    padding: 3rem 7rem 4rem 3rem;
    justify-content: space-between;
  }

  .left-side {
    flex: unset;
    justify-content: space-between;
  }

  h2 {
    width: 80%;
  }

  .right-side {
    flex-direction: column;
    gap: 2rem;
    flex: unset;
  }

  .title, .subtitle {
    font-size: 1.125rem;
  }

  .schedule, .contacts {
    gap: 1rem;
  }

  .schedule-content {
    grid-template-columns: 1fr 1fr;
  }
}

@media screen and (max-width: 1000px) {
  .contacts-max {
    padding: 0;
  }

  .contacts-component {
    padding-top: 5rem;
  }

  .contacts-content {
    padding: 3rem 4.5rem 4rem 2.25rem;
  }

  h2 {
    width: 70%;
  }

  .social-links {
    font-size: 0.75rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.5rem 1rem;
    width: 80%;
  }

  .title, .subtitle {
    font-size: 1rem;
  }

  .schedule-content {
    gap: 0.5rem 0.9375rem;
    grid-template-columns: 1fr 2fr;
  }
}

@media screen and (max-width: 640px) {
  .contacts-component {
    padding-top: 4.4rem;
  }

  .contacts-max {
    gap: 0.5rem;
  }

  .contacts-content {
    padding: 2rem 4.5rem 3rem 4.5rem;
    flex-direction: column;
    gap: 1.5rem;
  }

  .left-side {
    align-items: center;
  }

  h2 {
    width: 43vw;
    text-align: center;
  }

  .social-links.top {
    display: none;
  }

  .social-links.bottom {
    display: grid;
    width: fit-content;
    gap: 0.5rem 2rem;
    margin: 0 auto;

  }

  .social-links.bottom > a {
    width: fit-content;

  }

  .schedule, .contacts {
    align-items: center;
  }

  .schedule-content {
    grid-template-columns: 1fr 1fr;
  }

  .subtitle {
    font-size: 0.875rem;
  }

  .phone, .mail {
    text-align: center;
  }
}

@media screen and (max-width: 400px) {
  h2 {
    width: 50vw;
  }
}

@media screen and (max-width: 360px) {
  .social-links {
    grid-template-columns: 1fr;
  }
}
</style>