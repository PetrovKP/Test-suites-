from django.shortcuts import render
from django.db import IntegrityError

from .models import Test


# Стартовая страница
def index(request):
    if request.method == 'POST':
        test = Test.objects.get(name = request.POST['name'])
        request.session['id'] = test.id
        return run(request)

    tests_name = [obj.name for obj in Test.objects.all()]
    return render(request, "index.html", {"list_test": tests_name})


# Запуск скрипта и вывод результов
def run(request):
    test = Test.objects.get(id=request.session['id'])

    return render(request, 'run.html', {"test": test.run})


# Добавления теста
def add(request):
    if request.method == 'POST':
        try:
            test = Test(name = request.POST['name'], run = request.POST['run'])
            test.save()
            return render(request, "add.html", {"isAdd": "ok"})
        except IntegrityError:
            return render(request, "add.html", {"isAdd": "error"})

    return render(request, "add.html")


# Удаление теста
def delete(request):
    tests_name = [obj.name for obj in Test.objects.all()]
    if request.method == 'POST':
        try:
            test = Test.objects.get(name = request.POST['name'])
            test.delete()
            tests_name.remove(test.name)
            return render(request, "delete.html", {"isAdd": 'ok', "list_test": tests_name})
        except:
            return render(request, "delete.html", {"isAdd": 'error', "list_test": tests_name})

    return render(request, "delete.html", {"list_test": tests_name})
