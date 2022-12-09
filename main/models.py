from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)


class CompanyReview(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=500)


class Job(models.Model):
    position_name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position_url = models.CharField(max_length=200)


class JobApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)


class Event(models.Model):
    event_type = models.CharField(max_length=200)
    event_date = models.DateField()
    personal_notes = models.CharField(max_length=500)
    public_notes = models.CharField(max_length=500)
    job_app = models.ForeignKey(JobApp, on_delete=models.CASCADE)


# Create your models here.
