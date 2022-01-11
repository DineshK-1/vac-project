from django.shortcuts import render,redirect
from .models import BackendModel

def Backend(request):
    if request.method == "GET":
        Data = BackendModel.objects.all
        return render(request, "Backend.html", {"Data" : Data})
    elif request.method == "POST" :
        data = request.POST
        Di = data.dict()
        instance = BackendModel(username = Di["username"], Text = Di["textt"])
        instance.save()
        return redirect("Backend")