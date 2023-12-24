from django.shortcuts import render
from django.http import JsonResponse
from pages.main_page.models import (
    MainBlock,
    CatalogTeaserBlock,
    ServiceOptionsBlock,
    NewProductBlock,
    PopularProductBlock,
    DeliveryBlock,
    AdvantagesBlock,
    CartonInfoBlock,
    RequestBlock,
    QuestionsBlock,
    ContactsBlock,
)
from pages.main_page.serializers import (
    MainBlockSerializer,
    CatalogTeaserBlockSerializer,
    ServiceOptionsBlockSerializer,
    NewProductBlockSerializer,
    PopularProductBlockSerializer,
    DeliveryBlockSerializer,
    AdvantagesBlockSerializer,
    CartonInfoBlockSerializer,
    RequestBlockSerializer,
    QuestionsBlockSerializer,
    ContactsBlockSerializer,
)
from pages.common_elements.models import (
    HeaderBlock,
    AddQuestionBlock
)
from pages.common_elements.serializers import (
    HeaderBlockSerializer,
    AddQuestionBlockSerializer
)

from shop.models import Category
from shop.serializers import CategorySerializer


def aggregate_data(request):
    try:
        response_data = {}

        header_block = HeaderBlock.objects.first()

        main_block = MainBlock.objects.first()
        catalog_teaser_block = CatalogTeaserBlock.objects.first()
        category_list = Category.objects.all()
        service_options_block = ServiceOptionsBlock.objects.first()

        new_product_block = NewProductBlock.objects.select_related("product").all()
        popular_product_block = PopularProductBlock.objects.select_related("product").all()

        delivery_block = DeliveryBlock.objects.first()
        advantages_block = AdvantagesBlock.objects.first()
        carton_info_block = CartonInfoBlock.objects.first()
        request_block = RequestBlock.objects.first()
        questions_block = QuestionsBlock.objects.all()
        contacts_block = ContactsBlock.objects.first()
        add_question_block = AddQuestionBlock.objects.first()

        if header_block:
            response_data['header_block'] = HeaderBlockSerializer(header_block).data
        if main_block:
            response_data['main_block'] = MainBlockSerializer(main_block).data
        if catalog_teaser_block:
            response_data['catalog_teaser_block'] = CatalogTeaserBlockSerializer(catalog_teaser_block).data
        if category_list:
            response_data['category_list'] = CategorySerializer(category_list, many=True).data
        if service_options_block:
            response_data['service_options_block'] = ServiceOptionsBlockSerializer(service_options_block).data
        if new_product_block:
            response_data['new_product_block'] = NewProductBlockSerializer(new_product_block, many=True).data
        if popular_product_block:
            response_data['popular_product_block'] = PopularProductBlockSerializer(popular_product_block,  many=True).data
        if delivery_block:
            response_data['delivery_block'] = DeliveryBlockSerializer(delivery_block).data
        if advantages_block:
            response_data['advantages_block'] = AdvantagesBlockSerializer(advantages_block).data
        if carton_info_block:
            response_data['carton_info_block'] = CartonInfoBlockSerializer(carton_info_block).data
        if request_block:
            response_data['request_block'] = RequestBlockSerializer(request_block).data
        if questions_block:
            response_data['questions_block'] = QuestionsBlockSerializer(questions_block, many=True).data
        if contacts_block:
            response_data['contacts_block'] = ContactsBlockSerializer(contacts_block).data
        if add_question_block:
            response_data['add_question_block'] = AddQuestionBlockSerializer(add_question_block).data

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

