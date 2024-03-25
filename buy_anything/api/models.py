from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.postgres.fields import JSONField

# Create your models here.


######################################################################
#### Address Related
######################################################################
class Country(models.Model):

    class Meta:
        db_table = 'country'
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80, unique=True)
    
    def __str__(self):
        return self.name


class Address(models.Model):

    class Meta:
        db_table = 'address'
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

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
        verbose_name = "Product"
        verbose_name_plural = "Products"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    


class Category(models.Model):

    class Meta:
        db_table = 'category'
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):

    class Meta:
        db_table = 'sub_category'
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"
        unique_together = ('name', 'category')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.category) + '___' + self.name


class ProductCategory(models.Model):

    class Meta:
        db_table = 'product_category'
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
        unique_together = ('product', 'sub_category')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True)
    
    
    def __str__(self) -> str:
        return str(self.product) + '___' + str(self.sub_category)


class VariationType(models.Model):

    class Meta:
        db_table = 'variation_type'
        verbose_name = "Variation Type"
        verbose_name_plural = "Variation Types"
        unique_together = ('name', 'sub_category')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name + '___' + str(self.sub_category)


class VariationClass(models.Model):

    class Meta:
        db_table = 'variation_class'
        verbose_name = "Variation Class"
        verbose_name_plural = "Variation Classes"
        unique_together = ('variation_type', 'value',)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    variation_type = models.ForeignKey(VariationType, on_delete=models.CASCADE)
    value = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return str(self.variation_type) + '___' + self.value


class ProductItem(models.Model):

    class Meta:
        db_table = 'product_item'
        verbose_name = "Product Item"
        verbose_name_plural = "Product Items"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    stock_available = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    
    # def __str__(self) -> str:
    #     return str(self.variation_combination)


class VariationCombination(models.Model):

    class Meta:
        db_table = 'variation_combination'
        verbose_name = "Variation Combination"
        verbose_name_plural = "Variation Combinations"
        unique_together = ('product_item', 'variation_type')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, default=None, null=True)
    variation_class = models.ForeignKey(VariationClass, on_delete=models.SET_NULL, null=True, blank=True)
    variation_type = models.ForeignKey(VariationType, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.product_item) + '___' + str(self.variation_class)
    
####


######################################################################
#### Shopping Cart Related
######################################################################

class ShoppingCart(models.Model):

    class Meta:
        db_table = 'shopping_cart'
        verbose_name = "Shopping Cart"
        verbose_name_plural = "Shopping Carts"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ShoppingCartItem(models.Model):

    class Meta:
        db_table = 'shopping_cart_item'
        verbose_name = "Shopping Cart Item"
        verbose_name_plural = "Shopping Cart Items"
        unique_together = ('product_item', 'shopping_cart')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
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
        verbose_name = "User Review"
        verbose_name_plural = "User Reviews"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=rating_choices, default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#####


######################################################################
#### Wish List Related
######################################################################

class WishlistTub(models.Model):

    class Meta:
        db_table = 'wishlist_tub'
        verbose_name = "Wishlist Tub"
        verbose_name_plural = "Wishlist Tubs"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class WishListItem(models.Model):

    class Meta:
        db_table = 'wishlist_item'
        verbose_name = "Wishlist Item"
        verbose_name_plural = "Wishlist Items"
        unique_together = ('wishlist_tub', 'product_item')

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
        verbose_name = "Payment Method"
        verbose_name_plural = "Payment Methods"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    method = models.CharField(max_length=50, choices=choices, unique=True)
    
    def __str__(self) -> str:
        return self.method


class PaymentStatus(models.Model):

    choices = [
        ('INPROGRESS', 'INPROGRESS'),
        ('SUCCESS', 'SUCCESS'),
        ('FAILED', 'FAILED')
    ]

    class Meta:
        db_table = 'payment_status'
        verbose_name = "Payment Status"
        verbose_name_plural = "Payment Statuses"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, choices=choices, unique=True)
    
    def __str__(self) -> str:
        return self.status


class PaymentDetail(models.Model):

    class Meta:
        db_table = 'payment_detail'
        verbose_name = "Payment Detail"
        verbose_name_plural = "Payment Details"

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
        verbose_name = "Order Status"
        verbose_name_plural = "Order Statuses"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=50, choices=choices, unique=True)
    
    def __str__(self) -> str:
        return self.status


class Order(models.Model):

    class Meta:
        db_table = 'order'
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shopping_cart_item = models.ForeignKey(ShoppingCartItem, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True, blank=True)
    payment = models.ForeignKey(PaymentDetail, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



