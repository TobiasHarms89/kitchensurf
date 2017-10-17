from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
#uebrenimmt standard felder vom User
    user = models.OneToOneField(User)

#additional
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class Events(models.Model):
    Name_Event = models.CharField(max_length=264,unique=True)
    Date_Event = models.DateField()
    Guest_Number = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.Name_Event
