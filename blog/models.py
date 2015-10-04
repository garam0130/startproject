from django.db import models
from blog.utils import random_name_upload_to, thumbnail
from uuid import uuid4
import os
from django.db.models.signals import pre_save
from django.core.files import File
from django.contrib.auth.models import User

class SiType(models.Model):
    si = models.CharField(max_length=20)

    def __str__(self):
        return self.si

class GuType(models.Model):
    gu = models.CharField(max_length=20)

    def __str__(self):
        return self.gu

class GroupType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Group(models.Model):
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    group = models.ForeignKey(GroupType)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=random_name_upload_to)
    numb = models.IntegerField()
    si = models.ForeignKey(SiType)
    gu = models.ForeignKey(GuType)
    status = models.ForeignKey(Status)

    def __str__(self):
        return self.name

def pre_save_callback(sender, **kwargs):
    record = kwargs['instance']
    if record.image:
        max_width = 500
        if record.image.width > max_width or record.image.height > max_width:
            f = thumbnail(record.image.file, max_width, max_width)
            record.image.save(record.image.name, File(f))

pre_save.connect(pre_save_callback, sender=Group)

class Comment(models.Model):
    post = models.ForeignKey(Group)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)

class Apply(models.Model):
    group = models.ForeignKey(Group)
    applicant = models.ForeignKey(User)
    memo = models.TextField()
    is_approved = models.BooleanField(default=False)

