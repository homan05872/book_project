from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User

from django.views.generic import CreateView

from .forms import SignupForm, Profielform

from django.urls import reverse_lazy 

from book.models import Profiel

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('profiel_new')
    

def profiel_new(request):
    if request.method == "POST":
        form = Profielform(request.POST)
        if form.is_valid:
            profiel = form.save(commit=False)
            profiel.outher = request.user
            profiel.save()
            return redirect('booklist')
    else:
        form = Profielform()
    return render(request,'profiel/profiel_new.html',{'form':form})


def profiel_detail(request,):
    # book = get_object_or_404(Profiel, pk=pk)
    return render(request, 'profiel/profiel_detail.html')

def profiel_edit(request):
    profiel = get_object_or_404(Profiel,)
    return render(request, 'profiel/profiel_edit.html')

