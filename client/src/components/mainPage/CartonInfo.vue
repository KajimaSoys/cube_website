<template>
  <div class="carton-component">
    <div class="carton-max">
      <div class="carton-content">
        <div class="left-side">
          <div class="carton-head">
            <h2 v-html="carton_info_block.title"></h2>
            <h2 class="description">{{ carton_info_block.description }}</h2>
          </div>
          <div class="quality-container top">
            <div class="svg-container">
              <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
                <path
                    d="M18 24L22 28L32 18M16.1122 8L10.3316 8C9.49149 8 9.07145 8 8.75058 8.16349C8.46834 8.3073 8.23887 8.53677 8.09506 8.81901C7.93157 9.13988 7.93157 9.55992 7.93157 10.4L7.93157 16.1199C7.93157 16.4458 7.93157 16.6087 7.89834 16.7639C7.86886 16.9016 7.82013 17.0345 7.7536 17.1586C7.6786 17.2985 7.57326 17.4228 7.3626 17.6715L3.31474 22.4484C2.84766 22.9997 2.61412 23.2753 2.52501 23.5838C2.44647 23.8557 2.44647 24.1443 2.52501 24.4162C2.61412 24.7247 2.84766 25.0003 3.31474 25.5515L7.3626 30.3285C7.57326 30.5771 7.6786 30.7015 7.7536 30.8414C7.82013 30.9655 7.86886 31.0984 7.89834 31.2361C7.93157 31.3913 7.93157 31.5542 7.93157 31.8801L7.93157 37.6C7.93157 38.4401 7.93157 38.8601 8.09506 39.181C8.23887 39.4632 8.46834 39.6927 8.75058 39.8365C9.07145 40 9.49149 40 10.3316 40L16.1122 40C16.4408 40 16.6052 40 16.7616 40.0338C16.9004 40.0637 17.0342 40.1132 17.159 40.1808C17.2998 40.257 17.4246 40.3639 17.6741 40.5778L22.4381 44.6612C22.9925 45.1364 23.2696 45.374 23.5805 45.4645C23.8545 45.5443 24.1455 45.5443 24.4195 45.4645C24.7304 45.374 25.0075 45.1364 25.5619 44.6612L30.3259 40.5778C30.5755 40.3639 30.7002 40.257 30.841 40.1808C30.9658 40.1132 31.0996 40.0637 31.2384 40.0338C31.3948 40 31.5592 40 31.8878 40L37.6 40C38.4401 40 38.8601 40 39.181 39.8365C39.4632 39.6927 39.6927 39.4632 39.8365 39.181C40 38.8601 40 38.4401 40 37.6L40 31.8878C40 31.5592 40 31.3948 40.0338 31.2384C40.0637 31.0996 40.1132 30.9658 40.1808 30.841C40.257 30.7002 40.3639 30.5754 40.5778 30.3259L44.6612 25.5619C45.1364 25.0075 45.374 24.7304 45.4645 24.4195C45.5443 24.1455 45.5443 23.8545 45.4645 23.5805C45.374 23.2696 45.1364 22.9925 44.6612 22.4381L40.5778 17.6741C40.3639 17.4245 40.257 17.2998 40.1808 17.159C40.1132 17.0342 40.0637 16.9004 40.0338 16.7616C40 16.6052 40 16.4408 40 16.1122L40 10.4C40 9.55992 40 9.13988 39.8365 8.81901C39.6927 8.53677 39.4632 8.3073 39.181 8.16349C38.8601 8 38.4401 8 37.6 8L31.8878 8C31.5592 8 31.3948 8 31.2384 7.96623C31.0996 7.93628 30.9658 7.88678 30.841 7.81921C30.7002 7.74304 30.5755 7.6361 30.3259 7.42222L25.5619 3.33877C25.0075 2.8636 24.7304 2.62602 24.4195 2.53547C24.1455 2.45566 23.8545 2.45566 23.5805 2.53547C23.2696 2.62602 22.9925 2.8636 22.4381 3.33877L17.6741 7.42222C17.4246 7.6361 17.2998 7.74304 17.159 7.81921C17.0342 7.88678 16.9004 7.93628 16.7616 7.96623C16.6052 8 16.4408 8 16.1122 8Z"
                    stroke="#40AB5E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            {{ carton_info_block.quality_block }}
          </div>
        </div>
        <div class="right-side">
          <div class="card">
            <div class="card-title">
              {{ carton_info_block.subtitle_first }}
            </div>
            <div class="card-description first" v-if="carton_info_block.text_first">
              <div v-for="item in processedCarton.text_first" :key="item" class="card-description-item">
                {{ item }}
              </div>
            </div>
            <div class="image-container first">
              <img :src="backendURL + carton_info_block.image_first" alt="">
            </div>
          </div>

          <div class="card">
            <div class="card-title">
              {{ carton_info_block.subtitle_second }}
            </div>
            <div class="card-description second" v-if="carton_info_block.text_second">
              <div v-for="item in processedCarton.text_second" :key="item" class="card-description-item">
                {{ item }}
              </div>
            </div>
            <div class="image-container second">
              <img :src="backendURL + carton_info_block.image_second" alt="">
            </div>
          </div>
        </div>
        <div class="quality-container bottom">
          <div class="svg-container">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
              <path
                  d="M18 24L22 28L32 18M16.1122 8L10.3316 8C9.49149 8 9.07145 8 8.75058 8.16349C8.46834 8.3073 8.23887 8.53677 8.09506 8.81901C7.93157 9.13988 7.93157 9.55992 7.93157 10.4L7.93157 16.1199C7.93157 16.4458 7.93157 16.6087 7.89834 16.7639C7.86886 16.9016 7.82013 17.0345 7.7536 17.1586C7.6786 17.2985 7.57326 17.4228 7.3626 17.6715L3.31474 22.4484C2.84766 22.9997 2.61412 23.2753 2.52501 23.5838C2.44647 23.8557 2.44647 24.1443 2.52501 24.4162C2.61412 24.7247 2.84766 25.0003 3.31474 25.5515L7.3626 30.3285C7.57326 30.5771 7.6786 30.7015 7.7536 30.8414C7.82013 30.9655 7.86886 31.0984 7.89834 31.2361C7.93157 31.3913 7.93157 31.5542 7.93157 31.8801L7.93157 37.6C7.93157 38.4401 7.93157 38.8601 8.09506 39.181C8.23887 39.4632 8.46834 39.6927 8.75058 39.8365C9.07145 40 9.49149 40 10.3316 40L16.1122 40C16.4408 40 16.6052 40 16.7616 40.0338C16.9004 40.0637 17.0342 40.1132 17.159 40.1808C17.2998 40.257 17.4246 40.3639 17.6741 40.5778L22.4381 44.6612C22.9925 45.1364 23.2696 45.374 23.5805 45.4645C23.8545 45.5443 24.1455 45.5443 24.4195 45.4645C24.7304 45.374 25.0075 45.1364 25.5619 44.6612L30.3259 40.5778C30.5755 40.3639 30.7002 40.257 30.841 40.1808C30.9658 40.1132 31.0996 40.0637 31.2384 40.0338C31.3948 40 31.5592 40 31.8878 40L37.6 40C38.4401 40 38.8601 40 39.181 39.8365C39.4632 39.6927 39.6927 39.4632 39.8365 39.181C40 38.8601 40 38.4401 40 37.6L40 31.8878C40 31.5592 40 31.3948 40.0338 31.2384C40.0637 31.0996 40.1132 30.9658 40.1808 30.841C40.257 30.7002 40.3639 30.5754 40.5778 30.3259L44.6612 25.5619C45.1364 25.0075 45.374 24.7304 45.4645 24.4195C45.5443 24.1455 45.5443 23.8545 45.4645 23.5805C45.374 23.2696 45.1364 22.9925 44.6612 22.4381L40.5778 17.6741C40.3639 17.4245 40.257 17.2998 40.1808 17.159C40.1132 17.0342 40.0637 16.9004 40.0338 16.7616C40 16.6052 40 16.4408 40 16.1122L40 10.4C40 9.55992 40 9.13988 39.8365 8.81901C39.6927 8.53677 39.4632 8.3073 39.181 8.16349C38.8601 8 38.4401 8 37.6 8L31.8878 8C31.5592 8 31.3948 8 31.2384 7.96623C31.0996 7.93628 30.9658 7.88678 30.841 7.81921C30.7002 7.74304 30.5755 7.6361 30.3259 7.42222L25.5619 3.33877C25.0075 2.8636 24.7304 2.62602 24.4195 2.53547C24.1455 2.45566 23.8545 2.45566 23.5805 2.53547C23.2696 2.62602 22.9925 2.8636 22.4381 3.33877L17.6741 7.42222C17.4246 7.6361 17.2998 7.74304 17.159 7.81921C17.0342 7.88678 16.9004 7.93628 16.7616 7.96623C16.6052 8 16.4408 8 16.1122 8Z"
                  stroke="#40AB5E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          {{ carton_info_block.quality_block }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CartonInfo",
  inject: ['backendURL'],
  props: {
    carton_info_block: Object,
  },
  components: {},
  data() {
    return {}
  },
  mounted() {
  },
  computed: {
    processedCarton() {
      const carton = this.carton_info_block;
      const result = {};

      Object.keys(carton).forEach(key => {
        if (key.startsWith('text_') && carton[key]) {
          result[key] = carton[key].split(';').map(item => item.trim());
        }
      });

      return result;
    },
  },
  methods: {},
}
</script>


