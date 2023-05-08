from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import SignupView, profiel_edit, profiel_detail

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),    
    path('signup/', SignupView.as_view(), name='signup'),
    path('profiel/<int:pk>/', profiel_edit, name='profiel_edit'),
    path('profiel/<int:pk>/detail/', profiel_detail, name='profiel_detail'),
]
