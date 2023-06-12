from typing import Any, Dict
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Book, Review, Profiel
from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import BookForm, ReviewForm,BookNameSearch,SubtitleSearch
from django.contrib import messages




class IndexBook(TemplateView):
    template_name = 'book/index.html'


def listBook(request):
    books  = Book.objects.select_related('created_by__profiels').all().order_by('-timestamp')
    bookSearchForm = BookNameSearch(request.GET)
    subtitleSearchForm = SubtitleSearch(request.GET)
    
    if bookSearchForm.is_valid():
        bookname = bookSearchForm.cleaned_data.get("bookname")
        
        if bookname:
            books = Book.objects.select_related('created_by__profiels').filter(bookname__contains=bookname).all().order_by('-timestamp')
        
    if subtitleSearchForm.is_valid():
        subtitle = subtitleSearchForm.cleaned_data.get("subtitle")
        if subtitle:
            books = Book.objects.select_related('created_by__profiels').filter(subtitle__contains=subtitle).all().order_by('-timestamp')
            
    return render(request, "book/book_list.html", {"books": books,"bookSearchForm":bookSearchForm,"subtitleSearchForm":subtitleSearchForm})


@login_required
def detailBook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = Review.objects.filter(book=book.id).select_related('created_by__profiels').all().order_by("-timestamp")
    form = ReviewForm()
    
    return render(request, 'book/book_detail.html', 
                  {'book': book,"reviews":reviews,'form':form})

@login_required
def new_review(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.created_by = request.user
            review.book = book
            review.save()
            messages.add_message(request, messages.SUCCESS,
                                 "コメントを投稿しました。")
        else:
            messages.add_message(request, messages.ERROR,
                                 "コメントを投稿しました。")
    else:
        form = ReviewForm()
    
    return redirect('detail', pk=book.pk)
        
        
        

@login_required
def createBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        
        if form.is_valid:
            book = form.save(commit=False)
            book.created_by = request.user
            book.profiel_connect = Profiel.objects.get(pk = request.user.pk)
            book.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Bookレビューが作成が完了しました。")
            return redirect('detail', pk=book.pk )
        else:
            messages.add_message(request, messages.ERROR,
                                 "Bookレビューの作成に失敗しました。")
    else:
        form = BookForm()
            
    return render(request,'book/book_form.html',{'form':form})


class CreateBook(CreateView):
    template_name = ('book/book_form.html')
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('booklist')

    def get_form_kwargs(self, *args, **kwargs):
        kwgs = super().get_form_kwargs(*args, **kwargs)
        kwgs["user"] = self.request.user
        return kwgs 
    
    
class CreateReview(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('book', 'text', 'rate')
    template_name = 'book/review_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def updateBook(request,pk):
    book = get_object_or_404(Book,pk=pk)
    
    if book.created_by.pk != request.user.pk:
        return HttpResponseForbidden("このBookの編集は許可されていません。")
    
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES, instance=book)
        if form.is_valid():
            book.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Bookレビューの編集が完了しました。")
            return redirect('detail', pk=book.pk)
        else:
            messages.add_message(request, messages.ERROR,
                                 "Bookレビューの編集に失敗しました。")
    
    else:
        form = BookForm(instance=book)    
    return render(request,'book/book_update.html',{'form': form})



class UpdateBook(UpdateView):
    model = Book
    fields = ('bookname', 'subtitle', 'text', 'thumbnail', 'category')
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        
        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj
    
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})


class DeleteBook(LoginRequiredMixin,DeleteView):
    model = Book
    success_url = reverse_lazy('booklist')



class CreateReview(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('book', 'text', 'rate')
    template_name = 'book/review_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# 未使用

class ListBook(ListView):
    modle = Book
    queryset = Book.objects.all().select_related()


class DetailBook(DetailView):
    model = Book

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.book.id})
