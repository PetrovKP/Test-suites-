#! -*- coding: utf-8 -*-
#! /usr/bin/env python

import imp
import os
import os.path
import sys
import xml.etree.ElementTree as ET

_passed = 0  # Количество пройденных тестов
_failed = 0  # Количество тестов со сбоем

class Logger(object):
    "Служебный класс для одновременного вывода в stdout и файл."
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("Log.txt", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
#
# Принцип работы этого класса основан на тои, что python исполняет
# функцию write() для любого переданного ей в sys.stdout объекта при записи
sys.stdout = Logger()
sys.stderr = sys.stdout  # объединение потока ошибок и потока вывода
#

def get_module_name(filename):
    "Получает имя модуля из полного пути к нему."
    filename = os.path.basename(filename)
    filename = os.path.splitext(filename)[0]
    return filename
#

def run_tests(xmlfile):
    "Запуск всех тестов, описанных в переданном XML-файле."
    global _passed
    global _failed
    # получение корневого элемента
    root = ET.parse(xmlfile).getroot()
    # проход по всем <task>
    for task in root:
        task_name = ''
        task_args = {}
        # получение имени теста
        if 'name' in task.attrib:
            task_name = task.attrib['name']
        args = task[0]
        # получение пути к тесту
        test_path = ''
        for arg in args:
            name = arg.attrib['name']
            task_args[name] = arg.text
            if name == 'test_file_path':
                test_path = eval(arg.text.replace('?PACKAGE_PATH + "', '".'))
                # на unix-like системах разделитель отличается от данного в файле
                if os.path.sep == '/':
                    test_path = test_path.replace('\\', '/')
        # вывод
        print 'TEST:', task_name
        print '========== OUTPUT =========='
        # динамическая загрузка модуля
        mod = imp.load_source(get_module_name(test_path), test_path)
        # создание тестового объекта
        test_obj = mod.newTestObject(task_args.items())
        print '========== RESULT =========='
        res_code = 1
        # вызов Execute(). Вызов обёрнут в try-except для отлова исключений
        try:
            res_code = test_obj.Execute()
        except:
            pass
        if res_code == 0 or res_code == None:
            print 'PASS'
            _passed += 1
        else:
            print 'FAIL'
            _failed += 1
        print ''
#

def find_xmls():
    "Поиск всех xml-файлов в текущей папке по расширению."
    for entry in os.listdir('.'):
        if os.path.isfile(entry) and \
        os.path.splitext(entry)[1].lower() == '.xml':
            run_tests(entry)
#

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        run_tests(sys.argv[1])
    else:
        find_xmls()
    # общая статистика
    print '========= SUMMARY =========='
    print 'Passed:', _passed
    print 'Failed:', _failed
#
