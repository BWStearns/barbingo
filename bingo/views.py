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
            "squares": [{"position": s.position, "status": s.status, "text": s.text, "id": s.id} for s in c.squares],
        }
    data = json.dumps(data)
    content_type = 'application/json'
    return HttpResponse(data, content_type=content_type)


def specific_card(request, game_id, card_id):
    if request.method == "GET":
        card = BingoCard.objects.prefetch_related('square').get(id=card_id, game_id=game_id)
        data = {
            "squares": {s.position: {"status": s.get_status_display(), "text": s.text, "position": s.position,  "id": s.id} for s in card.squares},
        }
        data = json.dumps(data)
        content_type = 'application/json'
        return HttpResponse(data, content_type=content_type)
    if request.method == "POST":
        data = json.loads(request.body)
        print data
        # import ipdb; ipdb.set_trace()
        actions = {
            "confirm": mark_as_confirmed,
            "reject": mark_as_confirmed,
            "promote": promote,
        }
        try:
            return actions[data["action"]](data)
        except:
            pass

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

def promote(data):
    try:
        data = {
            "Status": "Success",
            "square": SquareOnCard.promote(data["square"])
        }
        s = data["square"]
        data["square"] = {"status": s.get_status_display(), "text": s.text, "position": s.position}

    except Exception, e:
        import ipdb; ipdb.set_trace()
        data = {"Status": "Failure"}
    content_type = 'application/json'
    print "RETURN DATA: ", data
    return HttpResponse(json.dumps(data), content_type=content_type)

def main_view(request):
    cxt = {}
    return render(request, 'main.html', cxt)
