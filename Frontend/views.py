from django.shortcuts import render

def Frontend(request):
    return render(request, "Frontend.html")