from django.db import models

class standup(models.Model):
    date_added = models.DateTimeField('date published')
    employee_id = models.CharField(primary_key='True', max_length=200) 
    employee_name = models.CharField(max_length = 300)
    work_done = models.CharField(max_length = 300)
    work_to_do = models.CharField(max_length = 300)
    issues_faced = models.CharField(max_length = 300)

class comments(models.Model):
    thoughts = models.CharField(max_length = 500)
    recommendations = models.CharField(max_length = 500)
