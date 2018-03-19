# -*- coding: utf-8 -*-
import csv

from django.shortcuts import render

from . import forms


def main(request):
    # Handling the form
    form = forms.CSVImporterForm()

    if request.method == 'POST':
        form = forms.CSVImporterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    # Other stuff
    template = 'importer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)