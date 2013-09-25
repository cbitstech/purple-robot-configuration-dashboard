# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Configuration'
        db.create_table(u'purple_config_configuration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('study_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('json', self.gf('json_field.fields.JSONField')(default=u'null')),
        ))
        db.send_create_signal(u'purple_config', ['Configuration'])

        # Adding model 'PurpleRobotConfigTemplate'
        db.create_table(u'purple_config_purplerobotconfigtemplate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uploaded', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('template_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'purple_config', ['PurpleRobotConfigTemplate'])


    def backwards(self, orm):
        # Deleting model 'Configuration'
        db.delete_table(u'purple_config_configuration')

        # Deleting model 'PurpleRobotConfigTemplate'
        db.delete_table(u'purple_config_purplerobotconfigtemplate')


    models = {
        u'purple_config.configuration': {
            'Meta': {'object_name': 'Configuration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('json_field.fields.JSONField', [], {'default': "u'null'"}),
            'study_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'purple_config.purplerobotconfigtemplate': {
            'Meta': {'object_name': 'PurpleRobotConfigTemplate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['purple_config']