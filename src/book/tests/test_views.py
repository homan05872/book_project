from urllib import response
from django.test import TestCase
from book.models import Book,Review,Profiel,User
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Model_add_test(TestCase):
    
    def SetUp(self):
        self.user = User.objects.create(
            username = 'test_user',
            email = 'test@example.com',
            password = 'secret',    
        )
        self.client.force_login(self.user)
        
    # def test_create_views(self):
    #     """ユーザーがログイン状態でcreateにアクセス時のステータスコードテスト"""
    #     response = self.client.get("create/")
    #     self.assertContains(response, "text", status_code=200)
            
    # def test_create_book(self):
    #     """ユーザーがポスト送信でデータを送った際のBookモデルの保存テスト"""
    #     response = self.client.get("create/")
        
    #     book = '書籍'
    #     subtitle = 'タイトル'
    #     text = '本文'
    #     category = 'ビジネス'
    #     data = {'bookname':book , 'subtitle':subtitle,'text':text, 'category':category}
    #     self.client.post('create/',data)
    #     book = Book.objects.get(bookname=book)
    #     self.assertContains(response, "text", status_code=200)
    #     self.assertEqual('タイトル', book.subtitle)