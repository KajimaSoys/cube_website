<template>

  <Header
      :header_block="header_block"
  />

  <div v-if="show">

    <Breadcrumbs/>

    <Advantages
        :advantages_block="advantages_block"
        :separate="true"
    />

    <ServiceOptions
        :service_options_block="service_options_block"
    />

    <CartonInfo
        :carton_info_block="carton_info_block"
    />

    <Contacts
        :contacts_block="contacts_block"
    />

    <OutsideView
        :outside_view="outside_view"
    />

    <AddQuestion
        :add_question_block="add_question_block"
    />
  </div>
  <div v-else class="loading">
    <div class="spinner spinner-1"></div>
  </div>

  <Footer
      :header_block="header_block"
      :category_list="category_list"
  />

</template>

<script>
import Header from "../components/common/Header.vue";
import Advantages from "../components/mainPage/Advantages.vue";
import ServiceOptions from "../components/mainPage/ServiceOptions.vue";
import CartonInfo from "../components/mainPage/CartonInfo.vue";
import Contacts from "../components/mainPage/Contacts.vue";
import OutsideView from "../components/contactsPage/OutsideView.vue";
import AddQuestion from "../components/common/AddQuestion.vue";
import Footer from "../components/common/Footer.vue";
import Breadcrumbs from "../components/common/Breadcrumbs.vue";
import axios from "axios";

export default {
  name: "AboutView",
  inject: ['backendURL'],
  components: {
    Header,
    Advantages,
    ServiceOptions,
    CartonInfo,
    Contacts,
    OutsideView,
    AddQuestion,
    Footer,
    Breadcrumbs
  },
  data() {
    return {
      header_block: {},
      advantages_block: {},
      service_options_block: {},
      carton_info_block: {},
      contacts_block: {},
      outside_view: {},
      add_question_block: {},
      category_list: [],

      show: false
    }
  },
  created() {
    this.getPageData()
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero();

    document.title = 'О магазине | Магазин упаковки КУБ в Казани';
    this.setMetaTag('description', 'Узнайте больше о магазине упаковки КУБ, ведущем производителе картонных коробок и упаковок в Казани.');
    this.setMetaTag('keywords', 'о компании КУБ, производитель картонных коробок, упаковка Казань, история магазина, качество упаковки');
  },
  methods: {
    async getPageData() {
      await axios
          .get(`${this.backendURL}/api/v1/about_page/`)
          .then(response => {
            let receivedData = response.data

            this.header_block = receivedData.header_block
            this.advantages_block = receivedData.advantages_block
            this.service_options_block = receivedData.service_options_block
            this.carton_info_block = receivedData.carton_info_block
            this.contacts_block = receivedData.contacts_block
            this.outside_view = receivedData.outside_view
            this.add_question_block = receivedData.add_question_block
            this.category_list = receivedData.category_list

            this.show = true
          })
          .catch(error => {
            console.log('An error occurred: ', error);
          })
    },
    scrollToZero() {
      document.documentElement.scrollTop = 0;
    },
    setMetaTag(name, content) {
      let tag = document.querySelector(`meta[name="${name}"]`);
      if (!tag) {
        tag = document.createElement('meta');
        tag.setAttribute('name', name);
        document.head.appendChild(tag);
      }
      tag.setAttribute('content', content);
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