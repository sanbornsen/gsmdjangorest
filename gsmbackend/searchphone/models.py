from __future__ import unicode_literals

from django.db import models

import pickle
# Create your models here.

def searchByRank(params, number=10):
    f = open('data/data.pkl', 'rb')
    data = pickle.load(f)
    f.close()
    return data