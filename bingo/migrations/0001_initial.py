# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bar'
        db.create_table(u'bingo_bar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'bingo', ['Bar'])

        # Adding model 'BingoGame'
        db.create_table(u'bingo_bingogame', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('bar', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bingo_games', to=orm['bingo.Bar'])),
        ))
        db.send_create_signal(u'bingo', ['BingoGame'])

        # Adding model 'BingoCard'
        db.create_table(u'bingo_bingocard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bingo_cards', to=orm['bingo.BingoGame'])),
        ))
        db.send_create_signal(u'bingo', ['BingoCard'])

        # Adding model 'BingoSquare'
        db.create_table(u'bingo_bingosquare', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('bar', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bingo_squares', to=orm['bingo.Bar'])),
            ('is_global', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('needs_proof', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('needs_confirm', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'bingo', ['BingoSquare'])

        # Adding unique constraint on 'BingoSquare', fields ['text', 'bar']
        db.create_unique(u'bingo_bingosquare', ['text', 'bar_id'])

        # Adding model 'CardOnSquare'
        db.create_table(u'bingo_cardonsquare', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('card', self.gf('django.db.models.fields.related.ForeignKey')(related_name='square', to=orm['bingo.BingoCard'])),
            ('square', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bingo.BingoSquare'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='U', max_length=2)),
            ('needs_proof', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('needs_confirm', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'bingo', ['CardOnSquare'])

        # Adding unique constraint on 'CardOnSquare', fields ['card', 'square']
        db.create_unique(u'bingo_cardonsquare', ['card_id', 'square_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'CardOnSquare', fields ['card', 'square']
        db.delete_unique(u'bingo_cardonsquare', ['card_id', 'square_id'])

        # Removing unique constraint on 'BingoSquare', fields ['text', 'bar']
        db.delete_unique(u'bingo_bingosquare', ['text', 'bar_id'])

        # Deleting model 'Bar'
        db.delete_table(u'bingo_bar')

        # Deleting model 'BingoGame'
        db.delete_table(u'bingo_bingogame')

        # Deleting model 'BingoCard'
        db.delete_table(u'bingo_bingocard')

        # Deleting model 'BingoSquare'
        db.delete_table(u'bingo_bingosquare')

        # Deleting model 'CardOnSquare'
        db.delete_table(u'bingo_cardonsquare')


    models = {
        u'bingo.bar': {
            'Meta': {'object_name': 'Bar'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'bingo.bingocard': {
            'Meta': {'object_name': 'BingoCard'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bingo_cards'", 'to': u"orm['bingo.BingoGame']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'bingo.bingogame': {
            'Meta': {'object_name': 'BingoGame'},
            'bar': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bingo_games'", 'to': u"orm['bingo.Bar']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'bingo.bingosquare': {
            'Meta': {'unique_together': "(('text', 'bar'),)", 'object_name': 'BingoSquare'},
            'bar': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bingo_squares'", 'to': u"orm['bingo.Bar']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_global': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'needs_confirm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'needs_proof': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'bingo.cardonsquare': {
            'Meta': {'unique_together': "(('card', 'square'),)", 'object_name': 'CardOnSquare'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'square'", 'to': u"orm['bingo.BingoCard']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'needs_confirm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'needs_proof': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'square': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bingo.BingoSquare']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '2'})
        }
    }

    complete_apps = ['bingo']