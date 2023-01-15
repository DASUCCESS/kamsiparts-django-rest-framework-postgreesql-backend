from dataclasses import fields
from rest_framework import serializers
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password','address','phone','created_at']
        
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title','storeid','category','price','stock','condition','created_at']
        
class ProductImgSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImg
        fields = ['id','title','productId', 'url']
        
class StoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id','userId','name', 'created_at']

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','userId','quantity']
        
class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cartId','productId','quantity','created_at']
     
class FileUploadSerializers(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['imgFile']
        
        
class JoinSerializers(serializers.ModelSerializer):
    product_details = ProductSerializers(source = 'productId')
    class Meta:
        model = CartItem
        fields = ['cartId','productId','quantity','','created_at']