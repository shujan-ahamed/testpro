from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from base_app.forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
            
        form = CreateUserForm()
        

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                username = form.cleaned_data.get('username')

                messages.success(request,'Account has been created succesfully for '+ username)

                return redirect('login')
                
        context = {'form':form}
        return render(request,'register_page.html',context)



def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username , password= password)
            if user is not None:
                login(request,user)

                messages.success(request,'Login succesfull')
                return redirect('index')

            else:
                messages.info(request,'Username or Password is incorrect.')

        return render(request,'login_page.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)

    return redirect('login')


