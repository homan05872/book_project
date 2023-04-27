from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from .models import Book
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin



class IndexBook(TemplateView):
    template_name = 'book/index.html'


class ListBook(ListView):
    modle = Book
    queryset = Book.objects.all().select_related()
    
    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            Book_list = Book.objects.filter(
                name__icontains=query)
        else:
            Book_list = Book.objects.all()
        return Book_list

class DetailBook(LoginRequiredMixin, DetailView):
    model = Book


class CreateBook(LoginRequiredMixin, CreateView):
    model = Book
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('booklist')


class UpdateBook(LoginRequiredMixin, UpdateView):
    model = Book    
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('booklist')


class DeleteBook(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('booklist')


def logout_view(request):
    logout(request)
    return redirect('index')