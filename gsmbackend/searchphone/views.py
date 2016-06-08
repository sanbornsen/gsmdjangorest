from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import searchByRank
# Create your views here

@api_view(['GET'])
def index(request):
    requiredParams = ['wc', 'wb', 'wr', 'ws']
    params = dict()
    for i in requiredParams:
        if i in request.query_params:
            params[i] = float(request.query_params[i][0])
        else:
            params[i] = 0
    data = searchByRank(params, 10)
    return Response(data)
