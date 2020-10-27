from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from accounts.models import GuestEmail
from django.utils.http import is_safe_url



def home_page(request):
    context ={
      "title":"Hello World",
      "content":" Welcome to the homepage",
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context ={
      "title":"About",
      "content":" Welcome to the about_page",
    }
    return render(request, "about_page.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
      "form": form
    }
    print("User logged in")
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            print("Error")
    return render(request, "login.html", context)

def logout_page(request):
    logout(request)
    return redirect("/login")

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
      "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        if new_user is not None:
            return redirect("/")
    return render(request, "register.html", context)
