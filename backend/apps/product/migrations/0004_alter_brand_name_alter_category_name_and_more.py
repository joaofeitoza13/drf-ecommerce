# Generated by Django 4.2.5 on 2023-09-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_brand_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
