from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def student(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=StudentForm(request.POST)

        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))

        else:
            return HttpResponse('Data is not Valid')
    return render(request,'student.html',d)