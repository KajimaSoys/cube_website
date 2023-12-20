<template>
  <Header
    :header_block="header_block"
  />

  <Catalog/>

  <AddQuestion
    :add_question_block="add_question_block"
  />

  <Footer
    :header_block="header_block"
  />
</template>

<script>
import Header from "../components/common/Header.vue";
import Catalog from "../components/catalogPage/Catalog.vue";
import AddQuestion from "../components/common/AddQuestion.vue";
import Footer from "../components/common/Footer.vue";
import axios from "axios";

export default {
  name: "CatalogView",
  inject: ['backendURL'],
  components: {
    Header,
    Catalog,
    AddQuestion,
    Footer
  },
  data() {
    return {
      header_block: {},
      add_question_block: {},
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
          .get(`${this.backendURL}/api/v1/catalog_page/`)
          .then(response => {
            let receivedData = response.data

            this.header_block = receivedData.header_block
            this.add_question_block = receivedData.add_question_block

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


@media screen and (max-width: 960px) {

}

@media screen and (max-width: 640px) {

}

@media screen and (max-width: 360px) {

}
</style>