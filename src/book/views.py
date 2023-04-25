from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Book

class ListBook(ListView):
    template_name = 'book/book_list.html'
    modle = Book
    queryset = Book.objects.all().select_related()
    
class DetailBook(DetailView):
    template_name = 'book/book_detail.html'
    model = Book

class CreateBook(CreateView):
    template_name = 'book/book_create.html'
    model = Book
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('booklist')
    
class UpdateBook(UpdateView):
    template_name = 'book/book_update.html'
    model = Book    
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('booklist')
    
class DeleteBook(DeleteView):
    template_name = 'book/book_delete.html'
    model = Book
    success_url = reverse_lazy('booklist')