from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models.fields import DateField

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import SgOneToOne, ClientOneToOne
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
        paginator = Paginator(client, 50)
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
        paginator = Paginator(sg, 50)
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
