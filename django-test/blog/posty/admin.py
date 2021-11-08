from django.contrib import admin

# Register your models here.
from posty.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('autor_imie', 'autor_nazwisko', )
    search_fields = ['tresc']