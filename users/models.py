import os
import uuid
import boto3
import random
from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.core.files.storage import default_storage
from botocore.client import Config
from datetime import datetime as dt
#from django.contrib.auth.hashers import make_password


class AppUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    is_student = models.BooleanField(default=False)
    grade = models.CharField(max_length=4, blank=True, null=True)
    sclass = models.PositiveIntegerField(blank=True, null=True)
    school_name = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)


class Subject(models.Model):
    subject_name = models.CharField(max_length=50, blank=True, null=True)
    chapter_name = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(default=dt.now, null=True)
    modified_on = models.DateTimeField(default=dt.now, null=True)
    belongs_to = models.ForeignKey(AppUser, on_delete=models.PROTECT)


class Answer(models.Model):
    ANSWER_TYPE = (
        (1, 'Text'),
        (2, 'File'),
    )
    answer_type = models.IntegerField(choices=ANSWER_TYPE, default=1)
    detailed_solution = models.TextField(blank=True, null=True)
    file = models.CharField(max_length=100, blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)


class Question(models.Model):
    COMPLEXITY = (
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced')
    )
    Q_TYPE = (
        (1, 'MCQ'),
        (2, 'Subjective'),
        (3, 'Fill in the blanks'),
        (4, 'Comprehension')
    )
    complexity = models.IntegerField(choices=COMPLEXITY, default=1)
    q_type = models.IntegerField(choices=Q_TYPE, default=1)
    question = models.CharField(max_length=50, blank=True, null=True)
    correct_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, blank=True, null=True) 
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    answer = models.ManyToManyField(Answer, related_name='answer_question')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)


class Test(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    questions = models.ManyToManyField(Question, blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)


class Response(models.Model):
    score = models.FloatField(blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    test = models.ForeignKey(Test, on_delete=models.PROTECT)
    belongs_to = models.ForeignKey(AppUser, on_delete=models.PROTECT)
