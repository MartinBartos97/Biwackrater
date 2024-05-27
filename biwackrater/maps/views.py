from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class MapView:
    def init_maps(request):
        return HttpResponse('Well, hello to biwackrater')