from django.shortcuts import render
from django.db import IntegrityError

from .models import Test

from subprocess import Popen, PIPE
from os import path, pardir
import re


# Запуск указанного скрипта
def execute(command):
    process = Popen(
        command,
        stdout = PIPE,
        stderr = PIPE,
        shell = True,
        cwd = path.join(pardir, "scripts")
    )

    out, err = process.communicate()
    out = out.decode("utf-8")

    list_test = []
    conclusion = ''

    # Магический парсинг
    if out:
        out, conclusion = out.split("========= SUMMARY ==========")
        pattern = re.compile(r'\=+.*\=+|\n\n')
        temp = pattern.split(out)
        title = temp[0::3]
        log = temp[1::3]
        res = [st.replace("\n", "") for st in temp[2::3]]
        list_test = zip(title, log, res)

    return list_test, conclusion


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
    list_test, conclusion = execute(test.run)

    return render(request, "run.html", {"list_test": list_test, "conclusion": conclusion})


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
            return render(request, "delete_test.html", {"isAdd": 'ok', "list_test": tests_name})
        except:
            return render(request, "delete_test.html", {"isAdd": 'error', "list_test": tests_name})

    return render(request, "delete_test.html", {"list_test": tests_name})
