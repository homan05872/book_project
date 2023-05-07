from django.db import models
from .consts import MAX_RATE
from django.contrib.auth.models import User


RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]


CATEGORY = (('bussines','ビジネス'),('life','生活'),('novel','小説'),('comic','マンガ'),('other','その他'),)


class Book(models.Model):
    bookname = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    text = models.TextField()
    category = models.name = models.CharField(
        max_length=100,
        choices=CATEGORY
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(blank=True,null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
         return self.bookname


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='reviewuser', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


# カスタムユーザー　作成予定
class Profiel(models.Model):
    outher = models.OneToOneField(User,related_name='profiels', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    text = models.TextField()
    sex = models.CharField(choices=(('男性','男性'),('女性','女性')),
                           max_length=50)
    


