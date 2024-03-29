# Generated by Django 3.2.20 on 2023-09-07 16:21
from django.conf import settings
from django.db import migrations, models


def apply_default_image(apps, schema_editor):
    product = apps.get_model('products', 'Product')
    default_image = settings.MEDIA_ROOT + '/default.jpg'
    product.objects.filter(image=None).update(image=default_image)


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.svg', upload_to='product_images'),
        ),
        migrations.RunPython(apply_default_image),
    ]
