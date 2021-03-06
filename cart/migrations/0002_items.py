# Generated by Django 3.2.7 on 2021-12-07 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_cata_options'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q', models.IntegerField()),
                ('cartlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('prodt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.products')),
            ],
        ),
    ]
