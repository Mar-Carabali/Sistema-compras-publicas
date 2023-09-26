from django.contrib import admin
from django.urls import path
from .models import *
from django import forms
from import_export.admin import ImportExportModelAdmin


@admin.register(Csv)
@admin.register(Premios)
@admin.register(Contratos)
@admin.register(Planificacion)
@admin.register(Lanzamiento)
@admin.register(Provedores)
@admin.register(Licitacion)


class ViewAdmin(ImportExportModelAdmin):
	pass


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


    
    


# Register your models here.
