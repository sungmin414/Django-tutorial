from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    return HttpResponse(
        '<html><boddy>Post List</boddy></html>'
    )