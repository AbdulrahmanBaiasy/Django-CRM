from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout 
from django.contrib import messages 
from .forms import SignUpForm,AddRecordForm
from .models import Record
# Create your views here.

def home (request):
    #Check to see if logging in 
    records = Record.objects.all()
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        #auth 
        user = authenticate(request,username= username , password = password )
        if user is not None : 
            login(request, user)
            messages.success(request,'u logged in ')
            return redirect('home')
        else:
            messages.success(request,'couldnt login')
            return redirect('home')
    else:
        return render (request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


def register_user (request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Auth and login 
            username = form.cleaned_data ['username']
            password = form.cleaned_data['password1']
            user = authenticate( username = username , password = password)
            login (request, user )
            messages.success(request, 'success')
            return redirect('home')
    else :
        form = SignUpForm()
        return render (request, 'register.html', {'form':form})
    return render (request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated: 
        #lookup 
        customer_record = Record.objects.get(id = pk)
        return render (request, 'record.html', {'customer_record':customer_record})
    else : 
        messages.success(request, 'You must be logged in to view')
        return redirect('home')

def customer_delete_record(request, pk):
    if request.user.is_authenticated:
        item = Record.objects.get(id = pk)
        item.delete()
        messages.success(request, 'Deleted Successfully')
        return redirect('home')
    else :
        messages.success(request, 'You must be logged in to delete')
        return redirect('home')


def add_record (request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated: 
        if request.method== "POST":
            if form.is_valid():
                add_record= form.save()
                messages.success(request, 'Added')
                return redirect('home')
        return render (request, 'add_record.html',{'form':form})
    else :
            messages.success(request, 'You must be logged in')
            return redirect('home')
def customer_update_record(request, pk):
    if request.user.is_authenticated: 
        current_record = Record.objects.get(id = pk)
        form = AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid ():
            form.save()
            messages.success(request, 'Record has been updated')
            return redirect('home')
        return render (request, 'update_record.html',{'form':form})
    else: 
        messages.success(request, 'You must be logged in')
        return redirect('home')