<template>
  <Header
      :header_block="header_block"
  />

  <div v-if="show">

    <Breadcrumbs/>

    <Contacts
        :contacts_block="contacts_block"
        :separate="true"
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
import Contacts from "../components/mainPage/Contacts.vue";
import OutsideView from "../components/contactsPage/OutsideView.vue";
import AddQuestion from "../components/common/AddQuestion.vue";
import Footer from "../components/common/Footer.vue";
import Breadcrumbs from "../components/common/Breadcrumbs.vue";
import axios from "axios";
import Advantages from "../components/mainPage/Advantages.vue";

export default {
  name: "ContactsView",
  inject: ['backendURL'],
  components: {
    Advantages,
    Header,
    Contacts,
    OutsideView,
    AddQuestion,
    Footer,
    Breadcrumbs
  },
  data() {
    return {
      header_block: {},
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

    document.title = 'Контакты | Магазин упаковки КУБ в Казани';
    this.setMetaTag('description', 'Свяжитесь с магазином упаковки КУБ в Казани для заказа картонных коробок и упаковок. Телефон, адрес, электронная почта для удобства клиентов.');
    this.setMetaTag('keywords', 'контакты КУБ, упаковка Казань, заказ коробок, адрес магазина, телефон магазина упаковки');


    window.ym(96164548, 'hit', window.location.href);
  },
  methods: {
    async getPageData() {
      await axios
          .get(`${this.backendURL}/api/v1/contacts_page/`)
          .then(response => {
            let receivedData = response.data

            this.header_block = receivedData.header_block
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