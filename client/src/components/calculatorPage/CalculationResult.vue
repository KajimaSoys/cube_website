<template>
<div v-if="calculationData" class="calculation-result-component" id="calculation-result">
    <div class="calculation-result-max">

      <h2>Расчет</h2>
      <div  class="calculation-result-content">
        <div class="calculation-result-text">
          Большая коробка {{ displayDimensions.largeBox }} мм. (внутренние размеры)
          <br>
          Маленькая коробка {{ displayDimensions.smallBox }} мм. (внешние размеры)
          <br>
          По дну: {{ boxesPerBase.length }} x {{ boxesPerBase.width }} = {{ boxesPerBase.total }} шт.
          <br>
          В высоту: {{ boxesPerHeight }} шт.
          <br>
          Итого: {{ totalBoxes }} шт. коробок или товаров поместится в большую коробку
          <br>
          <br>
          Возможны погрешности. Чтобы всё точно поместилось, замерьте ваши товары с небольшим запасом или проверьте всё ещё раз у нас в магазине, продавец вам поможет
          <br>
          <br>
          Калькулятор не учитывает размер прокладок между рядами.
        </div>

        <div class="suggested-products-block">
          <h3>Ваши товары</h3>
          <div class="suggested-products-list">
            <div class="suggested-product">
              1
            </div>
            <div class="suggested-product">
              2
            </div>
          </div>
        </div>

        <div class="additional-products-block">
          <h3>С этими товарами часто берут</h3>
          <div class="additional-products-list">
            <div class="additional-product">
              1
            </div>
            <div class="additional-product">
              2
            </div>
          </div>
        </div>

      </div>

      <div class="buttons">
        <div class="order-button button">
          Оформить заказ
        </div>

        <div class="contact-manager-button button">
          Связаться с менеджером
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CalculationResult",
  inject: ['backendURL'],
  props: ['calculationData'],
  components: {},
  data() {
    return {
    }
  },
  computed: {
    displayDimensions() {
      if (!this.calculationData) return { largeBox: '', smallBox: '' };

      const largeBox = this.convertDimensions('external', this.calculationData.external);
      const smallBox = this.convertDimensions('inner', this.calculationData.inner);

      return {
        largeBox: `${largeBox.length}x${largeBox.width}x${largeBox.height}`,
        smallBox: `${smallBox.length}x${smallBox.width}x${smallBox.height}`,
      };
    },
    boxesPerBase() {
      if (!this.calculationData) return { length: 0, width: 0, total: 0 };

      const largeBox = this.convertDimensions('external', this.calculationData.external);
      const smallBox = this.convertDimensions('inner', this.calculationData.inner);

      const length = Math.floor(largeBox.length / smallBox.length);
      const width = Math.floor(largeBox.width / smallBox.width);
      const total = length * width;

      return { length, width, total };
    },
    boxesPerHeight() {
      if (!this.calculationData) return 0;

      const largeBox = this.convertDimensions('external', this.calculationData.external);
      const smallBox = this.convertDimensions('inner', this.calculationData.inner);
      
      return Math.floor(largeBox.height / smallBox.height);
    },
    totalBoxes() {
      return this.boxesPerBase.total * this.boxesPerHeight;
    }
  },
  mounted() {
  },
  methods: {
    convertDimensions(componentType, boxData) {
      let selectedType = boxData.selectedType;
      let parsedDimensions = boxData.parsedDimensions;
      let selectedSizeType = boxData.selectedSizeType;

      let { length, width, height } = parsedDimensions;
      if (componentType === 'external' && selectedSizeType === 'external') {
        if (selectedType === 'self-assembled') {
          // console.log('Большая коробка внешний размер самосборной во внутренний размер')
          length -= 0.8;
          width -= 0.2;
          height -= 0.2;
        } else if (selectedType === 'four-valve') {
          // console.log('Большая коробка внешний размер четырехклапанной во внутренний размер')
          length -= 0.5;
          width -= 0.5;
          height -= 0.5;
        }
      } else if (componentType === 'inner' && selectedSizeType === 'inner') {
          if (selectedType === 'self-assembled') {
            // console.log('Маленькая коробка внутренний размер самосборной во внешний размер')
            length += 0.8;
            width += 0.2;
            height += 0.2;
          } else if (selectedType === 'four-valve') {
            // console.log('Маленькая коробка внутренний размер четырехклапанной во внешний размер')
            length += 0.5;
            width += 0.5;
            height += 0.5;
          }
      }
      return { length, width, height };
    }
  },
}
</script>


<style scoped>
.calculation-result-component {
  margin-left: auto;
  margin-right: auto;
  padding-top: 5rem;

  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.calculation-result-max {
  max-width: 76.3rem;
  padding: 0 6.8rem;
  width: 100%;
  position: relative;
  display: flex;
  flex-direction: column;

  gap: 2rem;
}

h2 {
  font-size: 2rem;
}

.calculation-result-content {
  border-radius: 1.5rem;
  background: #FFF;

  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 4rem;
}

.calculation-result-text {
  width: 60%;
}

h3 {
  margin-bottom: 1rem;
  font-size: 1.5rem;
}
.buttons {
  display: flex;
  flex-direction: row;
  gap: 1rem;
}

.order-button {
  padding: 1rem 6rem;
  height: 2.5rem;

  display: flex;
  justify-content: space-between;
  align-items: center;

  border-radius: 0.5rem;
  border: 2px solid var(--green-light);
  background: var(--green-light, #40AB5E);
  text-decoration: none;
  cursor: pointer;
  color: white;
  user-select: none;
  opacity: 1;

  transition: all 0.2s ease-in-out;
}

.order-button:hover {
  opacity: 0.5;
}

.contact-manager-button {
  padding: 1rem 6rem;
  height: 2.5rem;

  display: flex;
  justify-content: space-between;
  align-items: center;

  border-radius: 0.5rem;
  border: 2px solid var(--green-light);
  text-decoration: none;
  cursor: pointer;
  color: var(--green-primary);
  user-select: none;

  transition: all 0.2s ease-in-out;
}

.contact-manager-button:hover {
  background: var(--green-light, #40AB5E);
  color: white;
}

@media screen and (max-width: 1280px) {
  .calculation-result-component {
    padding-top: 8rem;
  }

  .calculation-result-max {
    padding: 0 2.25rem;
  }

  .calculation-result-content {
    padding: 3rem 7rem 4rem 3rem;
    justify-content: space-between;
  }
}

@media screen and (max-width: 1000px) {
  .calculation-result-max {
    padding: 0;
  }

  .calculation-result-component {
    padding-top: 5rem;
  }

  .calculation-result-content {
    padding: 3rem 4.5rem 4rem 2.25rem;
  }
}

@media screen and (max-width: 640px) {
  .calculation-result-component {
    padding-top: 4.4rem;
  }

  .calculation-result-max {
    gap: 0.5rem;
  }

  .calculation-result-content {
    padding: 2rem 4.5rem 3rem 4.5rem;
    flex-direction: column;
    gap: 1.5rem;
  }
}
</style>