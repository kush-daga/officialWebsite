from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Event(models.Model):

    date_time = models.DateTimeField()
    venue = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    topics = models.ManyToManyField(
        Topic, related_name='topics', blank=True)
    link = models.URLField(blank=True)
    docs = models.URLField(blank=True)
    headline_event = models.BooleanField(default=False)

    def __str__(self):
        return self.title
