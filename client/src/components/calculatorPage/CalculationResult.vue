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

        <div class="calculation-result-tip">
          В расчёте мы использовали введённые вами размеры. Ниже предлагаем подходящие товары из каталога. Количество штук уже указано в соответствии с расчётом.
        </div>

        <div class="suggested-products-block">
          <h3>Ваши товары</h3>
          <div class="suggested-products-list">
            <div class="suggested-product">
              <ProductCardHorizontal
                :product="outerBoxForOrder"
                :quantity="outerBoxQuantity"
                :removable="false"
                @remove-from-add-list="removeFromAddList"
              />
            </div>
            <div class="suggested-product">
              <ProductCardHorizontal
                :product="innerBoxForOrder"
                :quantity="innerBoxQuantity"
                :removable="false"
                @remove-from-add-list="removeFromAddList"
              />
            </div>
          </div>
        </div>

        <div class="additional-products-block" v-if="additionalProducts.length > 0">
          <h3>С этими товарами часто берут</h3>
          <div class="additional-products-list">

            <ProductCardHorizontal
              v-for="product in additionalProducts"
              :key="product.id"
              :product="product"
              :quantity="1"
              :removable="true"
              @remove-from-add-list="removeFromAddList"
            />
          </div>
        </div>

      </div>

      <div class="buttons">
        <div class="order-button button" @click="processToCart">
          Оформить заказ
        </div>

        <a
          class="contact-manager-button button"
          :href="get_whatsapp_text()"
          target="_blank"
        >
          Связаться с менеджером
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import ProductCardHorizontal from "../calculatorPage/ProductCardHorizontal.vue";

