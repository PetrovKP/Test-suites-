### Задание
С помощью Django создать веб-приложение, отображающее список *test suites* 
и умеющее запускать их, вызывая скрипт [(см. задание №5)](https://docs.google.com/document/d/19t4FpTjurzWBo3JUpCWCyrxyKgtHwtAVL-nV9qza7cM/edit) с разными .xml файлами. У каждого test suite должно быть ID, имя, строка запуска (вида “python run_tests.py list1.xml”). После запуска для test suite должен показываться pass rate (список запусков можно сделать отдельной страницей).

Также нужно реализовать форму ввода нового test suite.

### Инструменты

* Python  3.4
* Django  1.9
* PyMySQL 0.7
* 