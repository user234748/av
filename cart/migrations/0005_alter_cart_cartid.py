# Generated by Django 3.2.7 on 2022-01-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20220106_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cartid',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
