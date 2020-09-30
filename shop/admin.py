from django.contrib import admin
from .models import Blog,Product, Category,Testimonial,About

# Register your models here.

admin.site.register(Blog)
admin.site.register(Product)

class AdminCategory(admin.ModelAdmin):
    list_display = ['category_id','category', 'category_image']


admin.site.register(Category,AdminCategory)
admin.site.register(Testimonial)
admin.site.register(About)