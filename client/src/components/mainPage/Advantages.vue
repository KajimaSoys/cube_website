<template>
  <div class="advantages-component">
    <div class="advantages-max">
      <h2 class="advantages-head" v-html="advantages_block.title"></h2>
      <div class="advantages-content">
        <div class="card odd">
          <h3 class="card-title" v-html="advantages_block.subtitle_first"></h3>
          <div class="card-bottom-container">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
              <rect width="48" height="48" rx="16" fill="white"/>
              <rect x="21.75" y="30.75" width="11.25" height="10.5" rx="2" fill="white" stroke="#40AB5E"
                    stroke-width="2"/>
              <rect x="6.75" y="13.5" width="10.5" height="21.75" rx="2" fill="white" stroke="#40AB5E"
                    stroke-width="2"/>
              <rect x="21.75" y="7.5" width="19.5" height="18.75" rx="3" fill="white" stroke="#40AB5E"
                    stroke-width="2"/>
            </svg>
            <div class="card-description">{{ advantages_block.text_first }}</div>
            <div class="card-additional small-text-2" v-if="advantages_block.additional_first">
              <div v-for="item in processedAdvantages.additional_first" :key="item" class="card-additional-item">
                {{ item }}
              </div>
            </div>
          </div>
        </div>
        <div class="card even">
          <h3 class="card-title" v-html="advantages_block.subtitle_second"></h3>
          <div class="card-bottom-container">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
              <path
                  d="M10.9983 22.9098V10C10.9983 8.34315 12.3415 7 13.9983 7H34.0017C35.6585 7 37.0017 8.34315 37.0017 10V22.9098M10.9983 22.9098V26.7575C10.9983 28.4144 12.3415 29.7575 13.9983 29.7575H34.0017C35.6585 29.7575 37.0017 28.4144 37.0017 26.7575V22.9098M10.9983 22.9098H8C5.79086 22.9098 4 24.7007 4 26.9098V33C4 37.4183 7.58172 41 12 41H36C40.4183 41 44 37.4183 44 33V26.9098C44 24.7007 42.2091 22.9098 40 22.9098H37.0017M17.5165 22.5V13.3144M22.0286 22.5V13.3144M26.5 22.5V13.3144M30.9306 22.5V13.3144"
                  stroke="#40AB5E" stroke-width="2" stroke-linecap="round"/>
            </svg>
            <div class="card-description">{{ advantages_block.text_second }}</div>
            <div class="card-additional small-text-2" v-if="advantages_block.additional_second">
              <div v-for="item in processedAdvantages.additional_second" :key="item" class="card-additional-item">
                {{ item }}
              </div>
            </div>
          </div>
        </div>
        <div class="card odd">
          <h3 class="card-title" v-html="advantages_block.subtitle_third"></h3>
          <div class="card-bottom-container">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
              <path
                  d="M16.8 4V9.42857M31.2 4V9.42857M33.9 16.6667H14.1M16.8 24.8095C16.8 25.3092 16.3971 25.7143 15.9 25.7143C15.4029 25.7143 15 25.3092 15 24.8095M16.8 24.8095C16.8 24.3098 16.3971 23.9048 15.9 23.9048C15.4029 23.9048 15 24.3098 15 24.8095M16.8 24.8095H15M16.8 32.0476C16.8 32.5473 16.3971 32.9524 15.9 32.9524C15.4029 32.9524 15 32.5473 15 32.0476M16.8 32.0476C16.8 31.5479 16.3971 31.1429 15.9 31.1429C15.4029 31.1429 15 31.5479 15 32.0476M16.8 32.0476H15M24.9 24.8095C24.9 25.3092 24.4971 25.7143 24 25.7143C23.5029 25.7143 23.1 25.3092 23.1 24.8095M24.9 24.8095C24.9 24.3098 24.4971 23.9048 24 23.9048C23.5029 23.9048 23.1 24.3098 23.1 24.8095M24.9 24.8095H23.1M24.9 32.0476C24.9 32.5473 24.4971 32.9524 24 32.9524C23.5029 32.9524 23.1 32.5473 23.1 32.0476M24.9 32.0476C24.9 31.5479 24.4971 31.1429 24 31.1429C23.5029 31.1429 23.1 31.5479 23.1 32.0476M24.9 32.0476H23.1M33 24.8095C33 25.3092 32.5971 25.7143 32.1 25.7143C31.6029 25.7143 31.2 25.3092 31.2 24.8095M33 24.8095C33 24.3098 32.5971 23.9048 32.1 23.9048C31.6029 23.9048 31.2 24.3098 31.2 24.8095M33 24.8095H31.2M33 32.0476C33 32.5473 32.5971 32.9524 32.1 32.9524C31.6029 32.9524 31.2 32.5473 31.2 32.0476M33 32.0476C33 31.5479 32.5971 31.1429 32.1 31.1429C31.6029 31.1429 31.2 31.5479 31.2 32.0476M33 32.0476H31.2M15.6 42H32.4C35.7603 42 37.4405 42 38.7239 41.346C39.8529 40.7708 40.7708 39.8529 41.346 38.7239C42 37.4405 42 35.7603 42 32.4V15.4095C42 12.0492 42 10.3691 41.346 9.08558C40.7708 7.95661 39.8529 7.03872 38.7239 6.46348C37.4405 5.80952 35.7603 5.80952 32.4 5.80952H15.6C12.2397 5.80952 10.5595 5.80952 9.27606 6.46348C8.14708 7.03872 7.2292 7.95661 6.65396 9.08558C6 10.3691 6 12.0492 6 15.4095V32.4C6 35.7603 6 37.4405 6.65396 38.7239C7.2292 39.8529 8.14708 40.7708 9.27606 41.346C10.5595 42 12.2397 42 15.6 42Z"
                  stroke="#40AB5E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <div class="card-description">{{ advantages_block.text_third }}</div>
            <div class="card-additional small-text-2" v-if="advantages_block.additional_third">
              <div v-for="item in processedAdvantages.additional_third" :key="item" class="card-additional-item">
                {{ item }}
              </div>
            </div>
          </div>
        </div>
        <div class="card even">
          <h3 class="card-title" v-html="advantages_block.subtitle_fourth"></h3>
          <div class="card-bottom-container">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
              <path
                  d="M39.5556 34C42.3351 35.0546 44 36.3975 44 37.8597C44 41.2509 35.0457 44 24 44C12.9543 44 4 41.2509 4 37.8597C4 36.3975 5.66489 35.0546 8.44444 34M28 16C28 18.2091 26.2091 20 24 20C21.7909 20 20 18.2091 20 16C20 13.7909 21.7909 12 24 12C26.2091 12 28 13.7909 28 16ZM24 36C27.1111 36 38 30.1631 38 17.6001C38 9.60005 31.7778 4 24 4C16.2222 4 10 9.60005 10 17.6001C10 30.1631 20.8889 36 24 36Z"
                  stroke="#40AB5E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <div class="card-description">{{ advantages_block.text_fourth }}</div>
            <div class="card-additional small-text-2" v-if="advantages_block.additional_fourth">
              <div v-for="item in processedAdvantages.additional_fourth" :key="item" class="card-additional-item">
                {{ item }}
              </div>
            </div>
          </div>
        </div>
        <div class="card odd">
          <h3 class="card-title" v-html="advantages_block.subtitle_fifth"></h3>
          <div class="card-bottom-container">
            <div class="svg-container">
              <img :src="frontendURL + '/images/icons/whatsapp.png'" alt="">
            </div>
            <div class="card-description">{{ advantages_block.text_fifth }}</div>
            <div class="card-additional small-text-2" v-if="advantages_block.additional_fifth">
              <div v-for="item in processedAdvantages.additional_fifth" :key="item" class="card-additional-item">
                {{ item }}
              </div>
            </div>
          </div>
        </div>
        <div class="card even last">
          <h3 class="card-title" v-html="advantages_block.subtitle_sixth"></h3>
          <div class="card-bottom-container">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
              <path
                  d="M44 35.9999V23.9999M44 35.9999H32M44 35.9999L28.2627 20.2626C27.4707 19.4706 27.0747 19.0746 26.618 18.9262C26.2163 18.7957 25.7837 18.7957 25.382 18.9262C24.9253 19.0746 24.5293 19.4706 23.7373 20.2626L20.2627 23.7372C19.4706 24.5292 19.0746 24.9252 18.618 25.0736C18.2163 25.2041 17.7836 25.2041 17.3819 25.0736C16.9252 24.9252 16.5292 24.5292 15.7372 23.7372L4 12"
                  stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <div class="card-description">{{ advantages_block.text_sixth }}</div>
            <div class="card-additional small-text-2" v-if="advantages_block.additional_sixth">
              <div v-for="item in processedAdvantages.additional_sixth" :key="item" class="card-additional-item">
                {{ item }}
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Advantages",
  inject: ['backendURL', 'frontendURL'],
  props: {
    advantages_block: Object,
  },
  components: {},
  data() {
    return {}
  },
  mounted() {
  },
  computed: {
    processedAdvantages() {
      const advantages = this.advantages_block;
      const result = {};

      Object.keys(advantages).forEach(key => {
        if (key.startsWith('additional_') && advantages[key]) {
          result[key] = advantages[key].split(';').map(item => item.trim());
        }
      });

      return result;
    },
  },
  methods: {},
}
</script>


