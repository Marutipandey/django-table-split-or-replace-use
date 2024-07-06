from django.db import models
from django.utils import timezone




class TimeAndDate(models.Model):
    bookname = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bookname
