# Generated by Django 3.2.20 on 2023-09-04 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
