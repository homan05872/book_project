from django.db import models

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
