from django.shortcuts import render, redirect
from board.models import Board, Comment

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    board_list=Board.objects.all().order_by('-date')

    return render(request, 'board/index.html', {'board_list':board_list})

def boardCreate(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        new_board = Board.objects.create(
            title = request.POST['title'],
            contents = request.POST['contents'],
            author = request.user.username,
            tag = request.POST['tag'],
        )
        return redirect(f'/board/{ new_board.id }')

    return render(request, 'board/create.html')

def boardDetail(request, board_id):
    if not request.user.is_authenticated:
        return redirect('login')
        
    board = Board.objects.get(id=board_id)

    if request.method == 'POST':
        Comment.objects.create(
            board = board,
            author = request.user.username,
            contents = request.POST['contents']
        )
        return redirect(f'/board/{board_id}')

    return render(request, 'board/detail.html', {'board':board})


def boardUpdate(request, board_id):
    if not request.user.is_authenticated:
        return redirect('login')

    board = Board.objects.get(id=board_id)

    if board.author != request.user.username:
        redirect(f'/board/{ board_id }')

    if request.method == 'POST':
        board.title = request.POST['title']
        board.contents = request.POST['contents']
        board.tag = request.POST['tag']
        board.save()
        return redirect(f'/board/{ board.id }')

    return render(request, 'board/update.html',{'board':board})


def boardDelete(request, board_id):
    if not request.user.is_authenticated:
        return redirect('login')

    board = Board.objects.get(id=board_id)

    if request.method == 'POST':
        if board.author != request.user.username:
            redirect(f'/board/{ board_id }')
        else:
            board.delete()
            return redirect('/board/')

##################################################################################################################################

def commentUpdate(request, comment_id):
    comment = Comment.objects.get(id=comment_id)

    if request.method == 'POST':
        if request.POST['password'] == comment.password:
            comment.name = request.POST['name']
            comment.contents = request.POST['contents']
            comment.save()
            return redirect(f'/board/{ comment.board.id }')

    return render(request, 'board/cupdate.html',{'comment':comment})


def commentDelete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)

    if request.method == 'POST':
        if request.POST['password'] == comment.password:
            comment.delete()
            return redirect(f'/board/{comment.board.id}')

    return render(request, 'board/cdelete.html',{'comment':comment})
