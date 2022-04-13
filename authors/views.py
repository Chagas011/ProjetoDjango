from django.shortcuts import render

from .forms import RegisterForm

# Create your views here.


def register_view(request):
    form = RegisterForm(request.POST)
    return render(request, 'authors/pages/register_view.html', context={
        'form': form,
    })