from django.db import models
JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    published_at = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1000)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    Category = models.ForeignKey('Category',on_delete=models.CASCADE)
    def __str__(self):
        return self.title    
class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name        