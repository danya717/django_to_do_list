from django.shortcuts import render
from core.constants import TODOS
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def main(request):
    todo_list = set()
    path = request.path
    path = path.replace('/', '')
    if path == '':
        path = 'main'
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while len(todo_list) < 4:
        todo_list.add(random.choice(TODOS))
    context = {'week_days' : week_days, 'todo_list' : todo_list}
    return render(request, f'{path}.html', context)

def creator(request):
    return render(request, 'creator.html')