from django.shortcuts import render
from django.http import JsonResponse
from pages.delivery_page.models import PaymentBlock
from pages.delivery_page.serializers import PaymentBlockSerializer
from pages.main_page.models import DeliveryBlock
from pages.main_page.serializers import DeliveryBlockSerializer
from pages.common_elements.models import (
    HeaderBlock,
    RecommendedProductBlock,
    AddQuestionBlock,
)
from pages.common_elements.serializers import (
    HeaderBlockSerializer,
    RecommendedProductBlockSerializer,
    AddQuestionBlockSerializer,
)
from shop.models import Category
from shop.serializers import CategorySerializer


def aggregate_data(request):
    try:
        response_data = {}

        header_block = HeaderBlock.objects.first()
        delivery_block = DeliveryBlock.objects.first()
        payment_block = PaymentBlock.objects.first()
        recommended_product_block = RecommendedProductBlock.objects.select_related("product").all()
        add_question_block = AddQuestionBlock.objects.first()
        category_list = Category.objects.all()

        if header_block:
            response_data['header_block'] = HeaderBlockSerializer(header_block).data
        if delivery_block:
            response_data['delivery_block'] = DeliveryBlockSerializer(delivery_block).data
        if payment_block:
            response_data['payment_block'] = PaymentBlockSerializer(payment_block).data
        if recommended_product_block:
            response_data['recommended_product_block'] = RecommendedProductBlockSerializer(recommended_product_block, many=True).data
        if add_question_block:
            response_data['add_question_block'] = AddQuestionBlockSerializer(add_question_block).data
        if category_list:
            response_data['category_list'] = CategorySerializer(category_list, many=True).data

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

