# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Configuration.user'
        db.add_column(u'purple_config_configuration', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purple_config.RoboUser'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field users on 'Configuration'
        db.delete_table(db.shorten_name(u'purple_config_configuration_users'))


    def backwards(self, orm):
        # Deleting field 'Configuration.user'
        db.delete_column(u'purple_config_configuration', 'user_id')

        # Adding M2M table for field users on 'Configuration'
        m2m_table_name = db.shorten_name(u'purple_config_configuration_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('configuration', models.ForeignKey(orm[u'purple_config.configuration'], null=False)),
            ('robouser', models.ForeignKey(orm[u'purple_config.robouser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['configuration_id', 'robouser_id'])


    models = {
        u'purple_config.configuration': {
            'Meta': {'object_name': 'Configuration'},
            'config_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('json_field.fields.JSONField', [], {'default': "u'null'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purple_config.RoboUser']", 'null': 'True', 'blank': 'True'})
        },
        u'purple_config.purplerobotconfigtemplate': {
            'Meta': {'object_name': 'PurpleRobotConfigTemplate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'purple_config.robouser': {
            'Meta': {'object_name': 'RoboUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'studies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['purple_config.Study']", 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'purple_config.study': {
            'Meta': {'object_name': 'Study'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'study_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['purple_config']