# Generated by Django 3.0 on 2020-01-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_url',
            field=models.ImageField(upload_to='product-ecom-images'),
        ),
    ]
