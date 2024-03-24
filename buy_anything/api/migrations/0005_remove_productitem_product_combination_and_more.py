# Generated by Django 5.0.3 on 2024-03-24 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_address_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productitem',
            name='product_combination',
        ),
        migrations.AddField(
            model_name='productitem',
            name='variation_combination',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.variationcombination'),
            preserve_default=False,
        ),
    ]