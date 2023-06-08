from urllib import response
from django.test import TestCase
from book.models import Book,Review,Profiel,User
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

UserModel = get_user_model()

class status_check302_test(TestCase):
    
    def test_response_no_login(self):
        """未loginの場合のアクセス制限ページのリダイレクトチェック"""
        #アクセス制限なし    
        index_url = reverse('index')
        index_response = self.client.get(index_url)
        booklist_url = reverse('booklist')
        booklist_response = self.client.get(booklist_url)
        #アクセス制限あり
        create_url = reverse('create')
        create_response = self.client.get(create_url)
        detail_url = reverse('detail', kwargs={"pk": 1})
        detail_response = self.client.get(detail_url)
        update_url = reverse('update', kwargs={"pk": 1})
        update_response = self.client.get(update_url)
        delete_url = reverse('delete', kwargs={"pk": 1})
        delete_response = self.client.get(delete_url)
        self.assertEqual(index_response.status_code,200)
        self.assertEqual(booklist_response.status_code,200)
        self.assertEqual(create_response.status_code,302)
        self.assertEqual(detail_response.status_code, 302)
        self.assertEqual(update_response.status_code, 302)
        self.assertEqual(delete_response.status_code, 302)
        
    def test_response_login(self):
        """ログイン時 リダイレクトテスト"""
        
        #Userモデル作成
        self.user = UserModel.objects.create(
            username='test_user',
            password='top_secret_001'
        )
        saved_user = UserModel.objects.all()
        self.assertEqual(saved_user.count(), 1)
        self.assertEqual(saved_user[0].username, 'test_user')
        self.assertEqual(saved_user[0].pk, 1)
        
        #ログイン処理
        self.client.force_login(self.user)
        
        #Bookモデル作成
        book = Book(bookname="testbook", subtitle="testbook", text="text", category="ビジネス")
        book.created_by = UserModel.objects.get(pk=1)
        book.profiel_connect=Profiel.objects.get(pk=1)
        book.save()
        books=Book.objects.all()
        self.assertEqual(books.count(),1)
        
        #アクセス制限なし    
        index_url = reverse("index")
        index_response = self.client.get(index_url)
        booklist_url = reverse('booklist')
        booklist_response = self.client.get(booklist_url)
        #アクセス制限あり
        create_url = reverse('create')
        create_response = self.client.get(create_url)
        detail_url = reverse('detail', kwargs={"pk": 1})
        detail_response = self.client.get(detail_url)
        update_url = reverse('update', kwargs={"pk": 1})
        update_response = self.client.get(update_url)
        delete_url = reverse('delete', kwargs={"pk": 1})
        delete_response = self.client.get(delete_url)
        self.assertEqual(index_response.status_code,200)
        self.assertEqual(booklist_response.status_code,200)
        self.assertEqual(create_response.status_code,200)
        self.assertEqual(detail_response.status_code, 200)
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(delete_response.status_code, 200)
        
    def test_status_check404(self):
        #Userモデル作成
        self.user = UserModel.objects.create(
            username='test_user',
            password='top_secret_001'
        )
        saved_user = UserModel.objects.all()
        self.assertEqual(saved_user.count(), 1)
        self.assertEqual(saved_user[0].username, 'test_user')
        self.assertEqual(saved_user[0].pk, 1)
        
        #Bookモデル作成
        book = Book(bookname="testbook", subtitle="testbook", text="text", category="ビジネス")
        book.created_by = UserModel.objects.get(pk=1)
        book.profiel_connect=Profiel.objects.get(pk=1)
        book.save()
        books=Book.objects.all()
        self.assertEqual(books.count(),1)
        
        #ログイン処理
        self.client.force_login(self.user)
        detail_url = reverse('detail', kwargs={"pk": 100})
        detail_response = self.client.get(detail_url)
        update_url = reverse('update', kwargs={"pk": 100})
        update_response = self.client.get(update_url)
        delete_url = reverse('delete', kwargs={"pk": 100})
        delete_response = self.client.get(delete_url)
        self.assertEqual(detail_response.status_code, 404)
        self.assertEqual(update_response.status_code, 404)
        self.assertEqual(delete_response.status_code, 404)
        
