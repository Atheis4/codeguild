from django.http import HttpResponse
from django.shortcuts import render
from . import logic

def render_poll(request):
    return render(request, 'polls/poll.html', {})

def render_summary(request):
    vote = request.POST['ice-cream']
    logic.add_flavor(vote)

    flavor_dict = logic.combine_pieces()

    context = {
        'flavor_dict': flavor_dict,
    }
    return render(request, 'polls/index.html', context)
