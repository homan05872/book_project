from django.db import models
from .consts import MAX_RATE
from django.contrib.auth.models import User
from django.db.models.signals import post_save


RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]


CATEGORY = (('ビジネス','ビジネス'),('生活','生活'),('小説','小説'),('マンガ','マンガ'),('その他','その他'),)

class Profiel(models.Model):
    outher = models.OneToOneField(User,related_name='profiels',verbose_name='ユーザー', on_delete=models.CASCADE)
    nickname = models.CharField('ニックネーム',max_length=100)
    text = models.TextField('自己紹介')
    sex = models.CharField('性別',choices=(('男性','男性'),('女性','女性')),
                           max_length=50)
    
    class Meta:
         db_table = 'profiels'


class Book(models.Model):
    bookname = models.CharField('書籍名',max_length=100)
    subtitle = models.CharField('タイトル',max_length=100)
    text = models.TextField('本文',blank=False)
    category = models.CharField(
        'ジャンル',
        max_length=100,
        choices=CATEGORY
    )
    timestamp = models.DateTimeField('投稿日',auto_now_add=True)
    thumbnail = models.ImageField('Bookカバー',blank=True,null=True)
    created_by = models.ForeignKey(User,related_name='bookuser',verbose_name='投稿者', on_delete=models.CASCADE)
    profiel_connect = models.ForeignKey(Profiel,related_name='profiel_connect',default=1,on_delete=models.CASCADE)
    
    def __str__(self):
         return self.bookname
     
    class Meta:
         db_table = 'books'


class Review(models.Model):
    book = models.ForeignKey(Book,related_name='reviews',verbose_name='本', on_delete=models.CASCADE)
    text = models.TextField('本文')
    rate = models.IntegerField('評価',choices=RATE_CHOICES)
    timestamp = models.DateTimeField('投稿日',auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='reviewuser', verbose_name='投稿者', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(f'{self.pk} {self.book.bookname}へのコメント')
    
    class Meta:
         db_table = 'reviews'





#OneToOneでUserモデルと紐づけるため
#この関数はユーザーモデルが作成された際に、Profielモデルが自動生成されるようになっている。
def post_user_created(sender, instance, created, **kwargs):
    if created:
        profile_obj = Profiel(outher=instance) #instance = 作成されたUserモデルクラスのオブジェクトの事
        profile_obj.nickname = instance.username
        profile_obj.save()

post_save.connect(post_user_created, sender=User)

