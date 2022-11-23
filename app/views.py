from django.shortcuts import render

# Create your views here.
def sony(request):
    d={'name':'Teja'}
    return render (request,'sony.html',d)
