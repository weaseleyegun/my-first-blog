from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):   #모델 정의 model = object
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)      #다른 모델에 대한 링크
    title = models.CharField(max_length=200)    #CharField: 글자수가 제한된 텍스트를 정의
    text = models.TextField()   #TextField: 글자수에 제한이 없는 텍스트 정의
    created_date = models.DateTimeField(default=timezone.now)   #DateTimeField: 날짜와 시간을 의미
    published_date = models.DateTimeField(blank=True, null=True)

    def pulish(self):   #메서드 (method)
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#makemigrations -> migrate