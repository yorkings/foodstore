from django.shortcuts import render,redirect
from django.contrib.auth import login, logout,authenticate
from foodweb.forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required 
# Create your views here.
def home(request):
    return render (request,'home.html')
def signup(request):
   
    if request.method == "POST":
        sig=SignupForm(request.POST)
        if sig.is_valid():
            sig.save()
            messages.sucess(request,'account has been created')
    else:
         sig=SignupForm()
         return render(request,'signup.html',{'form':sig})
    return render(request,'signup.html',{'form':sig})
def login_user(request):
    if request.method =="POST":
        log =LoginForm(request.POST)
        if log.is_valid():
            username=log.cleaned_data.get['username']
            password =log.cleaned_data.get['password']
            user= authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"you have logged in successfully!")
            else:
                messages.error(request,'invalid username or password' )
        else: 
            messages.error(request,'invalid credentials')       
    else:
        log=LoginForm()
        return render(request,'login.html',{'form':log})
    return render(request,'login.html',{'form':log})                
def product_detail(request,product_id):
        item =Product.objects.get(id=product_id)
        return render(request,'product_detail.html',{'product':item}) 
def add_to_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    cart_item,created=Cart.objects.get_or_create(user=request.user,product=product)
    if not created:
        cart_item +=1
        cart_item.save()
    return redirect("cart")    
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

