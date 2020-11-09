# Generated by Django 3.1.3 on 2020-11-08 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201108_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=1000),
            preserve_default=False,
        ),
    ]
