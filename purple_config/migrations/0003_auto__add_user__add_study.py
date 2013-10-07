# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'purple_config_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('study_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'purple_config', ['User'])

        # Adding model 'Study'
        db.create_table(u'purple_config_study', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('study_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'purple_config', ['Study'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'purple_config_user')

        # Deleting model 'Study'
        db.delete_table(u'purple_config_study')


    models = {
        u'purple_config.configuration': {
            'Meta': {'object_name': 'Configuration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('json_field.fields.JSONField', [], {'default': "u'null'"}),
            'study_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'purple_config.purplerobotconfigtemplate': {
            'Meta': {'object_name': 'PurpleRobotConfigTemplate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'purple_config.study': {
            'Meta': {'object_name': 'Study'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'study_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'purple_config.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'study_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['purple_config']