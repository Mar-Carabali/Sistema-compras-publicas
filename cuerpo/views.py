from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
from django.http import HttpResponse, Http404
from django.db.models import Sum
from django.core.paginator import Paginator
from django.db.models import Count
import os
import pandas as pd
import json
from .forms import CsvModelForm
from .filters import ContratosFilter
from django.views.decorators.http import require_http_methods
from collections import Counter
import matplotlib.pyplot as plt
from io import BytesIO
import base64


import csv


@require_http_methods(['GET'])


def base(request):

  
    contrat = Contratos.objects.all()
    todo3 = Licitacion.objects.all()
    todo2 = Provedores.objects.all()
    total_provedor = todo2.count()
    total_contrato = contrat.count()
    entidades_unicas = todo3.values('procuringEntity_name').distinct()
    total_entidades_unicas = entidades_unicas.count()
    t_monto = contrat.aggregate(total=Sum('amount'))['total']
    proveedores_repetidos = todo2.values('name').annotate(count=Count('name')).filter(count__gt=1)
    num_prov = proveedores_repetidos.count()
    
   
    
    months = []

    for tender in contrat:
        start_date_str = tender.dateSigned
        if start_date_str:
            # Dividir la cadena de fecha y obtener el mes (posición 5 y 6)
            parts = start_date_str.split('-')
            if len(parts) >= 2:
                month = parts[1]
                months.append(month)

    # Mapear los números de mes a nombres de mes
    month_names = {
        '01': 'Enero',
        '02': 'Febrero',
        '03': 'Marzo',
        '04': 'Abril',
        '05': 'Mayo',
        '06': 'Junio',
        '07': 'Julio',
        '08': 'Agosto',
        '09': 'Septiembre',
        '10': 'Octubre',
        '11': 'Noviembre',
        '12': 'Diciembre',
    }

    # Contar la frecuencia de cada mes y asignar nombres de mes
    month_count = Counter(months)
    month_count_with_names = {month_names[key]: value for key, value in month_count.items()}

    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#c2f0f0', '#ff6666', '#c2f0b3', '#9999ff', '#ffb366']

    # Crear una gráfica de pastel con colores personalizados
    labels = month_count_with_names.keys()
    sizes = month_count_with_names.values()

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Guardar la gráfica de pastel en un archivo BytesIO
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()

    plt.close()



    
    base ={'total_contrato': total_contrato, 'total_entidades_unicas': total_entidades_unicas, 't_monto':t_monto
           ,'total_provedor':total_provedor,  'month_count': month_count_with_names,
           'image_base64': image_base64, 'num_prov': num_prov
        }
    

    return render(request, 'index.html', base)

#--------------------------------------


#--------------------------------------

def premio(request):
    todo = Premios.objects.all()
    total_pre = todo.count()
    t_monto = todo.aggregate(total=Sum('amount'))['total']
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(todo, 5)
        todo = paginator.page(page)
    except:
        raise Http404
    
    prem = {'todo': todo, 'entity':todo, 'paginator': paginator, 'total_pre':total_pre, 't_monto':t_monto}
                   
    return render(request, 'premio.html', prem)


def analisis(request):

    return render(request, 'index.html')

def contrato(request):
    contrat = Contratos.objects.all()
    total_contrato = contrat.count()
    t_estado = contrat.filter(status='terminated').count()
    t_monto = contrat.aggregate(total=Sum('amount'))['total']
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(contrat, 5)
        contrat = paginator.page(page)
    except:
        raise Http404
    
    tabla = {'contrat': contrat, 'total_contrato': total_contrato, 't_estado':t_estado, 't_monto':t_monto,
              'entity':contrat, 'paginator': paginator}

    return render(request, 'contrato.html', tabla)

def planificacion(request):
    todo5 = Planificacion.objects.all()
    total_pla = todo5.count()
    t_monto = todo5.aggregate(total=Sum('budget_amount'))['total']
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(todo5, 5)
        todo5 = paginator.page(page)
    except:
        raise Http404
    

    plan = {'todo5': todo5,'entity':todo5, 'paginator': paginator, 'total_pla':total_pla, 't_monto':t_monto}
    
    return render(request, 'planificacion.html', plan)


def lanzamiento(request):
    todo4 = Lanzamiento.objects.all()
    total_lan = todo4.count()
    entidades_unicas = todo4.values('buyer_name').distinct()
    total_entidades_unicas = entidades_unicas.count()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(todo4, 5)
        todo4 = paginator.page(page)
    except:
        raise Http404

    lan = {'todo4': todo4, 'entity':todo4, 'paginator': paginator, 'total_entidades_unicas': total_entidades_unicas
           , 'total_lan': total_lan}
    return render(request, 'lanzamiento.html', lan )

def licitacion(request):
    todo3 = Licitacion.objects.all()
    total_lic = todo3.count()
    t_monto = todo3.aggregate(total=Sum('value_amount'))['total']
    entidades_unicas = todo3.values('procuringEntity_name').distinct()
    total_entidades_unicas = entidades_unicas.count()
    t_estado1 = todo3.filter(status='active').count()
    t_estado2 = todo3.filter(status='complete').count()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(todo3, 5)
        todo3 = paginator.page(page)
    except:
        raise Http404
    
    lic = {'todo3': todo3, 'entity':todo3, 'paginator': paginator, 'total_lic':total_lic, 't_monto':t_monto, 
           'total_entidades_unicas': total_entidades_unicas, 't_estado1':t_estado1, 't_estado2':t_estado2}
    return render(request, 'licitacion.html', lic)

def provedores(request):
    todo2 = Provedores.objects.all()
    total_provedor = todo2.count()
    proveedores_repetidos = todo2.values('name').annotate(count=Count('name')).filter(count__gt=1)
    num_prov = proveedores_repetidos.count()
    
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(todo2, 5)
        todo2 = paginator.page(page)
    except:
        raise Http404
    
    prov = {'todo2': todo2, 'entity':todo2, 'paginator': paginator, 'total_provedor':total_provedor, 'num_prov':num_prov}
    
    return render(request, 'provedores.html', prov)