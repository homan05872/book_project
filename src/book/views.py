from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from .models import Book

class IndexBook(TemplateView):
    template_name = 'book/index.html'

class ListBook(ListView):
    modle = Book
    queryset = Book.objects.all().select_related()
    
    
    
    # def get_queryset(self):
    #     query = self.request.GET.get('query')

    #     if query:
    #         Book_list = Book.objects.filter(
    #             name__icontains=query)
    #     else:
    #         Book_list = Book.objects.all()
    #     return Book_list
    
class DetailBook(DetailView):
    model = Book

class CreateBook(CreateView):
    model = Book
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('booklist')
    
class UpdateBook(UpdateView):
    model = Book    
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('booklist')
    
class DeleteBook(DeleteView):
    model = Book
    success_url = reverse_lazy('booklist')