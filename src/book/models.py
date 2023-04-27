from django.db import models
from .consts import MAX_RATE
#from django.contrib.auth.models import AbstractUser

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

CATEGORY = (('bussines','ビジネス'),('life','生活'),('novel','小説'),('comic','マンガ'),('other','その他'),)

class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices=CATEGORY
    )
    
    def __str__(self):
         return self.title

#レビュー作成予定
# class Review(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     text = models.TextField()
#     rate = models.IntegerField(choices=RATE_CHOICES)
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.title
    
     

#カスタムユーザー　作成予定


# class Review(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     text = models.TextField()
#     rate = models.IntegerField(choices=RATE_CHOICES)
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.title
