from django.shortcuts import render, redirect
from .forms import Register, Auth
from .models import User1
from django.contrib import messages
# Create your views here.


def home(request):
    user = User1.objects.all()
    return render(request, 'personal_area/home.html', {"user": user})


def register(request):
    if request.method == 'POST':
        reg = Register(request.POST)
        if reg.is_valid():
            username = reg.value('username')
            users = User1.objects.all()
            for user in users:
                if user.username == username:
                    reg = Register()
                    return redirect(request, 'personal_area/register.html', {'reg': reg})
            reg.save()
    else:
        reg = Register()
        return render(request, 'personal_area/register.html', {'reg': reg})


def login(request):
    if request.method == 'POST':
        form = Auth(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            users = User1.objects.all()
            for user in users:
                if user.username == username:
                    if user.password == password:
                        return redirect('succsessfully')
                else:
                    print(f'{username} {password}')
                    return redirect('error')
    else:
        auth = Auth()
        return render(request, 'personal_area/login.html', {'auth': auth})


def profile(request):
    return render(request, 'personal_area/profile.html')


def suc(request):
    return render(request, 'personal_area/succsessfully.html')


def error(request):
    return render(request, 'personal_area/error.html')