from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # 用为数有限的字符来定义一个文本
    text = models.TextField()  # 没有长度限制的长文本
    created_date = models.DateTimeField(default=timezone.now)   # 日期和时间
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title