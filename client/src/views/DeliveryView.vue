<template>
  <Header/>

  <Delivery/>

  <Payment/>

  <RecommendedProduct/>

  <AddQuestion/>

  <Footer/>
</template>

<script>
import Header from "../components/common/Header.vue";
import Delivery from "../components/mainPage/Delivery.vue";
import Payment from "../components/deliveryPage/Payment.vue";
import RecommendedProduct from "../components/common/RecommendedProduct.vue";
import AddQuestion from "../components/common/AddQuestion.vue";
import Footer from "../components/common/Footer.vue";

export default {
  name: "DeliveryView",
  components: {
    Header,
    Delivery,
    Payment,
    RecommendedProduct,
    AddQuestion,
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