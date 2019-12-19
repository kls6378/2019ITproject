from django.shortcuts import render

def home(request):
    user = request.user
    return render(request, 'home/home.html',{'user':user})