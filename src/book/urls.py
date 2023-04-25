from django.urls import path
from .views import ListBook, DetailBook,CreateBook,UpdateBook,DeleteBook

urlpatterns = [
    path('list/',ListBook.as_view(), name='booklist'), 
    path('detail/<int:pk>/', DetailBook.as_view(), name='detail'),
    path('create/', CreateBook.as_view(),name='create'),
    path('update/<int:pk>/', UpdateBook.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteBook.as_view(), name='delete')
]
 