from django.db import models

# Create your models here.
class Jobs(models.Model):
    PYTHON = 'PYTHON'
    C-SHARP = 'C#'
    JAVA = 'JAVA'
    C = 'C'
    RUBY = 'RUBY'

    SKILL_CHOICES = (
        ('PYTHON', 'python'),
        ('C-SHARP', 'c#'),
        ('JAVA', 'java'),
        ('C', 'c'),
        ('RUBY', 'ruby')
    )


    MAYOR_ROAD = 'MAYOR_ROAD'
    RONGAI='RONGAI'
    GATAKA='GATAKA'
    OLOLUA='OLOLUA'

    LOCATION_CHOICES=(
        ('MAYOR_ROAD', 'mayor_road'),
        ('RONGAI', 'rongai'),
        ('GATAKA', 'gataka'),
        ('OLOLUA', 'ololua')


    
    CONTRACT = 'CONTRACT'
    PART_TIME = 'PART_TIME'
    PERMANENT = 'PERMANENT'

    JOB_TYPE_CHOICES =(
        ('PERMANENT', 'permanent'),
        ('CONTRACT', 'contract'),
        ('PART_TIME','part_time')
    )


    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    skill = models.CharField(max_length=60,choices=SKILL_CHOICES)
    location = models.CharField(max_length=60,choices=LOCATION_CHOICES)
    salary = models.IntegerField(blank=True, null=True)
    job_type = models.CharField(max_length=60,choices=JOB_TYPE_CHOICES)
    contact = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=250, blank=True)
