# Generated by Django 3.2.20 on 2023-09-11 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20230906_1358'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productreview',
            unique_together=set(),
        ),
    ]
