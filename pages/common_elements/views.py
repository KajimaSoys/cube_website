from django.http import JsonResponse
from pages.common_elements.models import HeaderBlock
from pages.common_elements.serializers import HeaderBlockSerializer


def header_data(request):
    try:
        response_data = {}

        header_block = HeaderBlock.objects.first()

        if header_block:
            response_data['header_block'] = HeaderBlockSerializer(header_block).data

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
