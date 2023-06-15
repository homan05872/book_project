from typing import Any, Dict, Optional
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View
from .models import Book, Review, Profiel
from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import BookForm, ReviewForm,BookNameSearch,SubtitleSearch
from django.contrib import messages
from django.db.models import Q


class OwnerOnly(UserPassesTestMixin):
  #アクセス制限
  def test_func(self):
    book_instance = self.get_object() #クラスベースビューにある関数で、使用してるモデルobjectを取得できる関数！
    return book_instance.created_by == self.request.user
  
  #↑上記関数がFalseだった時のリダイレクト先を指定
  def handle_no_permission(self):
    messages.error(self.request, "このBookレビューの編集・削除はできません。")
    return redirect("detail", pk=self.kwargs["pk"])


class IndexBook(TemplateView):
    template_name = 'book/index.html'
    
    

class ListBook(ListView):
    model = Book
    context_object_name = "book_list"
    paginate_by = 10
    
    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs).select_related('created_by__profiels').all().order_by('-timestamp') #←super().get_queryset(**kwargs)の部分はself.model.objectsでも代用可能！
        q = self.request.GET
        
        if book := q.get('book'):
            qs = self.model.objects.select_related('created_by__profiels').filter(Q(bookname__contains=book)|Q(subtitle__contains=book)).all().order_by('-timestamp')
            
        return qs
    
    #現在未使用
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['forms'] = CategorySearch(self.request.GET)
    #     return context
    


# def listBook(request):
#     books  = Book.objects.select_related('created_by__profiels').all().order_by('-timestamp')
#     bookSearchForm = BookNameSearch(request.GET)
#     subtitleSearchForm = SubtitleSearch(request.GET)
    
#     if bookSearchForm.is_valid():
#         bookname = bookSearchForm.cleaned_data.get("bookname")
        
#         if bookname:
#             books = Book.objects.select_related('created_by__profiels').filter(bookname__contains=bookname).all().order_by('-timestamp')
        
#     if subtitleSearchForm.is_valid():
#         subtitle = subtitleSearchForm.cleaned_data.get("subtitle")
#         if subtitle:
#             books = Book.objects.select_related('created_by__profiels').filter(subtitle__contains=subtitle).all().order_by('-timestamp')
            
#     return render(request, "book/book_list.html", {"books": books,"bookSearchForm":bookSearchForm,"subtitleSearchForm":subtitleSearchForm})


class DetailBook(LoginRequiredMixin,DetailView):
    model = Book
    context_object_name = "book"
    
    # 追加
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        # テンプレートにコメント作成フォームを渡す
        form = ReviewForm
        reviews = self.object.reviews.select_related('created_by__profiels').all().order_by("-timestamp")
        context.update({
            'reviews': reviews, 
            'form': form,
        })
        return context
    
        
class ReviewCreate(LoginRequiredMixin,CreateView):
    model = Review
    form_class = ReviewForm
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        book_pk = self.kwargs.get('pk')
        book = get_object_or_404(Book, pk=book_pk)
 
        comment = form.save(commit=False)
        comment.book = book
        comment.save()
 
        return redirect('detail', pk=book_pk)
        

# @login_required
# def detailBook(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     reviews = Review.objects.filter(book=book.id).select_related('created_by__profiels').all().order_by("-timestamp")
#     form = ReviewForm()
    
#     return render(request, 'book/book_detail.html', 
#                   {'book': book,"reviews":reviews,'form':form})

# #コメント投稿
# @login_required
# def new_review(request,pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.created_by = request.user
#             review.book = book
#             review.save()
#             messages.add_message(request, messages.SUCCESS,
#                                  "コメントを投稿しました。")
#         else:
#             messages.add_message(request, messages.ERROR,
#                                  "コメントを投稿しました。")
#     else:
#         form = ReviewForm()
    
#     return redirect('detail', pk=book.pk)

        
        
class CreateBook(LoginRequiredMixin ,CreateView):
    model = Book
    form_class = BookForm
    
    def form_valid(self, form):
        if form.is_valid:
            book = form.save(commit=False)
            book.created_by = self.request.user
            book.profiel_connect = Profiel.objects.get(pk = self.request.user.pk)
            book.save()
            messages.add_message(self.request, messages.SUCCESS,
                                 "Bookレビューが作成が完了しました。")
            return redirect('detail', pk=book.pk )
        else:
            messages.add_message(self.request, messages.ERROR,
                                 "Bookレビューの作成に失敗しました。")
            return redirect('create')
        
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "Bookアプリ｜Bookレビュー新規作成"
        ctx["title_h1"] = "紹介したい本のレビューを記載してください。"
        return ctx


# @login_required
# def createBook(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST,request.FILES)
        
#         if form.is_valid:
#             book = form.save(commit=False)
#             book.created_by = request.user
#             book.profiel_connect = Profiel.objects.get(pk = request.user.pk)
#             book.save()
#             messages.add_message(request, messages.SUCCESS,
#                                  "Bookレビューが作成が完了しました。")
#             return redirect('detail', pk=book.pk )
#         else:
#             messages.add_message(request, messages.ERROR,
#                                  "Bookレビューの作成に失敗しました。")
#     else:
#         form = BookForm()
            
#     return render(request,'book/book_form.html',{'form':form})



class UpdateBook(OwnerOnly, UpdateView):
    model = Book
    form_class = BookForm
    
    def get_success_url(self):
        messages.success(self.request, "Bookレビューの編集が完了しました。")
        return reverse('detail', kwargs={'pk': self.kwargs['pk']})
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "Bookアプリ｜Bookレビュー編集"
        ctx["title_h1"] = "編集画面"
        return ctx
    
    
    # def form_valid(self, form):
    #     if form.is_valid:
    #         book = form.save(commit=False)
    #         book.save()
    #         messages.add_message(self.request, messages.SUCCESS,
    #                                 "Bookレビューの編集が完了しました。")
    #         return redirect('detail', pk=book.pk)

    #     else:
    #         messages.add_message(self.request, messages.ERROR,
    #                              "Bookレビューの編集に失敗しました。")
    #         return redirect('update', pk=book.pk)



# @login_required
# def updateBook(request,pk):
#     book = get_object_or_404(Book,pk=pk)
    
#     if book.created_by.pk != request.user.pk:
#         return HttpResponseForbidden("このBookの編集は許可されていません。")
    
#     if request.method == 'POST':
#         form = BookForm(request.POST,request.FILES, instance=book)
#         if form.is_valid():
#             book.save()
#             messages.add_message(request, messages.SUCCESS,
#                                  "Bookレビューの編集が完了しました。")
#             return redirect('detail', pk=book.pk)
#         else:
#             messages.add_message(request, messages.ERROR,
#                                  "Bookレビューの編集に失敗しました。")
    
#     else:
#         form = BookForm(instance=book)    
#     return render(request,'book/book_update.html',{'form': form})
        

class DeleteBook(OwnerOnly, DeleteView):
    model = Book
    success_url = reverse_lazy('booklist')
    
    def get_success_url(self):
        messages.success(self.request, "Bookレビューの削除が完了しました。")
        return reverse_lazy('booklist')






