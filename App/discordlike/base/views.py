from re import I
from django.shortcuts import render

rooms = [
    {"id":1, "name":"Gracjan"},
    {"id":2, "name":"Marcin"},
    {"id":3, "name":"Oliviero"},
]

def home(request):
    context = {"rooms":rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i["id"] == int(pk):
            room = i
    context = {"room":room}
    return render(request, 'base/room.html', context)

# Create your views here.
