# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'purple_config_user')

        # Removing M2M table for field studies on 'User'
        db.delete_table(db.shorten_name(u'purple_config_user_studies'))

        # Adding model 'RoboUser'
        db.create_table(u'purple_config_robouser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'purple_config', ['RoboUser'])

        # Adding M2M table for field studies on 'RoboUser'
        m2m_table_name = db.shorten_name(u'purple_config_robouser_studies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('robouser', models.ForeignKey(orm[u'purple_config.robouser'], null=False)),
            ('study', models.ForeignKey(orm[u'purple_config.study'], null=False))
        ))
        db.create_unique(m2m_table_name, ['robouser_id', 'study_id'])


    def backwards(self, orm):
        # Adding model 'User'
        db.create_table(u'purple_config_user', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'purple_config', ['User'])

        # Adding M2M table for field studies on 'User'
        m2m_table_name = db.shorten_name(u'purple_config_user_studies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'purple_config.user'], null=False)),
            ('study', models.ForeignKey(orm[u'purple_config.study'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'study_id'])

        # Deleting model 'RoboUser'
        db.delete_table(u'purple_config_robouser')

        # Removing M2M table for field studies on 'RoboUser'
        db.delete_table(db.shorten_name(u'purple_config_robouser_studies'))


    models = {
        u'purple_config.configuration': {
            'Meta': {'object_name': 'Configuration'},
            'config_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('json_field.fields.JSONField', [], {'default': "u'null'"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['purple_config.RoboUser']", 'null': 'True', 'blank': 'True'})
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