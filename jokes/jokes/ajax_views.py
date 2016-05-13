from django.http import HttpResponse
from django.shortcuts import render
from . import logic

def render_ack(request):
    setup = request.GET['setup']
