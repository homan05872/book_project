from django.test import TestCase
from book.models import Book,Review,Profiel
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User

UserModel = get_user_model()


class ModelTests(TestCase):    
        
    def test_book_is_empty(self):
        """Book:初期状態では何も登録されていない事をチェック"""
        saved_posts = Book.objects.all()
        self.assertEqual(saved_posts.count(), 0)
        
    def test_profiel_is_empty(self):
        """Profiel:初期状態では何も登録されていない事をチェック"""
        saved_posts = Profiel.objects.all()
        self.assertEqual(saved_posts.count(), 0)
        
    def test_review_is_empty(self):
        """Profiel:初期状態では何も登録されていない事をチェック"""
        saved_posts = Review.objects.all()
        self.assertEqual(saved_posts.count(), 0)
        
    def test_user_is_empty(self):
        "Userモデルの存在確認"
        saved_posts = UserModel.objects.all()
        self.assertEqual(saved_posts.count(), 0)
        
        
class CreateTest(TestCase):
    
    def test_UserModel_create(self):
        """Userモデル作成テスト(同時にProfielモデルも自動作成)"""
        user = UserModel(username="test_user",password="top_secret_001")
        user.save()
        saved_users = User.objects.all()
        saved_profiels = Profiel.objects.all()
        self.assertEqual(saved_users.count(), 1)
        self.assertEqual(saved_profiels.count(), 1)
        
        saved_user = User.objects.get(pk=1)
        saved_profiel = Profiel.objects.get(pk=1)
        self.assertEqual(saved_profiel.nickname,saved_user.username)
        
    def test_book_create(self):
        """Bookモデル作成テスト"""
        user = UserModel(username="test_user",password="top_secret_001")
        user.save()
        
        book = Book(bookname="testbook", subtitle="testbook", text="text", category="ビジネス")
        book.created_by=UserModel.objects.get(pk=1)
        book.profiel_connect = Profiel.objects.get(pk = 1)
        book.save()
        saved_books = Book.objects.all()
        book = Book.objects.get(pk=1)
        self.assertEqual(saved_books.count(), 1)
        self.assertEqual(book.bookname,"testbook")
    
    
    def test_Review_create(self):
        """reviewモデル作成テスト"""
        user = UserModel(username="test_user",password="top_secret_001")
        user.save()
        book = Book(bookname="testbook", subtitle="testbook", text="text", category="ビジネス")
        book.created_by=UserModel.objects.get(pk=1)
        book.profiel_connect = Profiel.objects.get(pk = 1)
        book.save()
        
        review = Review(text="testtext", rate="1")
        review.created_by=UserModel.objects.get(pk=1)
        review.book = Book.objects.get(pk = 1)
        review.save()
        saved_books = Review.objects.all()
        review = Review.objects.get(pk=1)
        self.assertEqual(saved_books.count(), 1)
        self.assertEqual(review.text,"testtext")
        
class UpdateTest(TestCase):
    
    def test_update_book(self):
        """Book_Updateテスト"""
        user = UserModel(username="test_user",password="top_secret_001")
        user.save()
        book = Book(bookname="testbook", subtitle="testbook", text="text", category="ビジネス")
        book.created_by=UserModel.objects.get(pk=1)
        book.profiel_connect = Profiel.objects.get(pk = 1)
        book.save()
        
        self.assertEqual(book.bookname, "testbook")
        
        book = Book.objects.get(pk=1)
        book.bookname = "book編集後"
        book.subtitle = "title編集後"
        book.text = "text編集後"
        book.category = "category編集後"
        book.save()
        self.assertEqual(book.bookname, "book編集後")
        self.assertEqual(book.subtitle, "title編集後")
        self.assertEqual(book.text, "text編集後")
        self.assertEqual(book.category, "category編集後")
        
    def test_update_Profiel(self):
        """Book_Profeilテスト"""
        user = UserModel(username="test_user",password="top_secret_001")
        user.save()
        
        profiel = Profiel.objects.get(pk=1)
        self.assertEqual(profiel.pk, 1)

        profiel.nickname = "nickname編集後"
        profiel.text = "text編集後"
        profiel.sex = "男性"
        profiel.save()
        self.assertEqual(profiel.nickname,"nickname編集後")
        self.assertEqual(profiel.text,"text編集後")
        self.assertEqual(profiel.sex,"男性")
        
    
class DeleteTest(TestCase):
    """削除テスト"""
    
    def test_delete_book(self):
        """Book_Deleteテスト"""
        user = UserModel(username="test_user",password="top_secret_001")
        user.save()
        book = Book(bookname="testbook", subtitle="testbook", text="text", category="ビジネス")
        book.created_by=UserModel.objects.get(pk=1)
        book.profiel_connect = Profiel.objects.get(pk = 1)
        book.save()
        
        books = Book.objects.all()
        self.assertEqual(books.count(), 1)
        
        book = Book.objects.get(pk=1)
        book.delete()
        
        saved_books=Book.objects.all()
        
        self.assertEqual(saved_books.count(), 0)
        