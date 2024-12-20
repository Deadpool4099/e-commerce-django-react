# Generated by Django 5.0 on 2024-11-10 10:14

import django.core.validators
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_delete_productcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterUniqueTogether(
            name='productitem',
            unique_together={('product', 'variation_type', 'variation_class')},
        ),
    ]
