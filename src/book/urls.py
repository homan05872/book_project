from django.urls import path
# from .views import ListBook, DetailBook,CreateBook,UpdateBook,DeleteBook,IndexBook

from . import views


urlpatterns = [
    path('', views.IndexBook.as_view(), name='index'),
    path('list/', views.ListBook.as_view(), name='booklist'),
    path('listtable/', views.ListTableBook.as_view(), name='booktable'),
    path('detail/<int:pk>/', views.DetailBook.as_view(), name='detail'),
    path('create/', views.CreateBook.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateBook.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteBook.as_view(), name='delete'),
    path('comment/<int:pk>', views.ReviewCreate.as_view(), name='new_comment'),
]
