# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'SquareOnCard', fields ['square', 'card']
        db.delete_unique(u'bingo_squareoncard', ['square_id', 'card_id'])

        # Adding field 'SquareOnCard.position'
        db.add_column(u'bingo_squareoncard', 'position',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding unique constraint on 'SquareOnCard', fields ['position', 'square', 'card']
        db.create_unique(u'bingo_squareoncard', ['position', 'square_id', 'card_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'SquareOnCard', fields ['position', 'square', 'card']
        db.delete_unique(u'bingo_squareoncard', ['position', 'square_id', 'card_id'])

        # Deleting field 'SquareOnCard.position'
        db.delete_column(u'bingo_squareoncard', 'position')

        # Adding unique constraint on 'SquareOnCard', fields ['square', 'card']
        db.create_unique(u'bingo_squareoncard', ['square_id', 'card_id'])


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
            'bar': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'bingo_squares'", 'null': 'True', 'to': u"orm['bingo.Bar']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_global': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'needs_confirm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'needs_proof': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'bingo.squareoncard': {
            'Meta': {'unique_together': "(('card', 'square', 'position'),)", 'object_name': 'SquareOnCard'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'square'", 'to': u"orm['bingo.BingoCard']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'needs_confirm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'needs_proof': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'square': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bingo.BingoSquare']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '2'})
        }
    }

    complete_apps = ['bingo']