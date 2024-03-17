from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


######################################################################
#### Address Related
######################################################################
class Country(models.Model):

    class Meta:
        db_table = 'country'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)


class Address(models.Model):

    class Meta:
        db_table = 'address'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    address_lane_1 = models.TextField()
    address_lane_2 = models.TextField()
    landmark = models.TextField(null=True)
    city = models.CharField(max_length=80)
    pin_code = models.CharField(max_length=10)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    mobile = models.CharField(max_length=20)

####

######################################################################
#### Product Related
######################################################################
class Product(models.Model):

    class Meta:
        db_table = 'product'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField()


class Category(models.Model):

    class Meta:
        db_table = 'category'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()


class SubCategory(models.Model):

    class Meta:
        db_table = 'sub_category'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class ProductCategory(models.Model):

    class Meta:
        db_table = 'product_category'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True)


class ProductCombination(models.Model):

    class Meta:
        db_table = 'product_combination'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductItem(models.Model):

    class Meta:
        db_table = 'product_item'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_combination = models.ForeignKey(ProductCombination, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    stock_available = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)


class VariationType(models.Model):

    class Meta:
        db_table = 'variation_type'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)


class VariationClass(models.Model):

    class Meta:
        db_table = 'variation_class'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    variation_type = models.ForeignKey(VariationType, on_delete=models.CASCADE)
    value = models.CharField(max_length=20)


class VariationCombination(models.Model):

    class Meta:
        db_table = 'variation_combination'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_combination = models.ForeignKey(ProductCombination, on_delete=models.CASCADE)
    variation_class = models.ForeignKey(VariationClass, on_delete=models.SET_NULL, null=True, blank=True)
    variation_type = models.ForeignKey(VariationType, on_delete=models.SET_NULL, null=True, blank=True)

####


######################################################################
#### Shopping Cart Related
######################################################################

class ShoppingCart(models.Model):

    class Meta:
        db_table = 'shopping_cart'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ShoppingCartItem(models.Model):

    class Meta:
        db_table = 'shopping_cart_item'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_item_id = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)

####

######################################################################
#### User Reviews Related
######################################################################


class UserReview(models.Model):

    rating_choices = [
        (1, 'Very Bad'),
        (2, 'Bad'),
        (3, 'Ok'),
        (4, 'Good'),
        (5, 'Very Good')
    ]
    class Meta:
        db_table = 'user_review'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=rating_choices, default=0)
    comment = models.TextField()

#####


######################################################################
#### Wish List Related
######################################################################

class WishlistTub(models.Model):

    class Meta:
        db_table = 'wishlist_tub'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class WishListItem(models.Model):

    class Meta:
        db_table = 'wishlist_item'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wishlist_tub = models.ForeignKey(WishlistTub, on_delete=models.CASCADE)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)


####


######################################################################
#### Payment Related
######################################################################

class PaymentMethod(models.Model):

    choices = [
        ('UPI', 'UPI'),
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card')
    ]
    class Meta:
        db_table = 'payment_method'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    method = models.CharField(max_length=50, choices=choices, unique=True)


class PaymentStatus(models.Model):

    choices = [
        ('INPROGRESS', 'INPROGRESS'),
        ('SUCCESS', 'SUCCESS'),
        ('FAILED', 'FAILED')
    ]

    class Meta:
        db_table = 'payment_status'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, choices=choices, unique=True)


class PaymentDetail(models.Model):

    class Meta:
        db_table = 'payment_detail'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)
    payment_status = models.ForeignKey(PaymentStatus, on_delete=models.SET_NULL, null=True, blank=True)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



######################################################################
#### Orders Related
######################################################################

class OrderStatus(models.Model):

    choices = [
        ('PLACED', 'PLACED'),
        ('DISPACTCHED', 'DISPACTCHED'),
        ('DELIVERED', 'DELIVERED'),
    ]
    class Meta:
        db_table = 'order_status'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=50, choices=choices, unique=True)


class Order(models.Model):

    class Meta:
        db_table = 'order'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shopping_cart_item = models.ForeignKey(ShoppingCartItem, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True, blank=True)
    payment = models.ForeignKey(PaymentDetail, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)







