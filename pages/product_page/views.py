from django.shortcuts import render
from django.http import JsonResponse
from pages.common_elements.models import RecommendedProductBlock
from pages.common_elements.serializers import RecommendedProductBlockSerializer
from pages.common_elements.models import HeaderBlock
from pages.common_elements.serializers import HeaderBlockSerializer

from shop.models import Category
from shop.serializers import CategorySerializer


def aggregate_data(request) -> JsonResponse:
    try:
        response_data = {}

        header_block = HeaderBlock.objects.first()
        recommended_product_block = RecommendedProductBlock.objects.select_related("product").all()
        category_list = Category.objects.all()

        if header_block:
            response_data['header_block'] = HeaderBlockSerializer(header_block).data
        if recommended_product_block:
            response_data['recommended_product_block'] = RecommendedProductBlockSerializer(recommended_product_block, many=True).data
        if category_list:
            response_data['category_list'] = CategorySerializer(category_list, many=True).data

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
