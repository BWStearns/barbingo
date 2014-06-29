import json

from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.conf import settings

from models import BingoGame


def get_game(request, game_id):
    game = BingoGame.objects.prefetch_related('bingo_cards', 'bingo_cards__square', 'bar').get(id=int(game_id))
    data = {
        "bar_name": game.bar.name,
        "cards": {

        }
    }

    for c in game.bingo_cards.all():
        data["cards"][c.id] = {
            "squares": {s.position: {"status": s.status, "text": s.text} for s in c.squares},
        }
    data = json.dumps(data)
    content_type = 'application/json'
    return HttpResponse(data, content_type=content_type)