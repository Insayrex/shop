# Generated by Django 2.1.3 on 2018-12-05 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_prise'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prise',
            new_name='price',
        ),
    ]
