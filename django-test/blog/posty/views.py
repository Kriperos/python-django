from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def lista_postow(request):
    posty = Post.objects.all()
    title = "Nasz Blog"
    return render(request, 'posty/lista.html', {'posty': posty, 'tytul': title})

