# Generated by Django 5.1.3 on 2025-01-02 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_rename_name_productcategory_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
