from django.shortcuts import render
from django.http import JsonResponse
from pages.catalog_page.models import AddQuestionBlock
from pages.catalog_page.serializers import AddQuestionBlockSerializer

from pages.common_elements.models import HeaderBlock
from pages.common_elements.serializers import HeaderBlockSerializer
from shop.models import Category
from shop.serializers import CategorySerializer


def aggregate_data(request):
    try:
        response_data = {}

        header_block = HeaderBlock.objects.first()
        add_question_block = AddQuestionBlock.objects.first()
        category_list = Category.objects.all()

        if header_block:
            response_data['header_block'] = HeaderBlockSerializer(header_block).data
        if add_question_block:
            response_data['add_question_block'] = AddQuestionBlockSerializer(add_question_block).data
        if category_list:
            response_data['category_list'] = CategorySerializer(category_list, many=True).data

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

