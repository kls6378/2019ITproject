from django.contrib import admin
from board.models import Board, Comment, Vote

# Register your models here.

admin.site.register(Board)
admin.site.register(Comment)
admin.site.register(Vote)