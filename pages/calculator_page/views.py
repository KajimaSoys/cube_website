from django.http import JsonResponse

from pages.calculator_page.models import AdditionalProductBlock
from pages.calculator_page.serializers import AdditionalProductBlockSerializer

from pages.common_elements.models import HeaderBlock
from pages.common_elements.serializers import HeaderBlockSerializer

from shop.models import Category
from shop.serializers import CategorySerializer


def aggregate_data(request):
    try:
        response_data = {}

        header_block = HeaderBlock.objects.first()
        additional_products_block = AdditionalProductBlock.objects.select_related("product").all()
        category_list = Category.objects.all()

        if header_block:
            response_data['header_block'] = HeaderBlockSerializer(header_block).data
        if additional_products_block:
            response_data['additional_products_block'] = AdditionalProductBlockSerializer(additional_products_block, many=True).data
        if category_list:
            response_data['category_list'] = CategorySerializer(category_list, many=True).data

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
