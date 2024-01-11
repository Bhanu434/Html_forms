from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def htmlforms(request):
    if request.method=="POST":
        un=request.POST['un']
        pw=request.POST['pw']
        F=Form.objects.get_or_create(username=un,password=pw)[0]
        F.save()
        return HttpResponse('Date Submitted')
    return render(request,'htmlforms.html')
