from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=2000)
    question_text_my =models.CharField(max_length=2000,blank=True)
    question_text_md =models.CharField(max_length=2000,blank=True)
    question_text_ta=models.CharField(max_length=2000,blank=True)
    question_category1 = models.CharField(max_length=50,blank=True)
    question_category2 = models.CharField(max_length=50,blank=True)
    question_link = models.CharField(max_length=2000,blank=True)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text

class Category(models.Model):
    question_category1 = models.CharField(max_length=50,blank=True)
    question_category2 =models.CharField(max_length=50,blank=True )

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=10000)
    votes = models.FloatField(default=0)
    answer_link = models.CharField(max_length=2000,blank=True)

    def __str__(self):
        return self.choice_text

class authenticate(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
