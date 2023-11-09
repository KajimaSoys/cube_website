if (window.jQuery) {
    $(document).ready(function (jQuery) {
        jQuery(function ($) {
            if (window.location.href.indexOf("/change/") !== -1 || window.location.href.indexOf("/add/") !== -1) {
                // masking для полей номера и даты
                $('#id_phone_number').mask("8 (999) 999-99-99", {autoclear: false});
                $('#id_created_at_0').mask("99.99.9999", {autoclear: false});

                // Ссылка на whatsapp
                let whatsappDiv = $(".field-whatsapp_link > div > div");
                let whatsappText = whatsappDiv.text();

                if (whatsappText) {
                    let whatsappLink = $("<a>");
                    whatsappLink.attr("href", whatsappText);
                    whatsappLink.attr("target", "_blank");
                    whatsappLink.text(whatsappText)
                    whatsappLink.attr("style", "bottom: -9px; position: relative;")
                    whatsappDiv.replaceWith(whatsappLink);
                }
                else {
                    whatsappDiv.text('Сохраните заказ, чтобы получить ссылку')
                }

                // Поле для комментария
                $("textarea").attr({"rows": "3",
                        "cols": "54"
                });


                // Блок обработки true/false на поле самовывоза
                let address = $('.form-row.field-address');
                let pickup = $('input#id_pickup');
                if (pickup.prop('checked')) {
                    address.hide();
                }

                pickup.on('change', function() {
                    if (pickup.prop('checked')){
                        address.hide();
                    } else {
                        address.show();
                    }
                });


                // Блок с расчетом итоговой стоимости
                // Присваиваем элементу строку с итоговой стоимостью
                let total_fieldset = $(".module.aligned ")[1]

                // вставляем наш элемент после inline поля
                $(".js-inline-admin-formset.inline-group")[0].after(total_fieldset)

                listenersInit()
                calculateTotal()

                // Метод привязывающий листенер к инлайну
                function activateListener(element, type) {
                    if (type === 'product') {
                        let instance = element
                        console.log(element)
                        $(`#id_${instance}-product, #id_${instance}-count`).change(function () {
                            console.log('change on: ' + element)

                            // Находим селект инлайна
                            let select = $(`select#id_${instance}-product`)
                            let value = select.val();

                            let count = $(`#id_${instance}-count`).val();

                            $.ajax({
                                url: `/api/v1/get_price/`,
                                method: 'GET',
                                data: {
                                    'product_id': value,
                                    'count': count
                                },
                                success: function (res) {
                                    let price = res.price * count;

                                    if (isFloat(price)) {
                                        price = Math.round(price * 100) / 100;
                                    }

                                    $(`#id_${instance}-price`).val(price);

                                    // Подсчет итоговой стоимости
                                    calculateTotal()
                                },
                                error: function (err) {
                                    console.error('Ошибка при получении цены:', err);
                                }
                            });


                        });
                    }


                    $(`#${element} > h3 > span:nth-child(3) > a`).on('click', function () {
                        calculateTotal()
                    })
                }


                function listenersInit() {
                    let inlines = $('.inline-related.dynamic-productlist_set').toArray()
                    inlines.forEach(element => {
                        element = element['id']
                        // Берем только существующие инлайны
                        if (element !== 'productlist_set-empty') {
                            // Вешаем листенеры на каждый существующий инлайн
                            activateListener(element, 'product')
                        }
                    });
                }


                function newListenerInit(type) {
                    let inlines = $(`.inline-related.dynamic-${type}list_set`).toArray()
                    let element = inlines.at(-1)['id']
                    activateListener(element, type)
                }


                $(".add-row").on('click', function () {
                    if (this['textContent'].includes("Товар")) {
                        newListenerInit('product')
                    }
                })


                function calculateTotal() {
                    console.log('calcultaing')
                    var inlines = $('.inline-related.dynamic-productlist_set').toArray()
                    let total = 0
                    inlines.forEach(element => {
                        element = element['id']

                        if (element !== 'productlist_set-empty') {
                            let price = $(`#id_${element}-price`).val()
                            total = total + parseFloat(price)
                        }
                    });

                    if (isFloat(total)) {
                        total = Math.round(total * 100) / 100
                    }
                    console.log(total)
                    id_total.value = total
                }

                function isFloat(value) {
                    if (
                        typeof value === 'number' &&
                        !Number.isNaN(value) &&
                        !Number.isInteger(value)
                    ) {
                        return true;
                    }

                    return false;
                }

                console.log('orders_fields.js работает штатно');

                $("#id_total").attr("readOnly", true);

                var frm = $('form');
                var chosenBtn = frm.find('[name="_save"]');
                var btns = frm.find('[name="_save"], [name="_addanother"], [name="_continue"]');
                btns.unbind('click.btnAssign').bind('click.btnAssign', function (e) {
                    chosenBtn = $(this);
                });
                frm.unbind('submit.saveStuff').bind('submit.saveStuff', function (e) {
                    // Add your own validation here. If the validation fails, you can call:
                    // e.preventDefault();
                    // But if it works, no need for that line. If everything works...
                    calculateTotal()
                    // $("#id_total").attr("disabled", false);
                    $("#id_total").attr("readOnly", false);

                    frm.append(
                        [
                            '<input type="hidden" name="',
                            chosenBtn.attr('name'),
                            '" value="',
                            chosenBtn.attr('value'), // or maybe chosenBtn.text()
                            '" />'
                        ].join(''));
                });
            }
        })
    });
}