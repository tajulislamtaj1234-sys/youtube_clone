from django.shortcuts import render
from django.views import View
from contents.models import Shorts

class ShortsView(View):
    def get(self, request):
        short=Shorts.objects.all()
        return render (request, 'shorts.html')