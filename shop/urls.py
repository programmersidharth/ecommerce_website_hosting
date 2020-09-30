from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='Index'),
    path('index/', views.index, name='Index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('product_single/<int:product_detail_id>', views.product_single, name='product_single'),
    path('shop/', views.shop, name='shop'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('checkout/', views.checkout, name='checkout'),
    path('blog_single/<int:blog_detail_id>', views.blog_single, name='blog_single'),
    path('category_product/<int:category_id>', views.category_product, name='category_product')

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
