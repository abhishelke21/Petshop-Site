# Generated by Django 4.1.4 on 2023-01-19 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_product_cat_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_cat',
            name='desc',
            field=models.TextField(),
        ),
    ]
