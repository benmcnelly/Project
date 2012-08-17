from django.db import models

class Crap(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
