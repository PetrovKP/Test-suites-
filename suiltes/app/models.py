from django.db import models


from django import forms
# Create your models here.


class Test(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20, unique = True)
    run = models.CharField(max_length = 40)


class UploadScriptForm(forms.Form):
    title = forms.CharField(label='Название',max_length=50)
    script = forms.FileField(label='Скрипт')