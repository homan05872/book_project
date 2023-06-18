from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
User = get_user_model()

class UserAdmin(BaseUserAdmin):
    list_display = (
        "email",
        "active",
        "staff",
        "admin",
    )
    list_filter = (
        "admin",
        "active",
    )
    ordering = ("email",)
    filter_horizontal = ()
    #１.ここまでだけだと検索がエラーになる
    
    #1. 検索対象指定
    search_fields = ('email',)
    
    #2. User追加ページはエラーになる（ユーザーAdminにユーザーモデルがないため）
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nickname','password1', 'password2')}
        ),
    )
    
    #3．編集ページがエラーになる(下記を追加する)
    fieldsets = (
        (None, {'fields': ('email', 'nickname', 'password')}),
        ('Permissions', {'fields': ('staff','admin',)}),
    )

admin.site.register(User, UserAdmin)