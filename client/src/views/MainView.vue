<template>
  <Header/>

  <Main/>

  <CatalogTeaser/>

  <ServiceOptions/>

  <NewProduct/>

  <PopularProduct/>

  <Delivery/>

  <Advantages/>

  <CartonInfo/>

  <Request/>

  <Questions/>

  <Contacts/>

  <Footer/>
</template>

<script>
import Header from "../components/common/Header.vue";
import Main from "../components/mainPage/Main.vue"
import CatalogTeaser from "../components/mainPage/CatalogTeaser.vue"
import ServiceOptions from "../components/mainPage/ServiceOptions.vue"
import NewProduct from "../components/mainPage/NewProduct.vue"
import PopularProduct from "../components/mainPage/PopularProduct.vue"
import Delivery from "../components/mainPage/Delivery.vue"
import Advantages from "../components/mainPage/Advantages.vue"
import CartonInfo from "../components/mainPage/CartonInfo.vue"
import Request from "../components/mainPage/Request.vue"
import Questions from "../components/mainPage/Questions.vue"
import Contacts from "../components/mainPage/Contacts.vue"
import Footer from "../components/common/Footer.vue";

export default {
  name: "MainView",
  components: {
    Header,
    Main,
    CatalogTeaser,
    ServiceOptions,
    NewProduct,
    PopularProduct,
    Delivery,
    Advantages,
    CartonInfo,
    Request,
    Questions,
    Contacts,
    Footer
  },
  data() {
    return {}
  },
  mounted() {
    document.body.style.overflow = "";
    this.scrollToZero();
  },
  methods: {
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