<style scoped>
.carton-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 9rem;

  display: flex;
  justify-content: center;
  align-items: center;
}

.carton-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
}

.carton-content {
  display: flex;
  flex-direction: row;
  gap: 2.6rem;
}

.left-side {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-basis: 50%;
  gap: 3rem;
}

.description {
  margin-top: 2rem;
}

.quality-container {
  display: inline-flex;
  flex-direction: row;
  align-items: center;
  gap: 1rem;

  padding: 1.5rem;
  width: 80%;

  border-radius: 1rem;
  background: #FFF;
}

.svg-container {
  width: 3rem;
  height: 3rem;
}

.quality-container.bottom {
  display: none;
}

.right-side {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  flex-basis: 50%;
}

.card {
  display: flex;
  padding: 2rem;
  flex-direction: column;
  align-items: flex-start;
  gap: 1rem;

  border-radius: 1rem;
  background: #FFF;

  flex: 1;
  min-height: 17.3rem;
  position: relative;
  overflow: hidden;
}

.card-title {
  font-size: 1.25rem;
}

.card-description {
  color: var(--green-light);
  font-size: 1.125rem;
  font-weight: 500;

  display: flex;
}

.card-description.first {
  gap: 0.75rem;
}

.card-description.second {
  gap: 0.5rem;
  flex-direction: column;
}

