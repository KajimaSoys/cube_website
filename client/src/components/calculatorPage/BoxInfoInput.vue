<template>
<div class="box-info-input-content">
  <h3 v-if="componentType==='external'">
    Внешняя коробка
  </h3>
  <h3 v-else-if="componentType==='inner'">
    Внутренняя коробка или товар
  </h3>


  <div class="type-choice">
      <div
        class="type-choice-btn"
        :class="{ 'type-choice-btn-active': selectedType === 'self-assembled'}"
        @click="selectType('self-assembled')">
        Самосборная
      </div>
      <div
        class="type-choice-btn"
        :class="{ 'type-choice-btn-active': selectedType === 'four-valve' }"
        @click="selectType('four-valve')">
        Четырёхклапанная
      </div>
    </div>

  <div class="box-info-input">
    <span class="box-info-input-label">
      Введите размеры (ДxШxВ)
    </span>

    <input type="text"
           placeholder="100*100*100"
           v-model="dimensions"
           @input="validateField"
           maxlength="15"
           class="dimensions-input"
           :class="{'error-border': !isInputValid && isSubmitted}"
    >

    <div v-if="suggestions.length" class="suggestions">
      <div v-for="suggestion in suggestions" :key="suggestion.id" class="suggestion">
        {{ suggestion.name }} ({{ suggestion.dimensions }})
      </div>
    </div>

  </div>

  <div class="radio-buttons-container">
    <div class="radio-buttons">
      <div class="radio-button">
        <input type="radio" :id="innerRadioId" :name="uniqueName" value="inner" v-model="selectedSizeType">
        <label :for="innerRadioId">Внутренний размер</label>
      </div>

      <div class="radio-button">
        <input type="radio" :id="externalRadioId" :name="uniqueName" value="external" v-model="selectedSizeType">
        <label :for="externalRadioId">Внешний размер</label>
      </div>
    </div>

    <div class="hint">
      Выпадающий список с вариантами размеров
    </div>
  </div>

</div>
</template>

<script>
export default {
  name: "BoxInfoInput",
  inject: ['backendURL'],
  props: {
    componentType: String,
    defaultType: {
      type: String,
      default: 'self-assembled'
    },
    isSubmitted: {
      type: Boolean,
      default: false
    }
  },
  components: {},
  data() {
    return {
      selectedType: this.defaultType,
      selectedSizeType: 'inner',
      dimensions: '',
      suggestions: [],
      uniqueId: '',
      isInputValid: false
    }
  },

  created() {
    // Generate a unique ID for each instance
    this.uniqueId = `_${Math.random().toString(36).substr(2, 9)}`;
  },
  mounted() {
  },
  computed: {
    uniqueName() {
      return `size_type_${this.uniqueId}`;
    },
    innerRadioId() {
      return `inner_${this.uniqueId}`;
    },
    externalRadioId() {
      return `external_${this.uniqueId}`;
    }
  },
  methods: {
    selectType(type) {
      this.selectedType = type;
    },
    validateField(event) {
      const allowedCharacters = /[^0-9* xXхХ]/g;
      this.dimensions = event.target.value.replace(allowedCharacters, '');
      this.isInputValid = this.parseDimensions(this.dimensions);
    },
    parseDimensions(value) {
      const pattern = /(\d+)\D+(\d+)\D+(\d+)/;
      const match = value.match(pattern);
      if (match) {
        const [_, length, width, height] = match;
        console.log(`Parsed dimensions: Length=${length}, Width=${width}, Height=${height}`);
        return true; // Valid input
      }
      return false; // Invalid input
    }

  },
}
</script>


<style scoped>
.box-info-input-content {
  border-radius: 1.5rem;
  background: #FFF;

  padding: 2rem 2rem 1.25rem 2rem;
  width: -webkit-fill-available;
  width: -moz-fill-available;

  display: flex;
  flex-direction: column;
  gap: 1rem;
}

h3 {
  font-size: 1.5rem;
  margin-bottom: 0.75rem;
}

.type-choice {
  display: flex;
  flex-direction: row;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
}

.type-choice-btn {
  padding: 0.5rem 0.75rem;
  background-color: #e8e8e8;
  border-radius: 0.35rem;
  cursor: pointer;
  font-size: 1rem;
  user-select: none;
  transition: all 0.2s;
}

.type-choice-btn:not(.type-choice-btn-active):hover {
  opacity: 0.5;
}

.type-choice-btn-active {
  background-color: #4d4d4d;
  color: white;
}

.box-info-input {
  display: flex;
  flex-direction: column;
}

.box-info-input-label {
  font-size: 0.975rem;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.dimensions-input {
  padding: 0.5rem 1rem;
  font-size: 1rem;
  border: 1px solid var(--black-20);
  border-radius: 0.35rem;
  outline: none;
  resize: none;
  line-height: 1.5;
  width: -webkit-fill-available;
  width: -moz-fill-available;
  transition: all 0.2s ease-in-out;
}

.dimensions-input::placeholder {
  color: var(--black-20);
}

.dimensions-input:focus {
  border-color: var(--black-55);
}

.error-border {
  border-color: #ff5c7e !important;
  box-shadow: 0 1px 2px 0 rgba(16, 24, 40, 0.05), 0 0 0 4px #fdbecb !important;
}

.suggestions {
  margin-top: 0.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.suggestion {
  padding: 0.5rem;
  background-color: #f0f0f0;
  border-radius: 0.25rem;
  cursor: pointer;
}

.suggestion:hover {
  background-color: #e0e0e0;
}

.radio-buttons-container {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  justify-content: space-between;
}

.radio-buttons {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.radio-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.radio-buttons input[type="radio"] {
  appearance: none;
  background-color: #fff;
  margin: 0;
  font: inherit;
  color: currentColor;
  width: 1em;
  height: 1em;
  border: 0.15em solid currentColor;
  border-radius: 50%;
  transform: translateY(-0.075em);
  display: grid;
  place-content: center;
  cursor: pointer;
}

.radio-buttons input[type="radio"]::before {
  content: "";
  width: 0.67em;
  height: 0.65em;
  border-radius: 50%;
  transition: transform 0.2s ease-in-out;
  transform: scale(0);
  box-shadow: inset 1em 1em currentColor;
}

.radio-buttons input[type="radio"]:checked::before {
  transform: scale(1);
}

.radio-button label {
  user-select: none;
  font-weight: 500;
  cursor: pointer;
}

.hint {
  width: 13rem;
  color: var(--black-35);
  font-weight: 500;
}

@media screen and (max-width: 1280px) {
  .box-info-input-content {
    padding: 3rem 7rem 4rem 3rem;
    justify-content: space-between;
  }
}

@media screen and (max-width: 1000px) {
  .box-info-input-content {
    padding: 3rem 4.5rem 4rem 2.25rem;
  }
}

@media screen and (max-width: 640px) {
  .box-info-input-content {
    padding: 2rem 4.5rem 3rem 4.5rem;
    flex-direction: column;
    gap: 1.5rem;
  }
}
</style>