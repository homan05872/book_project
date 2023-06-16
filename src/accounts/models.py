from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

#User登録のために用意されているメソッドの上書き！※このクラスではobjects.○○のようなメソッドを自作することもできる！
class UserManager(BaseUserManager):
		#user登録のためのメソッド（User登録に必要な情報を引数に渡す「email」「password」）
    def create_user(self, email, nickname,password=None):
        if not email:
            raise ValueError('Eメールアドレスを登録してください。')
        
        user = self.model(
            email=self.normalize_email(email),
        )
        user.nickname = nickname
        user.set_password(password)
        user.save(using=self._db)   #これは現在のアプリ内で使用しているDBへ登録するように指定している
        return user

		#スタッフ権限のユーザー登録メソッドの書き換え(基本的には上記と同じだがスタッフ権限をTrueにしている)
    def create_staffuser(self, email, nickname,password):
        user = self.create_user(
            email,
            nickname,
            password=password,
        )
        user.staff = True  #←ココ
        user.save(using=self._db)
        return user

		#admin権限のユーザー登録の書き換え(上記に加えadmin属性をTrueにしている)
    def create_superuser(self, email, nickname, password,):
        user = self.create_user(
            email,
            nickname=nickname,
            password=password,
        )
        user.staff = True
        user.admin = True  #ココ
        user.save(using=self._db)
        return user

#カスタムユーザモデルの作成
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Eメール', max_length=255, unique=True,)
    nickname = models.CharField(verbose_name='ニックネーム', max_length=255, blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) 
    admin = models.BooleanField(default=False) 
   
		#USERNAME_FIELDを書き換えることでログインに必要なユーザー名をeメールに変更している。
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["nickname"]

    objects = UserManager()   #←上記で作成したUserManagerのインスタンスを作成し、上書きしたメソッドを使用できるようにしている

    def __str__(self):             
        return self.email
		
		#以下のメソッドはAdminやstaffのパーミッションを判定するためにTrue/Falseを返すようなメソッドを定義している
    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin
		
		#↓propertyを使用して属性を使えるようにしている？
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

