""" Python Package Support """
# Not applicable

""" Django Package Support """
from django.shortcuts import render_to_response

""" Internal Package Support """
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
        