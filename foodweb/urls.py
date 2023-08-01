from django.urls import path
from . views import *

urlpatterns= [
    path("",home,name='home'),
    path('signup/',signup,name='sign'),
    path("product/<int:product_id>/",product_detail,name='product_detail'),
    path("product/<int:product_id>/add_to_cart",add_to_cart,name='addcart'),
       path('cart/', cart, name='cart'),
]