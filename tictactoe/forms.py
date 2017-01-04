from django.forms import ModelForm
from .models import Invitation

class InvitationForm(ModelForm):
    # Syntax to let know which model we use
    class Meta:
        model = Invitation
        exclude = ['from_user']
        #fields = '__all__'
