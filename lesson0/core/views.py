from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def monday(request):
    todo_list = ['купить слона', 'покормить слона', 'Подружить слона с жирафом', 'Поиграть в кс', 'Проверить сайт']
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

def thursday(request):
    todo_list = ['купить попугая', 'покормить попугая', 'подружить попугая с котом']
    random.shuffle(todo_list)
    context = {'todo_list' : todo_list}
    return render(request, 'thursday.html', context=context)

def friday(request):
    todo_list = ['купить сову', 'покормить сову', 'подружить сову с китом', 'покормить кита']
    random.shuffle(todo_list)
    context = {'todo_list' : todo_list}
    return render(request, 'friday.html', context=context)

def saturday(request):
    todo_list = ['купить бумеранг', 'покидать бумеранг', 'сходиить в магазин', 'купить корм для совы']
    random.shuffle(todo_list)
    context = {'todo_list' : todo_list}
    return render(request, 'saturday.html', context=context)

def sunday(request):
    todo_list = ['купить кубик рубик', 'собрать кубик', 'сходить в зал', 'продать дом']
    random.shuffle(todo_list)
    context = {'todo_list' : todo_list}
    return render(request, 'sunday.html', context=context)

def creator(request):
    return render(request, 'creator.html')