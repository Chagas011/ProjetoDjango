from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/index.html', context={ 
        'name': 'washington'
    })


def sobre(request):
    return HttpResponse('SOBRE')


def contato(request):
    return HttpResponse('CONTATO')