<style scoped>
.advantages-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 9rem;

  display: flex;
  justify-content: center;
  align-items: center;

  height: calc(100% + 10rem);
}

.advantages-max {
  max-width: 76.3rem;
  padding: 0 6.8rem 10rem;
  width: 100%;
  position: relative;
}

.advantages-head {
  width: 72%;
}

.advantages-content {
  margin-top: 4rem;

  display: grid;
  grid-template-columns: 2fr 2fr;
  gap: 13.5rem;
}

h3 {
  font-size: 1.5rem;
}

.card {
  border-radius: 1rem;
  background: #FFF;

  display: flex;
  padding: 2rem;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;

  min-height: 24.75rem;
}

.card.last {
  background-color: var(--green-light);
  color: white;
}

.even {
  position: relative;
  bottom: -10rem;
}

.card-title {
  width: 70%;
}

.card-bottom-container {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.card-description {
  width: 90%;
}

.card-additional {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 0.5rem;
}

@media screen and (max-width: 1280px) {
  .advantages-component {
    padding-top: 8rem;
  }

  .advantages-max {
    padding: 0 2.25rem 7rem;
  }

  .advantages-content {
    margin-top: 2rem;
    gap: 10.25rem;
  }

  .advantages-head {
    width: 70%;
  }

  .even {
    bottom: -7rem;
  }

  .card-title {
    width: 100%;
  }

  .card-description {
    width: 100%;
  }

  .card-additional {
    flex-direction: column;
    gap: 0.25rem;
  }
}

@media screen and (max-width: 1000px) {
  .advantages-component {
    padding-top: 5rem;
  }

  .advantages-max {
    padding: 0 2.25rem;
  }

  .advantages-head {
    width: 85%;
  }

  .advantages-content {
    grid-template-columns: unset;
    gap: 1rem;
  }

  .even {
    bottom: unset;
    margin-left: auto;
  }

  .card {
    min-height: 14.75rem;
    width: 75%;
  }

  .card-title {
    font-size: 1.25rem;
  }

  .card-bottom-container {
    gap: 1rem;
  }

  .card-additional {
    flex-direction: row;
  }

}

@media screen and (max-width: 640px) {
  .advantages-component {
    padding-top: 4.4rem;
  }

  .advantages-max {
    padding: 0 1rem;
  }

  .advantages-head {
    width: 90%;
  }

  .advantages-content {
    margin-top: 1.5rem;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .card {
    width: unset;
    padding: 1.5rem;
    min-height: unset;
    gap: 3rem;
  }

  .even {
    margin-left: unset;
  }

  .card-title {
    font-size: 1.125rem;
  }

  .card svg, .card img {
    width: 2rem;
    height: 2rem;
  }

  .card-additional {
    flex-direction: column;
  }
}
</style>