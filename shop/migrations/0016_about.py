# Generated by Django 3.1 on 2020-09-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20200919_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('About_id', models.AutoField(primary_key=True, serialize=False)),
                ('About_tittle', models.CharField(max_length=50)),
                ('About_content', models.CharField(default='', max_length=500)),
                ('About_Video_url', models.CharField(default='', max_length=500)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
