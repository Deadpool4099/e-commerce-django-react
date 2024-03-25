# Generated by Django 5.0.3 on 2024-03-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_productcategory_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingcartitem',
            old_name='product_item_id',
            new_name='product_item',
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='productcategory',
            unique_together={('product', 'sub_category')},
        ),
        migrations.AlterUniqueTogether(
            name='shoppingcartitem',
            unique_together={('product_item', 'shopping_cart')},
        ),
        migrations.AlterUniqueTogether(
            name='subcategory',
            unique_together={('name', 'category')},
        ),
        migrations.AlterUniqueTogether(
            name='variationcombination',
            unique_together={('product_combination', 'variation_class')},
        ),
        migrations.AlterUniqueTogether(
            name='variationtype',
            unique_together={('name', 'sub_category')},
        ),
        migrations.AlterUniqueTogether(
            name='wishlistitem',
            unique_together={('wishlist_tub', 'product_item')},
        ),
    ]
