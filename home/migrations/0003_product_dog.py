# Generated by Django 4.1.4 on 2023-01-19 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_contact_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, null=True)),
                ('price', models.FloatField()),
                ('desc', models.TextField()),
                ('digital', models.BooleanField(default=True, null=True)),
                ('img', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
