from django.urls import path
from .views import ListBook, DetailBook,CreateBook,UpdateBook,DeleteBook,IndexBook

urlpatterns = [
    path('', IndexBook.as_view(), name='index'),
    path('list/',ListBook.as_view(), name='booklist'), 
    path('detail/<int:pk>/', DetailBook.as_view(), name='detail'),
    path('create/', CreateBook.as_view(),name='create'),
    path('update/<int:pk>/', UpdateBook.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteBook.as_view(), name='delete')
]
 