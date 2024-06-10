from django.contrib import admin
from .models import CustomUser, Publisher, Author, Book


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
