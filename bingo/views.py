import json

from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.conf import settings

from models import BingoGame, BingoCard, SquareOnCard


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


def get_card(request, game_id, card_id):
    card = BingoCard.objects.prefetch_related('square').get(id=card_id, game_id=game_id)
    data = {
        "squares": {s.position: {"status": s.status, "text": s.text} for s in card.squares},
    }
    data = json.dumps(data)
    content_type = 'application/json'
    return HttpResponse(data, content_type=content_type)


def mark_as_confirmed(request):
    user = request.user
    if request.method == "POST":
        data = request.POST
        if data.get("confirm"):
            try:
                SquareOnCard.confirm(data["confirm"])
            except:
                data = {"Status": "Success"}
        elif data.get("reject"):
            try:
                SquareOnCard.reject(data["reject"])
            except:
                data = {"Status": "Failure"}
    content_type = 'application/json'
    return HttpResponse(data, content_type=content_type)


def main_view(request):
    cxt = {}
    return render(request, 'main.html', cxt)
