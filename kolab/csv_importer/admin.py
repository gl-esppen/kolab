# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from csv_importer.models import CSVData


class CSVDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'idade','sexo','periodo','total',]
    list_filter = ['idade','sexo','periodo','total',]

admin.site.register(CSVData, CSVDataAdmin)
