from urllib import response
from django.test import TestCase
from book.models import Book,Review,Profiel,User
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve, reverse_lazy
from .. import views
from django.shortcuts import render, redirect
from book import forms

UserModel = get_user_model()

class View_test(TestCase):
    
    def setUp(self):
        #Userモデル作成
        self.user = UserModel.objects.create(
            username='test_user',
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
        
      
    def test_access_booklist(self):
        """Booklist_レスポンスチェックテスト"""
        book_obj = Book.objects.all()
        self.assertEqual(book_obj.count(), 1)
        response_list = self.client.get("/list/")
        self.assertEqual(response_list.status_code, 200)
        self.assertContains(response_list, "Book 一覧ページ")
        self.assertContains(response_list, book_obj[0].bookname)
        
    def test_access(self):
        """view関数確認テスト"""
        index_view = resolve('/') 
        list_view = resolve('/list/')
        detail_view = resolve('/detail/1/')
        create_view = resolve('/create/')
        update_view = resolve('/update/1/')
        delete_view = resolve('/delete/1/')
        self.assertEquals(index_view.func.view_class, views.IndexBook)
        self.assertEquals(list_view.func, views.listBook)
        self.assertEquals(detail_view.func, views.detailBook)
        self.assertEquals(create_view.func, views.createBook)
        self.assertEquals(update_view.func, views.updateBook)
        self.assertEquals(delete_view.func.view_class, views.DeleteBook)
        
    def test_create_view(self):
        """crateフォーム送信テスト"""
        url = reverse('create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        create_data = {"bookname": "bookname_from_test", "subtitle": "content_from_test","text": "bookname_from_test", "category": "ビジネス"}
        response = self.client.post(url, create_data)
        qs_counter = Book.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(qs_counter, 2)
        
        
    def test_update_form_instance(self):
        """update_フォームインスタンス確認テスト"""
        url = reverse('update', kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        book = Book.objects.get(pk=1)
        self.assertContains(response, book.bookname)
        self.assertContains(response, book.subtitle)
        self.assertContains(response, book.text)
        self.assertContains(response, book.thumbnail)
        self.assertContains(response, book.category)
        
    def test_update1(self):
        """Update_viewのpost送信をテストする"""
        books = Book.objects.all()
        url = reverse('update', kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(books.count(), 1)
        book = Book.objects.get(id=1)
        form = forms.BookForm(instance=book)
        form.bookname = 'Updateテスト'
        response = self.client.get(url, form)
        update_book = Book.objects.get(id=1)
        self.assertEqual(update_book.bookname, 'Updateテスト')
        
        
        
        
        
        # self.assertEqual(response.context['form'].initial['bookname'], book.bookname)
        
        # response = self.client.post(reverse_lazy('update', kwargs={'pk': book.pk}), update_data)
        # # 詳細ページへのリダイレクトを検証
        # self.assertRedirects(response, redirect('detail', kwargs={'pk': book.pk}))
        # response = self.client.post('/update/1/', update_data)
        # book = Book.objects.get(pk=1)
        
        # self.assertEqual(book.bookname, "updateテスト")
        
        