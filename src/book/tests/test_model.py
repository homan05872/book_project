from django.test import TestCase
from book.models import Book,Review,Profiel,User

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
        

# class Model_add_test(TestCase):
    
#     def SetUp(self):
#         self.user = User.objects.create(
#             username = 'test_user',
#             email = 'test@example.com',
#             password = 'secret',    
#         )
#         self.client.force_login(self.user)
        
#     def test_create_views(self):
#         """ユーザーがログイン状態でcreateにアクセス時のステータスコードテスト"""
#         def test_render_cretion_form(self):
#             response = self.client.get("create/")
#             self.assertContains(response, "text", status_code=200)

#     def test_saving_and_retrieving_post(self):
#         """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
#         super().setUp()
#         book = Book()
#         bookname = 'test_book'
#         title = 'test_title_to_retrieve'
#         text = 'test_text_to_retrieve'
#         category = 'bussines','ビジネス'
#         bookname = bookname
#         book.subtitle = title
#         book.text = text
#         book.category = category 
#         book.created_by = User.objects.get(id=self.user.id)
#         book.save()
        
#         saved_posts = Book.objects.all()
#         actual_post = saved_posts[0]

#         self.assertEqual(actual_post.subtitle, title)
#         self.assertEqual(actual_post.text, text)
    # def test_saving_and_retrieving_post(self):
    #     """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
    #     book = Book()
    #     bookname = 'test_bookname'
    #     title = 'test_title_to_retrieve'
    #     text = 'test_text_to_retrieve'
    #     category = {'bussines': 'ビジネス'}
    #     book.bookname = bookname
    #     book.subtitle = title
    #     book.text = text
    #     book.category = category
    #     book.created_by = self.user
    #     book.save()

    #     saved_book = Book.objects.all()
    #     actual_book = saved_book[0]

    #     self.assertEqual(actual_book.bookname, bookname)
    #     self.assertEqual(actual_book.subtitle, title)
    #     self.assertEqual(actual_book.text, text)
    #     self.assertEqual(actual_book.category, category)
    #     self.assertEqual(actual_book.created_by, self.user)