# Generated by Django 3.0 on 2021-06-07 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
