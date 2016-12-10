from django.shortcuts import render
from django.db import IntegrityError

from .models import Test

from subprocess import Popen, PIPE
from os import path, pardir


# Запуск указанного скрипта
def execute(command):
    process = Popen(
        command,
        stdout = PIPE,
        stderr = PIPE,
        shell = True,
        cwd = path.abspath(path.join(pardir, 'scripts'))
    )

    out, err = process.communicate()

    out = out.decode("utf-8")
    # print(err)
    return out


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

    test = Test.objects.get(id = request.session['id'])
    out = execute(test.run)
    return render(request, 'run.html', {"test": out})


# Добавления теста
def add_test(request):
    if request.method == 'POST':
        try:
            test = Test(name = request.POST['name'], run = request.POST['run'])
            test.save()
            return render(request, "add_test.html", {"isAdd": "ok"})
        except IntegrityError:
            return render(request, "add_test.html", {"isAdd": "error"})

    return render(request, "add_test.html")


# Удаление теста
def delete_test(request):
    tests_name = [obj.name for obj in Test.objects.all()]
    if request.method == 'POST':
        try:
            test = Test.objects.get(name = request.POST['name'])
            test.delete()
            tests_name.remove(test.name)
            return render(request, "delete_test.html", { "isAdd": 'ok', "list_test": tests_name })
        except:
            return render(request, "delete_test.html", { "isAdd": 'error', "list_test": tests_name })

    return render(request, "delete_test.html", { "list_test": tests_name })
