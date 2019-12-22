from django.shortcuts import render, redirect

def home(request):
    user = request.user
    return render(request, 'home/home.html',{'user':user})

def select(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home/select.html')