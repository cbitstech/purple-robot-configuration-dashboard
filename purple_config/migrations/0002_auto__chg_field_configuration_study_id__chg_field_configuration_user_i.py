# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Configuration.study_id'
        db.alter_column(u'purple_config_configuration', 'study_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Configuration.user_id'
        db.alter_column(u'purple_config_configuration', 'user_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Configuration.study_id'
        raise RuntimeError("Cannot reverse this migration. 'Configuration.study_id' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Configuration.user_id'
        raise RuntimeError("Cannot reverse this migration. 'Configuration.user_id' and its values cannot be restored.")

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
        }
    }

    complete_apps = ['purple_config']