from django.urls import path
from . import  views

app_name='cart'
urlpatterns = [
    path('add/<int:prod_id>/',views.addCart,name='add_cart'),
    path('cart/details/',views.cart_detail,name='cart_detail'),
    path('remove/<int:product_id>',views.cart_remove,name='remove_cart'),
    path('delete/<int:product_id>',views.delete,name='delete')
   ]