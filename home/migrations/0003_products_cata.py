# Generated by Django 3.2.7 on 2021-12-07 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='cata',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.cata'),
            preserve_default=False,
        ),
    ]
