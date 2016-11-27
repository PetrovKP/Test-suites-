from django.shortcuts import render

from .models import Test


# Стартовая страница
def index(request):
    if request.method == 'POST':
        test = Test.objects.get(name = request.POST['name'])
        request.session['id'] = test.id
        return run(request)

    tests_name = [obj.name for obj in Test.objects.all()]
    return render(request, "index.html", {"list_test": tests_name})


# Запуск скрипты=а и вывод результов
def run(request):
    test = Test.objects.get(id=request.session['id'])

    return render(request, 'run.html', {"test": test.run})
