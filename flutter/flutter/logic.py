from . import models
from django.utils import timezone
import pytz

timezone.localtime(timezone.now())

def create_flutt(user_name, text):
    new_flutt = models.Flutt(
        user_name=user_name,
        text=text,
        date_created=timezone.now()
    )
    new_flutt.save()

def return_latest_ten_flutts():
    return models.Flutt.objects.all().order_by('-date_created')[:10]

def return_ten_flutts_from_user(user_name):
    return models.Flutt.objects.filter(user_name=user_name).order_by('-date_created')[:10]

def return_flutts_from_query_text(query):
    return models.Flutt.objects.filter(text__contains=query).order_by('-date_created')[:10]
