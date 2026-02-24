from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def monday(request):
    todo_list = ['купить слона', 'покормить слона', 'Подружить слона с жирафом', 'Поиграть в кс']
    random.shuffle(todo_list)
    context = {'todo_list' : todo_list}
    return render(request, 'monday.html', context=context)

def tuesday(request):
    todo_list = ['Позаниматся АйТи', 'Покасить траву', 'Сходить в зал', 'Погулять с котом']
    random.shuffle(todo_list)
    context = {'todo_list' : todo_list}
    return render(request, 'tuesday.html', context=context)

def wednesday(request):
    todo_list = ['Слетать в Америку', 'Купить собаку', 'Покрасить дом', 'Помыть посуду']
    random.shuffle(todo_list)
    context = {'todo_list' : todo_list}
    return render(request, 'wednesday.html', context=context)