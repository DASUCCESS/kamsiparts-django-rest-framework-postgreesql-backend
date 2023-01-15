# from django.shortcuts import render
# from urllib import request
import os
from fileinput import filename
from itertools import product

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import filters, generics
from rest_framework.parsers import JSONParser

from .serializers import *

# Create your views here.

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def check_login(request, email):
    try:
        user = User.objects.filter(email=email)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = UserSerializers(user, many=True)
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def get_user(request, id):
    try:
        user = User.objects.filter(pk=id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = UserSerializers(user)
        return JsonResponse(serializer.data)
    
@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all().order_by('created_at').reverse()
        serializer = ProductSerializers(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status = 400)
        
@csrf_exempt
def product_by_id(request, pk):
    try:
        user = Product.objects.get(pk=id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProductSerializers(Product)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializers(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=201)
        
@csrf_exempt
def product_seller(request, storeid):
    try:
        user = Product.objects.get(storeid=storeid)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProductSerializers(product, many=True)
        return JsonResponse(serializer.data, safe=False)
    # elif request.method = 'PUT':
        
        
@csrf_exempt
def productImg_list(request, storeid):
    if request.method == 'GET':
        productImgs = ProductImg.objects.all()
        serializer = ProductImgSerializers(productImgs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductImgSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status = 400)
    
@csrf_exempt
def productImg_product_id(request, productid):
    try:
        # productImg = Product.objects.get(pk=id)
        productImg = Product.objects.filter(productid = productid)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProductImgSerializers(productImg, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def productImg_by_id(request, id):
    try:
        productImg = ProductImg.objects.get(pk=id)
        # productImg = Product.objects.filter(productid = productid)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProductImgSerializers(productImg, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        productImg.delete()
        return HttpResponse(status=201)

@csrf_exempt
def product_by_category(request, category):
    try:
        product = Product.objects.filter(category=category)
        # productImg = Product.objects.filter(productid = productid)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProductSerializers(product, many=True)
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def cart_list(request, category):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CartSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def cart_by_user(request, userid):
    try:
        cart = Cart.objects.filter(userid=userid)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CartSerializers(cart, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CartSerializers(cart, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        cart.delete()
        return HttpResponse(status=201)
    
@csrf_exempt
def cart_item_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CartItemSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

@csrf_exempt
def cart_item_by_id(request, pk):
    try:
        cartItem = CartItem.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CartItemSerializers(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CartSerializers(cartItem, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        cartItem.delete()
        return HttpResponse(status=201)
    
# @csrf_exempt
# def cart_item_by_cart(request, cartid):
#     try:
#         cartItem = CartItem.objects.filter(cartid=cartid)
#     except:
#         return HttpResponse(status=404)
#     if request.method = 'GET':
#         serializer = CartItemSerializers(cartItem, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def cart_item_cart_id(request, cartid):
    try:
        cartItem = CartItem.objects.filter(cartid=cartid)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CartItemSerializers(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)
        
@csrf_exempt
def cart_item_detect_same_product(request, cartid, productid):
    try:
        cartItem = CartItem.objects.filter(cartid=cartid).filter(productid=productid)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CartItemSerializers(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)
    
class search_product(generics.ListAPIView):
    search_fields = ('title','description','category')
    filter_backends = (filters.SearchFilter)
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
@csrf_exempt
def create_store(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StoreSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

@csrf_exempt
def get_store(request, userid):
    try:
        store = Store.objects.filter(userid=userid)
    except:
        return HttpResponse(status=404)

class upload_file(generics.CreateAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializers
    
@csrf_exempt
def delete_file(request, filename):
    if request.method == 'GET':
        ext = filename.split(".")[-1]
        filenamenoExt = filename.replace(f'{ext}',"")
        fileDir = "%s/%s.%s" % ("img",filenamenoExt, ext)
        if os.path.isfile((f'{img}/{filename}')):
            os.remove(fileDir)
            return HttpResponse(f'{filename} deleted')
        return HttpResponse('file not found')

def filter_range_price(request, minprice, maxprice):
    try:
        products = Product.objects.filter(price__range(minprice, maxprice))
    except:
        return HttpResponse(status=404)
    
    if request.method == "POST":
        serializer = ProductSerializers(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    
def filter_minprice(request, minprice):
    try:
        products = Product.objects.filter(price_gte=minprice)
    except:
        return HttpResponse(status=404)
    
    if request.method == "POST":
        serializer = ProductSerializers(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def filter_maxprice(request, maxprice):
    try:
        products = Product.objects.filter(price__gte=maxprice)
    except:
        return HttpResponse(status=404)
    
    if request.method == "POST":
        serializer = ProductSerializers(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    
def filter_rating(request, rating):
    try:
        products = Product.objects.filter(prating__gte=rating)
    except:
        return HttpResponse(status=404)
    
    if request.method == "POST":
        serializer = ProductSerializers(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    
def filter_condition(request, condition):
    try:
        products = Product.objects.filter(condition=condition)
    except:
        return HttpResponse(status=404)
    
    if request.method == "POST":
        serializer = ProductSerializers(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def filter_price_and_rating(request, minprice, maxprice, rating):
    try:
        products = Product.objects.filter(price__range(minprice, maxprice)).filter(rating_gte=rating)
    except:
        return HttpResponse(status=404)
    
    if request.method == "POST":
        serializer = ProductSerializers(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    
def filter_price_and_condition(request, minprice, maxprice, condition):
    try:
        products = Product.objects.filter(price__range(minprice, maxprice)).filter(condition=condition)
    except:
        return HttpResponse(status=404)
    
    if request.method == "POST":
        serializer = ProductSerializers(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def filter_rating_and_condition(request, rating, condition):
    try:
        products = Product.objects.filter(rating_gte=rating).filter(condition=condition)
    except:
        return HttpResponse(status=404)
    
    if request.method == "POST":
        serializer = ProductSerializers(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def filter_all(request, minprice, maxprice, rating, condition):
    try:
        products = Product.objects.filter(price__range(minprice, maxprice)).filter(rating_gte=rating).filter(condition=condition)
    except:
        return HttpResponse(status=404)
    
    if request.method == "POST":
        serializer = ProductSerializers(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    
def get_cart_item_by_cart_id(request, cartid):
    try:
        cartitem = CartItem.objects.filter(cartid=cartid).prefetch_related('productId').order_by('created_at')
    except:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = JoinSerializers(cartitem, many=True)
        return JsonResponse(serializer.data, safe=False)
    


        

