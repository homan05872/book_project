from django.test import TestCase
from book.models import Book,Review,Profiel

class ModelTests(TestCase):
        
    def book_is_empty(self):
        """Book:初期状態では何も登録されていない事をチェック"""
        saved_posts = Book.objects.all()
        self.assertEqual(saved_posts.count(), 1)
        
    def review_is_empty(self):
        """Review:初期状態では何も登録されていない事をチェック"""
        saved_posts = Profiel.objects.all()
        self.assertEqual(saved_posts.count(), 0)
        
    def review_is_empty(self):
        """Profiel:初期状態では何も登録されていない事をチェック"""
        saved_posts = Review.objects.all()
        self.assertEqual(saved_posts.count(), 0)


                