# -*- coding: utf-8 -*-
import csv
import codecs

from django.shortcuts import render

from .models import CSVData

def main(request):
    template = 'importer.html'
    context = {}

    if request.method == 'POST':
        csv_entries = []
        header_defined = False

        csvfile = request.FILES['csv_file']
        csvfile = csv.reader(codecs.iterdecode(csvfile, 'utf-8'), delimiter=';')

        for row in csvfile:
            empty_or_invalid_row = all(x==row[0] for x in row)

            if not empty_or_invalid_row and not header_defined:
                header = row
                header_defined = True
            elif header_defined:
                csv_entry = CSVData(
                    formulario = row[0],
                    idade = row[1],
                    sexo = row[2],
                    periodo = row[3],
                    q01 = row[4],
                    q02 = row[5],
                    q03 = row[6],
                    q04 = row[7],
                    q05 = row[8],
                    q06 = row[9],
                    q07 = row[10],
                    q08 = row[11],
                    q09 = row[12],
                    q10 = row[13],
                    q11 = row[14],
                    q12 = row[15],
                    q13 = row[16],
                    q14 = row[17],
                    q15 = row[18],
                    q16 = row[19],
                    q17 = row[20],
                    q18 = row[21],
                    q19 = row[22],
                    q20 = row[23],
                    q21 = row[24],
                    q22 = row[25],
                    q23 = row[26],
                    q24 = row[27],
                    q25 = row[28],
                    total = row[29],
                    cansaco_emocional = row[30],
                    class_i = row[31],
                    despersonalizacao = row[32],
                    class_ii = row[33],
                    realizacao_pessoal = row[34],
                    class_iii = row[35],
                    q3a25 = row[36],
                    valores = row[37],
                    q1e2 = row[38],
                    valores2 = row[39],
                    cansaco_emocional2 = row[40],
                    valores3 = row[41],
                    despersonalizacao2 = row[42],
                    valores4 = row[43],
                    realizacao_pessoal2 = row[44],
                    valores5 = row[45],

                )
                csv_entries.append(csv_entry)

        CSVData.objects.bulk_create(csv_entries)

        context.update({
            'imported': len(csv_entries),
            'header': header,
        })

    return render(request, template, context)