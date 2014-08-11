""" Python Package Support """
# Not applicable

""" Django Package Support """
from django import forms
from django.forms import ValidationError

""" Internal Package Support """
from devotional.models import Devotional

"""

 File       :: devotional/forms.py
 
 Author(s)  :: Matthew J Swann
 Version    :: 1.0
 Last Mod   :: 2014-08-11
 Mod by     :: Matthew J Swann

 """

class Devotional_Form(forms.ModelForm):
    """
    Form used to create event fields with optional location entry.
    Does not include the addressing information. Those fields can be
    filled in EventCreationFormPartTwo, below.
    """
    class Meta:
        model = Devotional
        fields = (
            'title',
            'month', 
            'day',
            'body',
            )
    
        
    def create_devotional(self, *args, **kwargs):
        """
        Creates a new event and its assignments.
        """
        the_title   = self.cleaned_data['the_title']
        the_month   = self.cleaned_data['the_month']
        the_day     = self.cleaned_data['the_day']
        the_body    = self.cleaned_data['the_body']
                        
        Devotional.objects.create (
            title = the_title,
            month = the_month,
            day   = the_day,
            body  = the_body   
                )
