from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator, MinLengthValidator , RegexValidator
from django.template.defaultfilters import slugify
from django.db.models import Avg
from django.urls import reverse
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
from django.db import IntegrityError
from PIL import Image
# from taggit.managers import TaggableManager
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
import requests
import random 

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    author =models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    # arti = models.Manager()


    def __str__(self):
        return self.title


class Locality(models.Model):
    city     = models.CharField(max_length=100)
    state    = models.CharField(max_length=100)
    locality = models.CharField(max_length=150)

    def __str__(self):
        return "{}, {}, {}".format(self.locality, self.city, self.state)