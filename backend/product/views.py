from django.shortcuts import render,redirect
from . models import *
from . forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.



def indexpage(request):
    
    items=Item.objects.all().order_by('-id')
    
    context={
        'items':items
    }
    return render(request, 'product/index.html',context)

def postpage(request):
    if request.method=='POST':
        form=Item()
        form.name=request.POST.get('name')
        form.price=request.POST.get('price')
        form.description=request.POST.get('description')

        if len(request.FILES) !=0:
            form.image=request.FILES['image']
        form.save()
        return redirect('home')
    return render(request, 'product/post.html')

def registerpage(request):
    
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')
        
    context={'form':form}
    
    
    return render(request, 'product/register.html', context)



def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('post')  # Ensure this redirect points to a valid URL name
        else:
            messages.info(request, 'Username OR Password is incorrect')

    # Always return a response, even for GET requests
    return render(request, 'product/login.html')