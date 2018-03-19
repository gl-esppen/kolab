from django.forms import ModelForm

from . import models

class CSVImporterForm(ModelForm):

    class Meta:
        model = models.CSVData
        fields = ['raw_file']