from django.http import HttpResponseForbidden
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User

from django.views.generic import CreateView

from .forms import SignupForm, ProfielUpdateForm

from django.urls import reverse_lazy 

from book.models import Profiel,Book

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')
    

def profiel_edit(request,pk):
    profiel = get_object_or_404(Profiel, pk=pk)
    
    if profiel.pk != request.user.profiels.pk:
        return HttpResponseForbidden("このBookの編集は許可されていません。")
    
    if request.method == "POST":
        form = ProfielUpdateForm(request.POST, request.FILES, instance=profiel)
        if form.is_valid:
            profiel = form.save(commit=False)
            profiel.outher = request.user
            profiel.save()
            return redirect('accounts:profiel_detail', pk=request.user.pk)
    else:
        form = ProfielUpdateForm(instance=profiel)
    return render(request,'profiel/profiel_edit.html',{'form':form})


def profiel_detail(request,pk):
    profiel = get_object_or_404(Profiel,pk=pk)
    profiel_connect = Profiel.objects.filter(pk=pk).prefetch_related('profiel_connect')
    mybooks = profiel_connect[0].profiel_connect.all()
    
    return render(request, 'profiel/profiel_detail.html',{'profiel':profiel,'mybooks':mybooks})


