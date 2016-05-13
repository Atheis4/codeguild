from django.shortcuts import render
from django.http import HttpResponse
from . import logic

def render_book_stats(request):
    word = request.GET['w']
    count_result = logic.word_to_word_count(word)
    response_string = '{}: {}'.format(word, logic.word_to_word_count(word))
    return HttpResponse(response_string, status=200)
