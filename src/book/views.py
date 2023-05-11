from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Book, Review
from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import BookForm, ReviewForm
from django.contrib import messages
from django.contrib.auth.models import User





class IndexBook(TemplateView):
    template_name = 'book/index.html'


def listBook(request):
    # books = Book.objects.select_related('created_by__profiels').all()
    # form = SearchForm(request.GET)
    
    # if form.is_valid:
    #     keyword = form.cleaned_data.get('bookname')
    #     books = Book.objects.filter(bookname=keyword).select_related('created_by__profiels').all()
    
    # else:
    #Bookとプロフィールjoin
    books = Book.objects.select_related('created_by__profiels').all()
    
    return render(request, "book/book_list.html", {"books": books})


@login_required
def detailBook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = Review.objects.filter(book=book.id).select_related('created_by__profiels').all()
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
    else:
        messages.add_message(request,messages.ERROR,'コメント投稿に失敗しました。')
    
    return redirect('detail', pk=book.pk)
        
        
        

@login_required
def createBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        
        if form.is_valid:
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            return redirect('detail', pk=book.pk )
    else:
        form = BookForm()
            
    return render(request,'book/book_form.html',{'form':form})

@login_required
def updateBook(request,pk):
    book = get_object_or_404(Book,pk=pk)
    
    if book.created_by.pk != request.user.pk:
        return HttpResponseForbidden("このBookの編集は許可されていません。")
    
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES ,instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            return redirect('detail', pk=book.pk)
    
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

class CreateBook(CreateView):
    template_name = ('book/book_form.html')
    model = Book
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('booklist')