from django.shortcuts import render
from django.http import JsonResponse
from pages.catalog_page.models import AddQuestionBlock
from pages.catalog_page.serializers import AddQuestionBlockSerializer

from pages.common_elements.models import HeaderBlock
from pages.common_elements.serializers import HeaderBlockSerializer


def aggregate_data(request):
    try:
        response_data = {}

        header_block = HeaderBlock.objects.first()
        add_question_block = AddQuestionBlock.objects.first()

        if header_block:
            response_data['header_block'] = HeaderBlockSerializer(header_block).data
        if add_question_block:
            response_data['add_question_block'] = AddQuestionBlockSerializer(add_question_block).data

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

