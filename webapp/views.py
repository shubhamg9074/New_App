from django.shortcuts import render
from django.http import HttpResponseRedirect
from webapp.forms import Modelform
from webapp.models import users

# Create your views here.

def Forms(requsest):
    forms=Modelform()
    if requsest.method=='POST':
        forms=Modelform(requsest.POST)
        if forms.is_valid():
            forms.save(commit=True)
        return HttpResponseRedirect('/users')
    else:
        return render(requsest,'myapp/index.html',{'forms':forms})

def thanks(request):
    data=users.objects.all()
    mydict={'elist':data}
    return render(request,'myapp/thanks.html',mydict)


def hello(request):
    return render(request,'myapp/thanks1.html')


def data_by_id(request, id):
    try:
        obj = users.objects.get(user_id=id)
        return render(request, 'myapp/dataid.html', {'obj': obj})
    except users.DoesNotExist:
        return render(request, 'myapp/dataid.html', {'obj': None})
