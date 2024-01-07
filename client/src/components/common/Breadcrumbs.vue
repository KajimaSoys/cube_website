<template>
  <div class="breadcrumb-component">
    <div class="breadcrumb-max">
      <div class="breadcrumb-content">
        <ul>
          <li
              v-for="(breadcrumb, idx) in breadcrumbList"
              :key="idx"
              @click="routeTo(idx)"
              :class="{'linked': !!breadcrumb.link}">
            {{ breadcrumb.name }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Breadcrumbs',
  data() {
    return {
      breadcrumbList: []
    }
  },
  mounted() {
    this.updateList()
  },
  watch: {
    '$route'() {
      this.updateList()
    },
  },
  methods: {
    routeTo(pRouteTo) {
      if (this.breadcrumbList[pRouteTo].link) this.$router.push(this.breadcrumbList[pRouteTo].link)
    },
    updateList() {
      this.breadcrumbList = JSON.parse(JSON.stringify(this.$route.meta.breadcrumb));
    }
  }
}
</script>


<style scoped>
.breadcrumb-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 12rem;
  padding-bottom: 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

.breadcrumb-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
}

.breadcrumb-content {
  font-size: 1rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  color: var(--black-55);
}

ul {
  display: flex;
  list-style-type: none;
  margin: 0;
  padding: 0;
  flex-wrap: wrap;
  gap: 1rem 0;
}

ul > li {
  display: flex;
  float: left;
  height: 10px;
  width: auto;
  cursor: default;
  align-items: center;
}

ul > li:not(:last-child)::after {
  content: '·';
  float: right;
  font-size: 1.5rem;
  margin: 0 .5em;
  cursor: default;
}

.linked {
  cursor: pointer;
  transition: opacity 0.2s ease-in-out;
}

.linked:hover {
  opacity: 0.5;
}

@media screen and (max-width: 1280px) {
  .breadcrumb-component {
    padding-top: 10rem;
  }

  .breadcrumb-max {
    padding: 0 2.25rem;
  }
}

@media screen and (max-width: 1000px) {
  .breadcrumb-component {
    padding-top: 8.75rem;
  }

  .breadcrumb-content {
    font-size: 0.875rem;
  }
}

@media screen and (max-width: 640px) {
  .breadcrumb-component {
    padding-top: 7.5rem;
    padding-bottom: 1rem;
  }

  .breadcrumb-max {
    padding: 0 1rem;
  }
}
</style>