from django.http import HttpResponse
from django.shortcuts import render
from .models import Content


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
