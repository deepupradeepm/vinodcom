from django.shortcuts import render
import pandas as pd
from .models import Medician
# Create your views here.
def show(request):
   # df=pd.read_csv( r"C:\Users\m pradeep\Documents\Book1.csv")
   # for x in df.values:
   #     a,b=x
   #     Medician(med=a,des=b).save()
   qs=Medician.objects.all()
   l = []
   if qs:

       for x in qs:
           if x.med not in l:
               l.append(x.med)
       print(l)
       return render(request,'index.html',{'msg':'details saved','data':l})


def search(request,data):
    qs=Medician.objects.filter(med=data)
    if qs:
       return render(request,'result.html',{'qs':qs})