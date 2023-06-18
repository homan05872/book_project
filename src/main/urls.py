import debug_toolbar 
from django.conf import settings 
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), #これ追加
    path('app_accounts/', include('accounts.urls')),
    path('',include('book.urls')),
    path('__ debug __ /', include(debug_toolbar.urls))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)