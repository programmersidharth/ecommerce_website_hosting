from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Blog,Product,Category,Testimonial,About

# Create your views here.

def index(request):
    product = Product.objects.all()
    category = Category.objects.all()
    testimonial = Testimonial.objects.all()
    return render(request, 'shop/index.html',{'product':product , 'category':category,'testimonial':testimonial})


def about(request):
    about = About.objects.all()
    return render(request, 'shop/about.html',{'about': about})


def blog(request):
    all_blog = Paginator(Blog.objects.all(),3)
    page = request.GET.get('page')
    try:
        blog = all_blog.page(page)
    except PageNotAnInteger:
        blog = all_blog.page(1)
    except EmptyPage:
        blog = all_blog.page(all_blog.num_pages)
    return render(request, 'shop/blog.html',{'blog': blog})


def blog_single(request,blog_detail_id):
    blog = Blog.objects.filter(blog_id= blog_detail_id)
    return render(request, 'shop/blog_single.html',{"blog":blog[0]})


def cart(request):
    return render(request, 'shop/cart.html')


def checkout(request):
    return render(request, 'shop/checkout.html')


def contact(request):
    return render(request, 'shop/contact.html')


def shop(request):
    all_product =Paginator(Product.objects.all(),8)
    product_page =request.GET.get('page')
    try:
        product = all_product.page(product_page)
    except PageNotAnInteger:
        product = all_product.page(1)
    except EmptyPage:
        product = all_product.product_page(all_product.num_pages)

    return render(request, 'shop/shop.html',{'product':product})


def product_single(request,product_detail_id):
    product_details = Product.objects.filter(product_id=product_detail_id)
    return render(request, 'shop/product_single.html',{'product':product_details[0]})

def category_product(request,category_id    ):

    all_category_products = Paginator(Product.objects.filter(category_product = category_id), 8)
    category_product_page = request.GET.get('page')
    try:
        category_var = all_category_products.page(category_product_page)
    except PageNotAnInteger:
        category_var = all_category_products.page(1)
    except EmptyPage:
        category_var = all_category_products.page(all_category_products.num_pages)

    return render(request, 'shop/category_product.html',{'category_var': category_var})

def wishlist(request):
    return render(request, 'shop/wishlist.html')