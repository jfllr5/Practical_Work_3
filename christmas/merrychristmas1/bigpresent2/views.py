from django.shortcuts import render

def Christmas(request):
    return render(request, 'hello_world.html')