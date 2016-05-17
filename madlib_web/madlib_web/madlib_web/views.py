from django.shortcuts import render
from django.http import HttpResponse

def render_giraffe(request):
    plural_noun = request.GET['plural_noun']
    plural_noun_2 = request.GET['plural_noun_2']
    body_part_name = request.GET['body_part_name']
    madlib_string = 'Giraffes have aroused the curiosity of ' + plural_noun + 'since earliest times. The giraffe is the tallest of all living ' + plural_noun_2 + ', but scientists are unable to explain how it got its long ' + body_part_name + '.'
    return HttpResponse(madlib_string)
