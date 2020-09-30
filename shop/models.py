from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.

class Blog(models.Model):
    blog_id =models.AutoField(primary_key=True)
    blog_head =models.CharField(max_length=100)
    blo_content =RichTextField(blank=True,null=True)
    blog_admin = models.CharField(max_length=50, default="")
    blog_date = models.DateField()
    blog_image = models.ImageField(upload_to="shop/images", default="")
    blog_teacher = models.CharField(max_length=50)
    blog_teacher_content = models.CharField(max_length=200)
    blog_teacher_image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.blog_head


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, default="")
    category_image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.category


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category_product =models.ForeignKey(Category, related_name='Category' ,on_delete=models.CASCADE , default=1 )
    old_price = models.IntegerField(default=0)
    price =models.IntegerField(default=0)
    desc = RichTextField(blank=True,null=True)
    discount_percentage = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

class Testimonial(models.Model):
    testimonial_id = models.AutoField(primary_key=True)
    testimonial_name = models.CharField(max_length=50)
    testimonial_content = models.CharField(max_length=500, default="")
    testimonial_post = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.testimonial_name

class About(models.Model):
    About_id = models.AutoField(primary_key=True)
    About_tittle = models.CharField(max_length=50)
    About_content = models.CharField(max_length=500, default="")
    About_Video_url = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.About_tittle
