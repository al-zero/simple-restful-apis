# Generated by Django 3.0 on 2021-03-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210302_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
    ]
