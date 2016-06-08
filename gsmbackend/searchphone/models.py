from __future__ import unicode_literals

from django.db import models

import pickle
from operator import itemgetter
# Create your models here.

def searchByRank(params, number=10):
    f = open('data/data.pkl', 'rb')
    data = pickle.load(f)
    f.close()
    print params
    for i in range(len(data)):
    	data[i]['rank'] = calculateRank(params, data[i])

    data = sorted(data, key=itemgetter('rank'), reverse=True)
    return data[0:10]


def calculateRank(params, data):
	return ((float(params['wc'])*data['camera']/8.0) +
		(float(params['wb'])*data['battery']/2100.0) +
		(float(params['wr'])*data['ram']/2.0) +
		(float(params['ws'])*data['memory']/8.0))