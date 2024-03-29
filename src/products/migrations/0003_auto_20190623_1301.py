# Generated by Django 2.0.7 on 2019-06-23 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='products',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
