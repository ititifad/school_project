from django.db import models
from django.contrib.auth.models import User
from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class School(models.Model):
    SCHOOL_CHOICES = (
        ('waja', 'Waja Schools'),
        ('Emaco', 'Emaco'),
        ('Pamoja school', 'Patwao Schools')
        
    )
    name = models.CharField(max_length=20, choices=SCHOOL_CHOICES)

    def __str__(self):
        return self.name


class Report(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    subjects = models.ManyToManyField(Subject)
    regions = models.ManyToManyField(Region)
    schools = models.ManyToManyField(School)
    publish_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    reviewed = models.BooleanField(default=False)
    report= models.FileField(upload_to='media/reports', max_length=100)

    def __str__(self):
        return self.title

def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk})
