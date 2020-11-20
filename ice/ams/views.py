from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import NewUserForm
from .models import AmsUserProfile

@login_required
def dashboard(request):
    return render(request,'dashboard.html')



def register(request):
    form = NewUserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            profile = AmsUserProfile(belongs_to_ams_user=user)
            profile.save()
            login(request, user)
            return redirect('ams:dashboard')

    return render(request,'register.html',{'form':form})