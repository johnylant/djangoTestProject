from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.urlresolvers import reverse

GAME_STATUS_CHOICES = (
    ('A', 'Active'),
    ('F', 'First Player Wins'),
    ('S', 'Second Player Wins'),
    ('D', 'Draw')
)

# inherits from models.Manager
# I REALLY DONT GET THIS!
class GamesManager(models.Manager):
    def games_for_user(self, user):
        return super(GamesManager, self).get_queryset().filter(
            Q(first_player_id=user.id) | Q(second_player_id=user.id))

    def new_game(self, invitation):
        game = Game(first_player=invitation.to_user,
                    second_player=invitation.from_user,
                    next_to_move=invitation.to_user)
        return game


class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="games_first_player")
    second_player = models.ForeignKey(User, related_name="games_second_player")
    next_to_move = models.ForeignKey(User, related_name="games_to_move")
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='A', choices=GAME_STATUS_CHOICES)
    objects = GamesManager()

    def get_absolute_url(self):
        # This does basically the same as URL tag.. construct reversly mapping URL, use it with Reverse
        return reverse('tictactoe_game_detail', args=[self.id])

    def __str__(self):
        return "{0} vs {1}".format(self.first_player, self.second_player)

# Create your models here.
class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300)
    game = models.ForeignKey(Game)

class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitations_sent")
    to_user = models.ForeignKey(User, related_name="invitations_received", verbose_name="User to invite", help_text="Please select the user you want to play with")
    message = models.CharField("Optional Message", max_length=300, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
