# Generated by Django 4.1.3 on 2023-02-22 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='product_stock_quantity_positive_integer',
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_available',
            field=models.BooleanField(default=True, verbose_name='Available'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_original_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Original Price'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_selling_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Selling Price'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_stock_quantity',
            field=models.IntegerField(verbose_name='Stock Quantity'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
    ]
