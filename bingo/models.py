from django.db import models


class Defmix(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Bar(Defmix):
    name = models.CharField(max_length=200)


class BingoGame(Defmix):
    bar = models.ForeignKey(Bar, related_name='bingo_games')


class BingoCard(Defmix):
    game = models.ForeignKey(BingoGame, related_name='bingo_cards')


class BingoSquare(Defmix):
    text = models.CharField(max_length=200)
    bar = models.ForeignKey(Bar, related_name='bingo_squares')
    is_global = models.BooleanField(default=True)
    needs_proof = models.BooleanField(default=False)
    needs_confirm = models.BooleanField(default=False)

    class Meta:
        unique_together = ('text', 'bar')


class CardOnSquare(Defmix):
    STATUSES = {
        "F": "Found",
        "A": "Awaiting Approval",
        "N": "Needs Evidence",
        "U": "Unfound",
    }.items()

    card = models.ForeignKey(BingoCard, related_name='square')
    square = models.ForeignKey(BingoSquare)
    status = models.CharField(max_length=2, choices=STATUSES, default="U")
    needs_proof = models.BooleanField(default=False)
    needs_confirm = models.BooleanField(default=False)

    class Meta:
        unique_together = ('card', 'square')
