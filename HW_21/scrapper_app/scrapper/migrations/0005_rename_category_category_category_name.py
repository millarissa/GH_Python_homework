# Generated by Django 4.1.2 on 2023-01-30 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0004_category_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='category_name',
        ),
    ]
