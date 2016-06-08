from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from operator import itemgetter
from .models import searchByRank
# Create your views here

@api_view(['GET'])
def index(request):
    requiredParams = ['wc', 'wb', 'wr', 'ws', 'price']
    params = dict()
    for i in requiredParams:
        if i in request.query_params:
            params[i] = str(request.query_params[i])
        else:
            params[i] = 0
    data = searchByRank(params)
    newData = list()
    for i in range(len(data)):
        rank = calculateRank(params, data[i])
        if rank >= 0:
            data[i]['rank'] = rank
            newData.append(data[i])

    # Sorting the data based on rank
    newData = sorted(newData, key=itemgetter('rank'), reverse=True)
    return Response(newData[0:10])

def calculateRank(params, data):
    # Out of price bound or no price from the crawled data
    if data['price'] == 0 or data['price'] > float(params['price']):
        return -1
    return ((float(params['wc'])*data['camera']/8.0) +
        (float(params['wb'])*data['battery']/2100.0) +
        (float(params['wr'])*data['ram']/2.0) +
        (float(params['ws'])*data['memory']/8.0))
