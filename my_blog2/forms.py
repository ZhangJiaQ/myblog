from django import forms

from my_blog2.models import LeaveMessage


class LeaveMessageForm(forms.ModelForm):

    class Meta:
        model = LeaveMessage
        fields = ['name', 'email', 'subject', 'message']