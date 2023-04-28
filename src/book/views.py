from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from .models import Book, Review
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

class CreateReview(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('book', 'title', 'text', 'rate')
    template_name = 'book/review_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.book.id})