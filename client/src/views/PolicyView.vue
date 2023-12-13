<template>
  <Header/>

  <Footer/>
</template>

<script>
import Header from "../components/common/Header.vue";

import Footer from "../components/common/Footer.vue";

export default {
  name: "PolicyView",
  components: {
    Header,
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