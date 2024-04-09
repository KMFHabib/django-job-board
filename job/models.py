from django.db import models

my_job_type = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
)
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20,choices=my_job_type)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    def __str__(self):
        return self.title