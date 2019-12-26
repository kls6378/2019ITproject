from django.shortcuts import render,redirect
from board.models import Board
from rest_framework.views import APIView

# Create your views here.

def recipe(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'recipe/index.html')

class Search(APIView):
    def get(self, request, format=None):
        tags = request.query_params.get('tags', None)

        if tags is not None:
            tags = tags.replace(" ","").split(',')
            board = Board.objects.filter(tags__name__in=tags).distinct()

        else:
            board = Board.objects.all()
        return render(request, 'recipe/results.html', {'board':board})

