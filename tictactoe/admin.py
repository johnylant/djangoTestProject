from django.contrib import admin

from .models import Game, Move, Invitation

# Register your models here.
admin.site.register(Invitation)
admin.site.register(Game)
admin.site.register(Move)
