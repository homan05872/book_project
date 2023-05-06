from django.urls import path
# from .views import ListBook, DetailBook,CreateBook,UpdateBook,DeleteBook,IndexBook

from . import views


urlpatterns = [
    path('', views.IndexBook.as_view(), name='index'),
    path('list/', views.listBook, name='booklist'),
    path('detail/<int:pk>/', views.detailBook, name='detail'),
    path('create/', views.CreateBook.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateBook.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteBook.as_view(), name='delete'),
    path('review/<int:book_id>', views.CreateReview.as_view(),name='review'),
]
