from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='board'),
    path('create/', views.boardCreate, name='board_create'),
    path('<int:board_id>/', views.boardDetail, name='board_detail'),
    path('<int:board_id>/update/', views.boardUpdate, name='board_update'),
    path('<int:board_id>/delete/', views.boardDelete, name='board_delete'),
    path('<int:board_id>/goodVote/', views.goodVote, name='good_vote'),
    path('<int:board_id>/badVote/', views.badVote, name='bad_vote'),
    path('<int:board_id>/<int:comment_id>/update/', views.commentUpdate, name='comment_update'),
    path('<int:board_id>/<int:comment_id>/delete/', views.commentDelete, name='comment_delete'),
]