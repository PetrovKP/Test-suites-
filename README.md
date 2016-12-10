[![Build Status](https://travis-ci.org/PetrovKP/test-suites.svg?branch=master)] (https://travis-ci.org/PetrovKP/test-suites)[![codecov](https://codecov.io/gh/PetrovKP/test-suites/branch/master/graph/badge.svg)](https://codecov.io/gh/PetrovKP/test-suites)

### Задание
С помощью Django создать веб-приложение, отображающее список *test suites* 
и умеющее запускать их, вызывая скрипт [(см. задание №5)](https://docs.google.com/document/d/19t4FpTjurzWBo3JUpCWCyrxyKgtHwtAVL-nV9qza7cM/edit) с разными .xml файлами. У каждого test suite должно быть ID, имя, строка запуска (вида “python run_tests.py list1.xml”). После запуска для test suite должен показываться pass rate (список запусков можно сделать отдельной страницей).

Также нужно реализовать форму ввода нового test suite.

### По пунктам

1) Разработка шаблона **[DONE]**

2) Отображение *test suites* **[DONE]**

3) Запуск test suites посредством вызова скрипта 5 **[DONE]**

4) Форма для ввода нового test_suits **[DONE]**

5) Формирование и вёрстка stdout

### Инструменты

* Python  3.4
* Django  1.9
* [Bootstrap 3](https://github.com/dyve/django-bootstrap3)
