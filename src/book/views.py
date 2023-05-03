from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Book
from django.contrib.auth import logout
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
    fields = "__all__"


class UpdateBook(UpdateView):
    model = Book
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('booklist')


class DeleteBook(DeleteView):
    model = Book
    success_url = reverse_lazy('booklist')


def logout_view(request):
    logout(request)
    return redirect('index')


# 未使用

class ListBook(ListView):
    modle = Book
    queryset = Book.objects.all().select_related()


class DetailBook(DetailView):
    model = Book
