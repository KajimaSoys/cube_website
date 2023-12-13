from django.shortcuts import render
from django.http import JsonResponse
from news.models import Reviews
from news.serializers import ReviewsSerializer
from pages.common_elements.models import RecommendedProductBlock
from pages.common_elements.serializers import RecommendedProductBlockSerializer
from pages.common_elements.models import (
    HeaderBlock,
    AddQuestionBlock
)
from pages.common_elements.serializers import (
    HeaderBlockSerializer,
    AddQuestionBlockSerializer
)


def aggregate_data(request):
    try:
        response_data = {}

        header_block = HeaderBlock.objects.first()
        reviews = Reviews.objects.all()
        recommended_product_block = RecommendedProductBlock.objects.select_related("product").all()
        add_question_block = AddQuestionBlock.objects.first()

        if header_block:
            response_data['header_block'] = HeaderBlockSerializer(header_block).data
        if reviews:
            response_data['reviews'] = ReviewsSerializer(reviews, many=True).data
        if recommended_product_block:
            response_data['recommended_product_block'] = RecommendedProductBlockSerializer(recommended_product_block, many=True).data
        if add_question_block:
            response_data['add_question_block'] = AddQuestionBlockSerializer(add_question_block).data

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
