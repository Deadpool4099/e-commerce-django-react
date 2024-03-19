# Generated by Django 5.0.3 on 2024-03-17 12:49

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='address',
            table='address',
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='country',
            table='country',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
        migrations.AlterModelTable(
            name='productcategory',
            table='product_category',
        ),
        migrations.AlterModelTable(
            name='productcombination',
            table='product_combination',
        ),
        migrations.AlterModelTable(
            name='productitem',
            table='product_item',
        ),
        migrations.AlterModelTable(
            name='shoppingcart',
            table='shopping_cart',
        ),
        migrations.AlterModelTable(
            name='subcategory',
            table='sub_category',
        ),
        migrations.AlterModelTable(
            name='variationclass',
            table='variation_class',
        ),
        migrations.AlterModelTable(
            name='variationtype',
            table='variation_type',
        ),
        migrations.CreateModel(
            name='VariationCombination',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_combination_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productcombination')),
            ],
            options={
                'db_table': 'variation_combination',
            },
        ),
    ]
