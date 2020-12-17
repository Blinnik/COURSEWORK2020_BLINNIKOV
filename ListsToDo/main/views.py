from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound


def index(request):
    lists = List.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'lists': lists})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неправильная форма заполнения'

    form = ListForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


# удаление данных из бд
def delete(request, id):
    try:
        lists = List.objects.get(id=id)
        lists.delete()
        return HttpResponseRedirect("/")
    except List.DoesNotExist:
        return HttpResponseNotFound("<h2>List is not found</h2>")