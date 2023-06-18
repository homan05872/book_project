from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import SignupForm, ProfielUpdateForm
from django.urls import reverse_lazy, reverse
from book.models import Profiel
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model

User = get_user_model()

class OwnerOnly(UserPassesTestMixin):
  #アクセス制限
  def test_func(self):
    profiel_instance = self.get_object() #クラスベースビューにある関数で、使用してるモデルobjectを取得できる関数！
    return profiel_instance.outher == self.request.user
  
  #↑上記関数がFalseだった時のリダイレクト先を指定
  def handle_no_permission(self):
    messages.error(self.request, "このプロフィールの編集はできません。")
    return redirect("accounts:profiel_detail", pk=self.kwargs["pk"])


class SignupView(SuccessMessageMixin,CreateView):
    model = User
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')
    success_message = 'アカウント登録が完了しました。'
    
    
class Profiel_edit(OwnerOnly,UpdateView):
    model = Profiel
    form_class = ProfielUpdateForm
    template_name = 'profiel/profiel_edit.html'
    
    def get_success_url(self):
        return reverse('accounts:profiel_detail', kwargs={'pk': self.kwargs['pk']})


# def profiel_edit(request,pk):
#     profiel = get_object_or_404(Profiel, pk=pk)
    
#     if profiel.pk != request.user.profiels.pk:
#         return HttpResponseForbidden("このBookの編集は許可されていません。")
    
#     if request.method == "POST":
#         form = ProfielUpdateForm(request.POST, request.FILES, instance=profiel)
#         if form.is_valid:
#             profiel = form.save(commit=False)
#             profiel.outher = request.user
#             profiel.save()
#             messages.add_message(request, messages.SUCCESS,
#                                  "プロフィールの編集が完了しました。")
#             return redirect('accounts:profiel_detail', pk=request.user.pk)
#         else:
#             messages.add_message(request, messages.ERROR,
#                                  "プロフィールの編集に失敗しました。")
#             return redirect('accounts:profiel_edit', pk=request.user.pk)
        
#     else:
#         form = ProfielUpdateForm(instance=profiel)
#     return render(request,'profiel/profiel_edit.html',{'form':form})

class DetailProfiel(LoginRequiredMixin ,DetailView):
    model = Profiel
    context_object_name = 'profiel'
    template_name = 'profiel/profiel_detail.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['mybooks'] = self.object.profiel_connect.select_related('profiel_connect__outher').all().order_by("-timestamp")
        return context
        


# def profiel_detail(request,pk):
#     profiel = get_object_or_404(Profiel,pk=pk)
#     profiel_connect = Profiel.objects.filter(pk=pk).prefetch_related('profiel_connect')
#     mybooks = profiel_connect[0].profiel_connect.all()
    
#     return render(request, 'profiel/profiel_detail.html',{'profiel':profiel,'mybooks':mybooks})


