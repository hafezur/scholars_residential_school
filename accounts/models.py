from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Extra fields for user profile (optional)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_secondary_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username