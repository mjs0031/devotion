""" Python Package Support """
# Not applicable

""" Django Package Support """
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.views.generic import TemplateView

""" Internal Package Support """
from devotional.forms import Devotional_Form
from devotional.models import Devotional

"""

 File       :: devotional/views.py
 
 Author(s)  :: Matthew J Swann
 Version    :: 1.0
 Last Mod   :: 2014-08-11
 Mod by     :: Matthew J Swann
 
 
 Importing CSV to Devotional Table.

 """

def devotionals(request):
    devotionals_all = Devotional.objects.all()
    return render_to_response('all_devotionals_template.html', locals())



def specific_devotional(request, offset):
    the_devotional = Devotional.objects.get(pk=int(offset))
    return render_to_response('specific_devotional_template.html', locals())



def the_count(request):
    
    total = 0
    for entry in Devotional.objects.all():
        
        split_text = entry.body.split(' ')
        
        total = total + len(split_text)
        
    dictionary = {
        'total' : total,
            }
    return render_to_response('the_count_template.html', dictionary)


class create_devotional(TemplateView):
    """
    View for rendering and submitting the form for creating a new devotional. 
    """
    form_class    = Devotional_Form
    template_name = 'create_devotional.html'


    def get(self, request, *args, **kwargs):
            
        form = self.form_class()

        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
        #form = self.form_class()
            
        if form.is_valid():
            
            form.create_devotional()
               
            return HttpResponseRedirect('/')
          
        return render(request, self.template_name, {'form': form})

        