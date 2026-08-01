from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout, get_user_model
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
import logging
logger = logging.getLogger(__name__)

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("coniform_password")

        if password != confirm_password:
            messages.error(request, "Parol mos emas")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email allaqochon royhatan otkan")
            return redirect(register)

        user = User.objects.create_user(email=email, username=username, password=password)
        user.save()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            messages.success(request, "Siz Tizimga Kirdingiz")
            return redirect("login")

        messages.error(request, "Nomalum Xato")
        return redirect("register")

    return render(request, "register.html")
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        parol = request.POST.get('parol', " ").strip()
        if not username:
            messages.warning(request, "Iltimos login kiriting")
            messages.error(request, "Username bo'sh")
            return redirect("login")
        try:
            user = User.objects.get(username=username)
            if user.is_superuser:
                logger.info(f"Admin {user.username} login qilindi")
                return redirect("home")
            else:
                if not parol:
                    messages.warning(request, "Iltimos parol kiriting")
                    messages.error(request, "Parol bo'sh")
                    return redirect("login")
            user = authenticate(request, username=username, password=parol)
            if user:
                auth_login(request, user)
                messages.success(request, "Siz tizimga kirdingiz")
                return redirect("home")
            else:
                logger.warning(f"{user.username} login qilolmadi")
                messages.error(request, "Parol xato")
                return redirect("login")
        except:
            pass
        

    return render(request, 'login.html')