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
            <!--@add-to-cart="addToCart"-->
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
import ProductCardHorizontal from "../calculatorPage/ProductCardHorizontal.vue";

export default {
  name: "CalculationResult",
  inject: ['backendURL'],
  props: {
    calculationData: Object,
    additionalProductsDefault: Array,
    productList: Array
  },
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
    calculateBoxesPerBase() {
      if (!this.calculationData) return { length: 0, width: 0, total: 0 };

      const length = Math.floor(largeBox.length / smallBox.length);
      const width = Math.floor(largeBox.width / smallBox.width);
      const total = length * width;

      return { length, width, total };
    },
    calculateBoxesPerHeight() {
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
      const pattern = /(\d+(\.\d+)?)[ xXхХ]+(\d+(\.\d+)?)[ xXхХ]+(\d+(\.\d+)?)$/;
      const match = value.match(pattern);
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
      handler(newVal) {
        const largeBox = this.convertDimensions('outer', newVal.outer);
        const smallBox = this.convertDimensions('inner', newVal.inner);

        this.displayDimensions = this.calculateDisplayDimensions(largeBox, smallBox)
        this.boxesPerBase = this.calculateBoxesPerBase(largeBox, smallBox)
        this.boxesPerHeight = this.calculateBoxesPerHeight(largeBox, smallBox)
        this.totalBoxes = this.calculateTotalBoxes(largeBox, smallBox)
        if (newVal) {
          this.searchFittingBoxes(newVal)
        }
        this.additionalProducts = [...this.additionalProductsDefault];
      },
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
  gap: 4rem;
}

.calculation-result-text {
  width: 60%;
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

  .additional-products-list {
    gap: 0.5rem;
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