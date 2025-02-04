from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Content

def get_contents_api(request):
    json_obj = serialize("json", Content.objects.all())
    return HttpResponse(
        json_obj,
        content_type="application/json"
    )



class ContentDetailView(DetailView):
    model = Content
    template_name = "core/detail.html"
    context_object_name = "content"

class ContentListView(ListView):
    model = Content
    template_name = "core/index.html"
    context_object_name = "contents"

    def get_queryset(self):
        return Content.objects.filter(title__contains="Title").order_by("title")


class ContentView(View):
    def get(self, request):
        contents = Content.objects.all()
        return render(
            request,
            template_name="core/index.html",
            context={"contents": contents}
        )

def index(request):
    contents = Content.objects.all()
    return render(
        request,
        template_name="core/index.html",
        context={"contents": contents}
    )

def detail(request, id):
    content = Content.objects.get(id=id)
    return render(
        request,
        template_name="core/detail.html",
        context={"content": content}
    )
