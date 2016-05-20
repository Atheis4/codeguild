from django.db import models
from django.utils import timezone

class Flutt(models.Model):
    """docstring for Flutt"""
    user_name = models.TextField(null=True)
    text = models.TextField()
    date_created = models.DateTimeField(
        default=timezone.now,
    )

    def __str__(self):
        return '{!r}: {!r}, {!r}'.format(
            self.user_name,
            self.text,
            self.date_created,
        )

    def __repr__(self):
        return 'Flutt(user_name:{!r}, text:{!r}, date_created: {!r})'.format(
            self.user_name,
            self.text,
            self.date_created,
        )
