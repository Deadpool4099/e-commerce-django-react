from django.contrib import admin
from .models import Country, Address, Category, SubCategory, ProductCategory, \
    ProductCombination, ProductItem, VariationType, VariationClass, \
        VariationCombination, ShoppingCart, ShoppingCartItem, UserReview, \
            WishlistTub, WishListItem, PaymentMethod, PaymentStatus, \
                PaymentDetail, OrderStatus, Order, Product
# Register your models here.

admin.site.register(Country)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProductCategory)
admin.site.register(ProductCombination)
admin.site.register(ProductItem)
admin.site.register(VariationType)
admin.site.register(VariationClass)
admin.site.register(VariationCombination)
admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)
admin.site.register(UserReview)
admin.site.register(WishlistTub)
admin.site.register(WishListItem)
admin.site.register(PaymentMethod)
admin.site.register(PaymentStatus)
admin.site.register(PaymentDetail)
admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(Product)
