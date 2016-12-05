from django.shortcuts import render
from django.db import IntegrityError

from .models import Test, UploadScriptForm

from os import path


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
def add_test(request):
    if request.method == 'POST':
        try:
            test = Test(name = request.POST['name'], run = request.POST['run'])
            test.save()
            return render(request, "add_test.html", {"isAdd": "ok"})
        except IntegrityError:
            return render(request, "add_test.html", {"isAdd": "error"})

    return render(request, "add_test.html")


# Добавления скрипта
def add_script(request):
    if request.method == 'POST':
        form = UploadScriptForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['script'], request.POST['title'])
            return render(request, "add_script.html", {'form': form})
    else:
        form = UploadScriptForm()
    return render(request, "add_script.html", {'form': form})


# Сохранение скрипта
def handle_uploaded_file(file, name):
    with open(path.join('..', 'scripts',  name +'.py'), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


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
