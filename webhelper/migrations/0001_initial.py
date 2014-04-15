# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SocialLinks'
        db.create_table(u'webhelper_sociallinks', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=100, null=True, blank=True)),
            ('linkedin', self.gf('django.db.models.fields.URLField')(max_length=100, null=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.URLField')(max_length=100, null=True, blank=True)),
            ('gpluse', self.gf('django.db.models.fields.URLField')(max_length=100, null=True, blank=True)),
            ('rss', self.gf('django.db.models.fields.URLField')(max_length=100, null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True)),
        ))
        db.send_create_signal(u'webhelper', ['SocialLinks'])

        # Adding model 'RegisterAddress'
        db.create_table(u'webhelper_registeraddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('street_1', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('street_2', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True)),
        ))
        db.send_create_signal(u'webhelper', ['RegisterAddress'])

        # Adding model 'OfficeAddress'
        db.create_table(u'webhelper_officeaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('street_1', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('street_2', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True)),
        ))
        db.send_create_signal(u'webhelper', ['OfficeAddress'])

        # Adding model 'GeneralInfo'
        db.create_table(u'webhelper_generalinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('phone_2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('phone_3', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tollfree', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('support_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('sales_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('Billing_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('Website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('site', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True)),
        ))
        db.send_create_signal(u'webhelper', ['GeneralInfo'])


    def backwards(self, orm):
        # Deleting model 'SocialLinks'
        db.delete_table(u'webhelper_sociallinks')

        # Deleting model 'RegisterAddress'
        db.delete_table(u'webhelper_registeraddress')

        # Deleting model 'OfficeAddress'
        db.delete_table(u'webhelper_officeaddress')

        # Deleting model 'GeneralInfo'
        db.delete_table(u'webhelper_generalinfo')


    models = {
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'webhelper.generalinfo': {
            'Billing_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'GeneralInfo'},
            'Website': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'fax': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phone_2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phone_3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sales_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'support_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'tollfree': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'webhelper.officeaddress': {
            'Meta': {'object_name': 'OfficeAddress'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'street_1': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'street_2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'webhelper.registeraddress': {
            'Meta': {'object_name': 'RegisterAddress'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'street_1': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'street_2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'webhelper.sociallinks': {
            'Meta': {'object_name': 'SocialLinks'},
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'gpluse': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rss': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['webhelper']