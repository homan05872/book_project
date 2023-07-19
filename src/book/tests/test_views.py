from urllib import response
from django.test import TestCase
from book.models import Book,Review,Profiel,User
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve 
from .. import views
from django.shortcuts import render, redirect

UserModel = get_user_model()
from accounts.models import User

class View_test_access(TestCase):
    
    def setUp(self):
        #Userモデル作成
        self.user = User.objects.create(
            email='test_user',
            nickname='test_user',
            password='top_secret_001'
        )
        self.client.force_login(self.user)
        #Bookモデル作成
        book = Book(bookname="testbook", subtitle="testbook", text="text", category="ビジネス")
        book.created_by = UserModel.objects.get(pk=1)
        book.profiel_connect=Profiel.objects.get(pk=1)
        book.save()
        
        
    def test_login_setup(self):
        """ログイン確認"""
        create_url = reverse('create')
        create_response = self.client.get(create_url)
        self.assertEqual(create_response.status_code,200)
        
        
    def test_access(self):
        """view関数確認テスト"""
        index_view = resolve('/') 
        list_view = resolve('/list/')
        detail_view = resolve('/detail/1/')
        create_view = resolve('/create/')
        update_view = resolve('/update/1/')
        delete_view = resolve('/delete/1/')
        self.assertEquals(index_view.func.view_class, views.IndexBook)
        self.assertEquals(list_view.func.view_class, views.ListBook)
        self.assertEquals(detail_view.func.view_class, views.DetailBook)
        self.assertEquals(create_view.func.view_class, views.CreateBook)
        self.assertEquals(update_view.func.view_class, views.UpdateBook)
        self.assertEquals(delete_view.func.view_class, views.DeleteBook)
        
        
class list_view_test(TestCase):
    def setUp(self):
        #Userモデル作成
        self.user = User.objects.create(
            email='test_user',
            nickname='test_user',
            password='top_secret_001'
        )
        self.client.force_login(self.user)
        #Bookモデル作成
        book = Book(bookname="testbook1", subtitle="testbook1", text="text", category="ビジネス")
        book.created_by = UserModel.objects.get(pk=1)
        book.profiel_connect = Profiel.objects.get(pk=1)
        book.save()
        book2 = Book(bookname="testbook2", subtitle="testbook2", text="text", category="ビジネス")
        book2.created_by = UserModel.objects.get(pk=1)
        book2.profiel_connect = Profiel.objects.get(pk=1)
        book2.save()
        book3 = Book(bookname="testbook3", subtitle="testbook3", text="text", category="ビジネス")
        book3.created_by = UserModel.objects.get(pk=1)
        book3.profiel_connect = Profiel.objects.get(pk=1)
        book3.save()
        
    def test_book_model_quantity(self):
        """Bookモデル数 確認"""
        book = Book.objects.all()
        self.assertEqual(book.count(), 3)
        
    def test_book_search(self):
        """serarchformテスト(1で検索した場合)"""
        book = Book.objects.all()
        response = self.client.get("/list/?bookname=1")
        self.assertContains(response, "Book 一覧ページ")
        self.assertContains(response, book[0].bookname)
        self.assertNotContains(response, book[1].bookname)
        self.assertNotContains(response, book[2].bookname)
        self.assertContains(response, book[0].subtitle)
        self.assertNotContains(response, book[1].subtitle)
        self.assertNotContains(response, book[2].subtitle)
        
    def test_book_search(self):
        """serarchformテスト(2で検索した場合)"""
        book = Book.objects.all()
        response = self.client.get("/list/?bookname=2")
        self.assertContains(response, "Book 一覧ページ")
        self.assertContains(response, book[1].bookname)
        self.assertNotContains(response, book[0].bookname)
        self.assertNotContains(response, book[2].bookname)
        self.assertContains(response, book[1].subtitle)
        self.assertNotContains(response, book[0].subtitle)
        self.assertNotContains(response, book[2].subtitle)
    
    def test_book_search(self):
        """serarchformテスト(3で検索した場合)"""
        book = Book.objects.all()
        response = self.client.get("/list/?book=3")
        self.assertContains(response, "Book 一覧ページ")
        self.assertContains(response, book[2].bookname)
        self.assertNotContains(response, book[0].bookname)
        self.assertNotContains(response, book[1].bookname)
        self.assertContains(response, book[2].subtitle)
        self.assertNotContains(response, book[0].subtitle)
        self.assertNotContains(response, book[1].subtitle)
        
    def test_access_booklist(self):
        """Booklist_レスポンスチェックテスト"""
        book_obj = Book.objects.all()
        self.assertEqual(book_obj.count(), 3)
        response_list = self.client.get("/list/")
        self.assertEqual(response_list.status_code, 200)
        self.assertContains(response_list, "Book 一覧ページ")
        self.assertContains(response_list, book_obj[0].bookname)
        self.assertContains(response_list, book_obj[0].subtitle)
        self.assertContains(response_list, book_obj[0].text)
        self.assertContains(response_list, book_obj[0].category)
       
    def test_search(self):
        """searchformからのGET送信テスト"""
        url = "/list/?bookname=テスト"
        response = self.client.get(url)
        
    
        
            
