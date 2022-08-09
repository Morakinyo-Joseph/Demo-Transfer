from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Client
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from .forms import ClientForm
from django.contrib import messages
import random #Courtesy Jmoraks
import string #Courtesy Jmoraks
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.

# User = get_user_model()

def homeview(request):
    return render(request, "landing_page.html", {})

def dashboard(request):
    return render(request, "dashboard.html", {})

def registerview(request):
    form = ClientForm()

    # This is the correct way of using forms in your views

    if request.method == "POST":
        form = ClientForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_namae']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            pin = form.cleaned_data['pin']

            # Using cleaned_data is another way to get the correct inputs corresponding with the fields type in your MODELS.py

            Acc_Num = random.randint(100000000, 9999999999)

            if Client.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect("transfer:Register")
            
            elif Client.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect("transfer:Register")

            else:
                new_client = Client.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, pin=pin, Acc_Num=Acc_Num)
                new_client.save()
                return redirect("transfer:Login")

        else:
            messages.info(request, 'Invalid details')
            return redirect('transfer:Register')

    else:
        return render(request, "Transfer/register.html", {"form": form})


def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        pin = request.POST['pin']

        user = authenticate(username=username, password=pin) # i changed this to password because pin is not a recognized variable name

        if user is not None:
            login(request, user)
            return redirect("transfer:Dashboard")

        else:
            messages.info(request, 'Invalid username/pin')
            return redirect('transfer:Login')

    else:
        return render(request, "Transfer/login.html")

def logout_view(request):
    logout(request)
    return redirect("/")




