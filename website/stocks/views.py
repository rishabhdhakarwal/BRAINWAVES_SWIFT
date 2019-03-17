from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models.fields import DateField

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import SgOneToOne, ClientOneToOne, matched
from .serializers import *
from datetime import datetime
from django.db.models import Q
from django.db.models import Max



@api_view(['GET'])
def client(request):
    
    

    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        client = ClientOneToOne.objects.all()

        page = request.GET.get('page', 1)
        paginator = Paginator(client, 500)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = ClientSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/top_50/?page=' + str(nextPage), 'prevlink': '/api/userss/?page=' + str(previousPage)})


@api_view(['GET'])
def sg(request):
    
    

     if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        sg = SgOneToOne.objects.all()

        page = request.GET.get('page', 1)
        paginator = Paginator(sg, 500)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = SgSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/top_50/?page=' + str(nextPage), 'prevlink': '/api/userss/?page=' + str(previousPage)})


@api_view(['GET'])
def status(request):
    
    

    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1

        status = matched.objects.all()

        page = request.GET.get('page', 1)
        paginator = Paginator(status, 500)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = statusSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/top_50/?page=' + str(nextPage), 'prevlink': '/api/userss/?page=' + str(previousPage)})

@api_view(['GET'])
def stock_history(request):
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        symbol = request.GET.get('query', '')
        stock_history = ClientOneToOne.objects.filter(field_20 = symbol);
      
        page = request.GET.get('page', 1)
        paginator = Paginator(stock_history, 500)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = ClientSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/history/?page=' + str(nextPage), 'prevlink': '/api/users/?page=' + str(previousPage)})

@api_view(['GET'])
def make_matching(request):
    if request.method == "GET":
        object_1 = SgOneToOne.objects.all()
        object_2 = ClientOneToOne.objects.all()
        

        for x in range(len(object_1)):
            obj1 = object_1[x]
            obj2 = object_2[x]
            
            if (obj1.field_32b==obj2.field_33b) and (obj1.field_33b==obj2.field_32b) and (obj1.field_82a==obj2.field_87a) and (obj1.field_87a==obj2.field_82a) and (obj1.field_77h==obj2.field_77h) and (obj1.field_30t==obj2.field_30t) and (obj1.field_30v==obj2.field_30v) and (obj1.field_36==obj2.field_36) :
                matched.objects.create(client=object_2[x], sg=object_1[x], status="Yes")
            else:
                matched.objects.create(client=object_2[x], sg=object_1[x], status="No")
    return Response({})