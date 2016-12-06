from django.db import models


from django import forms
# Create your models here.


class Test(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20, unique = True)
    run = models.CharField(max_length = 40)


class UploadScriptForm(forms.Form):
    script = forms.FileField()