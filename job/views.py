from django.shortcuts import render
from .models import Job
# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    print(job_list)
    context = {'job_list': job_list}
    return render(request, 'job/job_list.html', context)
def job_details(request, id):
    job_details = Job.objects.get(id=id)
    context = {'job_details': job_details}
    return render(request, 'job/job_details.html', context)
