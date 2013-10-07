from django.db import models
from json_field import JSONField

class Study(models.Model):
    study_name = models.CharField(max_length=50, null=True, blank=True)
    
    def __unicode__(self):
        return self.study_name

class RoboUser(models.Model):
    studies = models.ManyToManyField(Study, blank=True, null=True, related_name='users')
    username = models.CharField(max_length=50, null=True, blank=True)
    
    def __unicode__(self):
        return self.username


class Configuration(models.Model):
    default = models.NullBooleanField(null=True, blank=True)
    user = models.ForeignKey(RoboUser, null=True, blank=True, related_name='user')
    config_name = models.CharField(max_length=100, null=True, blank=True)
    json = JSONField()

class PurpleRobotConfigTemplate(models.Model):
    uploaded = models.DateTimeField(auto_now_add = True)
    template_file = models.FileField(upload_to = 'pr_configs')

