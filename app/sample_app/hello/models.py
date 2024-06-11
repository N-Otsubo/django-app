from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    class Meta:
        db_table = "custom_users"

    gender = models.CharField(verbose_name="性別", max_length=1, default=2) # 0=男　1=女 2=不明
    age = models.IntegerField(verbose_name="年齢", null=True, blank=True)
    birth_date = models.DateField(verbose_name="生年月日", null=True, blank=True)
    address = models.TextField(verbose_name="住所", null=True, blank=True)


class Publisher(models.Model):
    # 出版社モデル
    class Meta:
        db_table = "publishers"

    name = models.CharField(verbose_name="出版社", max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    # 著者モデル
    class Meta:
        db_table = "authors" # 作成されるテーブルの名前

    # テーブルのフィールド設定
    name = models.CharField(verbose_name='著者名', max_length=255)

    # おまじない
    def __str__(self):
        return self.name


class Book(models.Model):
    # Bookモデル
    class Meta:
        db_table = "books"

    title = models.CharField(verbose_name='タイトル', max_length=255)
    publisher = models.ForeignKey(Publisher, verbose_name='出版社', on_delete=models.PROTECT)
    author = models.ManyToManyField(Author, verbose_name='著者')
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    description = models.TextField(verbose_name='詳細', null=True, blank=True)
    publish_date = models.DateField(verbose_name='発売日')

    def __str__(self):
        return self.title
