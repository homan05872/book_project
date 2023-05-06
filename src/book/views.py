
from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Book, Review
from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied
# from django.contrib.auth.mixins import LoginRequiredMixin





class IndexBook(TemplateView):
    template_name = 'book/index.html'


def listBook(request):
    books = Book.objects.all()

    return render(request, "book/book_list.html", {"books": books})



def detailBook(request, pk):
    object = get_object_or_404(Book, pk=pk)

    return render(request, 'book/book_detail.html', {'object': object})


class CreateBook(CreateView):
    template_name = ('book/book_form.html')
    model = Book
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('booklist')
  

class UpdateBook(UpdateView):
    model = Book
    fields = ('title', 'text', 'category')
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj
    
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})


class DeleteBook(DeleteView):
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


def logout_view(request):
    logout(request)
    return redirect('index')


# 未使用

class ListBook(ListView):
    modle = Book
    queryset = Book.objects.all().select_related()


class DetailBook(DetailView):
    model = Book

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.book.id})
