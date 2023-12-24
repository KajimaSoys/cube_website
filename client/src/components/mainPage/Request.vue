<template>
  <div class="request-component">
    <div class="request-max">
      <div class="request-content">
        <h2 v-html="request_block.title"></h2>
        <div class="description">{{ request_block.description }}</div>
        <a class="button" :href="request_block.whatsapp_link" target="_blank">Написать в What's App</a>
      </div>
      <div class="request-background"></div>
      <div class="svg-container">
        <svg xmlns="http://www.w3.org/2000/svg" width="289" height="150" viewBox="0 0 289 150" fill="none">
          <path fill-rule="evenodd" clip-rule="evenodd"
                d="M0 177V352C0 353.105 0.895431 354 2 354H2.98966H3.97931C5.08388 354 5.97931 353.105 5.97931 352V177V2C5.97931 0.89543 5.08388 0 3.97931 0H2.98966H2C0.895431 0 0 0.895431 0 2V177ZM8.96897 177C8.96897 353.044 8.97993 354 10.9621 354C12.9442 354 12.9552 353.044 12.9552 177C12.9552 59.5717 12.9552 11.7864 12.9552 1.97548C12.9552 0.874721 12.0628 0 10.9621 0C9.86131 0 8.96897 0.888265 8.96897 1.98903C8.96897 8.88317 8.96897 39.6595 8.96897 177ZM18.9345 177C18.9345 333.378 19.1089 354 20.4293 354C21.7497 354 21.9241 333.378 21.9241 177C21.9241 61.3019 21.9241 10.4468 21.9241 1.47203C21.9241 0.646456 21.2549 0 20.4293 0C19.6037 0 18.9345 0.643455 18.9345 1.46903C18.9345 8.23793 18.9345 42.1246 18.9345 177ZM34.8793 177C34.8793 333.378 35.0537 354 36.3741 354C37.6946 354 37.869 333.378 37.869 177C37.869 61.3019 37.869 10.4468 37.869 1.47203C37.869 0.646455 37.1997 0 36.3741 0C35.5486 0 34.8793 0.643456 34.8793 1.46903C34.8793 8.23794 34.8793 42.1246 34.8793 177ZM47.8345 177V352C47.8345 353.105 48.7299 354 49.8345 354H52.8172H55.8C56.9046 354 57.8 353.105 57.8 352V177V2C57.8 0.89543 56.9046 0 55.8 0H52.8172H49.8345C48.7299 0 47.8345 0.895431 47.8345 2V177ZM60.7896 177V352C60.7896 353.105 61.6851 354 62.7896 354H63.7793H64.769C65.8735 354 66.769 353.105 66.769 352V177V2C66.769 0.89543 65.8735 0 64.769 0H63.7793H62.7896C61.6851 0 60.7896 0.895431 60.7896 2V177ZM70.7552 177V352C70.7552 353.105 71.6506 354 72.7552 354H75.2396H77.7241C78.8287 354 79.7241 353.105 79.7241 352V177V2C79.7241 0.89543 78.8287 0 77.7241 0H75.2396H72.7552C71.6506 0 70.7552 0.895431 70.7552 2V177ZM83.7103 177V352C83.7103 353.105 84.6058 354 85.7103 354H86.7H87.6896C88.7942 354 89.6896 353.105 89.6896 352V177V2C89.6896 0.89543 88.7942 0 87.6896 0H86.7H85.7103C84.6058 0 83.7103 0.895431 83.7103 2V177ZM99.6552 177C99.6552 333.378 99.8296 354 101.15 354C102.47 354 102.645 333.378 102.645 177C102.645 63.6256 102.645 10.6997 102.645 1.47921C102.645 0.653638 101.976 0 101.15 0C100.324 0 99.6552 0.643456 99.6552 1.46903C99.6552 8.23794 99.6552 42.1246 99.6552 177ZM105.634 177C105.634 333.378 105.809 354 107.129 354C108.45 354 108.624 333.378 108.624 177C108.624 63.6256 108.624 10.6997 108.624 1.47921C108.624 0.653641 107.955 0 107.129 0C106.304 0 105.634 0.643454 105.634 1.46902C105.634 8.23792 105.634 42.1246 105.634 177ZM112.61 177V352C112.61 353.105 113.506 354 114.61 354H117.095H119.579C120.684 354 121.579 353.105 121.579 352V177V2C121.579 0.89543 120.684 0 119.579 0H117.095H114.61C113.506 0 112.61 0.895431 112.61 2V177ZM131.545 177V352C131.545 353.105 132.44 354 133.545 354H134.534H135.524C136.629 354 137.524 353.105 137.524 352V177V2C137.524 0.89543 136.629 0 135.524 0H134.534H133.545C132.44 0 131.545 0.895431 131.545 2V177ZM141.51 177C141.51 333.378 141.685 354 143.005 354C144.326 354 144.5 333.378 144.5 177C144.5 61.3019 144.5 10.4468 144.5 1.47203C144.5 0.646452 143.831 0 143.005 0C142.18 0 141.51 0.643458 141.51 1.46903C141.51 8.23796 141.51 42.1246 141.51 177ZM150.479 177V352C150.479 353.105 151.375 354 152.479 354H155.462H158.445C159.549 354 160.445 353.105 160.445 352V177V2C160.445 0.89543 159.549 0 158.445 0H155.462H152.479C151.375 0 150.479 0.895431 150.479 2V177ZM166.424 177V352C166.424 353.105 167.32 354 168.424 354H169.912H171.4C172.505 354 173.4 353.105 173.4 352V177V2C173.4 0.89543 172.505 0 171.4 0H169.912H168.424C167.32 0 166.424 0.895431 166.424 2V177ZM176.39 177C176.39 333.378 176.564 354 177.884 354C179.205 354 179.379 333.378 179.379 177C179.379 61.3018 179.379 10.4468 179.379 1.47201C179.379 0.646446 178.71 0 177.884 0C177.059 0 176.39 0.643452 176.39 1.46902C176.39 8.23791 176.39 42.1245 176.39 177ZM186.355 177V352C186.355 353.105 187.251 354 188.355 354H190.84H193.324C194.429 354 195.324 353.105 195.324 352V177V2C195.324 0.89543 194.429 0 193.324 0H190.84H188.355C187.251 0 186.355 0.895431 186.355 2V177ZM202.3 177V352C202.3 353.105 203.195 354 204.3 354H205.29H206.279C207.384 354 208.279 353.105 208.279 352V177V2C208.279 0.89543 207.384 0 206.279 0H205.29H204.3C203.195 0 202.3 0.895431 202.3 2V177ZM211.269 177V352C211.269 353.105 212.164 354 213.269 354H214.757H216.245C217.349 354 218.245 353.105 218.245 352V177V2C218.245 0.89543 217.349 0 216.245 0H214.757H213.269C212.164 0 211.269 0.895431 211.269 2V177ZM224.224 177V352C224.224 353.105 225.12 354 226.224 354H229.207H232.19C233.294 354 234.19 353.105 234.19 352V177V2C234.19 0.89543 233.294 0 232.19 0H229.207H226.224C225.12 0 224.224 0.895431 224.224 2V177ZM241.165 177C241.165 333.378 241.34 354 242.66 354C243.981 354 244.155 333.378 244.155 177C244.155 75.2611 244.155 11.7008 244.155 1.46155C244.155 0.635983 243.486 0 242.66 0C241.835 0 241.165 0.643456 241.165 1.46903C241.165 8.23794 241.165 42.1246 241.165 177ZM247.145 177V352C247.145 353.105 248.04 354 249.145 354H252.128H255.11C256.215 354 257.11 353.105 257.11 352V177V2C257.11 0.89543 256.215 0 255.11 0H252.128H249.145C248.04 0 247.145 0.895431 247.145 2V177ZM260.1 177V352C260.1 353.105 260.995 354 262.1 354H263.09H264.079C265.184 354 266.079 353.105 266.079 352V177V2C266.079 0.89543 265.184 0 264.079 0H263.09H262.1C260.995 0 260.1 0.895431 260.1 2V177ZM270.065 177V352C270.065 353.105 270.961 354 272.065 354H274.55H277.034C278.139 354 279.034 353.105 279.034 352V177V2C279.034 0.89543 278.139 0 277.034 0H274.55H272.065C270.961 0 270.065 0.895431 270.065 2V177ZM282.024 177V352C282.024 353.105 282.92 354 284.024 354H285.512H287C288.105 354 289 353.105 289 352V177V2C289 0.89543 288.105 0 287 0H285.512H284.024C282.92 0 282.024 0.895431 282.024 2V177Z"
                fill="#40AB5E"/>
        </svg>
      </div>
      <div class="image-container">
        <img :src="backendURL + request_block.image" alt="">
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "Request",
  inject: ['backendURL'],
  props: {
    request_block: Object,
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
.request-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 14rem;

  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.request-max {
  max-width: 90rem;
  width: 100%;
  position: relative;
}

.request-background {
  position: absolute;
  max-width: 90rem;
  width: 100%;
  height: calc(100%);
  border-radius: 1.5rem;
  background: #FFF;
  top: 0;
  z-index: 0;
}

.request-content {
  padding: 5rem 0 5rem 6.8rem;
  position: relative;
  z-index: 2;

  display: flex;
  flex-direction: column;
  align-items: flex-start;

  width: 50%;
  gap: 1.5rem;
}

.button {
  margin-top: 2.5rem;
  padding: 1rem 2rem;
  height: 2.5rem;

  display: flex;
  justify-content: space-between;
  align-items: center;

  border-radius: 0.5rem;
  background: var(--green-light, #40AB5E);
  text-decoration: none;
  color: white;
}

.svg-container {
  z-index: 1;
  position: absolute;
  transform: scale(1, -1);
  bottom: 0;
  right: 5.4rem;
}

.image-container {
  position: absolute;
  z-index: 1;
  bottom: -14rem;
  right: -1rem;
  rotate: 2deg;
}

.image-container img {
  width: 70%;
  object-fit: cover;
}

@media screen and (max-width: 1400px) {
  .image-container {
    bottom: -13rem;
    right: -8rem;
  }

  .image-container img {
    width: 60%;
  }
}

@media screen and (max-width: 1280px) {
  .request-component {
    padding-top: 11.5rem;
  }

  .request-content {
    padding: 3rem 2.25rem 3rem 2.25rem;
  }

  .description {
    width: 60%;
  }

  .button {
    height: 1.5rem;
    margin-top: 1.5rem;
  }

  .svg-container {
    right: 0;
    bottom: -3rem;
  }

  .image-container {
    bottom: -9.5rem;
    right: -18rem;
  }

  .image-container img {
    width: 50%;
  }
}

@media screen and (max-width: 1000px) {
  .request-component {
    padding-top: 8rem;
  }

  .request-content {
    gap: 1rem;
  }

  .description {
    width: 80%;
  }

  .button {
    margin-top: 1rem;
    padding: 0.75rem 1.5rem;
  }

  .image-container {
    bottom: -2.5rem;
    right: -27rem;
  }

  .image-container img {
    width: 35%;
  }

  .svg-container {
    right: -4rem;
    bottom: -5rem;
  }

  .svg-container svg {
    width: 80%;
  }
}

@media screen and (max-width: 640px) {
  .request-component {
    padding-top: 4.4rem;
  }

  .request-max {

  }

  .request-background {
    height: calc(100%);
  }

  .request-content {
    padding: 2rem 1rem 2rem 1rem;
    gap: 1.5rem;
    align-items: center;
    width: unset;
  }

  h2 {
    text-align: center;
  }

  .description {
    text-align: center;
    width: 75%;
  }

  .button {
    justify-content: center;
  }

  .image-container {
    position: relative;
    bottom: -1rem;
    right: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 19rem;
  }

  .image-container img {
    width: 18rem;
  }

}
</style>