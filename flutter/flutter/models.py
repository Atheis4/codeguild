from django.db import models
from django.utils import timezone

class Flutt(models.Model):
    """docstring for Flutt"""
    user_name = models.TextField(null=True)
    text = models.TextField()
    date_created = models.DateTimeField(editable=False)

    def __str__(self):
        return '{!r}: {!r}, {!r}'.format(
            self.user_name,
            self.text,
            self.date_created
        )

    def __repr__(self):
        return 'Flutt(User:{!r}, Text:{!r}, Created Date: {!r})'.format(
            self.user_name,
            self.text,
            self.date_created,
        )
