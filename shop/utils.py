from django.shortcuts import render


def handle_non_found(request, *args, **kwargs):
    return render(request, 'shop/not_found.html')


def handle_error(request, *args, **kwargs):
    return render(request, 'shop/etirnal_error.html')