from django.shortcuts import render, redirect
from board.models import Board, Comment, Vote

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
        if board.author != request.user.username:
            redirect(f'/board/{ board_id }')
        else:
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


def commentUpdate(request, board_id, comment_id):
    if not request.user.is_authenticated:
        return redirect('login')

    comment = Comment.objects.get(id=comment_id)

    if request.method == 'POST':
        if comment.author != request.user.username:
            redirect(f'/board/{ board_id }')
        else:
            comment.contents = request.POST['contents']
            comment.save()
            return redirect(f'/board/{ board_id }')


def commentDelete(request, board_id, comment_id):
    if not request.user.is_authenticated:
        return redirect('login')

    comment = Comment.objects.get(id=comment_id)

    if request.method == 'POST':
        if comment.author != request.user.username:
            redirect(f'/board/{ board_id }')
        else:
            comment.delete()
            return redirect(f'/board/{comment.board.id}')

def goodVote(request, board_id):
    if request.method == 'POST':
        user = request.user
        board = Board.objects.get(id=board_id)
        vote = Vote.objects.filter(board__id=board_id)
        if vote.filter(voteUser = user.username).exists():
            return redirect(f'/board/{ board_id }')
        else:
            Vote.objects.create(
                board = board,
                voteUser = user.username
            )
            board.goodVote += 1
            board.save()
        return redirect(f'/board/{ board_id }')
        
        

def badVote(request, board_id):
    if request.method == 'POST':
        user = request.user
        board = Board.objects.get(id=board_id)
        vote = Vote.objects.filter(board__id=board_id)
        if vote.filter(voteUser = user.username).exists():
            return redirect(f'/board/{ board_id }')
        else:
            Vote.objects.create(
                board = board,
                voteUser = user.username
            )
            board.badVote += 1
            board.save()
        return redirect(f'/board/{ board_id }')
        
        