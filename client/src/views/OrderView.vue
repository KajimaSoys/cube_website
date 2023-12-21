<template>
  <Header
    :header_block="header_block"
  />

  <Order/>

  <Footer
    :header_block="header_block"
  />
</template>

<script>
import Header from "../components/common/Header.vue";
import Order from "../components/orderPage/Order.vue";
import Footer from "../components/common/Footer.vue";
import axios from "axios";

export default {
  name: "OrderView",
  inject: ['backendURL'],
  components: {
    Header,
    Order,
    Footer
  },
  data() {
    return {
      header_block: {},
    }
  },
  created() {
    this.getPageData()
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero();
  },
  methods: {
    async getPageData() {
      await axios
          .get(`${this.backendURL}/api/v1/header_data/`)
          .then(response => {
            let receivedData = response.data

            this.header_block = receivedData.header_block

            console.log(response.data)
          })
          .catch(error => {
            console.log('An error occurred: ', error)
          })
    },
    scrollToZero() {
      document.documentElement.scrollTop = 0;
    }
  },
  setup() {
    const title = 'Title';
    const description = 'Description';
  }
}
</script>


<style scoped>


@media screen and (max-width: 1280px) {

}

@media screen and (max-width: 1000px) {

}

@media screen and (max-width: 640px) {

}
</style>