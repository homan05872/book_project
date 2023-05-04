from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import SignupView, profiel_new,profiel_edit, profiel_detail

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),    
    path('signup/', SignupView.as_view(), name='signup'),
    path('profiel/new/', profiel_new, name='profiel_new'),
    path('profiel/detail/', profiel_detail, name='profiel_detail'),
    path('profiel/edit/',profiel_edit,name='profiel_edit'),
]
