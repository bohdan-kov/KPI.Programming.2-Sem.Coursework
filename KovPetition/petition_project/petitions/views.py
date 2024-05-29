from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import PetitionForm, PetitionSignForm
from .models import Petition


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def user_logout(request):
    auth_logout(request)
    return redirect('home')


def create_petition(request):
    if request.method == 'POST':
        form = PetitionForm(request.POST)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.author = request.user
            petition.save()
            return redirect('home')
    else:
        form = PetitionForm()
    return render(request, 'create_petition.html', {'form': form})


def petition_list(request):
    petitions = Petition.objects.all()
    return render(request, 'petition_list.html', {'petitions': petitions})


def petition_detail(request, pk):
    petition = get_object_or_404(Petition, pk=pk)
    form = PetitionSignForm()
    subscribed = petition.supporters.filter(
        pk=request.user.pk).exists()  # Перевірка, чи користувач підписаний на петицію
    if request.method == 'POST':
        if 'subscribe' in request.POST:
            petition.supporters.add(request.user)
        elif 'unsubscribe' in request.POST:
            petition.supporters.remove(request.user)
        return redirect('petition_detail', pk=pk)
    return render(request, 'petition_detail.html', {'petition': petition, 'form': form, 'subscribed': subscribed})


def delete_petition(request, pk):
    petition = get_object_or_404(Petition, pk=pk)
    if request.user == petition.author:
        petition.delete()
    return redirect('petition_list')