.image-container img {
  width: 100%;
  object-fit: cover;
}

.image-container {
  width: 13rem;
  height: 13rem;
  position: absolute;
}

.image-container.first {
  width: 15rem;
  bottom: 0.5rem;
  right: -4rem;
}

.image-container.second {
  bottom: 0.5rem;
  height: 13.375rem;
  width: 11rem;
  right: -3rem;
}

@media screen and (max-width: 1280px) {
  .carton-component {
    padding-top: 8rem;
  }

  .carton-max {
    padding: 0 2.25rem;
  }

  .carton-content {
    gap: 1.6rem;
  }

  .carton-head {
    gap: 2.4rem;
  }

  .left-side {
    gap: 4rem;
  }

  .quality-container {
    width: 83%;
  }

  .right-side {
    gap: 0.5rem;
  }

  .card {
    padding-bottom: 1.5rem;
  }

  .card-title {
    font-size: 1.125rem;
  }

  .image-container.first {
    bottom: -1rem;
  }

  .image-container.second {
    bottom: -1rem;
  }
}

@media screen and (max-width: 1000px) {
  .carton-component {
    padding-top: 5rem;
  }

  .carton-max {
    padding: 0 2.25rem;
  }

  .carton-content {
    flex-direction: column;
    gap: 0.5rem;
  }

  .right-side {
    margin-top: 1.5rem;
  }

  .description {
    margin-top: 0.5rem;
  }

  .quality-container.top {
    display: none;
  }

  .card {
    min-height: 13rem;
  }

  .card-title, .card-description {
    font-size: 1rem;
  }

  .card-description.second {
    flex-direction: row;
    gap: 0.75rem;
  }

  .image-container.first {
    width: 12rem;
    bottom: -4rem;
    right: -3rem;
  }

  .image-container.second {
    width: 9rem;
    bottom: -4.5rem;
    right: -1rem;
  }

  .quality-container.bottom {
    display: flex;
    width: unset;
    padding: 1.5rem 5.5rem;
    justify-content: center;
  }
}

@media screen and (max-width: 640px) {
  .carton-component {
    padding-top: 4.4rem;
  }

  .carton-max {
    padding: 0 1rem;
  }

  .description {
    margin-top: 1rem;
  }

  .right-side {
    flex-direction: column;
  }

  .card {
    min-height: unset;
  }

  .card-title {
    font-size: 0.875rem;
    width: 50%;
  }

  .card-description.second {
    flex-direction: column;
    gap: 0.25rem;
  }

  .quality-container.bottom {
    display: flex;
    width: unset;
    padding: 1.5rem;
    justify-content: center;
  }

  .image-container.first {
    width: 10rem;
    bottom: -5.5rem;
    right: -2rem;
  }

  .image-container.second {
    width: 8rem;
    bottom: -4.5rem;
    right: -1rem;
  }
}
</style>