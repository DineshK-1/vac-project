from django.shortcuts import render
from .models import FrontendModels
import requests

def Frontend(request, _Type, _Title):
    All_Objects = FrontendModels.objects.all
    HTML = FrontendModels.objects.filter(Type  = "HTML")
    CSS = FrontendModels.objects.filter(Type  = "CSS")
    JS = FrontendModels.objects.filter(Type  = "JS")

    Data = FrontendModels.objects.get(Type = _Type, Title = _Title)
    return render(request, "Frontend.html", {"ModelData_HTML": HTML,"ModelData_CSS": CSS,"ModelData_JS": JS, "PageData":Data})

def FrontendHome(request):
    HTML = FrontendModels.objects.filter(Type  = "HTML")
    CSS = FrontendModels.objects.filter(Type  = "CSS")
    JS = FrontendModels.objects.filter(Type  = "JS")
    return render(request, "FrontendHome.html", {"ModelData_HTML": HTML,"ModelData_CSS": CSS,"ModelData_JS": JS})