class Detail_view_test(TestCase):
    def setUp(self):
        #Userモデル作成
        self.user = User.objects.create(
            email='test_user',
            nickname='test_user',
            password='top_secret_001'
        )
        self.client.force_login(self.user)
        #Bookモデル作成
        book = Book(bookname="testbook", subtitle="testbook", text="text", category="ビジネス")
        book.created_by = UserModel.objects.get(pk=1)
        book.profiel_connect=Profiel.objects.get(pk=1)
        book.save()
        
    def test_detail_access(self):
        """detailView アクセスチェック"""
        url = reverse('detail', kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_detail_comment_post(self):
        """コメントPOST送信テスト"""
        url = reverse('new_comment', kwargs={"pk": 1})
        create_data = {"text":"testcomment", "rate": 1}
        response = self.client.post(url, create_data)
        qs_counter = Review.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('detail', kwargs={"pk": 1}))
        self.assertEqual(qs_counter, 1)
        #detailviewの表示チェック
        review = Review.objects.get(pk=1)
        detail_url = reverse('detail', kwargs={"pk": 1})
        detail_response = self.client.get(detail_url)
        self.assertContains(detail_response, review.text)
        self.assertContains(detail_response, review.rate)
        

class Create_view_test(TestCase):
    
    def setUp(self):
        #Userモデル作成
        self.user = User.objects.create(
            email='test_user',
            nickname='test_user',
            password='top_secret_001'
        )
        self.client.force_login(self.user)
        #Bookモデル作成
        book = Book(bookname="testbook", subtitle="testbook", text="text", category="ビジネス")
        book.created_by = UserModel.objects.get(pk=1)
        book.profiel_connect=Profiel.objects.get(pk=1)
        book.save()
        
        
    def test_login_setup(self):
        """ログイン確認"""
        create_url = reverse('create')
        create_response = self.client.get(create_url)
        self.assertEqual(create_response.status_code,200)
        
    def test_create_view(self):
        """crateフォーム送信テスト"""
        url = reverse('create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        create_data = {"bookname": "bookname_from_test", "subtitle": "content_from_test","text": "bookname_from_test", "category": "ビジネス"}
        response = self.client.post(url, create_data)
        qs_counter = Book.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('detail', kwargs={"pk": 2}))
        self.assertEqual(qs_counter, 2)
        
        
class Update_view_test(TestCase):
    def setUp(self):
        #Userモデル作成
        self.user = User.objects.create(
            email='test_user',
            nickname='test_user',
            password='top_secret_001'
        )
        self.client.force_login(self.user)
        #Bookモデル作成
        book = Book(bookname="testbook", subtitle="testbook", text="text", category="ビジネス")
        book.created_by = UserModel.objects.get(pk=1)
        book.profiel_connect=Profiel.objects.get(pk=1)
        book.save()
        
        
    def test_login_setup(self):
        """ログイン確認"""
        create_url = reverse('create')
        create_response = self.client.get(create_url)
        self.assertEqual(create_response.status_code,200)
            
    def test_update_form_instance(self):
        """update_フォームインスタンス確認テスト & アクセステスト"""
        url = reverse('update', kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        book = Book.objects.get(pk=1)
        self.assertContains(response, book.bookname)
        self.assertContains(response, book.subtitle)
        self.assertContains(response, book.text)
        self.assertContains(response, book.thumbnail)
        self.assertContains(response, book.category)
        
    def test_update_post(self):
        """update_post送信テスト"""
        url = reverse('update', kwargs={"pk": 1})
        update_data = {"bookname": "bookname_update_test", "subtitle": "subtitle_update_test","text": "text_update_test", "category": "生活"}
        response = self.client.post(url, update_data)
        qs_counter = Book.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('detail', kwargs={"pk": 1}))
        self.assertEqual(qs_counter, 1)
        
        #編集されているかテスト
        book = Book.objects.get(pk=1)
        self.assertEqual(book.bookname, "bookname_update_test")
        self.assertEqual(book.subtitle, "subtitle_update_test")
        self.assertEqual(book.text, "text_update_test")
        self.assertEqual(book.category, "生活")
    
        
        
        
class DeleteTest(TestCase):
    def setUp(self):
        #Userモデル作成
        self.user = User.objects.create(
            email='test_user',
            nickname='test_user',
            password='top_secret_001'
        )
        self.client.force_login(self.user)
        #Bookモデル作成
        book = Book(bookname="testbook", subtitle="testbook", text="text", category="ビジネス")
        book.created_by = UserModel.objects.get(pk=1)
        book.profiel_connect=Profiel.objects.get(pk=1)
        book.save()
    
    def test_delete_view(self):
        """アクセステスト"""
        url = reverse('delete', kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_delete_post(self):
        url = reverse('delete', kwargs={"pk": 1})
        response = self.client.post(url)
        books=Book.objects.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('booklist'))
        self.assertEqual(books.count(), 0)