from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    #장고에서 구현하는 user 불러와 photo를 fk로 연결
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'timeline_photo/%Y/%m/%d')
    #timeline_photo 폴더에 연, 월, 일 만들어 사진 저장
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "text : " + self.text
        #admin 사이트 화면 표시 구현 

    class Meta:
        ordering = ['-created']
        #ordering 정렬

    def get_absolute_url(self):
        return reverse('photo:detail', args = [self.id])
        #상세페이지로 이동하도록 absolute_url 설정, views 에서 return super가 나오게되면 absolute가 실행