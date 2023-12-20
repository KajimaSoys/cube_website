from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve as mediaserve
from django.conf import settings
from django.conf.urls.static import static

from pages.main_page import views as main_page_views
from pages.catalog_page import views as catalog_page_views
from pages.product_page import views as product_page_views
from pages.delivery_page import views as delivery_page_views
from pages.contacts_page import views as contacts_page_views
from pages.about_page import views as about_page_views
from pages.reviews_page import views as reviews_page_views
from pages.common_elements import views as common_elements_views

from shop import views as shop_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/v1/', include('DEPRECATED_api.urls')),
    path('company/', include('news.urls')),

    path('api/v1/main_page/', main_page_views.aggregate_data, name='main_page'),
    path('api/v1/catalog_page/', catalog_page_views.aggregate_data, name='catalog_page'),
    path('api/v1/product_page/', product_page_views.aggregate_data, name='product_page'),
    path('api/v1/delivery_page/', delivery_page_views.aggregate_data, name='delivery_page'),
    path('api/v1/contacts_page/', contacts_page_views.aggregate_data, name='contacts_page'),
    path('api/v1/about_page/', about_page_views.aggregate_data, name='about_page'),
    path('api/v1/reviews_page/', reviews_page_views.aggregate_data, name='reviews_page'),
    path('api/v1/header_data/', common_elements_views.header_data, name='header_data'),


    path(
        'api/v1/category/',
        shop_views.CategoryListView.as_view(),
        name='category-list'
    ),
    path(
        'api/v1/products/',
        shop_views.ProductListView.as_view(),
        name='product-list'
    ),
    path(
        'api/v1/category/<slug:category_slug>/',
        shop_views.CategoryProductListView.as_view(),
        name='category-product-list'
    ),

    path(
        'api/v1/products/<int:product_id>/',
        shop_views.ProductView.as_view(),
        name='product'
    ),

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
