from django.shortcuts import render

def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return(request, 'galeria/imagem.html')