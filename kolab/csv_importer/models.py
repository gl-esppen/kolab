# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CSVData(models.Model):
    formulario = models.CharField(max_length=250, null=True, blank=True)

    idade = models.CharField(max_length=250, null=True, blank=True)
    sexo = models.CharField(max_length=250, null=True, blank=True)
    periodo = models.CharField(max_length=250, null=True, blank=True)

    q01 = models.CharField(max_length=5, null=True, blank=True)
    q02 = models.CharField(max_length=5, null=True, blank=True)
    q03 = models.CharField(max_length=5, null=True, blank=True)
    q04 = models.CharField(max_length=5, null=True, blank=True)
    q05 = models.CharField(max_length=5, null=True, blank=True)
    q06 = models.CharField(max_length=5, null=True, blank=True)
    q07 = models.CharField(max_length=5, null=True, blank=True)
    q08 = models.CharField(max_length=5, null=True, blank=True)
    q09 = models.CharField(max_length=5, null=True, blank=True)
    q10 = models.CharField(max_length=5, null=True, blank=True)
    q11 = models.CharField(max_length=5, null=True, blank=True)
    q12 = models.CharField(max_length=5, null=True, blank=True)
    q13 = models.CharField(max_length=5, null=True, blank=True)
    q14 = models.CharField(max_length=5, null=True, blank=True)
    q15 = models.CharField(max_length=5, null=True, blank=True)
    q16 = models.CharField(max_length=5, null=True, blank=True)
    q17 = models.CharField(max_length=5, null=True, blank=True)
    q18 = models.CharField(max_length=5, null=True, blank=True)
    q19 = models.CharField(max_length=5, null=True, blank=True)
    q20 = models.CharField(max_length=5, null=True, blank=True)
    q21 = models.CharField(max_length=5, null=True, blank=True)
    q22 = models.CharField(max_length=5, null=True, blank=True)
    q23 = models.CharField(max_length=5, null=True, blank=True)
    q24 = models.CharField(max_length=5, null=True, blank=True)
    q25 = models.CharField(max_length=5, null=True, blank=True)
    total = models.CharField(max_length=250, null=True, blank=True)

    cansaco_emocional = models.CharField(max_length=250, null=True, blank=True)

    class_i = models.CharField(max_length=250, null=True, blank=True)

    despersonalizacao = models.CharField(max_length=250, null=True, blank=True)

    class_ii = models.CharField(max_length=250, null=True, blank=True)

    realizacao_pessoal = models.CharField(max_length=250, null=True, blank=True)

    class_iii = models.CharField(max_length=250, null=True, blank=True)

    q3a25 = models.CharField(
        max_length=250, null=True, blank=True,
        verbose_name='Questões (3 a 25)'
    )

    valores = models.CharField(max_length=250, null=True, blank=True)

    q1e2 = models.CharField(
        max_length=250,null=True, blank=True,
        verbose_name='Questões (1 e 2)'
    )

    valores2 = models.CharField(max_length=250, null=True, blank=True)

    cansaco_emocional2 = models.CharField(max_length=250, null=True, blank=True)
    valores3 = models.CharField(max_length=250, null=True, blank=True)

    despersonalizacao2 = models.CharField(max_length=250, null=True, blank=True)
    valores4 = models.CharField(max_length=250, null=True, blank=True)

    realizacao_pessoal2 = models.CharField(max_length=250, null=True, blank=True)
    valores5 = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'Imported CSV Data'
        verbose_name_plural = 'Imported CSVs Data'

    def __str__(self):
        return self.formulario
