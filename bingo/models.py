from random import shuffle

from django.db import models
from django.contrib.auth import get_user_model
Account = get_user_model()
# from django.contrib.auth.decorators import permission_required


class Defmix(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Bar(Defmix):
    owner = models.ForeignKey(Account, related_name='bars')
    name = models.CharField(max_length=200)

    @classmethod
    def test_setup(cls):
        me = Account.objects.get(email="brianw.stearns@gmail.com")
        bar, is_new = cls.objects.get_or_create(name="Parkside", owner=me)
        game = BingoGame.objects.create(bar=bar)
        card = BingoCard.objects.create(game=game)
        card.make_card()
        return card, game


class BarAdministration(Defmix):
    admin = models.ForeignKey(Account)
    bar = models.ForeignKey(Bar)

    class Meta:
        unique_together = ("admin", "bar")

    def is_owner(self):
        return self.bar.owner_id == self.admin_id


class BingoGame(Defmix):
    bar = models.ForeignKey(Bar, related_name='bingo_games')


class BingoCard(Defmix):
    game = models.ForeignKey(BingoGame, related_name='bingo_cards')

    @property
    def squares(self):
        return sorted(list(self.square.all()), key=lambda c: c.position)

    def make_card(self, prefer_local=False):
        import ipdb; ipdb.set_trace()
        bar = self.game.bar
        squares = []
        if prefer_local:
            squares = list(BingoSquare.objects.filter(bar=bar).order_by("?")[:25])
        if len(squares) < 25:
            need = (25 - len(squares))
            sq_ids = [s.id for s in squares]
            squares += list(BingoSquare.objects.order_by("?").exclude(id__in=sq_ids)[:need])
        shuffle(squares)
        squares = [SquareOnCard.make(self, sq, pos) for sq, pos in zip(squares, range(25))]
        import ipdb; ipdb.set_trace()
        SquareOnCard.objects.bulk_create(squares)

    def row_full(self, row):
        return all([s.is_found for s in self.squares[row*5:row*5+5]])

    def col_full(self, col):
        return all([s.is_found for s in self.squares if (s.position%5) == col])

    def l_diag_full(self):
        l_to_r = [(x*5)+y for x,y in zip(range(5), range(5))]
        return all([s.is_found for s in self.squares if s.position in l_to_r])

    def r_diag_full(self):
        r_to_l = [(x*5)+y for x,y in zip(range(5), range(4, -1, -1))]
        return all([s.is_found for s in self.squares if s.position in r_to_l])

    def check_for_wins(self):
        wins = []
        for r_or_c in range(5):
            if self.row_full(r_or_c):
                wins.append("R{0}".format(r_or_c))
            if self.col_full(r_or_c):
                wins.append("C{0}".format(r_or_c))
        if self.l_diag_full():
            wins.append("DL")
        if self.r_diag_full():
            wins.append("DR")
        return wins


class BingoSquare(Defmix):
    text = models.CharField(max_length=200)
    bar = models.ForeignKey(Bar, related_name='bingo_squares', null=True, default=None)
    is_global = models.BooleanField(default=True)
    needs_proof = models.BooleanField(default=False)
    needs_confirm = models.BooleanField(default=False)

    class Meta:
        unique_together = ('text', 'bar')


class SquareOnCard(Defmix):
    STATUSES = {
        "F": "Found",
        "A": "Awaiting Approval",
        "U": "Unfound",
    }.items()
    position_options = zip(range(25), range(25))

    card = models.ForeignKey(BingoCard, related_name='square')
    square = models.ForeignKey(BingoSquare)
    position = models.IntegerField(choices=position_options)
    status = models.CharField(max_length=2, choices=STATUSES, default="U")
    needs_proof = models.BooleanField(default=False)
    needs_confirm = models.BooleanField(default=False)
    text = models.CharField(max_length=200)

    class Meta:
        unique_together = ('card', 'square', 'position')

    @classmethod
    def make(cls, card, square, pos, *args, **kwargs):
        return cls(**{
            "card": card,
            "square": square,
            "needs_confirm": square.needs_confirm,
            "needs_proof": square.needs_proof,
            "position": pos,
            "text": square.text,
            })

    @property
    def is_found(self):
        return self.status == "F"

# Here's where we deal with the POST responses

    def _confirm(self):
        self.status = "F"
        self.save()

    @classmethod
    def confirm(cls, square_to_confirm):
        sq = cls.objects.get(id=square_to_confirm)
        sq._confirm()

    def _reject(self):
        self.status = "U"
        self.save()

    @classmethod
    def reject(cls, square_to_reject):
        sq = cls.objects.get(id=square_to_reject)
        sq._reject()

    def _promote(self):
        if self.status == "U":
            if self.needs_confirm:
                self.status = "A"
            else:
                self.status = "F"
            self.save()
        else:
            pass
        return self

    # Need square to data method
    @classmethod
    def promote(cls, square_to_promote):
        sq = cls.objects.get(id=square_to_promote["id"])
        print sq.__dict__
        sq._promote()
        return sq
