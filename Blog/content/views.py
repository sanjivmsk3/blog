from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from content.forms import RegForm,ContentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from content.models import Content

# Create your views here.

def reg(r):
    form = RegForm(r.POST or None)
    if r.method == 'POST':
        username = r.POST.get('username')
        if not (len(username)) >= 8 :
            return redirect(reg)
        
        if form.is_valid():
            form.save()
            return redirect('homepage')

    return render(r,'signup.html',{'form':form})


def home(r):
    if r.method == 'POST':
        username = r.POST.get('username')
        password = r.POST.get('password')
        user = authenticate(r,username=username,password=password)
        if user is not None:
            login(r,user)
            return redirect(log)
        else:
            return redirect(home)
    return render(r,'home.html')

@login_required(login_url='homepage')
def out(r):
    logout(r)
    return redirect(home)

@login_required(login_url='homepage')
def log(r):
    form = ContentForm(r.POST or None, r.FILES or None)
    if r.method == 'POST':
        if form.is_valid():
            f = form.save(commit=False)
            f.user = r.user
            f.save()
            return redirect(log)

    return render(r,'usercontent.html',{
        'con':Content.objects.filter(status='PUBLIC'),
        'add_form':form,
        'all_con':Content.objects.all(),
        'count':Content.objects.all().count(),
        })