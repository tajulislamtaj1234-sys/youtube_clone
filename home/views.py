from django.shortcuts import render
from django.views import View
from home.models import TagTitles
from contents.models import Video_Content
from contents.models import Channel
from contents.models import Shorts

# Create your views here.


class HomeView(View):
    def get(self, request):
        title=["shorts", "recent videos", "playlist"]
        tag=TagTitles.objects.all().exclude(titles="New to you")           
        videos= Video_Content.objects.all().order_by('uploaded_at')
        short=Shorts.objects.all().order_by("uploaded_at")
        return render(request, 'home.html', {"titles": title, "tag_names": tag, "videos": videos, "shorts": short})