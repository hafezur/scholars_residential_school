from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class NewsEvent(models.Model):
    # Choices for type of item
    TYPE_CHOICES = [
        ('news', 'News'),
        ('event', 'Event'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='news',blank=True,null=True)
    start_date = models.DateField(default=timezone.now)  # For events
    end_date = models.DateField(blank=True, null=True)  # Optional, only for events
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    image = models.ImageField(upload_to='news_events/', blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', blank=True,null=True)

    class Meta:
        ordering = ['-start_date', '-created_at']
        verbose_name = "News / Event"
        verbose_name_plural = "News & Events"

    def __str__(self):
        return f"{self.title} ({self.type})"

    def is_current(self):
        """
        Check if event is ongoing (useful for events)
        """
        if self.type == 'event' and self.end_date:
            return self.start_date <= timezone.now().date() <= self.end_date
        return True  # news are always "current"
    
from django.contrib.postgres.fields import ArrayField
class okgs_photo(models.Model):
    title=models.CharField(max_length=100,blank=True,null=True)
    picture1 = models.ImageField(upload_to="galary",blank=True,null=True)
    picture2 = models.ImageField(upload_to="galary",blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    def __str__(self):
        return f"{self.title}"

class scientest(models.Model):
    name=models.CharField(blank=True,null=True)
    scientest_pic=models.ImageField( upload_to="scientest", blank=True,null=True)
    description=models.TextField(blank=True,null=True)

from django.db import models

class singleUnique(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="others", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)  # যখন object তৈরি হবে তখন timestamp save করবে
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)      # যখন object update হবে তখন timestamp update করবে

    def __str__(self):
        return self.title or "No Title"
    
class students(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    roll=models.IntegerField(blank=True,null=True)
    section=models.CharField(max_length=10,blank=True,null=True)