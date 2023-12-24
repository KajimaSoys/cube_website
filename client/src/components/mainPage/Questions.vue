<template>
  <div class="questions-component">
    <div class="questions-max">
      <h2 class="title">
        Частые вопросы
      </h2>

      <div class="content">
        <div v-for="question in questions_block" :key="question.id" class="question-card"
             @click="toggleAnswer(question.id)">
          <div class="question-content">
            <h3>{{ question.question }}</h3>
            <div class="icon"
                 :style="{ transform: openQuestions.includes(question.id) ? 'rotate(45deg)' : 'rotate(0deg)' }">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M12 2V22M2 12H22" stroke="#40AB5E" stroke-width="2" stroke-linecap="round"/>
              </svg>
            </div>
          </div>
          <div class="answer" :class="{ 'answer-visible': openQuestions.includes(question.id)}"
               v-html="question.answer">
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "Questions",
  props: {
    questions_block: Array,
  },
  components: {},
  data() {
    return {
      openQuestions: [],
      showAll: false,
    }
  },
  mounted() {
  },
  computed: {
    shownQuestions() {
      return this.showAll ? this.questions_block : this.questions_block.slice(0, 4);
    },
  },
  methods: {
    toggleAnswer(id) {
      const index = this.openQuestions.indexOf(id);
      if (index === -1) {
        this.openQuestions.push(id);
      } else {
        this.openQuestions.splice(index, 1);
      }
    },
    toggleAllQuestions() {
      this.showAll = !this.showAll;
    },
  },
}
</script>


<style scoped>
.questions-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 9rem;

  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.questions-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
}

.content {
  margin-top: 4rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.question-card {
  cursor: pointer;
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
  user-select: none;

  border-radius: 1rem;
  background: #FFF;

  padding: 1.5rem 2rem 1.5rem 2rem;
}

.question-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  line-height: normal;
  text-align: left;
  height: 3.25rem;
}

h3 {
  cursor: pointer;
  font-size: 1.5rem;
  font-style: normal;
  font-weight: 500;
}

.icon {
  transition: transform 0.3s ease, background-color 0.2s ease-in-out;
  display: flex;
  cursor: pointer;
  padding: 12px;
  border-radius: 50%;
}

.question-card:hover .icon {
  background-color: var(--green-light);

}

.icon path {
  transition: stroke 0.2s ease-in-out;
}

.question-card:hover path {
  stroke: white;
}

.answer {
  margin-top: 0;

  font-size: 1.125rem;
  font-style: normal;
  font-weight: 400;
  line-height: 150%;
  text-align: left;
  height: 0;
  transition: all 0.3s ease;
}


:deep(.answer p) {
  opacity: 0;
  transition: all 0.2s ease;
}

.answer-visible {
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
  height: unset;
}

:deep(.answer-visible p) {
  opacity: 1;
}

@media screen and (max-width: 1280px) {
  .questions-component {
    padding-top: 8rem;
  }

  .questions-max {
    padding: 0 2.25rem;
  }

  .content {
    margin-top: 2rem;
  }
}

@media screen and (max-width: 1000px) {
  .questions-component {
    padding-top: 5rem;
  }

  .question-card {
    padding: 1.5rem;
  }

  h3 {
    font-size: 1.25rem;
    width: 80%;
  }

  .answer {
    font-size: 1rem;
  }

  .answer-visible {
    margin-top: 1rem;
    margin-bottom: 1rem;
  }

}

@media screen and (max-width: 640px) {
  .questions-component {
    padding-top: 4.4rem;
  }

  .questions-max {
    padding: 0 1rem;;
  }

  .content {
    gap: 0.5rem;
  }

  .question-card {
    padding: 1rem;
  }

  .question-content {
    height: unset;
  }

  h3 {
    font-size: 1rem;
  }

  .icon svg {
    width: 1rem;
    height: 1rem;
  }

  .answer {
    font-size: 0.875rem;
  }
}
</style>