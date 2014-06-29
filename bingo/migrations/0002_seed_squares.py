# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

        starter_squares = ['Toast', "Someone who's waiting", 'Spelling/grammatical errors', 'Girls night out', 'Date:', 'Sunglasses at night', 'Overly intoxicated person', 'Excess clevage', 'Seat dancer', 'Visible thong', 'Pickup!', u'\xa0', 'Cocktail shaker', 'The text messager', 'Frozen drink', 'Lipstick mark on glass', 'Martini', 'Public display of affection', 'Phone shouter', 'Name:', 'Handwritten signs', 'Frat boy', 'Fist pump', 'Doing shots', 'Bathroom line', 'Number swap', 'Free Space!', 'Gold chain']

        for sq in starter_squares:
            orm.BingoSquare.objects.create(text=sq, bar=None, is_global=True, needs_confirm=False, needs_proof=False)

    def backwards(self, orm):
        starter_squares = ['Toast', "Someone who's waiting", 'Spelling/grammatical errors', 'Girls night out', 'Date:', 'Sunglasses at night', 'Overly intoxicated person', 'Excess clevage', 'Seat dancer', 'Visible thong', 'Pickup!', u'\xa0', 'Cocktail shaker', 'The text messager', 'Frozen drink', 'Lipstick mark on glass', 'Martini', 'Public display of affection', 'Phone shouter', 'Name:', 'Handwritten signs', 'Frat boy', 'Fist pump', 'Doing shots', 'Bathroom line', 'Number swap', 'Free Space!', 'Gold chain']

        for sq in starter_squares:
            orm.BingoSquare.objects.filter(text__in=starter_squares).delete()

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
            'Meta': {'unique_together': "(('card', 'square'),)", 'object_name': 'SquareOnCard'},
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
    symmetrical = True
