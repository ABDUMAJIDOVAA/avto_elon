# Caqirib olingan funksiya va classlar

from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Avtomobillar
from .forms import AvtoForm, CategoryForm, LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Funksiyalaar

def all_avtolar(request):
    avtolar = Avtomobillar.objects.filter(published=True)
    categories = Category.objects.all()
    context = {
        'title': "Barcha Avtomobillar",
        'avtolar': avtolar,
        'categories': categories
    }
    return render(request, 'elonlar/index.html', context)

def avtolar_list(request):
    avtolar = Avtomobillar.objects.all()
    context = {
        'avtolar': avtolar
    }
    return render(request, 'elonlar/avto_list.html', context)

def avtolar_detail(request, pk):
    avto = get_object_or_404(Avtomobillar, pk=pk)
    avto.views += 1
    avto.save()
    return render(request, 'elonlar/avto_detail.html', {'avto': avto})

def avto_create(request):
    if request.method == "POST":
        form = AvtoForm(request.POST, request.FILES)
        if form.is_valid():
            avto = form.save(commit=False)
            avto.save()
            return redirect('avto_detail', pk=avto.pk)
    else:
        form = AvtoForm()
    return render(request, 'elonlar/avto_create.html', {'form': form})

def avto_update(request, pk):
    avto = get_object_or_404(Recipes, pk=pk)
    if request.method == "POST":
        form = AvtoForm(request.POST, request.FILES, instance=avto)
        if form.is_valid():
            avto = form.save(commit=False)
            avto.save()
            return redirect('avto_detail', pk=avto.pk)
    else:
        form = AvtoForm(instance=avto)
    return render(request, 'elonlar/avto_update.html', {'form': form})

def avto_delete(request, pk):
    avto = get_object_or_404(Avtomobillar, pk=pk)
    avto.delete()
    return redirect('avto_list')
    
def avto_by_category(request, category_id):
    avtolar = Avtomobillar.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'avtolar': avtolar,
        'categories': categories,
    }
    return render(request, 'elonlar/index.html', context=context)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'elonlar/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'elonlar/category_detail.html', {'category': category})

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = CategoryForm()
    return render(request, 'elonlar/category_create.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'elonlar/category_update.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')

def user_login(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, f'{user.username} saytga muvaffaqiyatli kirdingiz!')
        return redirect('index')
    return render(request, 'elonlar/user_login.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')

def user_register(request):
    form = RegisterForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, f'{user.username} saytdan muvaffaqiyatli ro\'yxatdan o\'tdingiz!')
        return redirect('index')
    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'elonlar/register.html', context)

def view_profile(request):
    if hasattr(request.user, 'profile'):
        profile = request.user.profile
        return render(request, 'view_profile.html', {'profile': profile})
    else:
        return render(request, 'elonlar/user_profile.html')

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'elonlar/edit_profile.html', {'form': form})