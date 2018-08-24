from django.contrib.auth.models import User
from django.db import models

'''
게시물 인덱스, 제목, 내용, 작성자, 작성시간, 고유 비밀번호
'''
class Post(models.Model):
    # 게시물 인덱스는 django의 고유키 pk를 이용.
    title = models.CharField(max_length=64)
    body = models.CharField(max_length=16384)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    regdate = models.DateTimeField(auto_created=True, auto_now_add=True)
    # 고유 비밀번호는 author의 권한인증을 이용.

# Create your models here.
