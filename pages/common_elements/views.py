from django.http import JsonResponse
from pages.common_elements.models import HeaderBlock
from pages.common_elements.serializers import HeaderBlockSerializer
from shop.models import Category
from shop.serializers import CategorySerializer

def header_data(request):
    try:
        response_data = {}

        header_block = HeaderBlock.objects.first()
        category_list = Category.objects.all()

        if header_block:
            response_data['header_block'] = HeaderBlockSerializer(header_block).data
        if category_list:
            response_data['category_list'] = CategorySerializer(category_list, many=True).data

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
