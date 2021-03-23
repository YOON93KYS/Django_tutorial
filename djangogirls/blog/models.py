from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):  # Class:객체를 정의한다 Post:모델이름. * Class의 첫 글자는 항사 대문
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  #ForeignKey:다른 모델에 대한 링크
    title = models.CharField(max_length=200)  # 글자 수가 제한된 텍스트를 정의할 때 사용
    text = models.TextField()  # 글자 수에 제한이 없는 긴 텍스트
    created_date = models.DateTimeField(
            default=timezone.now)  # 날짜와 시간
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):  # def:함수/메서드 publish:메서드의 이름 * 소문자와 언더스코어를 사용
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title