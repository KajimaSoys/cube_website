
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve as mediaserve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('shop.urls')),
                  path('__debug__/', include('debug_toolbar.urls')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  path('api/v1/', include('api.urls')),
                  path('company/', include('news.urls')),
              ]

admin.site.site_header = "Панель управления сайта Куб Казань"
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += [
#         re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
#             mediaserve, {'document_root': settings.MEDIA_ROOT}),
#         re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
#             mediaserve, {'document_root': settings.STATIC_ROOT}),
#     ]
handler404 = 'shop.utils.handle_non_found'
handler500 = 'shop.utils.handle_error'
