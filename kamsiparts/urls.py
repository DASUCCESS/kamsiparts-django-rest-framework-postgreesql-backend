from django.urls import path
from .views import *

urlpatterns = [
    path('user/', create_user),
    path('user/<int:id>/', get_user),
    path('showItemsCart/<int:cartid>/', get_cart_item_by_cart_id),
    path('store/', create_store),
    path('store/<int:userid>/', get_store),
    path('login/<str:email>/', check_login),
    path('product/', product_list),
    path('product/find/', search_product.as_view()),
    path('product/<int:pk>/', product_by_id),
    path('product/seller/<int:storeId>/', product_seller),
    path('cart/', cart_list),
    path('cart/<int:userId>/', cart_by_user),
    path('cartItem/', cart_item_list),
    path('cartItem/<int:cartId>/', cart_item_cart_id),
    path('cartItem/id/<int:pk>/', cart_item_by_id),
    path('cartItemDetectSameItem/<int:cartId>/<int:productId>/', cart_item_detect_same_product),
    path('productImg/', productImg_list),
    path('productImg/<int:productId>/', productImg_product_id),
    path('productImg/id/<int:id>/', productImg_by_id),
    path('product/find/<str:category>/', product_by_category),
    path('uploadFile/', upload_file.as_view()),
    path('deleteFile/<str:filename>/', delete_file),
    path('filter/price/<int:maxprice>/<int:minprice>/', filter_range_price),
    path('filter/price/min/<int:minprice>/', filter_minprice),
    path('filter/price/max/<int:maxprice>/', filter_maxprice),
    path('filter/rating/<int:rating>/', filter_rating),
    path('filter/condition/<str:condition>/', filter_condition),
    path('filter/price_and_rating/<int:minprice>/<int:maxprice>/<int:rating>', filter_price_and_rating),
    path('filter/price_and_condition/<int:minprice>/<int:maxprice>/<str:condition>', filter_price_and_condition),
    path('filter/rating_and_condition/<int:rating>/<str:condition>', filter_rating_and_condition),
     path('filter/<int:minprice>/<int:maxprice>/<int:rating>/<str:condition>', filter_all),
]
