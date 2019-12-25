from django.db import models

# Create your models here.

class Board(models.Model):
    goodVote = models.IntegerField(default=0)
    badVote = models.IntegerField(default=0)
    title = models.CharField(max_length=30)
    contents = models.CharField(max_length=300)
    author = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    contents = models.CharField(max_length=300)
    author = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.contents