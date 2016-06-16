"""."""

from django.http import HttpResponse
from django.shortcuts import render

from . import logic


def is_there_a_query(request):
    """."""
    try:
        if request.GET['q']:
            print(request.GET['q'])
            return render_query(request)
    except KeyError:
        return render_index(request)


def render_index(request):
    """."""
    flutt_list = logic.return_latest_ten_flutts()

    template_args = {
        'flutt_list': flutt_list,
    }
    return render(request, 'flutter/index.html', template_args)


def render_query(request):
    """."""
    query = request.GET['q']
    flutt_list = logic.return_flutts_from_query_text(query)

    template_args = {
        'query': query,
        'flutt_list': flutt_list,
    }
    return render(request, 'flutter/index.html', template_args)


def render_post(request):
    """."""
    return render(request, 'flutter/post.html', {})


def render_post_submit(request):
    """."""
    input_user = request.POST['user_name']
    text = request.POST['text']
    logic.create_flutt(input_user, text)
    return render(request, 'flutter/post_submit.html', {})


def render_user(request, user_name):
    """."""
    flutt_list = logic.return_ten_flutts_from_user(user_name)

    template_args = {
        'user_name': user_name,
        'flutt_list': flutt_list,
    }
    return render(request, 'flutter/user_page.html', template_args)
