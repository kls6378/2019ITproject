from django.shortcuts import render, redirect

def home(request):
    user = request.user

    if request.user.is_authenticated:
        return redirect('select')

    return render(request, 'home/sign_in.html',{'user':user})

def welcome(request):
    if not request.user.is_authenticated:
        return redirect('home')
    return render(request, 'home/welcome.html')


def select(request):
    if not request.user.is_authenticated:
        return redirect('home')
    return render(request, 'home/select.html')