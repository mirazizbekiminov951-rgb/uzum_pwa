from django.shortcuts import render, get_object_or_404
from .models import *

def navigation(request):
    return render(request, "navigation.html")

def footer(request):
    return render(request, "footer.html")

def home(request):
    Narsa = Product.objects.all()
    return render(request, "home.html", {"items" : Narsa})

def topshirish_punkiti(request):
    return render(request, "topshirish_punkiti.html")

def detail(request, id):
    mahsulot = get_object_or_404(Product, id=id)
    context = {
        "mahsulot": mahsulot  
    }
    return render(request, "detail.html", context)

def sotuvchi_bolish(request):
    return render(request, "sotuvchi_bolish.html")

def sotuv(request):
    return render(request, "sotuv.html")

def savol(request):
    return render(request, "savol.html")

def sotuvchilik(request):
    return render(request, "sotuvchilik.html")

def splash(request):
    return render(request, 'splash.html')

def register(request):
    return render(request, 'register.html')

def category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    narsalar = Product.objects.filter(category=category)
    return render(request, 'category.html', {
        "categories" : category,
        "items" : narsalar
    })
def savat(request):
    return render(request, "savat.html")