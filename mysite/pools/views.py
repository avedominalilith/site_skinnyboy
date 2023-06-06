from django.shortcuts import render

def index(request):
    return render(request, "pools/index.html",{})
