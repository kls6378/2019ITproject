from django.shortcuts import render, redirect
from board.models import Board, Comment

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    board_list=Board.objects.all().order_by('-date')
    return render(request, 'board/index.html', {'board_list':board_list})


# def detail(request, board_id):
#     board=get_object_or_404(Board, pk=board_id)

#     if request.method == 'POST':
#         Comment.objects.create(
#             board = board,
#             name = request.POST['name'],
#             password = request.POST['password'],
#             contents = request.POST['contents']
#         )
#         return redirect(f'/board/{board_id}')

#     return render(request, 'board/detail.html', {'board':board})


# def create(request):
#     if request.method == 'POST':
#         new_board = Board.objects.create(
#             name = request.POST['name'],
#             password = request.POST['password'],
#             title = request.POST['title'],
#             contents = request.POST['contents']
#         )
#         return redirect(f'/board/{ new_board.id }')

#     return render(request, 'board/create.html')


# def update(request, board_id):
#     board = Board.objects.get(id=board_id)

#     if request.method == 'POST':
#         if request.POST['password'] == board.password:
#             board.name = request.POST['name']
#             board.title = request.POST['title']
#             board.contents = request.POST['contents']
#             board.save()
#             return redirect(f'/board/{ board.id }')

#     return render(request, 'board/update.html',{'board':board})


# def delete(request, board_id):
#     board = Board.objects.get(id=board_id)

#     if request.method == 'POST':
#         if request.POST['password'] == board.password:
#             board.delete()
#             return redirect('/board/')

#     return render(request, 'board/delete.html',{'board':board})


# def cupdate(request, comment_id):
#     comment = Comment.objects.get(id=comment_id)

#     if request.method == 'POST':
#         if request.POST['password'] == comment.password:
#             comment.name = request.POST['name']
#             comment.contents = request.POST['contents']
#             comment.save()
#             return redirect(f'/board/{ comment.board.id }')

#     return render(request, 'board/cupdate.html',{'comment':comment})


# def cdelete(request, comment_id):
#     comment = Comment.objects.get(id=comment_id)

#     if request.method == 'POST':
#         if request.POST['password'] == comment.password:
#             comment.delete()
#             return redirect(f'/board/{comment.board.id}')

#     return render(request, 'board/cdelete.html',{'comment':comment})
