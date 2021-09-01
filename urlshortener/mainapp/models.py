from .helpers import generate_url
from django.db import models

# Create your models here.
class Shortener(models.Model):
    # date_created = models.DateTimeField(auto_now_add=True)
    # times_followed = models.PositiveIntegerField(default=0)    
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    # class Meta:

    #     ordering = ["-date_created"]


    # def __str__(self):

    
    
    #     return f'{self.long_url} to {self.short_url}'
    def save(self):
        if not self.short_url:
            self.short_url = generate_url()
        super().save()

