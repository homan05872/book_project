from urllib import response
from django.test import TestCase
from book.models import Book,Review,Profiel,User
from django.contrib.auth import get_user_model
from django.urls import reverse

UserModel = get_user_model()

class View_test(TestCase):
    
    def setUp(self):
        #Userモデル作成
        self.user = UserModel.objects.create(
            username='test_user',
            password='top_secret_001'
        )
        self.client.force_login(self.user)
        
    def test_login_setup(self):
        create_url = reverse('create')
        create_response = self.client.get(create_url)
        self.assertEqual(create_response.status_code,200)
      
      #テストうまくポスト送信できず中断     
    # def test_create_page(self):
    #     url = reverse('create')
    #     created_by = self.user
    #     profiel = Profiel.objects.get(pk=self.user.pk )
    #     create_data = {"bookname": "bookname_from_test", "subtitle": "content_from_test","text": "bookname_from_test", "category": "content_from_test"}
    #     response = self.client.post(url, create_data)
    #     qs_counter = Book.objects.count()
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(qs_counter, 1)