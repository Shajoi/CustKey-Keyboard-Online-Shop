from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth import logout
from .form import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from docxtpl import DocxTemplate


def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})



def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})



def add_to_cart(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
        cart_item.quantity += 1
        cart_item.save()
        return redirect('product_list')
    except:
        return redirect('registration/login.html')



def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')


def reg(request):
    # if request.POST:
    #     anketa = SignUpForm(request.POST)
    #     if anketa.is_valid():
    #         anketa.save()
    #         k1 = anketa.cleaned_data.get('username')
    #         k2 = anketa.cleaned_data.get('password')
    #         k4 = anketa.cleaned_data.get('first_name')
    #         k5 = anketa.cleaned_data.get('last_name')
    #         user = authenticate( first_name=k4, last_name=k5,username=k1, password=k2)
    #         login(request, user)
    #         return HttpResponse('product_list')
    # else:
    #     anketa = SignUpForm()
    #     data = {'form': anketa}
    #     return render(request,'registration/register.html',data)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data['username'], data['password'], data['first_name'], data['last_name']
            )
            return redirect('product_list')
    else:
        form = SignUpForm()
    context = {'title':'Signup', 'form':form}
    return render(request, 'registration/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
