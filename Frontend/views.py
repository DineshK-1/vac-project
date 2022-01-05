from django.shortcuts import render
from .models import FrontendModels
import requests

def Frontend(request, _Type, _Title):
    Data = FrontendModels.objects.get(Type = _Type, Title = _Title)
    r = requests.get( "http://127.0.0.1:8000/uploads/" + str(Data.Description), allow_redirects=False)
    PageContent = r.content
    return render(request, "Frontend.html", {"ModelData": FrontendModels.objects.all, "PageData":Data, "PageContent": PageContent})