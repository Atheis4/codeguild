from django.http import HttpResponse
from django.shortcuts import render
from . import logic

def render_poll(request):
    return render(request, 'polls/poll.html', {})

def render_summary(request):
    vote = request.POST['ice-cream']
    logic.add_flavor(vote)
    flavor_to_percentage = logic.main()
    context = {
        'flavor_to_percentage': flavor_to_percentage,
    }
    return render(request, 'polls/index.html', context)
