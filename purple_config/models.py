from django.db import models
from json_field import JSONField

class Configuration(models.Model):
        user_id = models.CharField(max_length=50)
        study_id = models.CharField(max_length=50)
        json = JSONField()

class PurpleRobotConfigTemplate(models.Model):
        uploaded = models.DateTimeField(auto_now_add = True)
        template_file = models.FileField(upload_to = 'pr_configs')
