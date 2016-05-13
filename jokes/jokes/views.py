from django.http import HttpResponse
from django.shortcuts import render
from . import logic

def render_form(request):
    return render(request, 'jokes/form.html', {})

def render_ack(request):
    setup = request.POST['setup']
    punchline = request.POST['punchline']
    logic.save_joke_obj(setup, punchline)
    context = {
        'setup': setup,
        'punchline': punchline,
    }
    return render(request, 'jokes/ack.html', context)

def render_index(request):
    joke_list = logic.return_humor()
    context = {
        'joke_list': joke_list,
    }
    return render(request, 'jokes/index.html', context)
