from django.db import models
from .consts import MAX_RATE
#from django.contrib.auth.models import AbstractUser

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        )
    
    def __str__(self):
         return self.title
    
class Category(models.Model):
     category = models.CharField(
         max_length=100,
     ) 
     
     def __str__(self):
         return self.category
     

#カスタムユーザー　作成予定


# class Review(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     text = models.TextField()
#     rate = models.IntegerField(choices=RATE_CHOICES)
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.title
