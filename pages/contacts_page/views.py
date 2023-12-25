from django.shortcuts import render
from django.http import JsonResponse
from pages.main_page.models import ContactsBlock
from pages.main_page.serializers import ContactsBlockSerializer
from pages.contacts_page.models import OutsideView
from pages.contacts_page.serializers import OutsideViewSerializer
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
        contacts_block = ContactsBlock.objects.first()
        outside_view = OutsideView.objects.first()
        add_question_block = AddQuestionBlock.objects.first()
        category_list = Category.objects.all()

        if header_block:
            response_data['header_block'] = HeaderBlockSerializer(header_block).data
        if contacts_block:
            response_data['contacts_block'] = ContactsBlockSerializer(contacts_block).data
        if outside_view:
            response_data['outside_view'] = OutsideViewSerializer(outside_view).data
        if add_question_block:
            response_data['add_question_block'] = AddQuestionBlockSerializer(add_question_block).data
        if category_list:
            response_data['category_list'] = CategorySerializer(category_list, many=True).data

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