export default {
  name: "CalculationResult",
  inject: ['backendURL'],
  props: {
    calculationData: Object,
    additionalProductsDefault: Array,
    productList: Array
  },
  emits: [
      'add-to-cart'
  ],
  components: {
    ProductCardHorizontal
  },
  data() {
    return {
      displayDimensions: {"largeBox": "", "smallBox": ""},
      boxesPerBase: { length: 0, width: 0, total: 0 },
      boxesPerHeight: 0,
      totalBoxes: 0,
      outerBoxForOrder: null,
      outerBoxQuantity: 1,
      innerBoxForOrder: null,
      innerBoxQuantity: 1,
      additionalProducts: []
    }
  },
  methods: {
    convertDimensions(componentType, boxData) {
      let selectedType = boxData.selectedType;
      let parsedDimensions = boxData.parsedDimensions;
      let selectedSizeType = boxData.selectedSizeType;

      let { length, width, height } = parsedDimensions;
      if (componentType === 'outer' && selectedSizeType === 'outer') {
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
    },
    calculateDisplayDimensions(largeBox, smallBox) {
      if (!this.calculationData) return { largeBox: '', smallBox: '' };

      return {
        largeBox: `${largeBox.length}x${largeBox.width}x${largeBox.height}`,
        smallBox: `${smallBox.length}x${smallBox.width}x${smallBox.height}`,
      };
    },
    calculateBoxesPerBase(largeBox, smallBox) {
      if (!this.calculationData) return { length: 0, width: 0, total: 0 };

      const length = Math.floor(largeBox.length / smallBox.length);
      const width = Math.floor(largeBox.width / smallBox.width);
      const total = length * width;

      return { length, width, total };
    },
    calculateBoxesPerHeight(largeBox, smallBox) {
      if (!this.calculationData) return 0;

      return Math.floor(largeBox.height / smallBox.height);
    },
    calculateTotalBoxes() {
      return this.boxesPerBase.total * this.boxesPerHeight;
    },

    searchFittingBoxes(newVal) {
      const outerBoxDimensions = newVal.outer.parsedDimensions;
      const innerBoxDimensions = newVal.inner.parsedDimensions;
      const outerFittingBox = this.findBox(outerBoxDimensions, this.productList);
      const innerFittingBox = this.findBox(innerBoxDimensions, this.productList);

      this.outerBoxForOrder = outerFittingBox.match;
      this.innerBoxForOrder = innerFittingBox.match;
      this.innerBoxQuantity = this.totalBoxes

      // Перерасчет, если хотя бы один из размеров не точен
      if (!outerFittingBox.isExact || !innerFittingBox.isExact) {
        this.recalculateQuantities();
      }

      // Отображаем результаты
      this.displayResults(outerFittingBox.match, innerFittingBox.match);
    },

    findBox(size, boxes) {
      const exactMatch = boxes.find(box => {
        const boxSize = this.parseDimensionsFromString(box.size);
        return boxSize && boxSize.length === size.length && boxSize.width === size.width && boxSize.height === size.height;
      });
      if (exactMatch) return { match: exactMatch, isExact: true };

      // Поиск ближайшего размера, если точного соответствия нет
      let nearestBox = null;
      let minDifference = Infinity;
      boxes.forEach(box => {
        const boxSize = this.parseDimensionsFromString(box.size);
        if (boxSize) {
          const difference = Math.sqrt(
            Math.pow(boxSize.length - size.length, 2) +
            Math.pow(boxSize.width - size.width, 2) +
            Math.pow(boxSize.height - size.height, 2)
          );
          if (difference < minDifference) {
            minDifference = difference;
            nearestBox = box;
          }
        }
      });
      return { match: nearestBox, isExact: false };
    },

    recalculateQuantities() {
      if (!this.outerBoxForOrder || !this.innerBoxForOrder) {
        console.error('Внешняя или внутренняя коробка не определена');
        return;
      }

      const outerDimensions = this.parseDimensionsFromString(this.outerBoxForOrder.size);
      const innerDimensions = this.parseDimensionsFromString(this.innerBoxForOrder.size);

      if (!outerDimensions || !innerDimensions) {
        console.error('Ошибка при парсинге размеров коробок');
        return;
      }

      const countByFloor = Math.floor(outerDimensions.length / innerDimensions.length) *
                           Math.floor(outerDimensions.width / innerDimensions.width);
      const countByHeight = Math.floor(outerDimensions.height / innerDimensions.height);

      // const totalBoxes = countByFloor * countByHeight;
      // console.log(`Перерасчитанное количество коробок: ${totalBoxes}`);
      this.innerBoxQuantity = countByFloor * countByHeight;
    },

    // Парсинг размеров из строки
    parseDimensionsFromString(value) {
      const pattern = /(\d+([.,]\d+)?)[ xXхХ]+(\d+([.,]\d+)?)[ xXхХ]+(\d+([.,]\d+)?)$/;
      const match = value.replace(',', '.').match(pattern);
      if (match) {
        const [_, length, __, width, ___, height, ____] = match.map(Number);
        return { length, width, height };
      }
      return null;
    },

    displayResults(outerBox, innerBox) {
      console.log(`Внешняя коробка: ${outerBox.name}, Внутренняя коробка: ${innerBox.name}`);
    },

    removeFromAddList (productId) {
      this.additionalProducts = this.additionalProducts.filter(product => product.id !== productId);
    },

    initializeCalculations() {
      if (!this.calculationData) return;
      const largeBox = this.convertDimensions('outer', this.calculationData.outer);
      const smallBox = this.convertDimensions('inner', this.calculationData.inner);
      this.displayDimensions = this.calculateDisplayDimensions(largeBox, smallBox);
      this.boxesPerBase = this.calculateBoxesPerBase(largeBox, smallBox);
      this.boxesPerHeight = this.calculateBoxesPerHeight(largeBox, smallBox);
      this.totalBoxes = this.calculateTotalBoxes();
      this.searchFittingBoxes(this.calculationData);
      this.additionalProducts = [...this.additionalProductsDefault];
    },

    processToCart() {
      if (this.outerBoxForOrder.count > 0) {
        this.$emit('add-to-cart', this.outerBoxForOrder.id, this.outerBoxForOrder.count)
      }
      if (this.innerBoxForOrder.count > 0) {
        this.$emit('add-to-cart', this.innerBoxForOrder.id, this.innerBoxForOrder.count)
      }
      if (this.additionalProducts.length > 0) {
        this.additionalProducts.forEach(product => {
          this.$emit('add-to-cart', product.id, product.count)
        })
      }

      this.$router.push({name: 'cart'});

    },

    get_whatsapp_text(){
      let greet_message = `Здравствуйте! На странице калькулятора я получил(-а) следующие результаты: %0D%0A
Большая коробка ${this.displayDimensions.largeBox} мм. (внутренние размеры) %0D%0A
Маленькая коробка ${this.displayDimensions.smallBox} мм. (внешние размеры) %0D%0A
По дну: ${this.boxesPerBase.length} x ${this.boxesPerBase.width} = ${this.boxesPerBase.total} шт. %0D%0A
В высоту: ${this.boxesPerHeight} шт. %0D%0A
Итого: ${this.totalBoxes} шт. %0D%0A%0D%0A`
      return `https://api.whatsapp.com/send/?type=phone_number&app_absent=0&phone=79950071654&text=${greet_message}`
    }
  },
  watch: {
    additionalProductsDefault: {
      handler(newVal) {
        this.additionalProducts = newVal
      },
      deep: true,
      immediate: true
    },
    calculationData: {
      handler: "initializeCalculations",
      deep: true,
      immediate: true
    },
  }
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
  gap: 2rem;
}

.calculation-result-text {
  width: 60%;
}

.calculation-result-tip {
  margin-bottom: 2rem;
  color: #3F6F4C;
  background-color: #D9EBDE;
  font-size: 1rem;
  padding: 0.875rem 1rem;
  border-radius: 0.5rem;
  width: 68%;
}

h3 {
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.suggested-products-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.additional-products-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.buttons {
  display: flex;
  flex-direction: row;
  gap: 1rem;
}

.button {
  padding: 1rem 6rem;
  height: 2.5rem;

  display: flex;
  justify-content: center;
  align-items: center;

  border-radius: 0.5rem;
  border: 2px solid var(--green-light);
  text-decoration: none;
  cursor: pointer;
  user-select: none;
  opacity: 1;

  transition: all 0.2s ease-in-out;
}

.order-button {
  background: var(--green-light, #40AB5E);
  color: white;
}

.order-button:hover {
  opacity: 0.5;
}

.contact-manager-button {
  color: var(--green-primary);
}

.contact-manager-button:hover {
  background: var(--green-light, #40AB5E);
  color: white;
}

@media screen and (max-width: 1280px) {
  .calculation-result-component {
    padding-top: 4rem;
  }

  .calculation-result-max {
    padding: 0 2.25rem;
  }

  .calculation-result-content {
    padding: 1.5rem;
    justify-content: space-between;
  }

  .calculation-result-text {
    width: 70%;
  }

  .calculation-result-tip {
    width: 77%;
    margin-bottom: unset;
  }

  .button {
    flex: 1;
    height: 2rem;
  }
}

@media screen and (max-width: 1000px) {
  .calculation-result-max {
    gap: 1rem;
  }

  .calculation-result-component {
    padding-top: 2.75rem;
  }

  h2 {
    font-size: 1.5rem;
  }

  .calculation-result-content {
    padding: 1rem;
    border-radius: 1rem;
  }

  .calculation-result-text {
    width: 100%;
  }

  .calculation-result-tip {
    width: -webkit-fill-available;
    width: -moz-fill-available;
    font-size: 0.875rem;
  }

  h3 {
    font-size: 1.25rem;
  }

  .button {
    padding: 1rem 1rem;
    height: 1.125rem;
  }
}

@media screen and (max-width: 640px) {
  .calculation-result-max {
    padding: 0 1rem;
  }

  .calculation-result-component {
    padding-top: 4rem;
  }

  .buttons {
    flex-direction: column;
    gap: 0.5rem;
  }

  .button {
    padding: 0.9125rem 1rem;
    height: 1rem;
  }
}
</style>